<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=4A90E2&height=120&section=header&text=Naive%20Bayes&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Classificador%20Probabilístico%20para%20Machine%20Learning&descAlignY=65&descSize=16">

</div>

# Classificador Naive Bayes

## Descrição

Naive Bayes é um algoritmo de classificação probabilística baseado no Teorema de Bayes com a suposição "naive" (ingênua) de independência condicional entre as features. Apesar da simplicidade, é muito eficaz para muitas aplicações reais, especialmente classificação de texto.

## Como Funciona

O algoritmo calcula a probabilidade posterior de cada classe dada as features observadas:

```
P(classe|features) = P(features|classe) × P(classe) / P(features)
```

### Suposição de Independência
```
P(x₁,x₂,...,xₙ|classe) = P(x₁|classe) × P(x₂|classe) × ... × P(xₙ|classe)
```

## Teorema de Bayes

### Fórmula Base
```
P(A|B) = P(B|A) × P(A) / P(B)
```

### Para Classificação
```
P(Cᵢ|X) = P(X|Cᵢ) × P(Cᵢ) / P(X)
```

Onde:
- **P(Cᵢ|X)**: Probabilidade posterior da classe i
- **P(X|Cᵢ)**: Likelihood (verossimilhança)
- **P(Cᵢ)**: Probabilidade a priori da classe i
- **P(X)**: Evidência (normalizador)

## Tipos Implementados

### 1. Gaussian Naive Bayes
Para features contínuas (numéricas):
```python
P(xᵢ|classe) = (1/√(2πσ²)) × exp(-(xᵢ-μ)²/(2σ²))
```

### 2. Multinomial Naive Bayes  
Para features categóricas:
```python
P(xᵢ|classe) = (count(xᵢ, classe) + α) / (count(classe) + α×V)
```
Onde α = 1 (Suavização de Laplace)

## Complexidade

| Operação | Complexidade | Observações |
|----------|--------------|-------------|
| **Treinamento** | O(n×d) | n=amostras, d=features |
| **Predição** | O(c×d) | c=classes, d=features |
| **Memória** | O(c×d) | Armazena estatísticas |

## Implementação Disponível

### Python (`naive_bayes_basico.py`)
```python
# Exemplo de uso
from naive_bayes_basico import NaiveBayesClassifier

# Criar classificador
nb = NaiveBayesClassifier()

# Dados de treino
X_train = [[5.1, 3.5, 1.4, 0.2], [6.7, 3.1, 4.4, 1.4]]
y_train = ['setosa', 'versicolor']

# Treinar modelo
nb.fit(X_train, y_train)

# Fazer predição
sample = [5.0, 3.0, 1.5, 0.3]
predicted_class, confidence = nb.predict(sample)

print(f"Classe: {predicted_class}")
print(f"Confiança: {confidence:.3f}")
```

## Características da Implementação

### Detecção Automática de Tipos
```python
def _determine_feature_type(self, values):
    # Detecta se feature é categórica ou contínua
    unique_ratio = len(set(values)) / len(values)
    return 'continuous' if unique_ratio > 0.5 else 'categorical'
```

### Suavização de Laplace
```python
# Evita probabilidade zero para features não vistas
likelihood = (count + 1) / (total_count + num_unique_values)
```

### Cálculo em Log-Space
```python
# Evita underflow numérico
log_prob = log(prior) + sum(log(likelihood_i) for i in features)
```

## Vantagens

### ✅ Pontos Fortes
- **Simplicidade**: Fácil de implementar e entender
- **Rapidez**: Treinamento e predição muito rápidos
- **Poucos Dados**: Funciona bem com datasets pequenos
- **Multiclasse**: Naturalmente suporta múltiplas classes
- **Features Mistas**: Lida com categóricas e numéricas
- **Baseline**: Excelente como modelo de referência

### ❌ Limitações
- **Independência**: Assume independência entre features
- **Dados Contínuos**: Assume distribuição Gaussiana
- **Features Correlacionadas**: Performance degrada
- **Desbalanceamento**: Sensível a classes desbalanceadas

## Casos de Uso

### 1. Classificação de Texto
```python
# Análise de sentimento
documents = [
    (["bom", "excelente", "ótimo"], "positivo"),
    (["ruim", "terrível", "péssimo"], "negativo")
]
```

### 2. Filtragem de Spam
```python
# Classificação de emails
features = ["viagra", "gratis", "dinheiro", "urgente"]
labels = ["spam", "ham"]
```

### 3. Diagnóstico Médico
```python
# Baseado em sintomas
symptoms = ["febre", "tosse", "dor_cabeca"]
diagnosis = ["gripe", "covid", "resfriado"]
```

### 4. Categorização de Notícias
```python
# Classificação por tópico
topics = ["esportes", "politica", "tecnologia", "economia"]
```

## Métricas de Avaliação

### Classificação Binária
```python
# Precisão, Recall, F1-Score
precision = TP / (TP + FP)
recall = TP / (TP + FN)  
f1_score = 2 * (precision * recall) / (precision + recall)
```

### Classificação Multiclasse
```python
# Acurácia macro e micro
macro_avg = mean([metric_per_class])
micro_avg = metric_across_all_samples
```

