![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=BFS%20Algorithm&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Breadth-First%20Search%20-%20Java%20Implementation&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=java)](https://java.com/)
[![Algorithm](https://img.shields.io/badge/Algorithm-BFS-FF6B6B?style=for-the-badge&logo=algorithm)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Queue-4ECDC4?style=for-the-badge&logo=data-structure)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Object-Oriented Design**: Clean Java implementation with proper encapsulation
- **Educational Version**: Step-by-step BFS visualization
- **Optimized Classes**: Production-ready with performance metrics
- **Graph Traversal**: Efficient level-order exploration

### 🇧🇷 Português
- **Design Orientado a Objetos**: Implementação Java limpa com encapsulamento adequado
- **Versão Educacional**: Visualização passo a passo do BFS
- **Classes Otimizadas**: Prontas para produção com métricas de performance
- **Travessia de Grafos**: Exploração eficiente por nível

<div align="center">

| Feature | Description | Descrição |
|:---:|:---|:---|
| 🎯 | Educational Implementation | Implementação Educacional - Clara e didática |
| 🚀 | Production-Ready Classes | Classes Prontas para Produção - Otimizadas |
| 📊 | Performance Statistics | Estatísticas de Performance - Métricas detalhadas |
| 🔍 | Multiple Search Types | Múltiplos Tipos de Busca - Caminho, conectividade |
| 📈 | Early Termination | Terminação Antecipada - Para quando encontra destino |
| 🧬 | Generic Type Support | Suporte a Tipos Genéricos - Type-safe |
| 🎮 | Pathfinding Ready | Pronto para Pathfinding - Aplicações em jogos |
| ⚡ | Optimized Data Structures | Estruturas de Dados Otimizadas - HashMap, ArrayDeque |

</div>

### 🛠️ Technologies | Tecnologias

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=java&theme=dark" />
  </a>
</div>

## 📁 Estrutura dos Arquivos

```
bfs/
├── BFSBasico.java                  # Implementação didática básica
├── otimizado/
│   ├── GrafoBFSOtimizado.java     # Implementação otimizada do grafo
│   ├── ResultadoBFS.java          # Classe para resultados da busca
│   ├── EstatisticasPerformance.java # Classe para métricas de performance
│   └── ExemploBFSOtimizado.java   # Exemplos de uso
└── README.md                       # Este arquivo
```

## 🎯 Versões Disponíveis

### 1. Versão Básica (`BFSBasico.java`)
- **Propósito**: Aprendizado e compreensão dos conceitos
- **Características**:
  - Implementação simples e didática
  - Código comentado linha por linha
  - Estruturas de dados básicas
  - Ideal para estudantes iniciantes

### 2. Versão Otimizada (`otimizado/`)
- **Propósito**: Uso em aplicações reais e estudos avançados
- **Características**:
  - Uso de `ArrayDeque` para melhor performance
  - Suporte a tipos genéricos (`<T>`)
  - Parada antecipada quando destino é encontrado
  - Estatísticas detalhadas de performance
  - Interface robusta com validações
  - Múltiplas funcionalidades avançadas

## 🚀 Como Executar

### Compilar e executar versão básica:
```bash
cd java/bfs
javac BFSBasico.java
java BFSBasico
```

### Compilar e executar versão otimizada:
```bash
cd java/bfs/otimizado
javac *.java
java ExemploBFSOtimizado
```

## 📊 Exemplos de Uso

### Exemplo Básico
```java
GrafoBFS grafo = new GrafoBFS();

// Adiciona conexões
grafo.adicionarAresta("A", "B");
grafo.adicionarAresta("A", "C");
grafo.adicionarAresta("B", "D");

// Executa BFS
grafo.bfs("A");
```

### Exemplo Otimizado
```java
GrafoBFSOtimizado<String> grafo = new GrafoBFSOtimizado<>();

// Adiciona conexões
grafo.adicionarAresta("Alice", "Bob");
grafo.adicionarAresta("Bob", "Carol");

// Busca caminho específico
ResultadoBFS<String> resultado = grafo.bfsOtimizado("Alice", "Carol");

// Obtém o caminho
List<String> caminho = resultado.getCaminho();
System.out.println("Caminho: " + caminho);

// Estatísticas
EstatisticasPerformance stats = grafo.obterEstatisticas();
stats.imprimir();
```

### Funcionalidades Avançadas
```java
// Verifica conectividade
boolean conectado = grafo.existeCaminho("A", "Z");

// Calcula distâncias
Map<String, Integer> distancias = grafo.calcularDistancias("A");

// Encontra vértices em nível específico
Set<String> nivel2 = grafo.verticesNoNivel("A", 2);

// Caminho mais curto
List<String> caminho = grafo.encontrarCaminhoMaisCurto("A", "Z");
```

## 🔍 Conceitos Importantes

### Como Funciona o BFS
1. **Inicialização**: Coloca o vértice inicial na fila
2. **Marcação**: Marca o vértice como visitado
3. **Exploração**: Remove da fila e explora todos os vizinhos não visitados
4. **Repetição**: Repete até a fila estar vazia ou encontrar o destino

### Estruturas de Dados Utilizadas
- **Fila (Queue)**: Para manter a ordem FIFO (primeiro a entrar, primeiro a sair)
- **Set/Boolean Array**: Para marcar vértices visitados
- **Map**: Para armazenar predecessores (reconstrução do caminho)

### Propriedades do BFS
- **Completude**: Sempre encontra uma solução se ela existir
- **Optimalidade**: Encontra o caminho mais curto (menor número de arestas)
- **Complexidade de Tempo**: O(V + E) onde V = vértices, E = arestas
- **Complexidade de Espaço**: O(V) para estruturas auxiliares

## 📈 Comparação de Performance

| Aspecto | Versão Básica | Versão Otimizada |
|---------|---------------|------------------|
| Estrutura de dados | ArrayList | ArrayDeque |
| Tipos suportados | String apenas | Genérico `<T>` |
| Parada antecipada | Não | Sim |
| Estatísticas | Básicas | Detalhadas |
| Validações | Mínimas | Robustas |
| Funcionalidades extras | Poucas | Muitas |

## 🎓 Aplicações Práticas

### 1. **Redes Sociais**
- Encontrar grau de separação entre pessoas
- Sugerir amigos em comum
- Analisar influência em redes

### 2. **Navegação e Mapas**
- Encontrar rota com menor número de paradas
- Análise de redes de transporte público
- Planejamento urbano

### 3. **Redes de Computadores**
- Descoberta de topologia de rede
- Protocolos de roteamento
- Análise de conectividade

### 4. **Jogos**
- Pathfinding em grades
- IA para movimentação de personagens
- Busca em espaços de estados

### 5. **Web e Internet**
- Web crawling
- Análise de links
- Indexação de páginas

## 🛠️ Características da Versão Otimizada

### Tipos Genéricos
```java
// Suporte a qualquer tipo de dados
GrafoBFSOtimizado<Integer> grafoNumerico = new GrafoBFSOtimizado<>();
GrafoBFSOtimizado<String> grafoTexto = new GrafoBFSOtimizado<>();
GrafoBFSOtimizado<Usuario> grafoUsuarios = new GrafoBFSOtimizado<>();
```

### Parada Antecipada
```java
// Para quando encontra o destino
ResultadoBFS<String> resultado = grafo.bfsOtimizado("origem", "destino");

// Busca completa (explora tudo)
ResultadoBFS<String> completo = grafo.bfsCompleto("origem");
```

### Estatísticas Detalhadas
```java
EstatisticasPerformance stats = grafo.obterEstatisticas();
// Retorna: tempo de execução, nós visitados, eficiência, etc.
```

### Validações Robustas
- Verificação de argumentos null
- Tratamento de vértices inexistentes
- Prevenção de loops infinitos

## 📊 Dicas de Uso

### Quando Usar a Versão Básica
- Aprendendo os conceitos fundamentais
- Grafos pequenos (< 100 vértices)
- Prototipagem rápida
- Fins educacionais

### Quando Usar a Versão Otimizada
- Aplicações de produção
- Grafos grandes (milhares de vértices)
- Necessidade de estatísticas
- Performance crítica
- Tipos de dados variados

### Otimizações Implementadas

#### 1. **ArrayDeque vs LinkedList**
- `ArrayDeque` é mais eficiente para operações de fila
- Melhor cache locality
- Menor overhead de memória

#### 2. **HashSet para Visitados**
- Verificação O(1) vs O(n) em listas
- Mais eficiente para grafos grandes

#### 3. **Parada Antecipada**
- Para quando encontra o destino
- Economiza tempo em buscas específicas

#### 4. **Generics**
- Type safety em tempo de compilação
- Elimina necessidade de casting
- Reutilização de código

## 🔗 Algoritmos Relacionados

- **DFS (Depth-First Search)**: Busca em profundidade
- **Dijkstra**: Caminho mais curto com pesos
- **A* (A-star)**: BFS com heurística
- **Bidirectional BFS**: Busca a partir de ambas as extremidades

## 📚 Teoria Adicional

### Invariantes do BFS
1. Vértices são visitados em ordem de distância crescente
2. Cada vértice é visitado exatamente uma vez
3. O primeiro caminho encontrado é sempre o mais curto

### Variações do BFS
- **Multi-source BFS**: Múltiplos pontos de partida
- **Bidirectional BFS**: Busca de ambos os lados
- **BFS em grafos ponderados**: Usando filas de prioridade

### Limitações
- **Uso de memória**: Pode ser alto para grafos largos
- **Não funciona bem com pesos**: Use Dijkstra para arestas ponderadas
- **Performance em grafos densos**: DFS pode ser melhor em alguns casos

### 📊 Complexity Analysis | Análise de Complexidade

<div align="center">

| Case | Time | Space | Descrição |
|:---:|:---:|:---:|:---|
| **Best** | O(1) | O(V) | Target is start vertex \| Destino é vértice inicial |
| **Average** | O(V+E) | O(V) | Explores part of graph \| Explora parte do grafo |
| **Worst** | O(V+E) | O(V) | Explores entire graph \| Explora todo o grafo |

</div>

### ⚡ Implementation Tips | Dicas de Implementação

```java
// ✅ Use ArrayDeque for better performance
Queue<Integer> queue = new ArrayDeque<>();

// ✅ Use HashSet for O(1) lookup
Set<Integer> visited = new HashSet<>();

// ✅ Early termination for specific searches
if (current == target) return path;

// ✅ Validate input
if (start < 0 || start >= vertices) throw new IllegalArgumentException();
```

### 🔗 Related Algorithms | Algoritmos Relacionados

- **DFS** - Depth-First Search | Busca em profundidade
- **Dijkstra** - Shortest path with weights | Caminho mais curto com pesos
- **A*** - BFS with heuristics | BFS com heurística
- **Bidirectional BFS** - Search from both ends | Busca de ambas as extremidades

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
