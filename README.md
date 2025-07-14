<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=000000&height=200&section=header&text=Algorithms&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Educational%20repository%20for%20algorithms%20and%20data%20structures&descAlignY=60&descSize=18">

<p align="center">
  <i>🧮 Educational repository for fundamental algorithms and data structures, organized for progressive learning with basic (educational) and optimized (production) versions.</i>
</p>

<p align="center">
  <i>🧮 Repositório educacional para algoritmos fundamentais e estruturas de dados, organizado para aprendizado progressivo com versões básicas (educacionais) e otimizadas (produção).</i>
</p>

---

### 🌟 Learning Philosophy | Filosofia de Aprendizado

<div align="center">

| Step | Description | Descrição |
|:---:|:---|:---|
| 🎯 | Basic Version | Versão Básica - Implementação didática com comentários extensos |
| 🚀 | Optimized Version | Versão Otimizada - Implementação para produção com melhorias de performance |
| 📖 | Detailed README | README Detalhado - Explicações teóricas, complexidade, e casos de uso |
| 🧪 | Practical Examples | Exemplos Práticos - Demonstrações reais de aplicação |

</div>

### 🛠️ Technologies | Tecnologias

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python&theme=dark" />
  </a>
  <p><i>🆕 Novos algoritmos implementados em Python | New algorithms implemented in Python</i></p>
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,python,java&theme=dark" />
  </a>
  <p><i>📚 Algoritmos existentes em múltiplas linguagens | Existing algorithms in multiple languages</i></p>
</div>

### 📁 Repository Structure | Estrutura do Repositório

```
Algorithms/
├── python/                 # Implementações em Python ✅
│   ├── bfs/               # Busca em Largura
│   ├── dijkstra/          # Algoritmo de Dijkstra  
│   ├── hashtable/         # Tabela Hash
│   ├── knn/               # K-Nearest Neighbors
│   ├── linkedlist/        # Lista Ligada
│   ├── simhash/           # 🆕 SimHash - Detecção de Similaridade
│   ├── sha/               # 🆕 SHA-256 - Hash Criptográfico
│   ├── inverted_index/    # 🆕 Índice Invertido com Hash
│   ├── ocr/               # 🆕 OCR - Reconhecimento Óptico
│   ├── fourier/           # 🆕 Transformada de Fourier
│   ├── naive_bayes/       # 🆕 Classificador Naive Bayes
│   └── ... mais algoritmos
├── go/                     # Implementações em Go ✅
│   ├── bfs/               # Busca em Largura
│   ├── dijkstra/          # Algoritmo de Dijkstra
│   ├── hashtable/         # Tabela Hash
│   ├── knn/               # K-Nearest Neighbors
│   ├── linkedlist/        # Lista Ligada
│   └── ... mais algoritmos
├── java/                   # Implementações em Java ✅
│   ├── bfs/               # Busca em Largura
│   ├── dijkstra/          # Algoritmo de Dijkstra
│   ├── hashtable/         # Tabela Hash
│   ├── knn/               # K-Nearest Neighbors
│   ├── linkedlist/        # Lista Ligada
│   └── ... mais algoritmos
└── README.md
```

### 🧮 Implemented Algorithms | Algoritmos Implementados

<div align="center">

| Algorithm | Description | Descrição | Complexity | Status |
|:---:|:---|:---|:---:|:---:|
| 🔍 | **BFS** - Breadth-First Search | **BFS** - Busca em Largura | O(V+E) | 🟢 Multi-lang |
| 🛣️ | **Dijkstra** - Shortest Path | **Dijkstra** - Caminho Mais Curto | O((V+E)logV) | 🟢 Multi-lang |
| 🗂️ | **Hash Table** - Key-Value Store | **Hash Table** - Armazenamento Chave-Valor | O(1) avg | 🟢 Multi-lang |
| 🔗 | **Linked List** - Dynamic Structure | **Lista Ligada** - Estrutura Dinâmica | O(n) | 🟢 Multi-lang |
| 🤖 | **KNN** - K-Nearest Neighbors | **KNN** - K-Vizinhos Mais Próximos | O(n·d) | 🟢 Multi-lang |
| 📄 | **SimHash** - Document Similarity | **SimHash** - Similaridade de Documentos | O(n) | 🐍 Python |
| 🔐 | **SHA-256** - Cryptographic Hash | **SHA-256** - Hash Criptográfico | O(n) | 🐍 Python |
| 📚 | **Inverted Index** - Search Engine | **Índice Invertido** - Motor de Busca | O(n×m) | 🐍 Python |
| 👁️ | **OCR** - Character Recognition | **OCR** - Reconhecimento de Caracteres | O(w×h) | 🐍 Python |
| 🌊 | **Fourier Transform** - Signal Analysis | **Transformada de Fourier** - Análise de Sinais | O(n log n) | 🐍 Python |
| 🧠 | **Naive Bayes** - ML Classifier | **Naive Bayes** - Classificador ML | O(n×d) | 🐍 Python |

