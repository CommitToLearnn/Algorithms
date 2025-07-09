/**
 * Implementação Otimizada do Algoritmo BFS (Busca em Largura)
 * ===========================================================
 * 
 * Esta implementação inclui várias otimizações:
 * - Uso de ArrayDeque para melhor performance
 * - Verificação de visitados mais eficiente
 * - Suporte a diferentes tipos de dados genéricos
 * - Estatísticas de performance
 * - Parada antecipada quando destino é encontrado
 * 
 * Características desta versão:
 * - Complexidade: O(V + E) onde V = vértices, E = arestas
 * - Uso de estruturas de dados otimizadas
 * - Interface mais flexível e robusta
 * - Coleta de métricas de performance
 * 
 * @author matheussricardoo
 * @version 2.0
 * @since Julho 2025
 */

package bfs.otimizado;

import java.util.*;

/**
 * Classe que armazena estatísticas de performance do BFS
 */
class EstatisticasPerformance {
    private long totalOperacoes;
    private long tempoTotalExecucao;
    private int totalVerticesVisitados;
    private int totalArestasExploradas;
    private long tempoUltimaOperacao;
    
    public EstatisticasPerformance() {
        this.totalOperacoes = 0;
        this.tempoTotalExecucao = 0;
        this.totalVerticesVisitados = 0;
        this.totalArestasExploradas = 0;
    }
    
    public void registrarOperacao(long tempoExecucao, int verticesVisitados, int arestasExploradas) {
        this.totalOperacoes++;
        this.tempoTotalExecucao += tempoExecucao;
        this.totalVerticesVisitados += verticesVisitados;
        this.totalArestasExploradas += arestasExploradas;
        this.tempoUltimaOperacao = tempoExecucao;
    }
    
    public void imprimir() {
        System.out.println("\n📊 ESTATÍSTICAS DE PERFORMANCE");
        System.out.println("=".repeat(40));
        System.out.println("📈 Total de operações BFS: " + totalOperacoes);
        System.out.println("⏱️  Tempo total de execução: " + (tempoTotalExecucao / 1_000_000.0) + " ms");
        System.out.println("🔍 Vértices visitados: " + totalVerticesVisitados);
        System.out.println("🔗 Arestas exploradas: " + totalArestasExploradas);
        if (totalOperacoes > 0) {
            System.out.println("⚡ Tempo médio por operação: " + 
                             (tempoTotalExecucao / totalOperacoes / 1_000_000.0) + " ms");
        }
        System.out.println("⏰ Última operação: " + (tempoUltimaOperacao / 1_000_000.0) + " ms");
    }
}

/**
 * Classe que armazena o resultado de uma operação BFS
 */
class ResultadoBFS<T> {
    private final T verticeOrigem;
    private final T verticeDestino;
    private final List<T> caminho;
    private final Map<T, Integer> distancias;
    private final boolean encontrado;
    private final long tempoExecucao;
    private final int verticesVisitados;
    private final int arestasExploradas;
    
    public ResultadoBFS(T origem, T destino, List<T> caminho, Map<T, Integer> distancias, 
                       boolean encontrado, long tempoExecucao, int verticesVisitados, int arestasExploradas) {
        this.verticeOrigem = origem;
        this.verticeDestino = destino;
        this.caminho = caminho != null ? new ArrayList<>(caminho) : null;
        this.distancias = distancias != null ? new HashMap<>(distancias) : null;
        this.encontrado = encontrado;
        this.tempoExecucao = tempoExecucao;
        this.verticesVisitados = verticesVisitados;
        this.arestasExploradas = arestasExploradas;
    }
    
