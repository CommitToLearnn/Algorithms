<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=3776AB&height=200&section=header&text=KNN%20Python&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=K-Nearest%20Neighbors%20Algorithm%20in%20Python&descAlignY=60&descSize=18">

<p align="center">
  <i>🐍 Simple yet powerful K-Nearest Neighbors implementation in Python with NumPy optimization</i>
</p>

---

</div>

# K-Nearest Neighbors (KNN) - Python 🐍

## 📝 Descrição

O algoritmo K-Nearest Neighbors (KNN) é um dos algoritmos de aprendizado de máquina mais simples e intuitivos. É um algoritmo de classificação **lazy** (preguiçoso) que classifica um ponto baseado na classe majoritária dos K vizinhos mais próximos.

## 🧮 Complexidade

| Operação | Versão Básica | Versão Otimizada |
|----------|---------------|------------------|
| **Treinamento** | O(1) | O(1) |
| **Predição** | O(n·d) | O(n·d) / O(log n) com KD-Tree |
| **Espaço** | O(n·d) | O(n·d) |

Onde:
- `n` = número de pontos de treino
- `d` = dimensionalidade dos dados

## 🎯 Quando Usar

### ✅ Ideal para:
- Datasets pequenos a médios (< 10.000 exemplos)
- Dados com baixa dimensionalidade (< 20 características)
- Problemas onde a estrutura local dos dados é importante
- Baseline para comparação com outros algoritmos
- Sistemas de recomendação simples

### ❌ Evitar quando:
- Datasets muito grandes (> 100.000 exemplos)
- Alta dimensionalidade (curse of dimensionality)
- Dados com muito ruído
- Características com escalas muito diferentes (sem normalização)

## 📁 Estrutura dos Arquivos

```
python/knn/
├── knn_basico.py      # 🎯 Implementação didática
├── otimizado/
│   └── knn_otimizado.py   # 🚀 Versão otimizada
└── README.md          # 📖 Esta documentação
```

## 🚀 Como Executar

### Versão Básica
```bash
cd python/knn
python knn_basico.py
```

### Versão Otimizada
```bash
cd python/knn/otimizado
pip install numpy  # Instala dependência
python knn_otimizado.py
```

## 🎓 Conceitos Fundamentais

### 1. **Algoritmo Lazy**
O KNN não constrói um modelo explícito durante o treinamento. Simplesmente armazena todos os dados de treino e faz computações durante a predição.

### 2. **Escolha do K**
- **K muito pequeno**: Sensível a ruído, overfitting
- **K muito grande**: Perda de informação local, underfitting
- **Regra prática**: K = √n ou usar validação cruzada

### 3. **Métricas de Distância**

#### Distância Euclidiana (L2)
```
d(x,y) = √(Σ(xi - yi)²)
```
- Mais comum
- Sensível a outliers
- Assume importância igual para todas as dimensões

#### Distância Manhattan (L1)
```
d(x,y) = Σ|xi - yi|
```
- Menos sensível a outliers
- Útil para dados categóricos ordinais

#### Distância Minkowski (Lp)
```
d(x,y) = (Σ|xi - yi|^p)^(1/p)
```
- Generalização das anteriores
- p=1: Manhattan, p=2: Euclidiana

#### Distância Cosseno
```
d(x,y) = 1 - (x·y)/(||x||·||y||)
```
- Mede ângulo entre vetores
- Útil para dados de alta dimensão
- Ignora magnitude, foca na direção

## 💡 Implementações

### 🎯 Versão Básica (`knn_basico.py`)

**Foco**: Clareza e entendimento dos conceitos

**Características**:
- Implementação step-by-step com comentários extensos
- Visualização detalhada do processo de classificação
- Cálculo manual de distâncias
- Demonstração com datasets simples

**Exemplo de uso**:
```python
from knn_basico import KNNBasico

# Dados de exemplo: [característica1, característica2] -> classe
dados = [
    ([2.0, 1.0], "A"),
    ([5.0, 3.0], "B"),
    ([6.5, 4.0], "C")
]

# Inicializa classificador
knn = KNNBasico(k=3)

# Treina (apenas armazena dados)
knn.treinar(dados)

# Classifica novo ponto
resultado = knn.classificar([3.0, 2.0])
print(f"Classe prevista: {resultado}")
```

### 🚀 Versão Otimizada (`knn_otimizado.py`)

**Foco**: Performance e recursos avançados

**Características**:
- Operações vetorizadas com NumPy
- Múltiplas métricas de distância
- Normalização automática de dados
- Validação cruzada para seleção de hiperparâmetros
- Análise detalhada de performance
- Estruturas de dados otimizadas

**Dependências**:
```bash
pip install numpy
```