</div>

## 🚀 Quick Start | Início Rápido

### 🆕 Novos Algoritmos Python
```bash
# Executar todos os novos algoritmos
chmod +x run_demos.sh && ./run_demos.sh

# Algoritmos individuais:
cd python/simhash && python simhash_basico.py        # Similaridade de documentos
cd python/sha && python sha_basico.py               # Hash criptográfico
cd python/inverted_index && python inverted_index_basico.py  # Motor de busca
cd python/fourier && python fourier_basico.py       # Análise de sinais
cd python/naive_bayes && python naive_bayes_basico.py # Classificação ML

# OCR (requer NumPy)
pip install numpy
cd python/ocr && python ocr_basico.py
```

### 📚 Algoritmos Existentes

#### Python
```bash
cd python/bfs && python bfs_basico.py
cd python/dijkstra && python dijkstra_basico.py
cd python/hashtable && python hashtable_basico.py
cd python/linkedlist && python linkedlist_basico.py
cd python/knn && python knn_basico.py
```

#### Go
```bash
cd go/bfs && go run bfs_basico.go
cd go/dijkstra && go run dijkstra_basico.go
cd go/hashtable && go run hashtable_basico.go
cd go/linkedlist && go run linkedlist_basico.go
cd go/knn && go run knn_basico.go
```

#### Java
```bash
cd java && javac bfs/*.java && java BFSBasico
cd java && javac dijkstra/*.java && java DijkstraBasico
cd java && javac hashtable/*.java && java HashTableBasico
cd java && javac linkedlist/*.java && java LinkedListBasico
cd java && javac knn/*.java && java KNNBasico
```

## 📊 Tabela de Complexidade

| Algoritmo | Estrutura | Tempo | Espaço | Melhor Para |
|-----------|-----------|-------|--------|-------------|
| **BFS** | Lista/Matriz | O(V+E) / O(V²) | O(V) | Grafos esparsos/densos |
| **Dijkstra** | Heap + Lista | O((V+E)log V) | O(V+E) | Grafos com pesos |
| **Hash Table** | Array + Listas | O(1) médio | O(n) | Acesso por chave |
| **Lista Ligada** | Ponteiros | O(1) inserção | O(n) | Inserção dinâmica |
| **KNN** | Arrays/Listas | O(n·d) | O(n·d) | Classificação/Recomendação |
| **SimHash** | Bit vectors | O(n) | O(1) | Detecção de duplicados |
| **SHA-256** | Hash blocks | O(n) | O(1) | Verificação de integridade |
| **Índice Invertido** | Hash + Listas | O(n×m) | O(n×m) | Busca textual |
| **OCR** | Template matching | O(w×h) | O(w×h) | Reconhecimento visual |
| **Fourier** | FFT/DFT | O(n log n) | O(n) | Análise espectral |
| **Naive Bayes** | Probabilidade | O(n×d) | O(n×d) | Classificação de texto |

## 🎯 Como Usar Este Repositório

### Para Iniciantes
1. **Comece com versões básicas** - foque no entendimento
2. **Leia os READMEs** - teoria e conceitos fundamentais
3. **Execute os exemplos** - veja o algoritmo em ação
4. **Modifique o código** - experimente e aprenda

### Para Estudantes Avançados
1. **Compare implementações** - básica vs otimizada
2. **Analise complexidade** - tempo e espaço
3. **Estude otimizações** - técnicas de melhoria
4. **Implemente variações** - exercícios sugeridos

### Para Profissionais
1. **Use versões otimizadas** - prontas para produção
2. **Entenda trade-offs** - quando usar cada algoritmo
3. **Adapte para seu contexto** - customize conforme necessário
4. **Contribua** - adicione melhorias e novas implementações

## 📊 Status de Implementação

