![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=BFS%20Algorithm&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Breadth-First%20Search%20-%20Python%20Implementation&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](https://python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-BFS-FF6B6B?style=for-the-badge&logo=algorithm)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Queue-4ECDC4?style=for-the-badge&logo=data-structure)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Educational Implementation**: Step-by-step BFS visualization
- **Optimized Version**: Production-ready with collections.deque
- **Clean Syntax**: Pythonic implementation with clear structure
- **Graph Traversal**: Efficient level-order exploration

### 🇧🇷 Português
- **Implementação Educacional**: Visualização passo a passo do BFS
- **Versão Otimizada**: Pronta para produção com collections.deque
- **Sintaxe Limpa**: Implementação pythônica com estrutura clara
- **Travessia de Grafos**: Exploração eficiente por nível

<div align="center">

| Feature | Description | Descrição |
|:---:|:---|:---|
| 🎯 | Educational Implementation | Implementação Educacional - Sintaxe clara |
| 🚀 | Optimized with Deque | Otimizada com Deque - collections.deque |
| 📊 | Performance Analysis | Análise de Performance - Métricas de tempo |
| 🔍 | Multiple Search Types | Múltiplos Tipos de Busca - Caminho, níveis |
| 📈 | Connectivity Analysis | Análise de Conectividade - Componentes |
| 🐍 | Pythonic Code | Código Pythônico - Idiomas Python |
| ⚡ | List vs Deque Comparison | Comparação List vs Deque - Performance |
| 🎮 | Game Applications | Aplicações em Jogos - Pathfinding |

</div>

### 🛠️ Technologies | Tecnologias

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python&theme=dark" />
  </a>
</div>

## 📁 Estrutura dos Arquivos

### Versão Básica
- **`bfs_basico.py`**: Implementação didática
  - Uso de `collections.deque` para fila eficiente
  - Comentários extensos e visualização passo a passo
  - Type hints básicos para clareza
  - Exemplo completo de uso

### Versão Otimizada
- **`otimizado/bfs_otimizado.py`**: Implementação para produção
  - Lista de adjacência com `defaultdict`
  - Type hints completos
  - Múltiplas variações especializadas
  - Early termination e otimizações avançadas

## 🚀 Como Executar

### Versão Básica
```bash
cd python/bfs
python3 bfs_basico.py
```

### Versão Otimizada
```bash
cd python/bfs/otimizado
python3 bfs_otimizado.py
```

## 🐍 Características Python

### Vantagens
- **Sintaxe clara**: Código muito legível
- **Estruturas de dados nativas**: `deque`, `defaultdict`
- **Type hints**: Melhor documentação e IDE support
- **List comprehensions**: Código conciso

### Bibliotecas Utilizadas
```python
from collections import deque, defaultdict
from typing import List, Tuple, Optional, Dict
```

## 📊 Funcionalidades Implementadas

### Versão Básica
1. BFS simples com visualização
2. BFS com cálculo de distâncias
3. Busca de caminhos
4. Análise de vizinhos

### Versão Otimizada
1. BFS completo (visitação + distâncias + predecessores)
2. Busca de caminho com early termination
3. Organização por níveis de distância
4. Verificação de conectividade
5. Encontrar componentes conectados
6. Verificação de grafo bipartido
7. Estatísticas completas do grafo

### 🚀 Getting Started | Começando

```bash
# Basic Version | Versão Básica
cd python/bfs
python3 bfs_basico.py

# Optimized Version | Versão Otimizada
cd python/bfs/otimizado
python3 bfs_otimizado.py
```

### 💡 Python Concepts Demonstrated | Conceitos Python Demonstrados

<div align="center">

| Concept | Example | Description |
|:---:|:---|:---|
| 🔄 | `collections.deque` | O(1) queue operations |
| 📝 | `list comprehensions` | Pythonic data processing |
| 🏷️ | `type hints` | Static type checking |
| 📚 | `defaultdict` | Automatic list initialization |
| 🎨 | `f-strings` | Modern string formatting |

</div>

```python
# Deque for efficient queue operations
queue = deque([start_vertex])
current = queue.popleft()  # O(1)

# List comprehensions for neighbors
neighbors = [i for i, connected in enumerate(adj_row) if connected]

# Type hints for clarity
def bfs_path(self, start: int, target: int) -> Optional[List[int]]:

# Defaultdict for adjacency lists
self.adj_list = defaultdict(list)
```

### 📊 Implemented Features | Funcionalidades Implementadas

<div align="center">

| Basic Version | Optimized Version |
|:---|:---|
| Simple BFS with visualization | Complete BFS with statistics |
| Distance calculation | Early termination search |
| Path finding | Level-based organization |
| Neighbor analysis | Connectivity verification |
| | Connected components |
| | Bipartite graph checking |

</div>

### 🎯 Next Steps | Próximos Passos

Explore other implementations | Explore outras implementações:
- **dijkstra/** - Shortest paths with weights | Caminhos mais curtos com pesos
- **hashtable/** - Associative data structures | Estruturas de dados associativas  
- **linkedlist/** - Linked lists and linear structures | Listas ligadas e estruturas lineares

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
