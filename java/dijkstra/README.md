![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Dijkstra%20Algorithm&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Shortest%20Path%20-%20Java%20Implementation&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=java)](https://java.com/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Dijkstra-FF6B6B?style=for-the-badge&logo=algorithm)](https://github.com/matheussricardoo/Algorithms)
[![Complexity](https://img.shields.io/badge/Time-O((V+E)logV)-red?style=for-the-badge)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Object-Oriented Design**: Clean Java implementation with proper encapsulation
- **Priority Queue**: Efficient implementation using Java's PriorityQueue
- **Shortest Path**: Find minimum distance paths in weighted graphs
- **Non-negative Weights**: Works with graphs having non-negative edge weights

### 🇧🇷 Português
- **Design Orientado a Objetos**: Implementação Java limpa com encapsulamento adequado
- **Fila de Prioridade**: Implementação eficiente usando PriorityQueue do Java
- **Caminho Mais Curto**: Encontra caminhos de distância mínima em grafos ponderados
- **Pesos Não-negativos**: Funciona com grafos tendo pesos de arestas não-negativos

<div align="center">

| Feature | Description | Descrição |
|:---:|:---|:---|
| 🎯 | Educational Implementation | Implementação Educacional - O(V²) didática |
| 🚀 | Optimized Version | Versão Otimizada - O((V+E)logV) com PriorityQueue |
| 📊 | Performance Statistics | Estatísticas de Performance - Métricas detalhadas |
| 🔍 | Path Reconstruction | Reconstrução de Caminhos - Predecessores |
| 📈 | Early Termination | Terminação Antecipada - Para quando encontra destino |
| 🌐 | Network Applications | Aplicações de Rede - GPS, roteamento |
| ⚡ | Heap Optimization | Otimização com Heap - Seleção eficiente |
| 🧬 | Generic Support | Suporte Genérico - Flexível para diferentes tipos |

</div>

### 🛠️ Technologies | Tecnologias

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=java&theme=dark" />
  </a>
</div>

## Estrutura dos Arquivos

- `DijkstraBasico.java` - Implementação básica e didática
- `otimizado/` - Versão otimizada com melhorias de performance
  - `GrafoDijkstraOtimizado.java` - Classe principal do grafo otimizado
  - `ResultadoDijkstra.java` - Classe para encapsular resultados
  - `EstatisticasPerformance.java` - Métricas de performance
  - `ExemploDijkstraOtimizado.java` - Exemplos de uso

## Sobre o Algoritmo

O algoritmo de Dijkstra encontra os caminhos mais curtos de um vértice origem para todos os outros vértices em um grafo com pesos não-negativos.

### Complexidade
- **Tempo**: O(V² + E) versão básica, O((V + E) log V) versão otimizada
- **Espaço**: O(V)

Onde V = número de vértices e E = número de arestas.

## Como Compilar e Executar

### Versão Básica
```bash
# Compilar
javac DijkstraBasico.java

# Executar
java DijkstraBasico
```

### Versão Otimizada
```bash
# Navegar para o diretório java
cd java

# Compilar todas as classes
javac dijkstra/otimizado/*.java

# Executar exemplo
java dijkstra.otimizado.ExemploDijkstraOtimizado
```

## Principais Melhorias na Versão Otimizada

1. **PriorityQueue**: Usa heap binário para seleção eficiente do próximo vértice
2. **Early Termination**: Para quando encontra o destino específico
3. **Estruturas Otimizadas**: HashMap para adjacências, arrays para distâncias
4. **Estatísticas de Performance**: Coleta métricas detalhadas de execução
5. **Separação de Responsabilidades**: Classes específicas para diferentes funcionalidades

## Exemplos de Uso

### Uso Básico
```java
// Criar grafo com 5 vértices
GrafoDijkstraOtimizado grafo = new GrafoDijkstraOtimizado(5);

// Adicionar arestas (origem, destino, peso)
grafo.adicionarAresta(0, 1, 4);
grafo.adicionarAresta(0, 2, 2);

// Executar Dijkstra
ResultadoDijkstra resultado = grafo.dijkstra(0, null);

// Obter distância
int distancia = resultado.getDistancia(1);

// Obter caminho
List<Integer> caminho = grafo.reconstruirCaminho(0, 1, resultado.getPredecessores());
```

### 🚀 Getting Started | Começando

```bash
# Basic Version | Versão Básica
javac DijkstraBasico.java && java DijkstraBasico

# Optimized Version | Versão Otimizada
cd java
javac dijkstra/otimizado/*.java
java dijkstra.otimizado.ExemploDijkstraOtimizado
```

### 📊 Complexity Analysis | Análise de Complexidade

<div align="center">

| Version | Time | Space | Description |
|:---:|:---:|:---:|:---|
| **Basic** | O(V² + E) | O(V) | Simple array-based implementation |
| **Optimized** | O((V+E)logV) | O(V) | PriorityQueue with adjacency list |

</div>

### 💡 Usage Examples | Exemplos de Uso

```java
// Create graph | Criar grafo
GrafoDijkstraOtimizado grafo = new GrafoDijkstraOtimizado(5);

// Add edges | Adicionar arestas
grafo.adicionarAresta(0, 1, 4);
grafo.adicionarAresta(0, 2, 2);

// Run Dijkstra | Executar Dijkstra
ResultadoDijkstra resultado = grafo.dijkstra(0, null);

// Get distance | Obter distância
int distancia = resultado.getDistancia(1);

// Get path | Obter caminho
List<Integer> caminho = grafo.reconstruirCaminho(0, 1, resultado.getPredecessores());
```

### 🎯 Use Cases | Casos de Uso

<div align="center">

| Application | Description | Descrição |
|:---:|:---|:---|
| 🌐 | **Network Routing** | Roteamento de Redes - Caminho mais eficiente |
| 🗺️ | **GPS Navigation** | Navegação GPS - Rotas mais curtas |
| 🎮 | **Game Pathfinding** | Pathfinding em Jogos - NPCs inteligentes |
| 📱 | **Social Networks** | Redes Sociais - Conexões mais próximas |
| 📦 | **Logistics** | Logística - Otimização de rotas |

</div>

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
