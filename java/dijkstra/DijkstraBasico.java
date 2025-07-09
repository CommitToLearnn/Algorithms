/**
 * Algoritmo de Dijkstra - Implementação Básica Educacional
 * ========================================================
 * 
 * Esta implementação demonstra o algoritmo clássico de Dijkstra para
 * encontrar o caminho mais curto em grafos com pesos positivos.
 * 
 * Características:
 * - Implementação básica sem heap (O(V²))
 * - Comentários educacionais detalhados
 * - Visualização passo a passo
 * - Construção de caminhos
 * - Análise de complexidade incluída
 * 
 * @author matheussricardoo
 * @version 1.0
 * @since Julho 2025
 */

package dijkstra;

import java.util.*;

public class DijkstraBasico {
    
    // Classe para representar um grafo com lista de adjacências
    static class Grafo {
        private int vertices;
        private List<List<Aresta>> adjacencia;
        
        // Classe interna para representar uma aresta ponderada
        static class Aresta {
            int destino;
            int peso;
            
            public Aresta(int destino, int peso) {
                this.destino = destino;
                this.peso = peso;
            }
            
            @Override
            public String toString() {
                return "→" + destino + "(peso:" + peso + ")";
            }
        }
        
        public Grafo(int vertices) {
            this.vertices = vertices;
            this.adjacencia = new ArrayList<>();
            
            // Inicializa a lista de adjacências
            for (int i = 0; i < vertices; i++) {
                adjacencia.add(new ArrayList<>());
            }
        }
        
        // Adiciona uma aresta direcionada ao grafo
        public void adicionarAresta(int origem, int destino, int peso) {
            if (peso < 0) {
                throw new IllegalArgumentException("Dijkstra não suporta pesos negativos");
            }
            adjacencia.get(origem).add(new Aresta(destino, peso));
            System.out.println("✅ Aresta adicionada: " + origem + " → " + destino + " (peso: " + peso + ")");
        }
        
        // Mostra a estrutura do grafo
        public void mostrarGrafo() {
            System.out.println("\n📊 Estrutura do Grafo:");
            for (int i = 0; i < vertices; i++) {
                System.out.print("Vértice " + i + ": ");
                if (adjacencia.get(i).isEmpty()) {
                    System.out.println("sem conexões");
                } else {
                    System.out.println(adjacencia.get(i));
                }
            }
            System.out.println();
        }
        
        // Algoritmo de Dijkstra - versão básica educacional
        public void dijkstra(int origem) {
            if (origem < 0 || origem >= vertices) {
                System.out.println("❌ Erro: Vértice de origem inválido!");
                return;
            }
            
            // Arrays para armazenar informações do algoritmo
            int[] distancia = new int[vertices];      // Distâncias mínimas
            boolean[] processado = new boolean[vertices]; // Vértices já processados
            int[] predecessor = new int[vertices];    // Para reconstruir caminhos
            
            // Inicialização
            Arrays.fill(distancia, Integer.MAX_VALUE);
            Arrays.fill(predecessor, -1);
            distancia[origem] = 0;
            
            System.out.println("🚀 Iniciando Algoritmo de Dijkstra");
            System.out.println("📍 Vértice origem: " + origem);
            System.out.println("🎯 Buscando caminhos mais curtos para todos os vértices...\n");
            
            // Processa todos os vértices
            for (int count = 0; count < vertices - 1; count++) {
                // Encontra o vértice com menor distância não processado
                int u = encontrarMenorDistancia(distancia, processado);
                
                if (u == -1) {
                    System.out.println("⚠️  Não há mais vértices alcançáveis");
                    break;
                }
                
                // Marca o vértice como processado
                processado[u] = true;
                
                System.out.println("🔄 Processando vértice " + u + 
                                 " (distância atual: " + formatarDistancia(distancia[u]) + ")");
                
                // Atualiza as distâncias dos vértices adjacentes
                int atualizacoes = 0;
                for (Aresta aresta : adjacencia.get(u)) {
                    int v = aresta.destino;
                    int peso = aresta.peso;
                    
                    // Relaxamento da aresta
                    if (!processado[v] && distancia[u] != Integer.MAX_VALUE && 
                        distancia[u] + peso < distancia[v]) {
                        
                        int distanciaAnterior = distancia[v];
                        distancia[v] = distancia[u] + peso;
                        predecessor[v] = u;
                        atualizacoes++;
                        
                        System.out.println("  ⬇️  Vértice " + v + ": " + 
                                         formatarDistancia(distanciaAnterior) + " → " + 
                                         distancia[v] + " (via " + u + ")");
                    }
                }
                
                if (atualizacoes == 0) {
                    System.out.println("  ➡️  Nenhuma atualização necessária");
                }
                System.out.println();
            }
            
            // Mostra os resultados finais
            mostrarResultados(origem, distancia, predecessor);
        }
        
        // Formata distância para exibição
        private String formatarDistancia(int distancia) {
            return distancia == Integer.MAX_VALUE ? "∞" : String.valueOf(distancia);
        }
        
