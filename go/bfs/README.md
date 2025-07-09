![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=BFS%20Algorithm&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Breadth-First%20Search%20-%20Go%20Implementation&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Go-white?style=for-the-badge&logo=go&logoColor=00ADD8)](https://golang.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-BFS-white?style=for-the-badge&logo=algorithm&logoColor=black)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Queue-white?style=for-the-badge&logo=data-structure&logoColor=black)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-white?style=for-the-badge&logo=open-source-initiative&logoColor=green)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Educational Implementation**: Step-by-step BFS visualization
- **Tree & Graph Support**: Two different approaches (tree and graph)
- **Optimized Version**: Production-ready with efficient queue operations
- **Level-order Traversal**: Complete breadth-first exploration

### 🇧🇷 Português
- **Implementação Educacional**: Visualização passo a passo do BFS
- **Suporte a Árvores e Grafos**: Duas abordagens diferentes (árvore e grafo)
- **Versão Otimizada**: Pronta para produção com operações de fila eficientes
- **Travessia por Nível**: Exploração completa em largura

<div align="center">

| Feature | Description | Descrição |
|:---:|:---|:---|
| 🎯 | Basic Implementation | Implementação Básica - Didática e visual |
| 🚀 | Optimized Version | Versão Otimizada - Performance e múltiplas variações |
| 📊 | Performance Analysis | Análise de Performance - Estatísticas detalhadas |
| 🔍 | Path Finding | Busca de Caminhos - Encontra caminhos mais curtos |
| 📈 | Connectivity Analysis | Análise de Conectividade - Componentes conectados |
| 🎮 | Game Applications | Aplicações em Jogos - Pathfinding |
| 🌐 | Social Networks | Redes Sociais - Graus de separação |
| ⚡ | Early Termination | Terminação Antecipada - Para quando encontra destino |

</div>

### 🛠️ Technologies | Tecnologias

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go&theme=dark" />
  </a>
</div>

### 📁 File Structure | Estrutura dos Arquivos

<div align="center">

| Version | File | Description | Descrição |
|:---:|:---|:---|:---|
| 🎯 | `bfs_basico.go` | Graph implementation with adjacency matrix | Implementação com matriz de adjacência |
| 🌳 | `bfs_basico_arvore.go` | Tree implementation with pointers | Implementação com árvores e ponteiros |
| 🚀 | `otimizado/bfs_otimizado.go` | Production-ready version | Versão otimizada para produção |

</div>

### 🔄 Implementation Approaches | Abordagens de Implementação

<div align="center">

| Aspect | Graph Version | Tree Version |
|:---:|:---|:---|
| **Structure** | Adjacency matrix | Node pointers |
| **Best For** | General graphs | Hierarchical data |
| **Memory** | O(V²) | O(V) |
| **Cycles** | Handles cycles | Assumes no cycles |
| **Visual** | Matrix display | Tree structure display |

</div>

### 🎯 When to Use BFS | Quando Usar BFS

<div align="center">

| ✅ Use BFS When | ❌ Don't Use BFS When |
|:---|:---|
| Finding **shortest path** in unweighted graphs | Graphs have edge weights (use Dijkstra) |
| Exploring vertices by **distance levels** | Looking for any solution (DFS might be better) |
| Checking if graph is **connected** | Search space is very deep (DFS uses less memory) |
| Implementing **pathfinding** in games | Need depth-specific search |
| Analyzing **social networks** (degrees of separation) | Working with very large graphs (memory constraints) |
| Solving **puzzles** with finite states | Need to find all solutions |

</div>

### 🚀 Getting Started | Começando

```bash
# Graph Version (Adjacency Matrix) | Versão Grafo (Matriz de Adjacência)
cd bfs
go run bfs_basico.go

# Tree Version (Node Pointers) | Versão Árvore (Ponteiros de Nós)
cd bfs
go run bfs_basico_arvore.go

# Optimized Version (Performance) | Versão Otimizada (Performance)
cd bfs/otimizado
go run bfs_otimizado.go
```

## 📊 Comparação das Versões

| Aspecto | Versão Básica | Versão Otimizada |
|---------|---------------|------------------|
| **Estrutura de Dados** | Matriz adjacência | Lista adjacência |
| **Fila** | Slice (O(n) remoção) | container/list (O(1)) |
| **Espaço** | O(V²) | O(V + E) |
| **Funcionalidades** | BFS simples | Múltiplas variações |
| **Didático** | ✅ Muito claro | ❌ Mais complexo |
| **Performance** | ❌ Lento para grafos grandes | ✅ Otimizado |
| **Análise** | ❌ Básica | ✅ Componentes, estatísticas |

## 🔧 Como Funciona o BFS

### Algoritmo Principal:
1. **Inicialização**:
   - Marca vértice inicial como visitado
   - Adiciona à fila

2. **Loop Principal**:
   - Remove vértice da fila (FIFO)
   - Para cada vizinho não visitado:
     - Marca como visitado
     - Adiciona à fila

3. **Resultado**:
   - Todos os vértices alcançáveis foram visitados
   - Ordem de visitação = níveis de distância

### Visualização:
```
     0
   ↙   ↘
  1     2      ← Nível 1
 ↙       ↘
3         4    ← Nível 2

Ordem BFS a partir de 0: 0 → 1 → 2 → 3 → 4
```

## 📈 Análise de Complexidade

### Complexidade Principal:
- **Tempo**: O(V + E) onde V = vértices, E = arestas
- **Espaço**: O(V) para fila e arrays auxiliares

### Detalhamento:
| Operação | Matriz Adjacência | Lista Adjacência |
|----------|-------------------|------------------|
| **Tempo** | O(V²) | O(V + E) |
| **Espaço** | O(V²) | O(V + E) |
| **Melhor para** | Grafos densos | Grafos esparsos |

## 🔍 Variações Implementadas

### 1. **BFS Básico**
```go
// Explora todos os vértices alcançáveis
visitOrder := bfs(startVertex)
```

### 2. **BFS com Distâncias**
```go
// Calcula distância mínima para cada vértice
visitOrder, distances, predecessors := bfs(startVertex)
```

### 3. **Busca de Caminho**
```go
// Encontra caminho mais curto entre dois vértices
path, found := bfsPath(start, target)
```

### 4. **BFS por Níveis**
```go
// Organiza vértices por níveis de distância
levels := bfsLevels(startVertex)
// levels[0] = [startVertex]
// levels[1] = [vizinhos diretos]
// levels[2] = [vizinhos dos vizinhos]
```

### 5. **Análise de Conectividade**
```go
// Verifica se grafo é conectado
connected := isConnected()

// Encontra componentes conectados
components := findComponents()
```

## 🎓 Aplicações Práticas

### 1. **Redes Sociais**
```
Encontrar grau de separação entre pessoas:
"6 graus de separação" - BFS para medir distância social
```

### 2. **Jogos - Pathfinding**
```
Encontrar caminho mais curto em labirinto:
- Cada célula = vértice
- Conexões = movimento possível
- BFS garante caminho ótimo
```

### 3. **Sistemas de Recomendação**
```
"Pessoas que você pode conhecer":
- BFS para encontrar amigos de amigos
- Distância 2 = potenciais conexões
```

### 4. **Análise de Redes**
```
Análise de propagação:
- Como informação se espalha
- Detecção de comunidades
- Análise de influência
```

### 5. **Processamento de Imagens**
```
Flood Fill (balde de tinta):
- BFS em pixels conectados
- Mesmo princípio do Paint
```

### 🧪 Exercises | Exercícios

<div align="center">

| Level | Exercise | Exercício |
|:---:|:---|:---|
| 🟢 | Implement BFS for directed graph | Implementar BFS para grafo direcionado |
| 🟢 | Find only even vertices | Encontrar apenas vértices pares |
| 🟢 | Count vertices at each level | Contar vértices em cada nível |
| 🟡 | Bidirectional BFS | BFS bidirecional |
| 🟡 | Find graph center | Encontrar centro do grafo |
| 🟡 | Detect cycles using BFS | Detectar ciclos usando BFS |
| 🔴 | Edmonds-Karp algorithm | Algoritmo de Edmonds-Karp |
| 🔴 | Parallel BFS | BFS paralelo |
| 🔴 | BFS on implicit graphs | BFS em grafos implícitos |

</div>

### ⚡ Advanced Optimizations | Otimizações Avançadas

```go
// ❌ Slice (O(n) to remove first)
queue = queue[1:]

// ✅ container/list (O(1) to remove)
element := queue.Front()
queue.Remove(element)

// Early Termination
if current == target {
    return path, true
}
```

### 🔄 BFS vs DFS Comparison | Comparação

<div align="center">

| Criteria | BFS | DFS |
|:---:|:---|:---|
| **Strategy** | Breadth first | Depth first |
| **Structure** | Queue (FIFO) | Stack (LIFO) |
| **Shortest Path** | ✅ Guarantees | ❌ No guarantee |
| **Memory Usage** | O(V) - can be high | O(h) - tree height |
| **Use Cases** | Distances, levels | Exploration, cycles |

</div>

### 🎯 Next Steps | Próximos Passos

After mastering BFS, explore | Após dominar BFS, explore:
- **DFS** - Depth-First Search | Busca em profundidade
- **Dijkstra** - BFS with weights | BFS com pesos
- **A*** - BFS with heuristics | BFS com heurística
- **Bidirectional BFS** - Search from both ends | Busca em ambas as direções
- **Multi-source BFS** - Multiple starting points | Múltiplos pontos de partida

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
