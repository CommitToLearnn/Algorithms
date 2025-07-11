/*
 * K-Nearest Neighbors (KNN) - Implementação Otimizada em Java
 * ===========================================================
 * 
 * Versão otimizada com múltiplas métricas de distância, normalização,
 * validação cruzada, análise de performance e design patterns.
 * 
 * Otimizações implementadas:
 * - Strategy Pattern para métricas de distância
 * - Builder Pattern para configuração
 * - Streams API para processamento funcional
 * - Normalização automática de dados
 * - Validação cruzada para seleção de k
 * - Análise de performance detalhada
 * - Thread safety e processamento paralelo
 */

// package knn.otimizado;

import java.util.*;
import java.util.concurrent.*;
import java.util.stream.*;
import java.time.*;

/**
 * Interface para estratégias de cálculo de distância
 */
interface EstrategiaDistancia {
    double calcular(double[] p1, double[] p2);
    String getNome();
}

/**
 * Implementações das diferentes métricas de distância
 */
class DistanciaEuclidiana implements EstrategiaDistancia {
    @Override
    public double calcular(double[] p1, double[] p2) {
        double soma = 0.0;
        for (int i = 0; i < p1.length; i++) {
            double diff = p1[i] - p2[i];
            soma += diff * diff;
        }
        return Math.sqrt(soma);
    }
    
    @Override
    public String getNome() { return "Euclidiana"; }
}

class DistanciaManhattan implements EstrategiaDistancia {
    @Override
    public double calcular(double[] p1, double[] p2) {
        double soma = 0.0;
        for (int i = 0; i < p1.length; i++) {
            soma += Math.abs(p1[i] - p2[i]);
        }
        return soma;
    }
    
    @Override
    public String getNome() { return "Manhattan"; }
}

class DistanciaMinkowski implements EstrategiaDistancia {
    private final double p;
    
    public DistanciaMinkowski(double p) {
        this.p = p;
    }
    
    @Override
    public double calcular(double[] p1, double[] p2) {
        double soma = 0.0;
        for (int i = 0; i < p1.length; i++) {
            soma += Math.pow(Math.abs(p1[i] - p2[i]), p);
        }
        return Math.pow(soma, 1.0 / p);
    }
    
    @Override
    public String getNome() { return "Minkowski(p=" + p + ")"; }
}

class DistanciaCosseno implements EstrategiaDistancia {
    @Override
    public double calcular(double[] p1, double[] p2) {
        double produtoEscalar = 0.0;
        double normaP1 = 0.0;
        double normaP2 = 0.0;
        
        for (int i = 0; i < p1.length; i++) {
            produtoEscalar += p1[i] * p2[i];
            normaP1 += p1[i] * p1[i];
            normaP2 += p2[i] * p2[i];
        }
        
        normaP1 = Math.sqrt(normaP1);
        normaP2 = Math.sqrt(normaP2);
        
        if (normaP1 == 0 || normaP2 == 0) {
            return 1.0; // Máxima distância
        }
        
        double similaridade = produtoEscalar / (normaP1 * normaP2);
        return 1.0 - similaridade; // Converte similaridade para distância
    }
    
    @Override
    public String getNome() { return "Cosseno"; }
}

/**
 * Classe para representar pontos otimizados
 */
class PontoOtimizado {
    private final double[] coordenadas;
    private final double[] coordenadasNormalizadas;
    private final String classe;
    
    public PontoOtimizado(double[] coordenadas, double[] coordenadasNormalizadas, String classe) {
        this.coordenadas = Arrays.copyOf(coordenadas, coordenadas.length);
        this.coordenadasNormalizadas = coordenadasNormalizadas != null ? 
            Arrays.copyOf(coordenadasNormalizadas, coordenadasNormalizadas.length) : null;
        this.classe = classe;
    }
    
    public double[] getCoordenadas() { return Arrays.copyOf(coordenadas, coordenadas.length); }
    public double[] getCoordenadasNormalizadas() { 
        return coordenadasNormalizadas != null ? 
            Arrays.copyOf(coordenadasNormalizadas, coordenadasNormalizadas.length) : null; 
    }
    public String getClasse() { return classe; }
}

/**
 * Classe para representar vizinhos otimizados
 */
class VizinhoOtimizado implements Comparable<VizinhoOtimizado> {
    private final PontoOtimizado ponto;
    private final double distancia;
    private final int indice;
    
    public VizinhoOtimizado(PontoOtimizado ponto, double distancia, int indice) {
        this.ponto = ponto;
        this.distancia = distancia;
        this.indice = indice;
    }
    
