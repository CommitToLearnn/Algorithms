![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Algoritmo%20de%20Dijkstra%20em%20Go&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Caminho%20mais%20curto%20em%20grafos%20ponderados&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Go-white?style=for-the-badge&logo=go&logoColor=00ADD8)](https://golang.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Dijkstra-white?style=for-the-badge&logo=algorithm&logoColor=black)](https://github.com/matheussricardoo/Algorithms)
[![Complexity](https://img.shields.io/badge/Time-O((V+E)logV)-white?style=for-the-badge&logoColor=red)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-white?style=for-the-badge&logo=open-source-initiative&logoColor=green)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Shortest Path**: Finds optimal paths in weighted graphs with non-negative weights
- **Educational Implementation**: Step-by-step visualization with detailed comments
- **Optimized Version**: Production-ready with priority queue (heap)
- **Multiple Representations**: Adjacency matrix and adjacency list versions
- **Early Termination**: Stops when target vertex is found
- **Path Reconstruction**: Returns both distances and actual paths

### 🇧🇷 Português
- **Caminho Mais Curto**: Encontra caminhos ótimos em grafos ponderados com pesos não-negativos
- **Implementação Didática**: Visualização passo a passo com comentários detalhados
- **Versão Otimizada**: Pronta para produção com fila de prioridade (heap)
- **Múltiplas Representações**: Versões com matriz de adjacência e lista de adjacência
- **Terminação Antecipada**: Para quando encontra o vértice de destino
- **Reconstrução de Caminhos**: Retorna tanto distâncias quanto caminhos reais

---

## 🛠️ Technologies | Tecnologias

<div align="center">

[![Go](https://skillicons.dev/icons?i=go)](https://golang.org/)
[![VS Code](https://skillicons.dev/icons?i=vscode)](https://code.visualstudio.com/)
[![Git](https://skillicons.dev/icons?i=git)](https://git-scm.com/)
[![GitHub](https://skillicons.dev/icons?i=github)](https://github.com/)

</div>

---

## 📁 Project Structure | Estrutura do Projeto

```
go/dijkstra/
├── dijkstra_basico.go      # 📚 Educational implementation
├── otimizado/
│   └── dijkstra_otimizado.go # 🚀 Optimized with heap
└── README.md              # 📖 Documentation
```

---

## 🚀 Quick Start | Início Rápido

### 🇺🇸 English

#### Basic Version (Educational)
```bash
cd dijkstra
go run dijkstra_basico.go
```

#### Optimized Version (Performance)
```bash
cd dijkstra/otimizado
go run dijkstra_otimizado.go
```

### 🇧🇷 Português

#### Versão Básica (Didática)
```bash
cd dijkstra
go run dijkstra_basico.go
```

#### Versão Otimizada (Performance)
```bash
cd dijkstra/otimizado
go run dijkstra_otimizado.go
```

---

## 💻 Practical Example | Exemplo Prático

### 🇺🇸 English
```go
// Basic usage example
graph := NewGraph(4)

// Add weighted edges: AddEdge(from, to, weight)
graph.AddEdge(0, 1, 4)  // A -> B (weight: 4)
graph.AddEdge(0, 2, 2)  // A -> C (weight: 2)
graph.AddEdge(1, 3, 5)  // B -> D (weight: 5)
graph.AddEdge(2, 3, 1)  // C -> D (weight: 1)

// Find shortest path from vertex 0 to all others
distances, paths := graph.Dijkstra(0)

// Result: Shortest path A -> D is A -> C -> D (cost: 3)
```

### 🇧🇷 Português
```go
// Exemplo de uso básico
grafo := NovoGrafo(4)

// Adicionar arestas ponderadas: AdicionarAresta(de, para, peso)
grafo.AdicionarAresta(0, 1, 4)  // A -> B (peso: 4)
grafo.AdicionarAresta(0, 2, 2)  // A -> C (peso: 2)
grafo.AdicionarAresta(1, 3, 5)  // B -> D (peso: 5)
grafo.AdicionarAresta(2, 3, 1)  // C -> D (peso: 1)

// Encontrar caminho mais curto do vértice 0 para todos os outros
distancias, caminhos := grafo.Dijkstra(0)

// Resultado: Caminho mais curto A -> D é A -> C -> D (custo: 3)
```

---

## 📊 Complexity Analysis | Análise de Complexidade

### 🇺🇸 English
| Version | Time Complexity | Space Complexity | Best For |
|---------|----------------|------------------|----------|
| **Basic** | O(V²) | O(V²) | Dense graphs, learning |
| **Optimized** | O((V + E) log V) | O(V + E) | Sparse graphs, production |

**Legend**: V = vertices, E = edges

### 🇧🇷 Português
| Versão | Complexidade de Tempo | Complexidade de Espaço | Melhor Para |
|--------|----------------------|------------------------|-------------|
| **Básica** | O(V²) | O(V²) | Grafos densos, aprendizado |
| **Otimizada** | O((V + E) log V) | O(V + E) | Grafos esparsos, produção |

**Legenda**: V = vértices, E = arestas

---

## 🎯 Use Cases | Casos de Uso

### 🇺🇸 English
- **🗺️ GPS Navigation**: Finding shortest routes between locations
- **🌐 Network Routing**: Optimal packet routing in computer networks
- **🎮 Game Development**: Pathfinding for NPCs and AI characters
- **📦 Logistics**: Optimizing delivery routes and supply chains
- **🏥 Emergency Services**: Finding fastest routes for ambulances

### 🇧🇷 Português
- **🗺️ Navegação GPS**: Encontrar rotas mais curtas entre localizações
- **🌐 Roteamento de Redes**: Roteamento ótimo de pacotes em redes de computadores
- **🎮 Desenvolvimento de Jogos**: Pathfinding para NPCs e personagens IA
- **📦 Logística**: Otimização de rotas de entrega e cadeias de suprimento
- **🏥 Serviços de Emergência**: Encontrar rotas mais rápidas para ambulâncias

---

## 💡 Implementation Details | Detalhes da Implementação

### 🇺🇸 English
#### Algorithm Steps
1. **Initialize**: Set distance to source = 0, all others = ∞
2. **Main Loop**: 
   - Find unvisited vertex with minimum distance
   - Mark as visited
   - Update distances to neighbors (relaxation)
3. **Result**: Arrays of distances and predecessors

#### Edge Relaxation
```go
// If we found a shorter path through current vertex
if dist[current] + weight < dist[neighbor] {
    dist[neighbor] = dist[current] + weight
    predecessor[neighbor] = current
}
```

### 🇧🇷 Português
#### Passos do Algoritmo
1. **Inicializar**: Definir distância para origem = 0, todas as outras = ∞
2. **Loop Principal**:
   - Encontrar vértice não visitado com distância mínima
   - Marcar como visitado
   - Atualizar distâncias para vizinhos (relaxamento)
3. **Resultado**: Arrays de distâncias e predecessores

#### Relaxamento de Arestas
```go
// Se encontramos um caminho mais curto através do vértice atual
if dist[atual] + peso < dist[vizinho] {
    dist[vizinho] = dist[atual] + peso
    predecessor[vizinho] = atual
}
```

---

## 🔧 Technical Features | Características Técnicas

### 🇺🇸 English
- **Non-negative Weights**: Works only with graphs having non-negative edge weights
- **Single Source**: Finds shortest paths from one source to all other vertices
- **Greedy Approach**: Makes locally optimal choices at each step
- **Priority Queue**: Optimized version uses min-heap for efficiency
- **Path Reconstruction**: Can reconstruct the actual shortest paths

### 🇧🇷 Português
- **Pesos Não-Negativos**: Funciona apenas com grafos com pesos de arestas não-negativos
- **Fonte Única**: Encontra caminhos mais curtos de uma origem para todos os outros vértices
- **Abordagem Gulosa**: Faz escolhas localmente ótimas em cada passo
- **Fila de Prioridade**: Versão otimizada usa min-heap para eficiência
- **Reconstrução de Caminhos**: Pode reconstruir os caminhos mais curtos reais

---

## ⚠️ Limitations | Limitações

### 🇺🇸 English
- **No Negative Weights**: Cannot handle graphs with negative edge weights
- **Single Optimal Path**: Returns only one shortest path (if multiple exist)
- **Connected Graphs**: Assumes graph connectivity (unreachable vertices get ∞ distance)
- **Memory Usage**: Can be memory-intensive for very large graphs

### 🇧🇷 Português
- **Sem Pesos Negativos**: Não consegue lidar com grafos com pesos de arestas negativos
- **Caminho Único Ótimo**: Retorna apenas um caminho mais curto (se múltiplos existem)
- **Grafos Conectados**: Assume conectividade do grafo (vértices inalcançáveis ficam com distância ∞)
- **Uso de Memória**: Pode usar muita memória para grafos muito grandes

---

## 🎯 Next Steps | Próximos Passos

### 🇺🇸 English
After mastering Dijkstra, explore:
- **Bellman-Ford**: For graphs with negative weights
- **Floyd-Warshall**: All-pairs shortest paths
- **A* Algorithm**: Heuristic-guided search
- **Johnson's Algorithm**: Combines multiple approaches

### 🇧🇷 Português
Após dominar Dijkstra, explore:
- **Bellman-Ford**: Para grafos com pesos negativos
- **Floyd-Warshall**: Caminhos mais curtos para todos os pares
- **Algoritmo A***: Busca guiada por heurística
- **Algoritmo de Johnson**: Combina múltiplas abordagens

---

### 👤 Author | Autor

<div align="center">
  <a href="https://github.com/matheussricardoo" target="_blank">
    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/matheus-ricardo-426452266/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn"/>
  </a>
</div>

### 📄 License | Licença

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=000000&height=120&section=footer"/>

