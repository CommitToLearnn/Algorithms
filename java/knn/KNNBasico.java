/*
 * K-Nearest Neighbors (KNN) - Implementação Básica em Java
 * ========================================================
 * 
 * Algoritmo de classificação que determina a classe de um ponto baseado
 * na classe majoritária dos K vizinhos mais próximos.
 * 
 * Complexidade:
 * - Tempo: O(n * d) para cada predição
 * - Espaço: O(n * d) para armazenar dados de treino
 * 
 * Características desta implementação:
 * - Orientação a objetos clara
 * - Encapsulamento adequado
 * - Comentários extensos para aprendizado
 * - Tratamento de exceções
 */

import java.util.*;

/**
 * Representa um ponto no espaço n-dimensional com sua classe
 */
class Ponto {
    private double[] coordenadas;
    private String classe;
    
    public Ponto(double[] coordenadas, String classe) {
        this.coordenadas = Arrays.copyOf(coordenadas, coordenadas.length);
        this.classe = classe;
    }
    
    public double[] getCoordenadas() {
        return Arrays.copyOf(coordenadas, coordenadas.length);
    }
    
    public String getClasse() {
        return classe;
    }
    
    @Override
    public String toString() {
        return String.format("Ponto{coordenadas=%s, classe='%s'}", 
                           Arrays.toString(coordenadas), classe);
    }
}

/**
 * Representa um vizinho com sua distância para o ponto de consulta
 */
class Vizinho implements Comparable<Vizinho> {
    private Ponto ponto;
    private double distancia;
    
    public Vizinho(Ponto ponto, double distancia) {
        this.ponto = ponto;
        this.distancia = distancia;
    }
    
    public Ponto getPonto() {
        return ponto;
    }
    
    public double getDistancia() {
        return distancia;
    }
    
    @Override
    public int compareTo(Vizinho outro) {
        return Double.compare(this.distancia, outro.distancia);
    }
    
    @Override
    public String toString() {
        return String.format("Vizinho{distância=%.3f, classe='%s'}", 
                           distancia, ponto.getClasse());
    }
}

/**
 * Implementação básica do algoritmo K-Nearest Neighbors
 */
public class KNNBasico {
    private int k;
    private List<Ponto> dadosTreino;
    
    /**
     * Construtor do classificador KNN
     * @param k Número de vizinhos mais próximos a considerar
     */
    public KNNBasico(int k) {
        if (k <= 0) {
            throw new IllegalArgumentException("K deve ser positivo");
        }
        
        this.k = k;
        this.dadosTreino = new ArrayList<>();
        
        System.out.printf("🎯 KNN Básico inicializado com k=%d%n", k);
    }
    
    /**
     * Calcula a distância euclidiana entre dois pontos
     * @param p1 Primeiro ponto
     * @param p2 Segundo ponto
     * @return Distância euclidiana
     * @throws IllegalArgumentException se os pontos têm dimensões diferentes
     */
    public double calcularDistanciaEuclidiana(double[] p1, double[] p2) {
        if (p1.length != p2.length) {
            throw new IllegalArgumentException("Pontos devem ter a mesma dimensão");
        }
        
        System.out.println("   📏 Calculando distância euclidiana:");
        
        double somaQuadrados = 0.0;
        for (int i = 0; i < p1.length; i++) {
            double diferenca = p1[i] - p2[i];
            double quadrado = diferenca * diferenca;
            somaQuadrados += quadrado;
            
            System.out.printf("      Dimensão %d: (%.3f - %.3f)² = %.3f%n", 
                            i + 1, p1[i], p2[i], quadrado);
        }
        
        double distancia = Math.sqrt(somaQuadrados);
        System.out.printf("      Distância: √%.3f = %.3f%n", somaQuadrados, distancia);
        
        return distancia;
    }
    
    /**
     * Treina o modelo KNN (armazena os dados de treinamento)
     * @param dados Lista de pontos para treinamento
     */
    public void treinar(List<Ponto> dados) {
        this.dadosTreino = new ArrayList<>(dados);
        
        System.out.printf("📚 Modelo treinado com %d exemplos%n", dadosTreino.size());
        
        // Conta distribuição das classes
        Map<String, Integer> contadorClasses = new HashMap<>();
        for (Ponto ponto : dados) {
            contadorClasses.merge(ponto.getClasse(), 1, Integer::sum);
        }
        
        System.out.print("📊 Distribuição das classes: ");
        contadorClasses.forEach((classe, count) -> 
            System.out.printf("%s:%d ", classe, count));
        System.out.println();
    }
    
