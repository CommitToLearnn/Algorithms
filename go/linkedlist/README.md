![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Linked%20List%20em%20Go&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Estrutura%20de%20dados%20linear%20dinâmica&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Go-white?style=for-the-badge&logo=go&logoColor=00ADD8)](https://golang.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Linked_List-white?style=for-the-badge&logo=algorithm&logoColor=black)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Linear-white?style=for-the-badge&logo=data-structure&logoColor=black)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-white?style=for-the-badge&logo=open-source-initiative&logoColor=green)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Dynamic Size**: Grows and shrinks as needed during runtime
- **Efficient Insertion**: O(1) insertion at the beginning
- **Memory Efficient**: Allocates only what's needed
- **Multiple Implementations**: Basic, optimized, and doubly linked versions
- **Educational**: Step-by-step learning with detailed comments
- **Generic Support**: Works with any data type using interface{}

### 🇧🇷 Português
- **Tamanho Dinâmico**: Cresce e diminui conforme necessário durante a execução
- **Inserção Eficiente**: Inserção O(1) no início
- **Eficiência de Memória**: Aloca apenas o que é necessário
- **Múltiplas Implementações**: Versões básica, otimizada e duplamente ligada
- **Didática**: Aprendizado passo a passo com comentários detalhados
- **Suporte Genérico**: Funciona com qualquer tipo de dado usando interface{}

---

## 🛠️ Technologies | Tecnologias

<div align="center">

[![Go](https://skillicons.dev/icons?i=go)](https://golang.org/)

</div>

---

## 📁 Project Structure | Estrutura do Projeto

```
go/linkedlist/
├── linkedlist_basico.go       # 📚 Basic implementation
├── otimizado/
│   └── linkedlist_otimizado.go # 🚀 Optimized version
├── doubly/
│   └── doubly_linkedlist_basico.go # 🔗 Doubly linked list
└── README.md                  # 📖 Documentation
```

---

## 🚀 Quick Start | Início Rápido

### 🇺🇸 English

#### Basic Version
```bash
cd linkedlist
go run linkedlist_basico.go
```

#### Optimized Version
```bash
cd linkedlist/otimizado
go run linkedlist_otimizado.go
```

#### Doubly Linked List
```bash
cd linkedlist/doubly
go run doubly_linkedlist_basico.go
```

### 🇧🇷 Português

#### Versão Básica
```bash
cd linkedlist
go run linkedlist_basico.go
```

#### Versão Otimizada
```bash
cd linkedlist/otimizado
go run linkedlist_otimizado.go
```

#### Lista Duplamente Ligada
```bash
cd linkedlist/doubly
go run doubly_linkedlist_basico.go
```

---

## 📊 Complexity Analysis | Análise de Complexidade

### 🇺🇸 English
| Operation | Basic Version | Optimized Version | Doubly Linked | Array (Comparison) |
|-----------|---------------|-------------------|---------------|-------------------|
| **Append** | O(n) | O(1) | O(1) | O(1) amortized |
| **Prepend** | O(1) | O(1) | O(1) | O(n) |
| **Delete** | O(n) | O(n) | O(n) | O(n) |
| **Search** | O(n) | O(n) | O(n) | O(n) |
| **Access by Index** | - | O(n) | O(n) | O(1) |

### 🇧🇷 Português
| Operação | Versão Básica | Versão Otimizada | Lista Dupla | Array (Comparação) |
|----------|---------------|-------------------|-------------|-------------------|
| **Append** | O(n) | O(1) | O(1) | O(1) amortizado |
| **Prepend** | O(1) | O(1) | O(1) | O(n) |
| **Delete** | O(n) | O(n) | O(n) | O(n) |
| **Search** | O(n) | O(n) | O(n) | O(n) |
| **Acesso por Índice** | - | O(n) | O(n) | O(1) |

---

## 🎯 Use Cases | Casos de Uso

### 🇺🇸 English
- **🔄 Undo/Redo Systems**: Implementing command history
- **📚 Music Playlists**: Dynamic song management
- **🧠 Memory Management**: Implementing custom allocators
- **📊 Stack Implementation**: LIFO data structure
- **🔗 Browser History**: Back/forward navigation

### 🇧🇷 Português
- **🔄 Sistemas de Desfazer/Refazer**: Implementação de histórico de comandos
- **📚 Playlists de Música**: Gerenciamento dinâmico de músicas
- **🧠 Gerenciamento de Memória**: Implementação de alocadores personalizados
- **📊 Implementação de Pilha**: Estrutura de dados LIFO
- **🔗 Histórico do Navegador**: Navegação voltar/avançar

---

## 💡 Implementation Details | Detalhes da Implementação

### 🇺🇸 English
#### Basic Node Structure
```go
type Node struct {
    data int
    next *Node
}

type LinkedList struct {
    head *Node
}
```

#### Optimized with Tail Pointer
```go
type OptimizedList struct {
    head *Node
    tail *Node
    size int
}
```

#### Doubly Linked Node
```go
type DoublyNode struct {
    data interface{}
    next *DoublyNode
    prev *DoublyNode
}
```

### 🇧🇷 Português
#### Estrutura Básica do Nó
```go
type Node struct {
    data int
    next *Node
}

type LinkedList struct {
    head *Node
}
```

#### Otimizada com Ponteiro Tail
```go
type OptimizedList struct {
    head *Node
    tail *Node
    size int
}
```

#### Nó Duplamente Ligado
```go
type DoublyNode struct {
    data interface{}
    next *DoublyNode
    prev *DoublyNode
}
```

---

## ⚡ Advantages vs Disadvantages | Vantagens vs Desvantagens

### 🇺🇸 English
#### ✅ Advantages
- **Dynamic Size**: No need to declare size beforehand
- **Efficient Insertion**: O(1) insertion at beginning
- **Memory Efficient**: Uses only required memory
- **No Memory Waste**: Allocates exactly what's needed

#### ❌ Disadvantages
- **Sequential Access**: No random access to elements
- **Memory Overhead**: Extra memory for pointers
- **Cache Locality**: Poor cache performance
- **Complex Implementation**: More complex than arrays

### 🇧🇷 Português
#### ✅ Vantagens
- **Tamanho Dinâmico**: Não precisa declarar tamanho antecipadamente
- **Inserção Eficiente**: Inserção O(1) no início
- **Eficiência de Memória**: Usa apenas a memória necessária
- **Sem Desperdício de Memória**: Aloca exatamente o que é necessário

#### ❌ Desvantagens
- **Acesso Sequencial**: Sem acesso aleatório aos elementos
- **Overhead de Memória**: Memória extra para ponteiros
- **Localidade de Cache**: Performance de cache ruim
- **Implementação Complexa**: Mais complexa que arrays

---

## 🔧 Advanced Features | Recursos Avançados

### 🇺🇸 English
- **Generic Type Support**: Works with any data type using interface{}
- **Tail Pointer Optimization**: O(1) append operations
- **Size Tracking**: Constant-time size queries
- **Error Handling**: Comprehensive error management
- **Memory Safety**: Prevents common pointer errors

### 🇧🇷 Português
- **Suporte a Tipos Genéricos**: Funciona com qualquer tipo de dado usando interface{}
- **Otimização com Ponteiro Tail**: Operações de append O(1)
- **Rastreamento de Tamanho**: Consultas de tamanho em tempo constante
- **Tratamento de Erros**: Gerenciamento abrangente de erros
- **Segurança de Memória**: Previne erros comuns de ponteiros

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