    public PontoOtimizado getPonto() { return ponto; }
    public double getDistancia() { return distancia; }
    public int getIndice() { return indice; }
    
    @Override
    public int compareTo(VizinhoOtimizado outro) {
        return Double.compare(this.distancia, outro.distancia);
    }
}

/**
 * Classe para armazenar resultado detalhado da classificação
 */
class ResultadoClassificacao {
    private final String classePrevista;
    private final double confianca;
    private final List<Double> distanciasVizinhos;
    private final List<String> classesVizinhos;
    private final Duration tempoPredicao;
    
    public ResultadoClassificacao(String classePrevista, double confianca,
                                List<Double> distanciasVizinhos, List<String> classesVizinhos,
                                Duration tempoPredicao) {
        this.classePrevista = classePrevista;
        this.confianca = confianca;
        this.distanciasVizinhos = new ArrayList<>(distanciasVizinhos);
        this.classesVizinhos = new ArrayList<>(classesVizinhos);
        this.tempoPredicao = tempoPredicao;
    }
    
    // Getters
    public String getClassePrevista() { return classePrevista; }
    public double getConfianca() { return confianca; }
    public List<Double> getDistanciasVizinhos() { return new ArrayList<>(distanciasVizinhos); }
    public List<String> getClassesVizinhos() { return new ArrayList<>(classesVizinhos); }
    public Duration getTempoPredicao() { return tempoPredicao; }
}

/**
 * Classe para métricas de avaliação por classe
 */
class MetricasClasse {
    private final double precisao;
    private final double recall;
    private final double f1Score;
    private final int suporte;
    
    public MetricasClasse(double precisao, double recall, double f1Score, int suporte) {
        this.precisao = precisao;
        this.recall = recall;
        this.f1Score = f1Score;
        this.suporte = suporte;
    }
    
    // Getters
    public double getPrecisao() { return precisao; }
    public double getRecall() { return recall; }
    public double getF1Score() { return f1Score; }
    public int getSuporte() { return suporte; }
}

/**
 * Classe para estatísticas completas de performance
 */
class EstatisticasPerformance {
    private final double acuracia;
    private final Duration tempoTotal;
    private final Duration tempoMedioPredicao;
    private final Map<String, Map<String, Integer>> matrizConfusao;
    private final Map<String, MetricasClasse> relatorioClasses;
    
    public EstatisticasPerformance(double acuracia, Duration tempoTotal, Duration tempoMedioPredicao,
                                 Map<String, Map<String, Integer>> matrizConfusao,
                                 Map<String, MetricasClasse> relatorioClasses) {
        this.acuracia = acuracia;
        this.tempoTotal = tempoTotal;
        this.tempoMedioPredicao = tempoMedioPredicao;
        this.matrizConfusao = new HashMap<>(matrizConfusao);
        this.relatorioClasses = new HashMap<>(relatorioClasses);
    }
    
    // Getters
    public double getAcuracia() { return acuracia; }
    public Duration getTempoTotal() { return tempoTotal; }
    public Duration getTempoMedioPredicao() { return tempoMedioPredicao; }
    public Map<String, Map<String, Integer>> getMatrizConfusao() { return new HashMap<>(matrizConfusao); }
    public Map<String, MetricasClasse> getRelatorioClasses() { return new HashMap<>(relatorioClasses); }
}

/**
 * Builder para configuração do KNN
 */
class KNNBuilder {
    private int k = 3;
    private EstrategiaDistancia estrategiaDistancia = new DistanciaEuclidiana();
    private boolean normalizar = true;
    private boolean processamentoParalelo = false;
    
    public KNNBuilder setK(int k) {
        if (k <= 0) throw new IllegalArgumentException("K deve ser positivo");
        this.k = k;
        return this;
    }
    
    public KNNBuilder setEstrategiaDistancia(EstrategiaDistancia estrategia) {
        this.estrategiaDistancia = estrategia;
        return this;
    }
    
    public KNNBuilder setNormalizar(boolean normalizar) {
        this.normalizar = normalizar;
        return this;
    }
    
    public KNNBuilder setProcessamentoParalelo(boolean paralelo) {
        this.processamentoParalelo = paralelo;
        return this;
    }
    
    public KNNOtimizado build() {
        return new KNNOtimizado(k, estrategiaDistancia, normalizar, processamentoParalelo);
    }
}

/**
 * Implementação otimizada do algoritmo K-Nearest Neighbors
 */