    /**
     * Encontra os k vizinhos mais próximos de um ponto
     * @param pontoConsulta Ponto para o qual encontrar vizinhos
     * @return Lista dos k vizinhos mais próximos
     * @throws IllegalStateException se o modelo não foi treinado
     */
    public List<Vizinho> encontrarKVizinhos(double[] pontoConsulta) {
        if (dadosTreino.isEmpty()) {
            throw new IllegalStateException("Modelo não foi treinado. Chame treinar() primeiro.");
        }
        
        System.out.printf("%n🔍 Buscando %d vizinhos mais próximos para %s%n", 
                         k, Arrays.toString(pontoConsulta));
        
        // Calcula distâncias para todos os pontos de treino
        List<Vizinho> vizinhos = new ArrayList<>();
        
        for (int i = 0; i < dadosTreino.size(); i++) {
            Ponto pontoTreino = dadosTreino.get(i);
            
            System.out.printf("%n📏 Calculando distância para ponto %d: %s (classe: %s)%n", 
                            i + 1, Arrays.toString(pontoTreino.getCoordenadas()), 
                            pontoTreino.getClasse());
            
            double distancia = calcularDistanciaEuclidiana(pontoConsulta, 
                                                         pontoTreino.getCoordenadas());
            
            vizinhos.add(new Vizinho(pontoTreino, distancia));
        }
        
        // Ordena vizinhos por distância (crescente)
        Collections.sort(vizinhos);
        
        // Retorna apenas os k primeiros
        List<Vizinho> kVizinhos = vizinhos.subList(0, Math.min(k, vizinhos.size()));
        
        System.out.printf("%n🎯 %d vizinhos mais próximos:%n", kVizinhos.size());
        for (int i = 0; i < kVizinhos.size(); i++) {
            Vizinho vizinho = kVizinhos.get(i);
            System.out.printf("   %dº vizinho: distância=%.3f, classe=%s%n", 
                            i + 1, vizinho.getDistancia(), vizinho.getPonto().getClasse());
        }
        
        return kVizinhos;
    }
    
    /**
     * Classifica um ponto baseado nos k vizinhos mais próximos
     * @param pontoConsulta Ponto a ser classificado
     * @return Classe prevista
     */
    public String classificar(double[] pontoConsulta) {
        // Encontra os k vizinhos mais próximos
        List<Vizinho> kVizinhos = encontrarKVizinhos(pontoConsulta);
        
        // Conta a frequência de cada classe
        Map<String, Integer> contadorClasses = new HashMap<>();
        for (Vizinho vizinho : kVizinhos) {
            String classe = vizinho.getPonto().getClasse();
            contadorClasses.merge(classe, 1, Integer::sum);
        }
        
        System.out.print("%n📊 Contagem de classes nos vizinhos: ");
        contadorClasses.forEach((classe, count) -> 
            System.out.printf("%s:%d ", classe, count));
        System.out.println();
        
        // Encontra a classe mais frequente
        String classePrevista = contadorClasses.entrySet().stream()
            .max(Map.Entry.comparingByValue())
            .map(Map.Entry::getKey)
            .orElse("desconhecida");
        
        int maxCount = contadorClasses.get(classePrevista);
        double confianca = (double) maxCount / kVizinhos.size();
        
        System.out.printf("🎯 Classe prevista: %s%n", classePrevista);
        System.out.printf("🔢 Confiança: %.1f%% (%d/%d vizinhos)%n", 
                         confianca * 100, maxCount, kVizinhos.size());
        
        return classePrevista;
    }
    
