![Header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Hash%20Table%20em%20Python&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=25&desc=Estrutura%20de%20dados%20para%20acesso%20rápido%20O(1)&descAlignY=51&descAlign=50)

<div align="center">

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](https://python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Hash_Table-FF6B6B?style=for-the-badge&logo=algorithm)](https://github.com/matheussricardoo/Algorithms)
[![Data Structure](https://img.shields.io/badge/Data_Structure-Dictionary-4ECDC4?style=for-the-badge&logo=data-structure)](https://github.com/matheussricardoo/Algorithms)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

</div>

---

## 🌟 Features | Características

| English | Português |
|---------|-----------|
| **Key-Value Mapping** | **Mapeamento Chave-Valor** |
| Efficient associative data structure | Estrutura de dados associativa eficiente |
| **Collision Resolution** | **Resolução de Colisões** |
| Multiple strategies for handling collisions | Múltiplas estratégias para lidar com colisões |
| **Dynamic Resizing** | **Redimensionamento Dinâmico** |
| Automatic table expansion/contraction | Expansão/contração automática da tabela |
| **Hash Functions** | **Funções Hash** |
| Various hash function implementations | Várias implementações de funções hash |

## 🛠️ Technologies | Tecnologias

<div align="center">

![Python](https://skillicons.dev/icons?i=python&theme=dark)

</div>

## 📁 Estrutura dos Arquivos

```
hashtable/
├── hashtable_basico.py          # Implementação didática básica
├── otimizado/
│   └── hashtable_otimizado.py   # Implementação otimizada avançada
└── README.md                    # Este arquivo
```

## 🎯 Versões Disponíveis

### 1. Versão Básica (`hashtable_basico.py`)
- **Propósito**: Aprendizado e compreensão dos conceitos
- **Características**:
  - Implementação simples com chaining
  - Função hash básica (método da divisão)
  - Código didático com comentários explicativos
  - Ideal para entender os conceitos fundamentais

### 2. Versão Otimizada (`otimizado/hashtable_otimizado.py`)
- **Propósito**: Uso em aplicações reais e estudos avançados
- **Características**:
  - Múltiplas funções de hash (divisão, multiplicação, djb2, FNV-1a)
  - Várias estratégias de resolução de colisões
  - Redimensionamento dinâmico (rehashing)
  - Estatísticas detalhadas de performance
  - Otimizações para melhor performance

## 🚀 Quick Start | Início Rápido

```bash
# Clone the repository | Clone o repositório
git clone https://github.com/matheussricardoo/Algorithms.git
cd algorithms/python/hashtable

# Run basic version | Execute versão básica
python hashtable_basico.py

# Run optimized version | Execute versão otimizada
python otimizado/hashtable_otimizado.py
```

## 📊 Exemplos de Uso

### Exemplo Básico
```python
from hashtable_basico import HashTable

# Cria uma hash table
ht = HashTable()

# Insere dados
ht.inserir("nome", "João")
ht.inserir("idade", 25)
ht.inserir("cidade", "São Paulo")

# Busca dados
nome = ht.buscar("nome")
print(f"Nome: {nome}")

# Remove dados
ht.remover("idade")
```

### Exemplo Otimizado
```python
from otimizado.hashtable_otimizado import HashTableOtimizada, TipoHash, TipoColisao

# Cria uma hash table otimizada
ht = HashTableOtimizada(
    capacidade_inicial=16,
    tipo_hash=TipoHash.DJIB2,
    tipo_colisao=TipoColisao.CHAINING
)

# Insere muitos dados
for i in range(1000):
    ht.inserir(f"key_{i}", f"value_{i}")

# Obtém estatísticas
stats = ht.obter_estatisticas()
print(f"Fator de carga: {stats['fator_carga']}")
print(f"Colisões: {stats['colisoes_total']}")
```

## 🔍 Conceitos Importantes

### Função Hash
Mapeia chaves para índices da tabela:
```
hash(chave) → índice
```

### Colisões
Quando duas chaves diferentes mapeiam para o mesmo índice.

### Estratégias de Resolução de Colisões

#### 1. **Chaining (Encadeamento)**
- Cada posição mantém uma lista de elementos
- Simples de implementar
- Permite fator de carga > 1

#### 2. **Open Addressing (Endereçamento Aberto)**
- **Linear Probing**: busca a próxima posição livre
- **Quadratic Probing**: busca usando saltos quadráticos
- **Double Hashing**: usa segunda função hash

### Fator de Carga
```
λ = número_de_elementos / capacidade_da_tabela
```

## 🔧 Funções Hash Implementadas

### 1. **Divisão** (método clássico)
```python
hash(chave) % capacidade
```

### 2. **Multiplicação** (método de Knuth)
```python
capacidade * ((hash(chave) * A) % 1)
# onde A = (√5 - 1) / 2 ≈ 0.618
```

### 3. **djb2** (Daniel J. Bernstein)
```python
hash = 5381
for char in chave:
    hash = ((hash << 5) + hash) + ord(char)
```

### 4. **FNV-1a** (Fowler-Noll-Vo)
```python
hash = FNV_OFFSET_BASIS
for char in chave:
    hash ^= ord(char)
    hash *= FNV_PRIME
```

## 📈 Complexidade de Tempo

| Operação | Melhor Caso | Caso Médio | Pior Caso |
|----------|-------------|------------|-----------|
| Inserção | O(1) | O(1) | O(n) |
| Busca | O(1) | O(1) | O(n) |
| Remoção | O(1) | O(1) | O(n) |

*Nota: O pior caso ocorre quando todas as chaves colidem.*

## 🎓 Aplicações Práticas

### 1. **Dicionários/Maps**
- Implementação de `dict` em Python
- `HashMap` em Java, `unordered_map` em C++

### 2. **Caches**
- Cache de páginas web
- Cache de resultados de funções (memoização)

### 3. **Bancos de Dados**
- Índices hash para busca rápida
- Particionamento de dados

### 4. **Compiladores**
- Tabela de símbolos
- Palavras-chave da linguagem

### 5. **Criptografia**
- Verificação de integridade
- Assinaturas digitais

## 🛠️ Características da Versão Otimizada

### Redimensionamento Dinâmico
```python
if fator_carga >= fator_carga_max:
    redimensionar()  # Dobra a capacidade
```

### Múltiplas Estratégias
- **Chaining**: Melhor para alta taxa de colisões
- **Linear Probing**: Melhor cache locality
- **Quadratic Probing**: Reduz clustering
- **Double Hashing**: Distribuição mais uniforme

### Estatísticas de Performance
- Número de colisões
- Fator de carga atual
- Média de probes por busca
- Número de redimensionamentos

## 🔍 Comparação de Estratégias

### Chaining
- ✅ Simples de implementar
- ✅ Permite fator de carga > 1
- ✅ Não há clustering
- ❌ Overhead de ponteiros
- ❌ Pior cache locality

### Open Addressing
- ✅ Melhor uso de memória
- ✅ Melhor cache locality
- ❌ Limitado por fator de carga
- ❌ Pode sofrer clustering
- ❌ Remoção complexa (lazy deletion)

## 📊 Analysis | Análise

### Time Complexity | Complexidade de Tempo
- **Average Case | Caso Médio**: O(1) para insert, search, delete
- **Worst Case | Pior Caso**: O(n) quando todas as chaves colidem

### Space Complexity | Complexidade de Espaço
- **Space Usage | Uso de Espaço**: O(n) onde n é o número de elementos

### Load Factor | Fator de Carga
- **Optimal Range | Faixa Ótima**: 0.7 - 0.8 para open addressing
- **Chaining | Encadeamento**: Pode exceder 1.0

## 🎯 Use Cases | Casos de Uso

| Application | Aplicação | Description | Descrição |
|-------------|-----------|-------------|-----------|
| **Dictionaries** | **Dicionários** | Python dict implementation | Implementação do dict do Python |
| **Database Indexing** | **Indexação BD** | Fast record retrieval | Recuperação rápida de registros |
| **Caching** | **Cache** | Memoization and web caches | Memoização e cache web |
| **Symbol Tables** | **Tabelas de Símbolos** | Compiler implementations | Implementações de compiladores |

## 🔧 Implementation Strategies | Estratégias de Implementação

### Collision Resolution | Resolução de Colisões

| Method | Método | Pros | Prós | Cons | Contras |
|--------|--------|------|------|------|---------|
| **Chaining** | **Encadeamento** | Simple, handles high load | Simples, lida com alta carga | Memory overhead | Overhead de memória |
| **Linear Probing** | **Sondagem Linear** | Good cache locality | Boa localidade de cache | Primary clustering | Clustering primário |
| **Quadratic Probing** | **Sondagem Quadrática** | Reduces clustering | Reduz clustering | Secondary clustering | Clustering secundário |
| **Double Hashing** | **Hash Duplo** | Uniform distribution | Distribuição uniforme | Complex implementation | Implementação complexa |

### Hash Functions | Funções Hash

```python
# Division Method | Método da Divisão
def hash_division(key, size):
    return hash(key) % size

# Multiplication Method | Método da Multiplicação
def hash_multiplication(key, size):
    A = 0.6180339887  # (√5 - 1) / 2
    return int(size * ((key * A) % 1))

# DJB2 Hash
def hash_djb2(key):
    hash_value = 5381
    for char in str(key):
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value
```

---

<div align="center">

### 📝 Notes | Observações

**English**: Hash tables are fundamental to many Python built-in types like `dict` and `set`. Understanding their implementation helps optimize code performance.

**Português**: Hash tables são fundamentais para muitos tipos built-in do Python como `dict` e `set`. Entender sua implementação ajuda a otimizar a performance do código.

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

This project is licensed under the MIT License. See the [LICENSE](../../../LICENSE) file for details.

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../../../LICENSE) para mais detalhes.

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=000000&height=120&section=footer"/>