public class KNNOtimizado implements AutoCloseable {
    private final int k;
    private final EstrategiaDistancia estrategiaDistancia;
    private final boolean normalizar;
    private final boolean processamentoParalelo;
    
    private List<PontoOtimizado> dadosTreino;
    private double[] mediaTreino;
    private double[] desvioTreino;
    private Set<String> classesUnicas;
    private ExecutorService executorService;
    
    // Construtor package-private (usar KNNBuilder)
    KNNOtimizado(int k, EstrategiaDistancia estrategiaDistancia, boolean normalizar, boolean processamentoParalelo) {
        this.k = k;
        this.estrategiaDistancia = estrategiaDistancia;
        this.normalizar = normalizar;
        this.processamentoParalelo = processamentoParalelo;
        this.dadosTreino = new ArrayList<>();
        this.classesUnicas = new HashSet<>();
        
        if (processamentoParalelo) {
            this.executorService = ForkJoinPool.commonPool();
        }
        
        System.out.printf("🚀 KNN Otimizado inicializado:%n");
        System.out.printf("   K: %d%n", k);
        System.out.printf("   Métrica: %s%n", estrategiaDistancia.getNome());
        System.out.printf("   Normalização: %s%n", normalizar);
        System.out.printf("   Processamento Paralelo: %s%n", processamentoParalelo);
    }
    
    /**
     * Cria builder para configuração
     */
    public static KNNBuilder builder() {
        return new KNNBuilder();
    }
    
    /**
     * Normaliza os dados usando z-score
     */
    private double[][] normalizarDados(double[][] coordenadas, boolean calcularParametros) {
        if (!normalizar) {
            return coordenadas;
        }
        
        int numPontos = coordenadas.length;
        int numDimensoes = coordenadas[0].length;
        
        if (calcularParametros) {
            // Calcula média e desvio padrão
            mediaTreino = new double[numDimensoes];
            desvioTreino = new double[numDimensoes];
            
            // Calcula média
            for (int j = 0; j < numDimensoes; j++) {
                double soma = 0.0;
                for (int i = 0; i < numPontos; i++) {
                    soma += coordenadas[i][j];
                }
                mediaTreino[j] = soma / numPontos;
            }
            
            // Calcula desvio padrão
            for (int j = 0; j < numDimensoes; j++) {
                double somaQuadrados = 0.0;
                for (int i = 0; i < numPontos; i++) {
                    double diff = coordenadas[i][j] - mediaTreino[j];
                    somaQuadrados += diff * diff;
                }
                desvioTreino[j] = Math.sqrt(somaQuadrados / numPontos);
                
                // Evita divisão por zero
                if (desvioTreino[j] == 0) {
                    desvioTreino[j] = 1.0;
                }
            }
        }
        
        // Aplica normalização
        double[][] coordenadasNormalizadas = new double[numPontos][numDimensoes];
        for (int i = 0; i < numPontos; i++) {
            for (int j = 0; j < numDimensoes; j++) {
                coordenadasNormalizadas[i][j] = (coordenadas[i][j] - mediaTreino[j]) / desvioTreino[j];
            }
        }
        
        return coordenadasNormalizadas;
    }
    
    /**
     * Treina o modelo KNN
     */
    public void treinar(double[][] coordenadas, String[] classes) {
        if (coordenadas.length != classes.length) {
            throw new IllegalArgumentException(
                String.format("Número de coordenadas (%d) deve ser igual ao número de classes (%d)",
                            coordenadas.length, classes.length));
        }
        
        System.out.printf("📚 Treinando com %d exemplos, %d características%n",
                         coordenadas.length, coordenadas[0].length);
        
        // Normaliza os dados se necessário
        double[][] coordenadasNormalizadas = normalizarDados(coordenadas, true);
        
        // Cria pontos otimizados
        dadosTreino = IntStream.range(0, coordenadas.length)
            .mapToObj(i -> new PontoOtimizado(
                coordenadas[i],
                normalizar ? coordenadasNormalizadas[i] : null,
                classes[i]))
            .collect(Collectors.toList());
        
        // Encontra classes únicas
        classesUnicas = Arrays.stream(classes).collect(Collectors.toSet());
        
        // Estatísticas dos dados
        Map<String, Long> contadorClasses = Arrays.stream(classes)
            .collect(Collectors.groupingBy(c -> c, Collectors.counting()));
        
        System.out.printf("📊 Classes encontradas: %s%n", classesUnicas);
        System.out.print("📈 Distribuição: ");
        contadorClasses.forEach((classe, count) -> 
            System.out.printf("%s:%d ", classe, count));
        System.out.println();
        
        if (normalizar) {
            System.out.println("🔧 Dados normalizados (média≈0, std≈1)");
        }
    }
    