### Matriz de Confusão
```
          Predito
Verdadeiro   A    B    C
    A       50    2    1
    B        3   45    2  
    C        1    1   48
```

## Exemplo Completo

### Dataset Iris (Numérico)
```python
# Features contínuas - usa Gaussian NB
X_iris = [
    [5.1, 3.5, 1.4, 0.2],  # sepal_length, sepal_width, petal_length, petal_width
    [6.7, 3.1, 4.4, 1.4],
    [6.3, 3.3, 6.0, 2.5]
]
y_iris = ['setosa', 'versicolor', 'virginica']

nb_iris = NaiveBayesClassifier()
nb_iris.fit(X_iris, y_iris)

# Predição
sample = [5.0, 3.0, 1.5, 0.3]
result = nb_iris.predict(sample)
print(f"Espécie: {result[0]} (confiança: {result[1]:.3f})")
```

### Dataset Texto (Categórico)
```python
# Features categóricas - usa Multinomial NB
X_text = [
    ["bom", "excelente", "ótimo"],
    ["ruim", "terrível", "péssimo"],
    ["legal", "bacana", "interessante"]
]
y_text = ["positivo", "negativo", "positivo"]

nb_text = NaiveBayesClassifier()
nb_text.fit(X_text, y_text)

# Predição
review = ["bom", "legal", "interessante"]
result = nb_text.predict(review)
print(f"Sentimento: {result[0]} (confiança: {result[1]:.3f})")
```

## Otimizações Avançadas

### 1. Feature Selection
```python
# Seleciona features mais informativas
def select_features_by_chi2(X, y, k=10):
    # Implementa teste qui-quadrado
    pass
```

### 2. Balanceamento de Classes
```python
# Ajusta probabilidades a priori
def balanced_priors(y):
    unique_classes = set(y)
    return {cls: 1/len(unique_classes) for cls in unique_classes}
```

### 3. Ensemble Methods
```python
# Combina múltiplos modelos Naive Bayes
def ensemble_prediction(models, sample):
    predictions = [model.predict_proba(sample) for model in models]
    return average_predictions(predictions)
```

## Comparação com Outros Algoritmos

| Algoritmo | Acurácia | Velocidade | Interpretabilidade |
|-----------|----------|------------|-------------------|
| **Naive Bayes** | 📊 Boa | 🚀 Muito Rápida | 👁️ Alta |
| Logistic Regression | 📊 Boa | 🚀 Rápida | 👁️ Média |
| Random Forest | 📊 Muito Boa | 🚀 Média | 👁️ Baixa |
| SVM | 📊 Muito Boa | 🚀 Lenta | 👁️ Baixa |
| Neural Networks | 📊 Excelente | 🚀 Muito Lenta | 👁️ Muito Baixa |

## Variantes do Algoritmo

### 1. Gaussian Naive Bayes
- **Uso**: Features contínuas
- **Distribuição**: Gaussiana (normal)
- **Parâmetros**: μ (média), σ² (variância)

### 2. Multinomial Naive Bayes
- **Uso**: Contagem de features (texto)
- **Distribuição**: Multinomial
- **Parâmetros**: Probabilidades de cada termo

### 3. Bernoulli Naive Bayes
- **Uso**: Features binárias
- **Distribuição**: Bernoulli
- **Parâmetros**: Probabilidade de ocorrência

### 4. Categorical Naive Bayes
- **Uso**: Features categóricas
- **Distribuição**: Categórica
- **Parâmetros**: Probabilidade de cada categoria

## Tratamento de Problemas

### Zero Probability
```python
# Suavização de Laplace
P(word|class) = (count(word, class) + α) / (count(class) + α * |V|)
```

### Numerical Underflow
```python
# Usar logaritmos
log_prob = log(prior) + sum(log(likelihood))
```

### Feature Scaling
```python
# Gaussian NB é sensível à escala
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

## Executar Exemplo

```bash
cd python/naive_bayes
python naive_bayes_basico.py
```

## Aplicações Industriais

### 1. Recomendação de Produtos
```python
# Baseado em histórico de compras
user_features = ["categoria_preferida", "faixa_preco", "marca"]
recommendation = nb.predict(user_features)
```

### 2. Detecção de Fraudes
```python
# Baseado em padrões de transação
transaction_features = ["valor", "horario", "local", "tipo"]
is_fraud = nb.predict(transaction_features)
```

### 3. Classificação de Documentos
```python
# Organização automática de documentos
document_features = extract_text_features(document)
category = nb.predict(document_features)
```

## Referências

- [Pattern Recognition and Machine Learning - Bishop](https://www.microsoft.com/en-us/research/people/cmbishop/)
- [The Elements of Statistical Learning - Hastie](https://web.stanford.edu/~hastie/ElemStatLearn/)
- [Machine Learning: A Probabilistic Perspective - Murphy](https://probml.github.io/pml-book/)
- [Naive Bayes and Text Classification - Manning](https://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html)

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
  <i>💡 "A simplicidade é o último grau de sofisticação" - Leonardo da Vinci</i>
  <br>
  <i>💡 "Simplicity is the ultimate sophistication" - Leonardo da Vinci</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=4A90E2&height=120&section=footer"/>

</div>
