![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Dijkstra%20Algorithm&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Shortest%20Path%20-%20Python%20Implementation&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](https://python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Dijkstra-FF6B6B?style=for-the-badge&logo=algorithm)](https://github.com/matheussricardoo/Algorithms)
[![Complexity](https://img.shields.io/badge/Time-O((V+E)logV)-red?style=for-the-badge)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

</div>

---

## 🌟 Features | Características

| English | Português |
|---------|-----------|
| **Shortest Path Calculation** | **Cálculo de Caminho Mais Curto** |
| Finds optimal paths in weighted graphs | Encontra caminhos ótimos em grafos ponderados |
| **Two Implementation Versions** | **Duas Versões de Implementação** |
| Basic (educational) and optimized (production) | Básica (educacional) e otimizada (produção) |
| **Graph Navigation** | **Navegação em Grafos** |
| Support for directed/undirected graphs | Suporte para grafos direcionados/não-direcionados |
| **Real-world Applications** | **Aplicações do Mundo Real** |
| GPS, network routing, games pathfinding | GPS, roteamento de redes, pathfinding em jogos |

## 🛠️ Technologies | Tecnologias

<div align="center">

![Python](https://skillicons.dev/icons?i=python&theme=dark)

</div>

## 📁 Estrutura dos Arquivos

```
dijkstra/
├── dijkstra_basico.py          # Implementação didática básica
├── otimizado/
│   └── dijkstra_otimizado.py   # Implementação otimizada com heap
└── README.md                   # Este arquivo
```

## 🎯 Versions Disponíveis

### 1. Versão Básica (`dijkstra_basico.py`)
- **Propósito**: Aprendizado e compreensão dos conceitos
- **Complexidade**: O(V²) onde V é o número de vértices
- **Características**:
  - Usa lista simples para encontrar o vértice com menor distância
  - Código mais legível e comentado
  - Ideal para estudantes
  - Processa todos os vértices do grafo

### 2. Versão Otimizada (`otimizado/dijkstra_otimizado.py`)
- **Propósito**: Uso em aplicações reais
- **Complexidade**: O((V + E) log V) onde V = vértices, E = arestas
- **Características**:
  - Usa heap (fila de prioridade) para eficiência
  - Parada antecipada quando destino é encontrado
  - Função adicional para calcular todos os caminhos
  - Mais eficiente para grafos grandes

## 🚀 Quick Start | Início Rápido

```bash
# Clone the repository | Clone o repositório
git clone https://github.com/matheussricardoo/Algorithms.git
cd algorithms/python/dijkstra

# Run basic version | Execute versão básica
python dijkstra_basico.py

# Run optimized version | Execute versão otimizada
python otimizado/dijkstra_otimizado.py
```

## 📊 Exemplos de Uso

### Exemplo Básico
```python
from dijkstra_basico import GrafoDijkstra

# Cria o grafo
grafo = GrafoDijkstra()

# Adiciona arestas (origem, destino, peso)
grafo.adicionar_aresta("A", "B", 4)
grafo.adicionar_aresta("A", "C", 2)
grafo.adicionar_aresta("B", "D", 5)
grafo.adicionar_aresta("C", "D", 8)

# Encontra o caminho mais curto
distancia, caminho = grafo.dijkstra("A", "D")
print(f"Caminho: {' -> '.join(caminho)}")
print(f"Distância: {distancia}")
```

### Exemplo Otimizado
```python
from otimizado.dijkstra_otimizado import GrafoDijkstraOtimizado

# Cria o grafo
grafo = GrafoDijkstraOtimizado()

# Adiciona arestas
grafo.adicionar_aresta("Hub", "A", 2)
grafo.adicionar_aresta("Hub", "B", 1)
grafo.adicionar_aresta("A", "Destino", 3)
grafo.adicionar_aresta("B", "Destino", 4)

# Caminho específico
distancia, caminho = grafo.dijkstra_otimizado("Hub", "Destino")

# Todos os caminhos a partir de um vértice
todos_caminhos = grafo.dijkstra_todos_caminhos("Hub")
```

## 🔍 Conceitos Importantes

### Como Funciona o Algoritmo
1. **Inicialização**: Define distância 0 para o vértice origem e infinito para os demais
2. **Seleção**: Escolhe o vértice não visitado com menor distância
3. **Relaxação**: Atualiza as distâncias dos vizinhos se um caminho mais curto for encontrado
4. **Repetição**: Repete até visitar todos os vértices ou encontrar o destino

### Relaxação de Arestas
```
Se distancia[atual] + peso(atual, vizinho) < distancia[vizinho]:
    distancia[vizinho] = distancia[atual] + peso(atual, vizinho)
    predecessor[vizinho] = atual
```

### Limitações
- **Não funciona com pesos negativos**: Use Bellman-Ford para esse caso
- **Grafos direcionados**: As implementações assumem grafos direcionados
- **Conectividade**: Vértices não conectados retornam distância infinita

## 📈 Comparação de Performance

| Aspecto | Versão Básica | Versão Otimizada |
|---------|---------------|------------------|
| Complexidade | O(V²) | O((V + E) log V) |
| Estrutura de dados | Lista simples | Heap |
| Melhor para | Grafos pequenos/estudo | Grafos grandes/produção |
| Legibilidade | Alta | Média |
| Performance | Baixa para grafos grandes | Alta |

## 🎓 Aplicações Práticas

### 1. **Sistemas de Navegação**
- GPS e mapas (Google Maps, Waze)
- Encontrar a rota mais rápida/curta

### 2. **Redes de Computadores**
- Protocolos de roteamento (OSPF)
- Encontrar o caminho com menor latência

### 3. **Jogos**
- Pathfinding para NPCs
- Navegação em mapas

### 4. **Redes Sociais**
- Grau de separação entre pessoas
- Recomendação de conexões

## 🛠️ Dicas de Implementação

### Versão Básica
- Use quando precisar entender os conceitos
- Boa para grafos com menos de 1000 vértices
- Código mais fácil de debugar

### Versão Otimizada
- Use para aplicações reais
- Eficiente para grafos grandes (milhares de vértices)
- Implementa parada antecipada

## 📚 Recursos Adicionais

- **Complexidade de Tempo**: Varia entre O(V²) e O((V + E) log V)
- **Complexidade de Espaço**: O(V) para ambas as versões
- **Inventor**: Edsger Dijkstra (1956)
- **Pré-requisitos**: Grafos com pesos não-negativos

## 📊 Analysis | Análise

### Time Complexity | Complexidade de Tempo
- **Basic Version | Versão Básica**: O(V²)
- **Optimized Version | Versão Otimizada**: O((V + E) log V)

### Space Complexity | Complexidade de Espaço
- **Both Versions | Ambas Versões**: O(V)

Where | Onde:
- V = Number of vertices | Número de vértices
- E = Number of edges | Número de arestas

## 🎯 Use Cases | Casos de Uso

| Application | Aplicação | Description | Descrição |
|-------------|-----------|-------------|-----------|
| **GPS Navigation** | **Navegação GPS** | Find shortest routes | Encontrar rotas mais curtas |
| **Network Routing** | **Roteamento de Redes** | OSPF protocol implementation | Implementação do protocolo OSPF |
| **Game Development** | **Desenvolvimento de Jogos** | NPC pathfinding | Pathfinding para NPCs |
| **Social Networks** | **Redes Sociais** | Connection recommendations | Recomendações de conexão |

## 🔧 Implementation Details | Detalhes de Implementação

### How it Works | Como Funciona
1. **Initialize | Inicializar**: Set distance 0 to source, ∞ to others | Define distância 0 para origem, ∞ para outros
2. **Select | Selecionar**: Choose unvisited vertex with minimum distance | Escolha vértice não visitado com distância mínima
3. **Relax | Relaxar**: Update neighbor distances if shorter path found | Atualize distâncias dos vizinhos se caminho mais curto for encontrado
4. **Repeat | Repetir**: Continue until all vertices visited | Continue até todos os vértices serem visitados

### Edge Relaxation | Relaxação de Arestas
```python
if distance[current] + weight(current, neighbor) < distance[neighbor]:
    distance[neighbor] = distance[current] + weight(current, neighbor)
    predecessor[neighbor] = current
```

---

<div align="center">

### 📝 Notes | Observações

**English**: This implementation assumes non-negative edge weights. For negative weights, use Bellman-Ford algorithm.

**Português**: Esta implementação assume pesos de arestas não-negativos. Para pesos negativos, use o algoritmo de Bellman-Ford.

---

### 📄 License | Licença

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 👤 Author | Autor

<div align="center">
  <a href="https://github.com/matheussricardoo" target="_blank">
    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/matheus-ricardo-426452266/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn"/>
  </a>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=000000&height=120&section=footer"/>