### 🟢 Python (11 algoritmos)
| Algoritmo | Básico | Otimizado | README | Casos de Uso |
|-----------|--------|-----------|--------|-------------|
| BFS | ✅ | ✅ | ✅ | Grafos, redes sociais |
| Dijkstra | ✅ | ✅ | ✅ | GPS, roteamento |
| Hash Table | ✅ | ✅ | ✅ | Caches, índices |
| Linked List | ✅ | ✅ | ✅ | Estruturas dinâmicas |
| KNN | ✅ | ✅ | ✅ | Recomendações, ML |
| **SimHash** | ✅ | ⏳ | ✅ | Detecção de plágio |
| **SHA-256** | ✅ | ⏳ | ✅ | Segurança, blockchain |
| **Índice Invertido** | ✅ | ⏳ | ✅ | Motores de busca |
| **OCR** | ✅ | ⏳ | ✅ | Digitalização, tradução |
| **Fourier** | ✅ | ⏳ | ✅ | Áudio, telecomunicações |
| **Naive Bayes** | ✅ | ⏳ | ✅ | Filtro spam, sentimento |

### 🟢 Go (5 algoritmos)
| Algoritmo | Básico | Otimizado | README | Performance |
|-----------|--------|-----------|--------|-------------|
| BFS | ✅ | ✅ | ✅ | Alta |
| Dijkstra | ✅ | ✅ | ✅ | Alta |
| Hash Table | ✅ | ✅ | ✅ | Alta |
| Linked List | ✅ | ✅ | ✅ | Alta |
| KNN | ✅ | ✅ | ✅ | Alta |

### 🟢 Java (5 algoritmos)
| Algoritmo | Básico | Otimizado | README | Enterprise |
|-----------|--------|-----------|--------|------------|
| BFS | ✅ | ✅ | ✅ | Pronto |
| Dijkstra | ✅ | ✅ | ✅ | Pronto |
| Hash Table | ✅ | ✅ | ✅ | Pronto |
| Linked List | ✅ | ✅ | ✅ | Pronto |
| KNN | ✅ | ✅ | ✅ | Pronto |

## 🚀 Próximos Algoritmos

### Planejados
- [ ] **DFS** - Depth-First Search | Busca em Profundidade
- [ ] **Sorting** - Bubble, Quick, Merge, Heap Sort | Algoritmos de Ordenação
- [ ] **Trees** - BST, AVL, Red-Black | Árvores
- [ ] **Advanced Graphs** - Kruskal, Prim, Floyd-Warshall | Grafos Avançados
- [ ] **Dynamic Programming** - Fibonacci, Knapsack, LCS | Programação Dinâmica
- [ ] **String Algorithms** - KMP, Rabin-Karp | Algoritmos de String

### Versões Otimizadas (Em Desenvolvimento)
- [ ] **SimHash** - Índice LSH para busca rápida
- [ ] **SHA-256** - Implementação SIMD para performance
- [ ] **Índice Invertido** - Compressão e skip lists
- [ ] **OCR** - Redes neurais e templates dinâmicos
- [ ] **Fourier** - Implementação GPU-accelerated
- [ ] **Naive Bayes** - Feature selection automática

## 🤝 How to Contribute | Como Contribuir

<div align="center">

| Step | Action | Ação |
|:---:|:---|:---|
| 🍴 | Fork the repository | Fork o repositório |
| 🌿 | Create a feature branch | Crie uma branch para sua feature |
| 💻 | Implement following patterns | Implemente seguindo os padrões |
| 🧪 | Test your implementations | Teste suas implementações |
| 📤 | Open a Pull Request | Abra um Pull Request |

</div>

## 📚 Additional Resources | Recursos Adicionais

**Books | Livros**
- "Introduction to Algorithms" - Cormen, Leiserson, Rivest, Stein
- "Data Structures and Algorithms" - Aho, Hopcroft, Ullman
- "Algorithms" - Robert Sedgewick

**Online Courses | Cursos Online**
- Coursera: Algorithms Specialization (Stanford)
- edX: MIT Introduction to Algorithms
- YouTube: Abdul Bari's Algorithm Playlist

**Practice | Prática**
- LeetCode: Practical problems | Problemas práticos
- HackerRank: Progressive challenges | Desafios progressivos
- CodeForces: Programming competitions | Competições de programação

## 👤 Author | Autor

<div align="center">
  <a href="https://github.com/matheussricardoo" target="_blank">
    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/matheus-ricardo-426452266/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn"/>
  </a>
</div>

## 📄 License | Licença

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Acknowledgments | Agradecimentos

- **CommitToLearn** community for inspiration | Comunidade pela inspiração
- All contributors who helped improve this repository | Todos os contribuidores
- Teachers and books that provided the foundational knowledge | Professores e livros que forneceram conhecimento base

---

<div align="center">
  <i>💡 Tip: Start with the algorithm that sparks your curiosity the most. All paths lead to learning!</i>
  <br>
  <i>💡 Dica: Comece pelo algoritmo que mais desperta sua curiosidade. Todos os caminhos levam ao aprendizado!</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=000000&height=120&section=footer"/>

</div>