    /**
     * Demonstração do algoritmo KNN com exemplo prático
     */
    public static void demonstracaoKNNBasico() {
        System.out.println("=".repeat(60));
        System.out.println("🤖 DEMONSTRAÇÃO: K-Nearest Neighbors (KNN) - Versão Básica");
        System.out.println("=".repeat(60));
        
        // Cria dados de exemplo: classificação de animais
        // [peso_kg, altura_cm] -> tipo_animal
        List<Ponto> dadosAnimais = Arrays.asList(
            new Ponto(new double[]{0.5, 20}, "gato"),
            new Ponto(new double[]{0.7, 25}, "gato"),
            new Ponto(new double[]{0.3, 18}, "gato"),
            new Ponto(new double[]{25, 60}, "cão"),
            new Ponto(new double[]{30, 65}, "cão"),
            new Ponto(new double[]{20, 55}, "cão"),
            new Ponto(new double[]{500, 180}, "cavalo"),
            new Ponto(new double[]{450, 175}, "cavalo"),
            new Ponto(new double[]{520, 185}, "cavalo")
        );
        
        System.out.printf("🐾 Dataset: Classificação de animais com %d exemplos%n", 
                         dadosAnimais.size());
        System.out.println("📊 Características: [peso_kg, altura_cm]");
        
        // Inicializa o classificador
        KNNBasico knn = new KNNBasico(3);
        
        // Treina o modelo
        knn.treinar(dadosAnimais);
        
        // Testa com diferentes pontos
        double[][] pontosTeste = {
            {0.6, 22},   // Deve ser gato
            {28, 62},    // Deve ser cão
            {480, 178},  // Deve ser cavalo
            {10, 40}     // Caso ambíguo
        };
        
        System.out.println("\n" + "=".repeat(40));
        System.out.println("🧪 TESTANDO CLASSIFICAÇÕES");
        System.out.println("=".repeat(40));
        
        for (int i = 0; i < pontosTeste.length; i++) {
            double[] ponto = pontosTeste[i];
            System.out.printf("%n🔍 TESTE %d: Classificando ponto %s%n", 
                            i + 1, Arrays.toString(ponto));
            System.out.println("-".repeat(40));
            
            try {
                String classePrevista = knn.classificar(ponto);
                System.out.printf("✅ Resultado final: %s → %s%n", 
                                Arrays.toString(ponto), classePrevista);
            } catch (Exception e) {
                System.out.printf("❌ Erro: %s%n", e.getMessage());
            }
        }
    }
    
    /**
     * Demonstra como diferentes valores de k afetam a classificação
     */
    public static void exemploComparacaoK() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("📈 COMPARAÇÃO: Efeito de diferentes valores de K");
        System.out.println("=".repeat(60));
        
        // Dados simples para demonstração
        List<Ponto> dados = Arrays.asList(
            new Ponto(new double[]{1, 1}, "A"),
            new Ponto(new double[]{1, 2}, "A"),
            new Ponto(new double[]{2, 1}, "A"),
            new Ponto(new double[]{5, 5}, "B"),
            new Ponto(new double[]{5, 6}, "B"),
            new Ponto(new double[]{6, 5}, "B"),
            new Ponto(new double[]{3, 3}, "A") // Ponto intermediário
        );
        
        double[] pontoTeste = {3, 4};
        int[] valoresK = {1, 3, 5};
        
        for (int k : valoresK) {
            System.out.printf("%n🎯 Testando com k=%d%n", k);
            System.out.println("-".repeat(30));
            
            try {
                KNNBasico knn = new KNNBasico(k);
                knn.treinar(dados);
                
                String resultado = knn.classificar(pontoTeste);
                System.out.printf("📊 Com k=%d: %s → %s%n", 
                                k, Arrays.toString(pontoTeste), resultado);
            } catch (Exception e) {
                System.out.printf("❌ Erro: %s%n", e.getMessage());
            }
        }
    }
    
    /**
     * Sugere exercícios práticos para aprendizado
     */
    public static void exerciciosPraticos() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("🎓 EXERCÍCIOS SUGERIDOS:");
        System.out.println("=".repeat(60));
        System.out.println("1. Implemente outras métricas de distância (Manhattan, Minkowski)");
        System.out.println("2. Adicione validação mais robusta dos dados de entrada");
        System.out.println("3. Implemente KNN para regressão (predizer valores numéricos)");
        System.out.println("4. Adicione função para encontrar o melhor k automaticamente");
        System.out.println("5. Crie classes para diferentes métricas de avaliação");
        System.out.println("6. Implemente normalização automática dos dados");
        System.out.println("7. Adicione suporte para pesos baseados na distância");
        System.out.println("8. Crie interface gráfica para visualização");
    }
    
    /**
     * Método principal - executa todas as demonstrações
     */
    public static void main(String[] args) {
        // Executa as demonstrações
        demonstracaoKNNBasico();
        exemploComparacaoK();
        exerciciosPraticos();
    }
}