    public void imprimirResumo() {
        System.out.println("🎯 Origem: " + verticeOrigem);
        if (verticeDestino != null) {
            System.out.println("🏁 Destino: " + verticeDestino);
            System.out.println("✅ Encontrado: " + (encontrado ? "Sim" : "Não"));
        }
        
        if (caminho != null && !caminho.isEmpty()) {
            System.out.println("🛣️  Caminho encontrado: " + caminho);
            System.out.println("📏 Distância: " + (caminho.size() - 1) + " saltos");
        }
        
        if (distancias != null && !distancias.isEmpty()) {
            System.out.println("📊 Distâncias calculadas: " + distancias.size() + " vértices");
        }
        
        System.out.println("⏱️  Tempo de execução: " + (tempoExecucao / 1_000_000.0) + " ms");
        System.out.println("🔍 Vértices visitados: " + verticesVisitados);
        System.out.println("🔗 Arestas exploradas: " + arestasExploradas);
    }
    
    public List<T> getCaminho() { return caminho; }
    public Map<T, Integer> getDistancias() { return distancias; }
    public boolean isEncontrado() { return encontrado; }
    public long getTempoExecucao() { return tempoExecucao; }
}

/**
 * Implementação otimizada de um grafo para BFS
 */
class GrafoBFSOtimizado<T> {
    private final Map<T, Set<T>> listaAdjacencia;
    private final EstatisticasPerformance estatisticas;
    
    public GrafoBFSOtimizado() {
        this.listaAdjacencia = new HashMap<>();
        this.estatisticas = new EstatisticasPerformance();
    }
    
    public void adicionarVertice(T vertice) {
        listaAdjacencia.putIfAbsent(vertice, new HashSet<>());
        System.out.println("  ✅ Vértice adicionado: " + vertice);
    }
    
    public void adicionarAresta(T origem, T destino) {
        listaAdjacencia.putIfAbsent(origem, new HashSet<>());
        listaAdjacencia.putIfAbsent(destino, new HashSet<>());
        
        listaAdjacencia.get(origem).add(destino);
        listaAdjacencia.get(destino).add(origem);
        
        System.out.println("  🔗 Aresta adicionada: " + origem + " ↔ " + destino);
    }
    
    public void imprimirGrafo() {
        System.out.println("\n🗺️  Estrutura do Grafo:");
        System.out.println("=" + "=".repeat(30));
        
        for (Map.Entry<T, Set<T>> entry : listaAdjacencia.entrySet()) {
            System.out.println("📍 " + entry.getKey() + " → " + entry.getValue());
        }
    }
    
    public void imprimirEstatisticasGrafo() {
        int vertices = listaAdjacencia.size();
        int arestas = listaAdjacencia.values().stream()
                                   .mapToInt(Set::size)
                                   .sum() / 2;
        
        System.out.println("\n📈 Estatísticas do Grafo:");
        System.out.println("  🔵 Vértices: " + vertices);
        System.out.println("  🔗 Arestas: " + arestas);
        System.out.println("  📊 Densidade: " + String.format("%.2f%%", 
                         (2.0 * arestas / (vertices * (vertices - 1))) * 100));
    }
    
    public ResultadoBFS<T> bfsCompleto(T origem) {
        long inicioTempo = System.nanoTime();
        
        if (!listaAdjacencia.containsKey(origem)) {
            return new ResultadoBFS<>(origem, null, null, null, false, 0, 0, 0);
        }
        
        ArrayDeque<T> fila = new ArrayDeque<>();
        Set<T> visitados = new HashSet<>();
        Map<T, Integer> distancias = new HashMap<>();
        Map<T, T> predecessores = new HashMap<>();
        
        fila.offer(origem);
        visitados.add(origem);
        distancias.put(origem, 0);
        
        int verticesVisitados = 0;
        int arestasExploradas = 0;
        
        while (!fila.isEmpty()) {
            T atual = fila.poll();
            verticesVisitados++;
            
            for (T vizinho : listaAdjacencia.get(atual)) {
                arestasExploradas++;
                
                if (!visitados.contains(vizinho)) {
                    visitados.add(vizinho);
                    distancias.put(vizinho, distancias.get(atual) + 1);
                    predecessores.put(vizinho, atual);
                    fila.offer(vizinho);
                }
            }
        }
        
        long tempoExecucao = System.nanoTime() - inicioTempo;
        estatisticas.registrarOperacao(tempoExecucao, verticesVisitados, arestasExploradas);
        
        return new ResultadoBFS<>(origem, null, null, distancias, true, 
                                 tempoExecucao, verticesVisitados, arestasExploradas);
    }
    