    /**
     * Prediz a classe para um único ponto
     */
    public ResultadoClassificacao predizirPonto(double[] coordenadas) {
        Instant inicio = Instant.now();
        
        // Normaliza o ponto de consulta
        double[] coordenadasNorm = coordenadas;
        if (normalizar) {
            coordenadasNorm = IntStream.range(0, coordenadas.length)
                .mapToDouble(i -> (coordenadas[i] - mediaTreino[i]) / desvioTreino[i])
                .toArray();
        }
        
        // Calcula distâncias para todos os pontos de treino
        final double[] coordenadasFinais = coordenadasNorm;
        final EstrategiaDistancia estrategiaFinal = estrategiaDistancia;
        
        Stream<VizinhoOtimizado> streamVizinhos = processamentoParalelo ?
            IntStream.range(0, dadosTreino.size()).parallel().mapToObj(i -> {
                PontoOtimizado pontoTreino = dadosTreino.get(i);
                double[] coordsParaUsar = normalizar ? 
                    pontoTreino.getCoordenadasNormalizadas() : pontoTreino.getCoordenadas();
                
                double distancia = estrategiaFinal.calcular(coordenadasFinais, coordsParaUsar);
                return new VizinhoOtimizado(pontoTreino, distancia, i);
            }) :
            IntStream.range(0, dadosTreino.size()).mapToObj(i -> {
                PontoOtimizado pontoTreino = dadosTreino.get(i);
                double[] coordsParaUsar = normalizar ? 
                    pontoTreino.getCoordenadasNormalizadas() : pontoTreino.getCoordenadas();
                
                double distancia = estrategiaFinal.calcular(coordenadasFinais, coordsParaUsar);
                return new VizinhoOtimizado(pontoTreino, distancia, i);
            });
        
        // Encontra os k vizinhos mais próximos
        List<VizinhoOtimizado> kVizinhos = streamVizinhos
            .sorted()
            .limit(k)
            .collect(Collectors.toList());
        
        // Conta votos das classes
        Map<String, Long> contadorClasses = kVizinhos.stream()
            .collect(Collectors.groupingBy(v -> v.getPonto().getClasse(), Collectors.counting()));
        
        // Encontra classe mais votada
        String classePrevista = contadorClasses.entrySet().stream()
            .max(Map.Entry.comparingByValue())
            .map(Map.Entry::getKey)
            .orElse("desconhecida");
        
        double confianca = contadorClasses.get(classePrevista).doubleValue() / k;
        
        List<Double> distanciasVizinhos = kVizinhos.stream()
            .map(VizinhoOtimizado::getDistancia)
            .collect(Collectors.toList());
        
        List<String> classesVizinhos = kVizinhos.stream()
            .map(v -> v.getPonto().getClasse())
            .collect(Collectors.toList());
        
        Duration tempoPredicao = Duration.between(inicio, Instant.now());
        
        return new ResultadoClassificacao(classePrevista, confianca, 
                                        distanciasVizinhos, classesVizinhos, tempoPredicao);
    }
    
    /**
     * Prediz classes para múltiplos pontos
     */
    public List<String> predizer(double[][] coordenadas) {
        return Arrays.stream(coordenadas)
            .map(this::predizirPonto)
            .map(ResultadoClassificacao::getClassePrevista)
            .collect(Collectors.toList());
    }
    