**Exemplo de uso**:
```python
from knn_otimizado import KNNOtimizado, MetricaDistancia
import numpy as np

# Dados sintéticos
X = np.random.randn(1000, 4)  # 1000 exemplos, 4 características
y = np.random.choice(['A', 'B', 'C'], 1000)

# Divide treino/teste
X_treino, X_teste = X[:800], X[800:]
y_treino, y_teste = y[:800], y[800:]

# Cria modelo otimizado
knn = KNNOtimizado(
    k=5,
    metrica=MetricaDistancia.EUCLIDIANA,
    normalizar=True
)

# Treina
knn.treinar(X_treino, y_treino)

# Prediz
predicoes = knn.predizer(X_teste)

# Avalia performance
stats = knn.avaliar_performance(X_teste, y_teste)
print(f"Acurácia: {stats.acuracia:.3f}")
```

## 📊 Comparação de Performance

| Aspecto | Básica | Otimizada |
|---------|--------|-----------|
| **Velocidade** | ~1000 ms | ~10 ms |
| **Memória** | Listas Python | Arrays NumPy |
| **Métricas** | Euclidiana | 4 métricas |
| **Normalização** | Manual | Automática |
| **Validação** | Não | Cross-validation |
| **Análise** | Básica | Completa |

## 🛠️ Técnicas de Otimização

### 1. **Normalização de Dados**
```python
# Z-score normalization
X_norm = (X - X.mean()) / X.std()
```
- Essencial quando características têm escalas diferentes
- Evita dominância de características com valores grandes

### 2. **Seleção de K por Validação Cruzada**
```python
# Testa diferentes valores de k
melhor_k = knn.validacao_cruzada(X, y, k_range=range(1, 21))
```

### 3. **Otimizações Algorítmicas**
- **KD-Tree**: Para busca eficiente em baixa dimensão
- **LSH**: Locality Sensitive Hashing para alta dimensão
- **Ball Tree**: Para métricas de distância arbitrárias

## 🧪 Exercícios Práticos

### Iniciante
1. **Teste diferentes valores de K** em um dataset e observe o efeito na acurácia
2. **Compare métricas de distância** no mesmo dataset
3. **Implemente visualização 2D** dos resultados de classificação

### Intermediário
4. **Adicione pesos baseados na distância** (vizinhos mais próximos têm maior peso)
5. **Implemente KNN para regressão** (prever valores contínuos)
6. **Crie detector de outliers** baseado na distância média aos vizinhos

### Avançado
7. **Implemente KD-Tree** para busca eficiente
8. **Adicione feature selection** automática
9. **Crie KNN incremental** para dados em streaming

## 📚 Casos de Uso Reais

### 1. **Sistema de Recomendação**
```python
# Recomenda produtos baseado em usuários similares
usuarios_similares = knn.encontrar_k_vizinhos(perfil_usuario)
produtos_recomendados = recomendar_baseado_em_vizinhos(usuarios_similares)
```

### 2. **Classificação de Imagens**
```python
# Classifica imagem baseada em características extraídas
caracteristicas_imagem = extrair_caracteristicas(imagem)
classe_imagem = knn.classificar(caracteristicas_imagem)
```

### 3. **Diagnóstico Médico**
```python
# Classifica paciente baseado em sintomas
sintomas_paciente = [febre, dor_cabeca, nausea, ...]
diagnostico = knn.classificar(sintomas_paciente)
```

## ⚡ Dicas de Performance

1. **Use normalização** quando características têm escalas diferentes
2. **Reduza dimensionalidade** com PCA para dados de alta dimensão
3. **Use métricas adequadas**: Manhattan para dados categóricos, Euclidiana para contínuos
4. **Considere sampling** para datasets muito grandes
5. **Implemente early stopping** na busca de vizinhos quando possível

## 🔗 Recursos Adicionais

- [Scikit-learn KNN Documentation](https://scikit-learn.org/stable/modules/neighbors.html)
- [Curse of Dimensionality in KNN](https://en.wikipedia.org/wiki/Curse_of_dimensionality)
- [KD-Tree Data Structure](https://en.wikipedia.org/wiki/K-d_tree)
- [Cross-validation Techniques](https://scikit-learn.org/stable/modules/cross_validation.html)

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

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../../LICENSE) para mais detalhes.

### 🙏 Acknowledgments | Agradecimentos

- **NumPy Community** for providing excellent mathematical operations
- **Scikit-learn** team for inspiring best practices in ML algorithms
- **Python Community** for making machine learning accessible to everyone
- All contributors who helped improve this implementation

---

<div align="center">
  <i>💡 Python makes machine learning simple and intuitive!</i>
  <br>
  <i>💡 Python torna o machine learning simples e intuitivo!</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=3776AB&height=120&section=footer"/>

</div>
