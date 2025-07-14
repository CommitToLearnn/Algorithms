<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=6C5CE7&height=120&section=header&text=Inverted%20Index&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Estrutura%20Fundamental%20para%20Motores%20de%20Busca&descAlignY=65&descSize=16">

</div>

# Índice Invertido com Hash

## Descrição

O Índice Invertido é uma estrutura de dados fundamental para sistemas de busca que mapeia cada termo único para uma lista de documentos que o contêm. Combinado com hash tables, oferece busca eficiente em grandes coleções de texto, sendo a base de mecanismos de busca como Google, Elasticsearch e Solr.

## Como Funciona

1. **Tokenização**: Documentos são divididos em termos (palavras)
2. **Indexação**: Cada termo aponta para lista de documentos que o contêm
3. **Hash de Documentos**: IDs únicos gerados via hash MD5
4. **Scoring TF-IDF**: Relevância calculada por frequência e raridade
5. **Busca**: Interseção/união de listas de documentos

## Estrutura de Dados

```
Termo -> Conjunto de Document IDs
"python" -> {doc1, doc3, doc5}
"machine" -> {doc2, doc3}
"learning" -> {doc2, doc3, doc4}
```

## Tipos de Busca Suportados

### 1. Busca Ranqueada (TF-IDF)
Ordena resultados por relevância usando Term Frequency × Inverse Document Frequency

### 2. Busca Booleana AND
Retorna documentos que contêm TODOS os termos da consulta

### 3. Busca Booleana OR
Retorna documentos que contêm QUALQUER termo da consulta

## Complexidade

| Operação | Complexidade | Observações |
|----------|--------------|-------------|
| Indexação | O(n×m) | n=docs, m=termos médios por doc |
| Busca TF-IDF | O(k×log(r)) | k=termos query, r=resultados |
| Busca AND | O(k×min(listas)) | Interseção de listas |
| Busca OR | O(k×sum(listas)) | União de listas |

## Implementação Disponível

### Python (`inverted_index_basico.py`)
```python
# Exemplo de uso
from inverted_index_basico import InvertedIndex

# Cria índice
idx = InvertedIndex()

# Adiciona documentos
doc_id = idx.add_document("Python é uma linguagem de programação")
print(f"Documento adicionado: {doc_id}")

# Busca documentos
results = idx.search("Python programação")
print(f"Resultados: {results}")

# Busca booleana
and_results = idx.search_boolean_and("Python programação")
or_results = idx.search_boolean_or("Python programação")
```

## Componentes Principais

### InvertedIndex
- **index**: Dicionário termo → conjunto de doc_ids
- **documents**: Armazena conteúdo original dos documentos
- **term_freq**: Frequência de termos por documento
- **doc_lengths**: Número de termos por documento

### Algoritmo TF-IDF
```
TF(t,d) = freq(t,d) / total_terms(d)
IDF(t) = log(total_docs / docs_containing(t))
Score(t,d) = TF(t,d) × IDF(t)
```

### Hash de Documentos
```python
def _hash_document_id(self, content):
    hash_obj = hashlib.md5(content.encode('utf-8'))
    return hash_obj.hexdigest()[:12]
```

## Características

### Vantagens
- **Busca Rápida**: O(1) para encontrar lista de documentos por termo
- **Flexível**: Suporta diferentes tipos de consulta
- **Escalável**: Eficiente para milhões de documentos
- **Ranqueamento**: Resultados ordenados por relevância

### Limitações
- **Uso de Memória**: Armazena todos os termos em memória
- **Atualização Custosa**: Reindexação pode ser lenta
- **Sinônimos**: Não trata sinônimos automaticamente
- **Ordem**: Não considera ordem das palavras

## Casos de Uso

1. **Mecanismos de Busca**: Google, Bing, Yahoo
2. **Busca Empresarial**: Elasticsearch, Solr, Lucene
3. **E-commerce**: Busca de produtos
4. **Bibliotecas Digitais**: Busca em documentos e livros
5. **Redes Sociais**: Busca em posts e comentários
6. **Bases de Conhecimento**: Wikis e documentação

## Otimizações Possíveis

### 1. Compressão de Listas
```python
# Usar delta encoding para listas de IDs
# [1, 5, 8, 12] -> [1, 4, 3, 4]
```

### 2. Skip Lists
```python
# Acelerar interseções de listas grandes
# Pular blocos de IDs durante busca AND
```

### 3. Caching
```python
# Cache de consultas frequentes
# LRU cache para resultados recentes
```

### 4. Paralelização
```python
# Processar múltiplos termos em paralelo
# Usar threading para consultas complexas
```

## Métricas de Performance

| Métrica | Fórmula | Uso |
|---------|---------|-----|
| Precisão | TP/(TP+FP) | Qualidade dos resultados |
| Recall | TP/(TP+FN) | Cobertura da busca |
| F1-Score | 2×(P×R)/(P+R) | Métrica combinada |
| MAP | Média de Average Precision | Qualidade do ranking |

## Estrutura de Arquivos

```
python/inverted_index/
├── inverted_index_basico.py    # Implementação principal
├── README.md                   # Esta documentação
└── requirements.txt            # Dependências (se houver)
```

## Exemplo Completo

```python
# Criar e popular índice
idx = InvertedIndex()

documents = [
    "Python é uma linguagem de programação versátil",
    "Machine learning com Python é muito popular",
    "Algoritmos de busca são fundamentais",
    "Estruturas de dados eficientes para busca"
]

# Indexar documentos
for i, doc in enumerate(documents):
    idx.add_document(doc, f"doc_{i+1}")

# Buscar e mostrar resultados
query = "Python busca"
results = idx.search(query)

print(f"Query: '{query}'")
for doc_id in results:
    content = idx.get_document(doc_id)
    print(f"[{doc_id}] {content}")
```

## Estatísticas do Índice

```python
stats = idx.get_stats()
print(f"Documentos: {stats['total_documents']}")
print(f"Termos únicos: {stats['total_unique_terms']}")
print(f"Memória estimada: {stats['index_size_bytes']} bytes")
```

## Executar Exemplo

```bash
cd python/inverted_index
python inverted_index_basico.py
```

## Extensões Avançadas

### 1. Índice de N-gramas
Suporte para frases e proximidade

### 2. Índice de Sinônimos
Expansão de consultas com sinônimos

### 3. Índice Fuzzy
Busca com tolerância a erros ortográficos

### 4. Índice Temporal
Suporte para dados com timestamp

## Referências

- [Introduction to Information Retrieval - Manning](https://nlp.stanford.edu/IR-book/)
- [Modern Information Retrieval - Baeza-Yates](https://www.mir2ed.org/)
- [Lucene in Action - Gospodnetic](https://www.manning.com/books/lucene-in-action-second-edition)
- [Elasticsearch Guide](https://www.elastic.co/guide/)

---

<div align="center">

## 👤 Autor | Author

<div align="center">
  <a href="https://github.com/matheussricardoo" target="_blank">
    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/matheus-ricardo-426452266/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn"/>
  </a>
</div>

## 📄 Licença | License

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../../LICENSE) para mais detalhes.

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

---

<div align="center">
  <i>🔍 "A informação não é conhecimento, conhecimento não é sabedoria" - T.S. Eliot</i>
  <br>
  <i>🔍 "Information is not knowledge, knowledge is not wisdom" - T.S. Eliot</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=6C5CE7&height=120&section=footer"/>

</div>