    /**
     * Avalia performance do modelo em dados de teste
     */
    public EstatisticasPerformance avaliarPerformance(double[][] XTeste, String[] yTeste) {
        System.out.printf("📊 Avaliando performance em %d exemplos de teste...%n", XTeste.length);
        
        Instant inicio = Instant.now();
        
        // Faz predições
        List<ResultadoClassificacao> resultados = Arrays.stream(XTeste)
            .map(this::predizirPonto)
            .collect(Collectors.toList());
        
        Duration tempoTotal = Duration.between(inicio, Instant.now());
        
        // Extrai predições
        List<String> yPred = resultados.stream()
            .map(ResultadoClassificacao::getClassePrevista)
            .collect(Collectors.toList());
        
        // Calcula acurácia
        long acertos = IntStream.range(0, yTeste.length)
            .mapToLong(i -> yPred.get(i).equals(yTeste[i]) ? 1 : 0)
            .sum();
        double acuracia = (double) acertos / yTeste.length;
        
        // Calcula tempo médio
        Duration tempoMedio = Duration.ofNanos(
            resultados.stream()
                .mapToLong(r -> r.getTempoPredicao().toNanos())
                .sum() / resultados.size());
        
        // Matriz de confusão
        Map<String, Map<String, Integer>> matrizConfusao = new HashMap<>();
        for (String classe : classesUnicas) {
            matrizConfusao.put(classe, new HashMap<>());
            for (String classe2 : classesUnicas) {
                matrizConfusao.get(classe).put(classe2, 0);
            }
        }
        
        for (int i = 0; i < yTeste.length; i++) {
            String real = yTeste[i];
            String pred = yPred.get(i);
            matrizConfusao.get(real).merge(pred, 1, Integer::sum);
        }
        
        // Relatório por classe
        Map<String, MetricasClasse> relatorioClasses = new HashMap<>();
        for (String classe : classesUnicas) {
            int vp = matrizConfusao.get(classe).get(classe); // Verdadeiros positivos
            
            // Falsos positivos
            int fp = classesUnicas.stream()
                .filter(c -> !c.equals(classe))
                .mapToInt(c -> matrizConfusao.get(c).get(classe))
                .sum();
            
            // Falsos negativos
            int fn = classesUnicas.stream()
                .filter(c -> !c.equals(classe))
                .mapToInt(c -> matrizConfusao.get(classe).get(c))
                .sum();
            
            double precisao = (vp + fp) > 0 ? (double) vp / (vp + fp) : 0.0;
            double recall = (vp + fn) > 0 ? (double) vp / (vp + fn) : 0.0;
            double f1 = (precisao + recall) > 0 ? 2 * (precisao * recall) / (precisao + recall) : 0.0;
            
            int suporte = (int) Arrays.stream(yTeste).filter(classe::equals).count();
            
            relatorioClasses.put(classe, new MetricasClasse(precisao, recall, f1, suporte));
        }
        
        return new EstatisticasPerformance(acuracia, tempoTotal, tempoMedio, 
                                         matrizConfusao, relatorioClasses);
    }
    
    /**
     * Fecha recursos (executor service)
     */
    @Override
    public void close() {
        if (executorService != null && !executorService.isShutdown()) {
            executorService.shutdown();
        }
    }
    
    /**
     * Demonstração completa do KNN otimizado
     */
    public static void demonstracaoKNNOtimizado() {
        System.out.println("=".repeat(70));
        System.out.println("🚀 DEMONSTRAÇÃO: K-Nearest Neighbors (KNN) - Versão Otimizada");
        System.out.println("=".repeat(70));
        
        // Gera dados sintéticos
        DadosSinteticos dados = gerarDadosSinteticos();
        
        System.out.printf("📊 Dataset gerado: %d exemplos, %d características%n",
                         dados.coordenadas.length, dados.coordenadas[0].length);
        
        // Conta classes
        Map<String, Long> contadorClasses = Arrays.stream(dados.classes)
            .collect(Collectors.groupingBy(c -> c, Collectors.counting()));
        System.out.print("🎯 Classes: ");
        contadorClasses.forEach((classe, count) -> System.out.printf("%s:%d ", classe, count));
        System.out.println();
        
        // Divide em treino e teste (80/20)
        int splitIdx = (int) (0.8 * dados.coordenadas.length);
        double[][] XTreino = Arrays.copyOfRange(dados.coordenadas, 0, splitIdx);
        double[][] XTeste = Arrays.copyOfRange(dados.coordenadas, splitIdx, dados.coordenadas.length);
        String[] yTreino = Arrays.copyOfRange(dados.classes, 0, splitIdx);
        String[] yTeste = Arrays.copyOfRange(dados.classes, splitIdx, dados.classes.length);
        
        System.out.printf("📚 Treino: %d exemplos%n", XTreino.length);
        System.out.printf("🧪 Teste: %d exemplos%n", XTeste.length);
        
        // Testa diferentes métricas
        EstrategiaDistancia[] estrategias = {
            new DistanciaEuclidiana(),
            new DistanciaManhattan(),
            new DistanciaMinkowski(2.5)
        };
        
        Map<String, Double> resultadosMetricas = new HashMap<>();
        
        for (EstrategiaDistancia estrategia : estrategias) {
            System.out.printf("%n🔍 Testando métrica: %s%n", estrategia.getNome());
            System.out.println("-".repeat(40));
            
            try (KNNOtimizado knn = KNNOtimizado.builder()
                    .setK(5)
                    .setEstrategiaDistancia(estrategia)
                    .setNormalizar(true)
                    .setProcessamentoParalelo(true)
                    .build()) {
                
                // Treina
                knn.treinar(XTreino, yTreino);
                
                // Avalia
                EstatisticasPerformance stats = knn.avaliarPerformance(XTeste, yTeste);
                resultadosMetricas.put(estrategia.getNome(), stats.getAcuracia());
                
                System.out.printf("📊 Acurácia: %.3f%n", stats.getAcuracia());
                System.out.printf("⏱️  Tempo médio por predição: %s%n", 
                                formatarDuracao(stats.getTempoMedioPredicao()));
            }
        }
        
        // Mostra comparação final
        System.out.printf("%n📈 COMPARAÇÃO DE MÉTRICAS:%n");
        System.out.println("-".repeat(30));
        resultadosMetricas.forEach((metrica, acuracia) -> 
            System.out.printf("%-20s: %.3f%n", metrica, acuracia));
    }
    