        // Encontra o vértice não processado com menor distância
        private int encontrarMenorDistancia(int[] distancia, boolean[] processado) {
            int min = Integer.MAX_VALUE;
            int indiceMin = -1;
            
            for (int v = 0; v < vertices; v++) {
                if (!processado[v] && distancia[v] <= min) {
                    min = distancia[v];
                    indiceMin = v;
                }
            }
            
            return indiceMin;
        }
        
        // Mostra os resultados finais de forma organizada
        private void mostrarResultados(int origem, int[] distancia, int[] predecessor) {
            System.out.println("╔══════════════════════════════════════════════════════════════╗");
            System.out.println("║                    RESULTADOS FINAIS                        ║");
            System.out.println("╠══════════════════════════════════════════════════════════════╣");
            System.out.println("║ Menores distâncias a partir do vértice " + origem + "                     ║");
            System.out.println("╠════════════╦═════════════════╦═══════════════════════════════╣");
            System.out.println("║   Vértice  ║    Distância    ║            Caminho            ║");
            System.out.println("╠════════════╬═════════════════╬═══════════════════════════════╣");
            
            for (int i = 0; i < vertices; i++) {
                String dist = distancia[i] == Integer.MAX_VALUE ? "∞" : String.valueOf(distancia[i]);
                String caminho = construirCaminho(origem, i, predecessor);
                
                System.out.printf("║ %10d ║ %15s ║ %29s ║%n", i, dist, caminho);
            }
            
            System.out.println("╚════════════╩═════════════════╩═══════════════════════════════╝");
        }
        
        // Constrói o caminho do vértice origem até o destino
        private String construirCaminho(int origem, int destino, int[] predecessor) {
            if (predecessor[destino] == -1 && origem != destino) {
                return "N/A";
            }
            
            List<Integer> caminho = new ArrayList<>();
            int atual = destino;
            
            while (atual != -1) {
                caminho.add(atual);
                atual = predecessor[atual];
            }
            
            Collections.reverse(caminho);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < caminho.size(); i++) {
                if (i > 0) sb.append("→");
                sb.append(caminho.get(i));
            }
            
            return sb.toString();
        }
    }
    
    // Método principal - exemplo de uso e demonstração
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════╗");
        System.out.println("║     Algoritmo de Dijkstra - Básico    ║");
        System.out.println("║      Implementação Educacional        ║");
        System.out.println("╚════════════════════════════════════════╝");
        System.out.println();
        
        // Cria um grafo exemplo representando uma rede de cidades
        System.out.println("🏗️  Construindo grafo exemplo (6 vértices):");
        Grafo grafo = new Grafo(6);
        
        // Adiciona arestas representando estradas com distâncias
        System.out.println("🛣️  Adicionando estradas:");
        grafo.adicionarAresta(0, 1, 4);  // Cidade 0 → Cidade 1 (4 km)
        grafo.adicionarAresta(0, 2, 2);  // Cidade 0 → Cidade 2 (2 km)
        grafo.adicionarAresta(1, 2, 1);  // Cidade 1 → Cidade 2 (1 km)
        grafo.adicionarAresta(1, 3, 5);  // Cidade 1 → Cidade 3 (5 km)
        grafo.adicionarAresta(2, 3, 8);  // Cidade 2 → Cidade 3 (8 km)
        grafo.adicionarAresta(2, 4, 10); // Cidade 2 → Cidade 4 (10 km)
        grafo.adicionarAresta(3, 4, 2);  // Cidade 3 → Cidade 4 (2 km)
        grafo.adicionarAresta(3, 5, 6);  // Cidade 3 → Cidade 5 (6 km)
        grafo.adicionarAresta(4, 5, 3);  // Cidade 4 → Cidade 5 (3 km)
        
        // Mostra a estrutura do grafo
        grafo.mostrarGrafo();
        
        // Executa o algoritmo a partir do vértice 0
        System.out.println("🚀 Executando Dijkstra a partir da cidade 0:");
        System.out.println("=" .repeat(60));
        grafo.dijkstra(0);
        
        System.out.println("\n📊 Análise de Complexidade:");
        System.out.println("   • Tempo: O(V²) - versão básica sem heap");
        System.out.println("   • Espaço: O(V) - para arrays de distância e predecessor");
        System.out.println();
        
        System.out.println("🎯 Características do Algoritmo:");
        System.out.println("   • Encontra o caminho mais curto para TODOS os vértices");
        System.out.println("   • Funciona apenas com pesos positivos");
        System.out.println("   • Usa estratégia gulosa (greedy)");
        System.out.println("   • Garante solução ótima");
        System.out.println();
        
        System.out.println("⚡ Otimizações Possíveis:");
        System.out.println("   • Usar Priority Queue/Heap: O((V+E)logV)");
        System.out.println("   • Usar Fibonacci Heap: O(E + VlogV)");
        System.out.println("   • Parar quando destino for encontrado");
        System.out.println();
        
        System.out.println("💡 Aplicações Práticas:");
        System.out.println("   • GPS e sistemas de navegação");
        System.out.println("   • Roteamento de redes");
        System.out.println("   • Análise de custos em grafos");
        System.out.println("   • Jogos (pathfinding)");
    }
}
