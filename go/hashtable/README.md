![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Hash%20Table%20em%20Go&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Estrutura%20de%20dados%20para%20acesso%20rápido%20O(1)&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Go-white?style=for-the-badge&logo=go&logoColor=00ADD8)](https://golang.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Hash_Table-white?style=for-the-badge&logo=algorithm&logoColor=black)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Dictionary-white?style=for-the-badge&logo=data-structure&logoColor=black)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-white?style=for-the-badge&logo=open-source-initiative&logoColor=green)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Fast Access**: O(1) average time for insertions, deletions, and lookups
- **Educational Implementation**: Step-by-step visualization of hash operations
- **Optimized Version**: Production-ready with FNV-1a hash function
- **Collision Handling**: Chaining method for collision resolution
- **Auto-Resizing**: Dynamic table resizing based on load factor
- **Type Support**: Generic interface{} support in optimized version

### 🇧🇷 Português
- **Acesso Rápido**: Tempo médio O(1) para inserção, remoção e busca
- **Implementação Didática**: Visualização passo a passo das operações hash
- **Versão Otimizada**: Pronta para produção com função hash FNV-1a
- **Tratamento de Colisões**: Método de encadeamento para resolução de colisões
- **Redimensionamento Automático**: Redimensionamento dinâmico baseado no fator de carga
- **Suporte a Tipos**: Suporte genérico interface{} na versão otimizada

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
go/hashtable/
├── hashtable_basico.go      # 📚 Educational implementation
├── otimizado/
│   └── hashtable_otimizado.go # 🚀 Production-ready version
└── README.md               # 📖 Documentation
```

---

## 🚀 Quick Start | Início Rápido

### 🇺🇸 English

#### Basic Version (Educational)
```bash
cd hashtable
go run hashtable_basico.go
```

#### Optimized Version (Performance)
```bash
cd hashtable/otimizado
go run hashtable_otimizado.go
```

### 🇧🇷 Português

#### Versão Básica (Didática)
```bash
cd hashtable
go run hashtable_basico.go
```

#### Versão Otimizada (Performance)
```bash
cd hashtable/otimizado
go run hashtable_otimizado.go
```

---

## 📊 Complexity Analysis | Análise de Complexidade

### 🇺🇸 English
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| **Get** | O(1) | O(n) | Worst case: all keys collide |
| **Put** | O(1) | O(n) | Includes possible resizing |
| **Delete** | O(1) | O(n) | Depends on chain length |
| **Contains** | O(1) | O(n) | Same as Get operation |

### 🇧🇷 Português
| Operação | Caso Médio | Pior Caso | Observações |
|----------|------------|-----------|-------------|
| **Get** | O(1) | O(n) | Pior caso: todas as chaves colidem |
| **Put** | O(1) | O(n) | Inclui possível redimensionamento |
| **Delete** | O(1) | O(n) | Depende do comprimento da cadeia |
| **Contains** | O(1) | O(n) | Mesmo que operação Get |

---

## 🎯 Use Cases | Casos de Uso

### 🇺🇸 English
- **🔍 Fast Lookups**: Database indexes and caching systems
- **📊 Frequency Counting**: Word frequency analysis
- **🗂️ Data Indexing**: Key-value storage systems
- **🚀 In-Memory Databases**: High-performance data structures
- **🔄 Symbol Tables**: Compiler design and interpreters

### 🇧🇷 Português
- **🔍 Buscas Rápidas**: Índices de banco de dados e sistemas de cache
- **📊 Contagem de Frequência**: Análise de frequência de palavras
- **🗂️ Indexação de Dados**: Sistemas de armazenamento chave-valor
- **🚀 Bancos de Dados em Memória**: Estruturas de dados de alta performance
- **🔄 Tabelas de Símbolos**: Design de compiladores e interpretadores

---

## 💡 Implementation Details | Detalhes da Implementação

### 🇺🇸 English
#### Hash Function
```go
// Basic version: Simple ASCII sum
func hash(key string) int {
    sum := 0
    for _, char := range key {
        sum += int(char)
    }
    return sum % tableSize
}

// Optimized version: FNV-1a hash
func fnv1a(key string) uint32 {
    hash := uint32(2166136261)
    for _, b := range []byte(key) {
        hash ^= uint32(b)
        hash *= 16777619
    }
    return hash
}
```

#### Collision Resolution
- **Chaining**: Each bucket contains a linked list
- **Load Factor**: Automatically resizes when > 0.75
- **Dynamic Resizing**: Doubles table size and rehashes

### 🇧🇷 Português
#### Função Hash
```go
// Versão básica: Soma ASCII simples
func hash(key string) int {
    sum := 0
    for _, char := range key {
        sum += int(char)
    }
    return sum % tableSize
}

// Versão otimizada: hash FNV-1a
func fnv1a(key string) uint32 {
    hash := uint32(2166136261)
    for _, b := range []byte(key) {
        hash ^= uint32(b)
        hash *= 16777619
    }
    return hash
}
```

#### Resolução de Colisões
- **Encadeamento**: Cada bucket contém uma lista ligada
- **Fator de Carga**: Redimensiona automaticamente quando > 0.75
- **Redimensionamento Dinâmico**: Dobra o tamanho da tabela e recalcula hash

---

## 🔧 Technical Features | Características Técnicas

### 🇺🇸 English
- **Generic Support**: Works with any data type using interface{}
- **Thread-Safe Operations**: Concurrent access handling
- **Memory Efficient**: Automatic shrinking and growing
- **Performance Monitoring**: Built-in statistics and metrics
- **Debugging Tools**: Visualization of hash distribution

### 🇧🇷 Português
- **Suporte Genérico**: Funciona com qualquer tipo de dado usando interface{}
- **Operações Thread-Safe**: Tratamento de acesso concorrente
- **Eficiência de Memória**: Diminuição e crescimento automático
- **Monitoramento de Performance**: Estatísticas e métricas integradas
- **Ferramentas de Debug**: Visualização da distribuição hash

---

![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Linked%20List%20em%20Python&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Estrutura%20de%20dados%20linear%20dinâmica&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](https://python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Linked_List-FF6B6B?style=for-the-badge&logo=algorithm)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Linear-4ECDC4?style=for-the-badge&logo=data-structure)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

</div>

---

## 🌟 Features | Características

| English | Português |
|---------|-----------|
| **Dynamic Memory Allocation** | **Alocação Dinâmica de Memória** |
| No fixed size limitation | Sem limitação de tamanho fixo |
| **Efficient Insertion/Deletion** | **Inserção/Remoção Eficiente** |
| O(1) operations at head/tail | Operações O(1) no início/fim |
| **Memory Efficiency** | **Eficiência de Memória** |
| Only allocates needed memory | Aloca apenas memória necessária |
| **Two Implementation Types** | **Dois Tipos de Implementação** |
| Singly and doubly linked lists | Listas simplesmente e duplamente ligadas |

## 🛠️ Technologies | Tecnologias

<div align="center">

![Python](https://skillicons.dev/icons?i=python&theme=dark)

</div>

## 📁 Estrutura dos Arquivos

```
linkedlist/
├── linkedlist_basico.py                    # Implementação didática básica
├── doubly/
│   └── doubly_linkedlist_basico.py         # Lista duplamente ligada básica
├── otimizado/
│   └── linkedlist_otimizado.py             # Implementação otimizada avançada
└── README.md                               # Este arquivo
```

## 🎯 Versões Disponíveis

### 1. Versão Básica (`linkedlist_basico.py`)
- **Propósito**: Aprendizado e compreensão dos conceitos
- **Características**:
  - Implementação simples e didática
  - Operações fundamentais claramente explicadas
  - Código comentado para facilitar entendimento
  - Ideal para estudantes iniciantes

### 2. Lista Duplamente Ligada (`doubly/doubly_linkedlist_basico.py`)
- **Propósito**: Compreensão de navegação bidirecional
- **Características**:
  - Cada nó possui ponteiros para próximo E anterior
  - Operações O(1) em ambas as extremidades
  - Navegação eficiente em ambas as direções
  - Casos de uso práticos demonstrados

### 3. Versão Otimizada (`otimizado/linkedlist_otimizado.py`)
- **Propósito**: Uso em aplicações reais e estudos avançados
- **Características**:
  - Cache do último nó acessado para buscas sequenciais
  - Ponteiro de cauda para inserções O(1) no final
  - Suporte completo a operadores Python
  - Lista duplamente ligada incluída
  - Estatísticas de performance
  - Interface Pythônica com iteradores

## 🚀 Quick Start | Início Rápido

```bash
# Clone the repository | Clone o repositório
git clone https://github.com/matheussricardoo/Algorithms.git
cd algorithms/python/linkedlist

# Run basic version | Execute versão básica
python linkedlist_basico.py

# Run doubly linked list | Execute lista duplamente ligada
python doubly/doubly_linkedlist_basico.py

# Run optimized version | Execute versão otimizada
python otimizado/linkedlist_otimizado.py
```

## 📊 Exemplos de Uso

### Exemplo Básico
```python
from linkedlist_basico import ListaLigada

# Cria uma lista ligada
lista = ListaLigada()

# Insere elementos
lista.inserir_inicio("primeiro")
lista.inserir_fim("último")
lista.inserir_posicao(1, "meio")

# Busca elementos
posicao = lista.buscar("meio")
print(f"'meio' está na posição: {posicao}")

# Remove elementos
removido = lista.remover_inicio()
print(f"Removido: {removido}")
```

### Exemplo Lista Duplamente Ligada
```python
from doubly.doubly_linkedlist_basico import ListaDuplamenteLigada

# Cria uma lista duplamente ligada
lista_dupla = ListaDuplamenteLigada()

# Inserções eficientes em ambas as extremidades
lista_dupla.inserir_inicio("primeiro")
lista_dupla.inserir_fim("último")
lista_dupla.inserir_posicao(1, "meio")

# Navegação bidirecional
print("Frente para trás:")
for item in lista_dupla:
    print(item)

print("Trás para frente:")  
for item in lista_dupla.iter_reverso():
    print(item)

# Remoções O(1) de ambas as extremidades
inicio = lista_dupla.remover_inicio()
fim = lista_dupla.remover_fim()
```

### Exemplo Otimizado
```python
from otimizado.linkedlist_otimizado import ListaLigadaOtimizada

# Cria uma lista otimizada
lista = ListaLigadaOtimizada()

# Interface Pythônica
lista.inserir_fim("a")
lista.inserir_fim("b")
lista.inserir_fim("c")

# Acesso por índice
print(lista[1])  # "b"

# Iteração
for item in lista:
    print(item)

# Estatísticas de cache
stats = lista.obter_estatisticas()
print(f"Cache hit rate: {stats['cache_hit_rate']}%")
```

## 🔍 Conceitos Importantes

### Estrutura Básica
```python
class No:
    def __init__(self, dados, proximo=None):
        self.dados = dados      # Dados armazenados
        self.proximo = proximo  # Referência para próximo nó
```

### Tipos de Lista Ligada

#### 1. **Lista Simples**
- Cada nó aponta apenas para o próximo
- Navegação unidirecional
- Menos uso de memória

#### 2. **Lista Duplamente Ligada**
- Cada nó tem ponteiros para próximo e anterior
- Navegação bidirecional
- Remoções mais eficientes

#### 3. **Lista Circular**
- Último nó aponta para o primeiro
- Útil para implementar buffers circulares

## 📈 Complexidade de Tempo

| Operação | Lista Básica | Lista Otimizada | Lista Dupla |
|----------|--------------|-----------------|-------------|
| Inserção no início | O(1) | O(1) | O(1) |
| Inserção no fim | O(n) | O(1)* | O(1) |
| Inserção no meio | O(n) | O(n)** | O(n) |
| Remoção do início | O(1) | O(1) | O(1) |
| Remoção do fim | O(n) | O(n) | O(1) |
| Busca por valor | O(n) | O(n)** | O(n) |
| Acesso por índice | O(n) | O(n)** | O(n) |

*\* Com ponteiro de cauda*  
*\*\* Com cache de último acesso*

## 🎓 Advantages vs Disadvantages | Vantagens vs Desvantagens

<div align="center">

| ✅ Advantages | ✅ Vantagens | ❌ Disadvantages | ❌ Desvantagens |
|:---|:---|:---|:---|
| Dynamic size | Tamanho dinâmico | Sequential access only | Apenas acesso sequencial |
| Efficient insertion O(1) | Inserção eficiente O(1) | Memory overhead per node | Overhead de ponteiros |
| Memory as needed | Uso eficiente de memória | Cache locality issues | Problemas de cache locality |
| Flexible reorganization | Flexibilidade de reorganização | More complex than arrays | Mais complexa que arrays |

</div>

## 🛠️ Otimizações Implementadas

### 1. **Cache de Último Acesso**
```python
# Evita buscar desde o início em acessos sequenciais
if cache_indice <= indice_desejado:
    partir_do_cache()
else:
    partir_do_inicio()
```

### 2. **Ponteiro de Cauda**
```python
# Inserção O(1) no final
def inserir_fim(self, dados):
    novo_no = No(dados)
    self.cauda.proximo = novo_no
    self.cauda = novo_no
```

### 3. **Interface Pythônica**
```python
# Suporte a operadores Python
lista[indice]           # __getitem__
lista[indice] = valor   # __setitem__
len(lista)              # __len__
for item in lista:      # __iter__
```

### 4. **Estatísticas de Performance**
```python
stats = lista.obter_estatisticas()
# Retorna: cache hits, total de acessos, hit rate
```

## 🎯 Casos de Uso Práticos

### 1. **Implementação de Pilhas e Filas**
```python
# Pilha (LIFO)
pilha = ListaLigada()
pilha.inserir_inicio(item)  # push
pilha.remover_inicio()      # pop

# Fila (FIFO) com lista otimizada
fila = ListaLigadaOtimizada()
fila.inserir_fim(item)      # enqueue
fila.remover_inicio()       # dequeue
```

### 2. **Histórico de Navegação**
```python
# Histórico do navegador
historico = ListaDuplamenteLigada()
historico.inserir_fim(url)  # nova página
historico.remover_fim()     # voltar
```

### 3. **Lista de Reprodução**
```python
# Player de música
playlist = ListaLigada()
playlist.inserir_fim(musica)
# Fácil de reorganizar e inserir no meio
```

### 4. **Implementação de Outras Estruturas**
- **Hash Table com Chaining**
- **Grafos** (lista de adjacências)
- **Árvores** (filhos como lista ligada)

## 🔧 Dicas de Implementação

### Versão Básica
- Use para aprender os conceitos fundamentais
- Ideal para entender ponteiros e referências
- Boa para listas pequenas (< 100 elementos)
- Foco na clareza do código

### Versão Otimizada
- Use para aplicações reais
- Melhor para acessos sequenciais frequentes
- Interface mais amigável para Python
- Inclui ferramentas de debugging

### Lista Duplamente Ligada
- Use quando precisar navegar nas duas direções
- Ideal para implementar deques
- Melhor para remoções frequentes no final
- Usar quando a memória extra não for problema

## 📊 Comparação com Outras Estruturas

| Estrutura | Acesso | Inserção | Remoção | Uso de Memória |
|-----------|--------|----------|---------|----------------|
| Lista Ligada | O(n) | O(1)* | O(1)* | Médio |
| Array/List | O(1) | O(n)** | O(n)** | Baixo |
| ArrayList | O(1) | O(1)*** | O(n) | Médio |
| Deque | O(n) | O(1) | O(1) | Médio |

*\* No início*  
*\*\* No meio/início*  
*\*\*\* No final, amortizado*

### 🎯 Ideal Use Cases | Casos de Uso Ideais

<div align="center">

| Application | Aplicação | Description | Descrição |
|:---:|:---:|:---|:---|
| 📚 | Stacks & Queues | **Pilhas e Filas** | LIFO/FIFO structures |
| 🎵 | Music Playlists | **Listas de Reprodução** | Easy reorganization |
| 🌐 | Browser History | **Histórico de Navegação** | Back/forward navigation |
| 🏗️ | Data Structures | **Outras Estruturas** | Hash tables, graphs, trees |
| 🔄 | Memory Management | **Gerenciamento de Memória** | Dynamic allocation |

</div>

### 🚀 When to Use | Quando Usar

<div align="center">

| ✅ Use When | ✅ Use Quando | ❌ Avoid When | ❌ Evite Quando |
|:---|:---|:---|:---|
| Dynamic size needed | Tamanho dinâmico necessário | Random access required | Acesso aleatório necessário |
| Frequent insertions | Inserções frequentes | Read-only operations | Operações somente leitura |
| Memory is fragmented | Memória fragmentada | Cache performance critical | Performance de cache crítica |
| Implementing structures | Implementando estruturas | Working with small data | Trabalhando com dados pequenos |

</div>

## 🔗 Estruturas Relacionadas

- **Stack (Pilha)**: Lista ligada + operações LIFO
- **Queue (Fila)**: Lista ligada + operações FIFO
- **Deque**: Lista duplamente ligada + operações em ambas extremidades
- **Skip List**: Lista ligada com níveis para busca mais rápida

## 📚 Recursos Adicionais

- **Complexidade de Espaço**: O(n)
- **Inventor**: Conceito fundamental da ciência da computação
- **Variações**: Circular, auto-organizante, skip list
- **Aplicações**: Compiladores, sistemas operacionais, bancos de dados

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