    public ResultadoBFS<T> bfsOtimizado(T origem, T destino) {
        long inicioTempo = System.nanoTime();
        
        if (!listaAdjacencia.containsKey(origem) || !listaAdjacencia.containsKey(destino)) {
            return new ResultadoBFS<>(origem, destino, null, null, false, 0, 0, 0);
        }
        
        if (origem.equals(destino)) {
            List<T> caminho = Arrays.asList(origem);
            return new ResultadoBFS<>(origem, destino, caminho, null, true, 
                                     System.nanoTime() - inicioTempo, 1, 0);
        }
        
        ArrayDeque<T> fila = new ArrayDeque<>();
        Set<T> visitados = new HashSet<>();
        Map<T, T> predecessores = new HashMap<>();
        
        fila.offer(origem);
        visitados.add(origem);
        
        int verticesVisitados = 0;
        int arestasExploradas = 0;
        boolean encontrado = false;
        
        while (!fila.isEmpty() && !encontrado) {
            T atual = fila.poll();
            verticesVisitados++;
            
            for (T vizinho : listaAdjacencia.get(atual)) {
                arestasExploradas++;
                
                if (!visitados.contains(vizinho)) {
                    visitados.add(vizinho);
                    predecessores.put(vizinho, atual);
                    fila.offer(vizinho);
                    
                    if (vizinho.equals(destino)) {
                        encontrado = true;
                        break;
                    }
                }
            }
        }
        
        List<T> caminho = null;
        if (encontrado) {
            caminho = new ArrayList<>();
            T atual = destino;
            while (atual != null) {
                caminho.add(0, atual);
                atual = predecessores.get(atual);
            }
        }
        
        long tempoExecucao = System.nanoTime() - inicioTempo;
        estatisticas.registrarOperacao(tempoExecucao, verticesVisitados, arestasExploradas);
        
        return new ResultadoBFS<>(origem, destino, caminho, null, encontrado, 
                                 tempoExecucao, verticesVisitados, arestasExploradas);
    }
    
    public Map<T, Integer> calcularDistancias(T origem) {
        ResultadoBFS<T> resultado = bfsCompleto(origem);
        return resultado.getDistancias();
    }
    
    public Set<T> verticesNoNivel(T origem, int nivel) {
        Map<T, Integer> distancias = calcularDistancias(origem);
        Set<T> resultado = new HashSet<>();
        
        for (Map.Entry<T, Integer> entry : distancias.entrySet()) {
            if (entry.getValue() == nivel) {
                resultado.add(entry.getKey());
            }
        }
        
        return resultado;
    }
    
    public boolean existeCaminho(T origem, T destino) {
        ResultadoBFS<T> resultado = bfsOtimizado(origem, destino);
        return resultado.isEncontrado();
    }
    
    public EstatisticasPerformance obterEstatisticas() {
        return estatisticas;
    }
}

/**
 * Classe principal para demonstração do BFS Otimizado
 */
public class BFSOtimizado {
    
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════╗");
        System.out.println("║      BFS Otimizado - Demonstração     ║");
        System.out.println("║     Implementação Educacional          ║");
        System.out.println("╚════════════════════════════════════════╝");
        System.out.println();
        
        // Cria um grafo otimizado de exemplo
        GrafoBFSOtimizado<String> grafo = new GrafoBFSOtimizado<>();
        
        // Adiciona vértices (cidades)
        System.out.println("🏙️  Construindo grafo de cidades:");
        grafo.adicionarVertice("São Paulo");
        grafo.adicionarVertice("Rio de Janeiro");
        grafo.adicionarVertice("Belo Horizonte");
        grafo.adicionarVertice("Salvador");
        grafo.adicionarVertice("Brasília");
        grafo.adicionarVertice("Curitiba");
        
