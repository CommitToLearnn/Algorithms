![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Hash%20Table%20em%20Java&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Estrutura%20de%20dados%20para%20acesso%20rápido%20O(1)&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=java)](https://java.com/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Hash_Table-FF6B6B?style=for-the-badge&logo=algorithm)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Dictionary-4ECDC4?style=for-the-badge&logo=data-structure)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

</div>

---

## 🌟 Features | Características

### 🇺🇸 English
- **Object-Oriented Design**: Clean Java implementation with proper encapsulation
- **Automatic Resizing**: Dynamic table expansion based on load factor
- **Collision Handling**: Efficient chaining method for collision resolution
- **Performance Metrics**: Built-in performance monitoring and analysis

### 🇧🇷 Português
- **Design Orientado a Objetos**: Implementação Java limpa com encapsulamento adequado
- **Redimensionamento Automático**: Expansão dinâmica da tabela baseada no fator de carga
- **Tratamento de Colisões**: Método de encadeamento eficiente para resolução de colisões
- **Métricas de Performance**: Monitoramento e análise de performance integrados

<div align="center">

| Feature | Description | Descrição |
|:---:|:---|:---|
| 🎯 | Educational Implementation | Implementação Educacional - Conceitos básicos |
| 🚀 | Auto-Resizing | Redimensionamento Automático - Fator de carga inteligente |
| 📊 | Collision Statistics | Estatísticas de Colisões - Métricas detalhadas |
| 🔄 | Chaining Resolution | Resolução por Encadeamento - Listas ligadas |
| 📈 | Performance Tracking | Rastreamento de Performance - Operações/segundo |
| 🧬 | Generic Support | Suporte Genérico - Type-safe para qualquer tipo |
| ⚡ | Optimized Hashing | Hash Otimizado - Distribuição uniforme |
| 🔍 | Load Factor Control | Controle de Fator de Carga - 0.25 - 0.75 |

</div>

### 🛠️ Technologies | Tecnologias

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=java&theme=dark" />
  </a>
</div>

## Estrutura dos Arquivos

- `HashTableBasico.java` - Implementação básica e didática
- `otimizado/` - Versão otimizada com melhorias de performance
  - `HashTableOtimizada.java` - Classe principal da hash table otimizada
  - `EstatisticasPerformance.java` - Métricas de performance
  - `ExemploHashTableOtimizada.java` - Exemplos de uso

## Sobre a Hash Table

Uma Hash Table é uma estrutura de dados que implementa um array associativo, permitindo mapeamento de chaves para valores com acesso rápido.

### Complexidade
- **Inserção**: O(1) médio, O(n) pior caso
- **Busca**: O(1) médio, O(n) pior caso
- **Remoção**: O(1) médio, O(n) pior caso
- **Espaço**: O(n)

## Como Compilar e Executar

### Versão Básica
```bash
# Compilar
javac HashTableBasico.java

# Executar
java HashTableBasico
```

### Versão Otimizada
```bash
# Navegar para o diretório java
cd java

# Compilar todas as classes
javac hashtable/otimizado/*.java

# Executar exemplo
java hashtable.otimizado.ExemploHashTableOtimizada
```

## Principais Melhorias na Versão Otimizada

1. **Função Hash Melhorada**: Usa bit manipulation para melhor distribuição
2. **Redimensionamento Automático**: Ajusta capacidade baseado no fator de carga
3. **Resolução de Colisões Otimizada**: Chaining com linked lists eficientes
4. **Estatísticas Detalhadas**: Coleta métricas de performance e colisões
5. **Generics**: Suporte completo a tipos genéricos
6. **Fator de Carga Inteligente**: Mantém performance através de redimensionamento

## Exemplos de Uso

### Uso Básico
```java
// Criar hash table
HashTableOtimizada<String, Integer> tabela = new HashTableOtimizada<>();

// Inserir elementos
tabela.put("apple", 10);
tabela.put("banana", 20);

// Buscar elementos
Integer valor = tabela.get("apple"); // retorna 10

// Remover elementos
Integer removido = tabela.remove("banana"); // retorna 20

// Verificar existência
boolean existe = tabela.containsKey("apple"); // true
```

### Análise de Performance
```java
// Obter estatísticas
EstatisticasPerformance stats = tabela.getEstatisticas();
System.out.println(stats.relatorioDetalhado());

// Verificar fator de carga
double fatorCarga = tabela.getFatorCarga();
System.out.printf("Fator de carga: %.2f\n", fatorCarga);
```

### Iteração sobre Elementos
```java
// Obter todas as chaves
List<String> chaves = tabela.getChaves();

// Obter todas as entradas
List<HashTableOtimizada.EntradaPublica<String, Integer>> entradas = tabela.getEntradas();
for (var entrada : entradas) {
    System.out.println(entrada.getChave() + " = " + entrada.getValor());
}
```

## Características Técnicas

### Redimensionamento
- **Fator de carga máximo**: 0.75 (redimensiona para cima)
- **Fator de carga mínimo**: 0.25 (redimensiona para baixo)
- **Capacidade inicial**: 16
- **Estratégia**: Dobra ou reduz pela metade

### Resolução de Colisões
- **Método**: Separate Chaining (Listas Ligadas)
- **Vantagens**: Simples, suporte a qualquer fator de carga
- **Performance**: O(1) médio, O(n) pior caso para busca/inserção/remoção

## Casos de Uso

### 🚀 Getting Started | Começando

```bash
# Basic Version | Versão Básica
javac HashTableBasico.java && java HashTableBasico

# Optimized Version | Versão Otimizada
cd java
javac hashtable/otimizado/*.java
java hashtable.otimizado.ExemploHashTableOtimizada
```

### 📊 Complexity Analysis | Análise de Complexidade

<div align="center">

| Operation | Average | Worst Case | Description |
|:---:|:---:|:---:|:---|
| **Insert** | O(1) | O(n) | Insertion with collision handling |
| **Search** | O(1) | O(n) | Hash-based lookup |
| **Delete** | O(1) | O(n) | Removal with chain traversal |
| **Space** | O(n) | O(n) | Storage for n elements |

</div>

### 🎯 Use Cases | Casos de Uso

<div align="center">

| Application | Description | Descrição |
|:---:|:---|:---|
| 🗄️ | **Caches** | Armazenamento temporário de dados |
| 🔍 | **Database Indexes** | Índices de Banco de Dados |
| 📚 | **Dictionaries** | Mapeamento palavra-definição |
| 📊 | **Frequency Counters** | Contadores de frequência |
| 💾 | **Memoization** | Cache de resultados de funções |
| ⚙️ | **Configuration Systems** | Sistemas de configuração |

</div>

### ⚡ Technical Features | Características Técnicas

```java
// Load Factor Control | Controle de Fator de Carga
- Maximum: 0.75 (resize up)
- Minimum: 0.25 (resize down)  
- Initial capacity: 16

// Collision Resolution | Resolução de Colisões
- Method: Separate Chaining
- Performance: O(1) average, O(n) worst case
```

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
