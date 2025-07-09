![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Linked%20List%20em%20Java&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Estrutura%20de%20dados%20linear%20dinâmica&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=java)](https://java.com/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Linked_List-FF6B6B?style=for-the-badge&logo=algorithm)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Linear-4ECDC4?style=for-the-badge&logo=data-structure)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Object-Oriented Design**: Clean Java implementation with proper encapsulation
- **Dynamic Allocation**: Memory efficient with node-based structure
- **Iterator Support**: Built-in iterator for easy traversal
- **Flexible Operations**: Efficient insertion and deletion at any position

### 🇧🇷 Português
- **Design Orientado a Objetos**: Implementação Java limpa com encapsulamento adequado
- **Alocação Dinâmica**: Eficiente em memória com estrutura baseada em nós
- **Suporte a Iteradores**: Iterador integrado para travessia fácil
- **Operações Flexíveis**: Inserção e remoção eficientes em qualquer posição

<div align="center">

| Feature | Description | Descrição |
|:---:|:---|:---|
| 🎯 | Educational Implementation | Implementação Educacional - Conceitos fundamentais |
| 🚀 | Tail Pointer Optimization | Otimização com Tail Pointer - O(1) inserção final |
| 📊 | Performance Statistics | Estatísticas de Performance - Métricas por operação |
| 🔄 | Iterator Pattern | Padrão Iterator - Suporte completo ao Java Iterator |
| 📈 | Position-Based Operations | Operações por Posição - Início, meio, fim |
| 🧬 | Generic Support | Suporte Genérico - Type-safe para qualquer tipo |
| ⚡ | Optimized Methods | Métodos Otimizados - Diferentes estratégias por posição |
| 🔍 | Iterable Interface | Interface Iterable - For-each loop support |

</div>

### 🛠️ Technologies | Tecnologias

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=java&theme=dark" />
  </a>
</div>

## Estrutura dos Arquivos

- `LinkedListBasico.java` - Implementação básica e didática
- `otimizado/` - Versão otimizada com melhorias de performance
  - `LinkedListOtimizada.java` - Classe principal da lista ligada otimizada
  - `EstatisticasPerformance.java` - Métricas de performance
  - `ExemploLinkedListOtimizada.java` - Exemplos de uso

## Sobre a Lista Ligada

Uma Lista Ligada é uma estrutura de dados linear onde os elementos são armazenados em nós, e cada nó contém dados e uma referência (ponteiro) para o próximo nó.

### Complexidade
- **Inserção no início**: O(1)
- **Inserção no final**: O(1) na versão otimizada, O(n) na básica
- **Inserção no meio**: O(n)
- **Remoção no início**: O(1)
- **Remoção no final**: O(n)
- **Remoção no meio**: O(n)
- **Busca**: O(n)
- **Espaço**: O(n)

## Como Compilar e Executar

### Versão Básica
```bash
# Compilar
javac LinkedListBasico.java

# Executar
java LinkedListBasico
```

### Versão Otimizada
```bash
# Navegar para o diretório java
cd java

# Compilar todas as classes
javac linkedlist/otimizado/*.java

# Executar exemplo
java linkedlist.otimizado.ExemploLinkedListOtimizada
```

## Principais Melhorias na Versão Otimizada

1. **Referência para o Tail**: Mantém ponteiro para o último nó, permitindo inserção O(1) no final
2. **Implementação de Iterator**: Suporte completo ao padrão Iterator do Java
3. **Interface Iterable**: Permite uso com for-each loops
4. **Estatísticas Detalhadas**: Coleta métricas de performance por tipo de operação
5. **Métodos Otimizados**: Implementações específicas para diferentes posições (início, meio, fim)
6. **Generics**: Suporte completo a tipos genéricos
7. **Tratamento de Exceções**: Validação adequada de índices e estados

## Exemplos de Uso

### Operações Básicas
```java
// Criar lista
LinkedListOtimizada<String> lista = new LinkedListOtimizada<>();

// Inserir elementos
lista.adicionarInicio("A");        // [A]
lista.adicionarFinal("C");         // [A, C]
lista.adicionarPosicao(1, "B");    // [A, B, C]

// Buscar elementos
boolean contem = lista.contem("B");     // true
int indice = lista.indiceDe("B");       // 1
String elemento = lista.obter(1);       // "B"

// Remover elementos
String removido = lista.removerInicio();      // "A"
lista.remover("B");                           // remove "B"
String ultimo = lista.removerFinal();         // "C"
```

### Iteração
```java
// Usando for-each (requer Iterable)
for (String elemento : lista) {
    System.out.println(elemento);
}

// Usando Iterator
Iterator<String> iterator = lista.iterator();
while (iterator.hasNext()) {
    String elemento = iterator.next();
    System.out.println(elemento);
}

// Convertendo para array
String[] array = lista.paraArray();
```

### Análise de Performance
```java
// Obter estatísticas
EstatisticasPerformance stats = lista.getEstatisticas();
System.out.println(stats.relatorioDetalhado());

// Verificar contadores específicos
int operacoesInsercao = stats.getContadorOperacao("adicionarInicio");
double tempoMedio = stats.getTempoMedioOperacao("adicionarInicio");
```

### Métodos de Acesso Rápido
```java
// Acesso O(1) aos extremos
String primeiro = lista.obterPrimeiro();
String ultimo = lista.obterUltimo();

// Verificações O(1)
boolean vazia = lista.estaVazia();
int tamanho = lista.tamanho();
```

## Vantagens da Lista Ligada

- **Tamanho Dinâmico**: Cresce e diminui conforme necessário
- **Inserção Eficiente**: O(1) no início e fim (versão otimizada)
- **Uso de Memória**: Aloca apenas o necessário
- **Flexibilidade**: Fácil inserção/remoção em qualquer posição

## Desvantagens

- **Acesso Sequencial**: Não há acesso direto por índice
- **Overhead de Memória**: Cada nó precisa armazenar ponteiro
- **Cache Miss**: Elementos não são contíguos na memória
- **Complexidade de Busca**: Sempre O(n) para localizar elementos

## Casos de Uso Ideais

- **Pilhas e Filas**: Implementação de estruturas LIFO/FIFO
- **Listas de Reprodução**: Onde inserção/remoção são frequentes
- **Histórico de Navegação**: Fácil adicionar/remover páginas
- **Desfazer/Refazer**: Sistemas que precisam manter histórico de ações
- **Processamento de Dados**: Quando o tamanho da lista é desconhecido

### 🚀 Getting Started | Começando

```bash
# Basic Version | Versão Básica
javac LinkedListBasico.java && java LinkedListBasico

# Optimized Version | Versão Otimizada
cd java
javac linkedlist/otimizado/*.java
java linkedlist.otimizado.ExemploLinkedListOtimizada
```

### 📊 Complexity Analysis | Análise de Complexidade

<div align="center">

| Operation | Operação | LinkedList | ArrayList | Description | Descrição |
|:---:|:---:|:---:|:---:|:---|:---|
| **Index Access** | **Acesso por Índice** | O(n) | O(1) | Access by index | Acesso por índice |
| **Insert Begin** | **Inserir Início** | O(1) | O(n) | Insert at beginning | Inserção no início |
| **Insert End** | **Inserir Final** | O(1) | O(1) | Insert at end | Inserção no final |
| **Insert Middle** | **Inserir Meio** | O(n) | O(n) | Insert in middle | Inserção no meio |
| **Remove Begin** | **Remover Início** | O(1) | O(n) | Remove from beginning | Remoção no início |
| **Search** | **Buscar** | O(n) | O(n) | Search element | Busca por elemento |

</div>

### ✅ Advantages vs ❌ Disadvantages | Vantagens vs Desvantagens

<div align="center">

| ✅ Advantages | ✅ Vantagens | ❌ Disadvantages | ❌ Desvantagens |
|:---|:---|:---|:---|
| Dynamic size | Tamanho dinâmico | Sequential access only | Apenas acesso sequencial |
| Efficient insertion O(1) | Inserção eficiente O(1) | Memory overhead per node | Overhead de memória por nó |
| Memory as needed | Memória conforme necessário | Cache miss issues | Problemas de cache miss |
| Flexible positioning | Posicionamento flexível | Always O(n) search | Busca sempre O(n) |

</div>

### 🎯 Ideal Use Cases | Casos de Uso Ideais

<div align="center">

| Application | Aplicação | Description | Descrição |
|:---:|:---:|:---|:---|
| 📚 | Stacks & Queues | **Pilhas e Filas** | LIFO/FIFO structures |
| 🎵 | Playlists | **Listas de Reprodução** | Frequent insertion/removal |
| 🌐 | Browser History | **Histórico de Navegação** | Easy add/remove |
| ↩️ | Undo/Redo Systems | **Sistemas Desfazer/Refazer** | Action history |
| 🔄 | Data Processing | **Processamento de Dados** | Unknown size |

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