        // Adiciona conexões (estradas)
        System.out.println("\n🛣️  Adicionando conexões:");
        grafo.adicionarAresta("São Paulo", "Rio de Janeiro");
        grafo.adicionarAresta("São Paulo", "Belo Horizonte");
        grafo.adicionarAresta("São Paulo", "Curitiba");
        grafo.adicionarAresta("Rio de Janeiro", "Belo Horizonte");
        grafo.adicionarAresta("Belo Horizonte", "Salvador");
        grafo.adicionarAresta("Belo Horizonte", "Brasília");
        grafo.adicionarAresta("Salvador", "Brasília");
        
        // Mostra informações do grafo
        grafo.imprimirEstatisticasGrafo();
        grafo.imprimirGrafo();
        
        // Exemplo 1: BFS completo
        System.out.println("\n" + "=".repeat(50));
        System.out.println("1️⃣  BFS COMPLETO - Explorando todas as conexões");
        System.out.println("=".repeat(50));
        
        ResultadoBFS<String> resultadoCompleto = grafo.bfsCompleto("São Paulo");
        resultadoCompleto.imprimirResumo();
        
        // Exemplo 2: BFS com destino específico
        System.out.println("\n" + "=".repeat(50));
        System.out.println("2️⃣  BFS COM DESTINO - Caminho mais curto");
        System.out.println("=".repeat(50));
        
        ResultadoBFS<String> resultadoDestino = grafo.bfsOtimizado("São Paulo", "Salvador");
        resultadoDestino.imprimirResumo();
        
        // Exemplo 3: Análise de distâncias
        System.out.println("\n" + "=".repeat(50));
        System.out.println("3️⃣  ANÁLISE DE DISTÂNCIAS");
        System.out.println("=".repeat(50));
        
        Map<String, Integer> distancias = grafo.calcularDistancias("São Paulo");
        System.out.println("Distâncias a partir de São Paulo:");
        distancias.entrySet().stream()
                .sorted(Map.Entry.comparingByValue())
                .forEach(entry -> 
                    System.out.println("  📍 " + entry.getKey() + ": " + entry.getValue() + " saltos"));
        
        // Exemplo 4: Vértices por nível
        System.out.println("\n" + "=".repeat(50));
        System.out.println("4️⃣  VÉRTICES POR NÍVEL");
        System.out.println("=".repeat(50));
        
        for (int nivel = 0; nivel <= 3; nivel++) {
            Set<String> verticesNivel = grafo.verticesNoNivel("São Paulo", nivel);
            if (!verticesNivel.isEmpty()) {
                System.out.println("Nível " + nivel + ": " + verticesNivel);
            }
        }
        
        // Exemplo 5: Verificação de conectividade
        System.out.println("\n" + "=".repeat(50));
        System.out.println("5️⃣  VERIFICAÇÃO DE CONECTIVIDADE");
        System.out.println("=".repeat(50));
        
        String[][] pares = {
            {"São Paulo", "Salvador"},
            {"Rio de Janeiro", "Curitiba"},
            {"Brasília", "São Paulo"},
            {"Curitiba", "Salvador"}
        };
        
        for (String[] par : pares) {
            boolean conectado = grafo.existeCaminho(par[0], par[1]);
            System.out.println("🔗 " + par[0] + " → " + par[1] + ": " + 
                             (conectado ? "✅ Conectado" : "❌ Não conectado"));
        }
        
        // Estatísticas finais
        EstatisticasPerformance stats = grafo.obterEstatisticas();
        stats.imprimir();
        
        System.out.println("\n💡 Características desta implementação:");
        System.out.println("   • Uso de ArrayDeque para melhor performance");
        System.out.println("   • Suporte a tipos genéricos");
        System.out.println("   • Parada antecipada quando destino é encontrado");
        System.out.println("   • Coleta de métricas de performance");
        System.out.println("   • Interface flexível e robusta");
    }
}