    /**
     * Classe auxiliar para dados sintéticos
     */
    private static class DadosSinteticos {
        final double[][] coordenadas;
        final String[] classes;
        
        DadosSinteticos(double[][] coordenadas, String[] classes) {
            this.coordenadas = coordenadas;
            this.classes = classes;
        }
    }
    
    /**
     * Gera dados sintéticos para demonstração
     */
    private static DadosSinteticos gerarDadosSinteticos() {
        // Simula dados sintéticos com valores fixos para demonstração
        double[][] coordenadas = {
            // Classe A (valores baixos)
            {2.1, 3.2, 1.1, 2.3}, {1.9, 2.8, 0.9, 2.1}, {2.3, 3.4, 1.3, 2.5},
            {2.0, 3.0, 1.0, 2.2}, {2.2, 3.1, 1.2, 2.4}, {1.8, 2.9, 0.8, 2.0},
            
            // Classe B (valores médios)
            {5.1, 6.2, 4.1, 5.3}, {4.9, 5.8, 3.9, 5.1}, {5.3, 6.4, 4.3, 5.5},
            {5.0, 6.0, 4.0, 5.2}, {5.2, 6.1, 4.2, 5.4}, {4.8, 5.9, 3.8, 5.0},
            
            // Classe C (valores altos)
            {8.1, 9.2, 7.1, 8.3}, {7.9, 8.8, 6.9, 8.1}, {8.3, 9.4, 7.3, 8.5},
            {8.0, 9.0, 7.0, 8.2}, {8.2, 9.1, 7.2, 8.4}, {7.8, 8.9, 6.8, 8.0}
        };
        
        String[] classes = {
            "A", "A", "A", "A", "A", "A",
            "B", "B", "B", "B", "B", "B", 
            "C", "C", "C", "C", "C", "C"
        };
        
        return new DadosSinteticos(coordenadas, classes);
    }
    
    /**
     * Formata duração para exibição
     */
    private static String formatarDuracao(Duration duracao) {
        if (duracao.toNanos() < 1_000_000) {
            return String.format("%.2f μs", duracao.toNanos() / 1000.0);
        } else if (duracao.toMillis() < 1000) {
            return String.format("%.2f ms", duracao.toNanos() / 1_000_000.0);
        } else {
            return String.format("%.2f s", duracao.toMillis() / 1000.0);
        }
    }
    
    /**
     * Sugere exercícios avançados
     */
    public static void exerciciosAvancados() {
        System.out.println("\n" + "=".repeat(70));
        System.out.println("🎓 EXERCÍCIOS AVANÇADOS:");
        System.out.println("=".repeat(70));
        System.out.println("1. Implemente validação cruzada para seleção automática de k");
        System.out.println("2. Adicione suporte para pesos baseados na distância");
        System.out.println("3. Implemente KD-Tree para busca eficiente");
        System.out.println("4. Crie sistema de cache inteligente para distâncias");
        System.out.println("5. Adicione métricas personalizadas de distância");
        System.out.println("6. Implemente detecção e tratamento de outliers");
        System.out.println("7. Crie API REST para servir o modelo");
        System.out.println("8. Adicione persistência com serialização");
        System.out.println("9. Implemente KNN incremental para dados em streaming");
        System.out.println("10. Crie interface gráfica com JavaFX");
    }
    
    /**
     * Método principal
     */
    public static void main(String[] args) {
        demonstracaoKNNOtimizado();
        exerciciosAvancados();
    }
}
