"""
Classificador Naive Bayes - Implementação básica
Algoritmo de classificação probabilística baseado no Teorema de Bayes
Suporta dados categóricos e contínuos (usando distribuição Gaussiana)
"""

import math
from collections import defaultdict, Counter


class NaiveBayesClassifier:
    def __init__(self):
        """Inicializa o classificador Naive Bayes"""
        self.classes = set()
        self.class_counts = defaultdict(int)
        self.feature_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        self.feature_stats = defaultdict(lambda: defaultdict(lambda: {'sum': 0, 'sum_sq': 0, 'count': 0}))
        self.total_samples = 0
        self.feature_types = {}  # 'categorical' ou 'continuous'
        self.trained = False
    
    def _determine_feature_type(self, values):
        """Determina automaticamente se uma feature é categórica ou contínua"""
        # Se todos os valores são números e há muitos valores únicos, trata como contínuo
        try:
            numeric_values = [float(v) for v in values]
            unique_ratio = len(set(numeric_values)) / len(numeric_values)
            # Se mais de 50% dos valores são únicos, trata como contínuo
            return 'continuous' if unique_ratio > 0.5 else 'categorical'
        except (ValueError, TypeError):
            return 'categorical'
    
    def fit(self, X, y):
        """
        Treina o classificador com os dados
        
        Args:
            X (list): Lista de amostras, onde cada amostra é uma lista de features
            y (list): Lista de classes correspondentes
        """
        self.classes = set(y)
        self.total_samples = len(y)
        
        # Conta classes
        for label in y:
            self.class_counts[label] += 1
        
        # Determina tipos de features analisando a primeira amostra
        if X:
            num_features = len(X[0])
            for feature_idx in range(num_features):
                feature_values = [sample[feature_idx] for sample in X]
                self.feature_types[feature_idx] = self._determine_feature_type(feature_values)
        
        # Processa cada amostra
        for sample, label in zip(X, y):
            for feature_idx, feature_value in enumerate(sample):
                if self.feature_types[feature_idx] == 'categorical':
                    # Feature categórica: conta ocorrências
                    self.feature_counts[feature_idx][label][feature_value] += 1
                else:
                    # Feature contínua: acumula estatísticas para distribuição Gaussiana
                    try:
                        numeric_value = float(feature_value)
                        stats = self.feature_stats[feature_idx][label]
                        stats['sum'] += numeric_value
                        stats['sum_sq'] += numeric_value ** 2
                        stats['count'] += 1
                    except (ValueError, TypeError):
                        # Se não conseguir converter para número, trata como categórico
                        self.feature_types[feature_idx] = 'categorical'
                        self.feature_counts[feature_idx][label][feature_value] += 1
        
        self.trained = True
    
    def _calculate_prior(self, class_label):
        """Calcula a probabilidade a priori de uma classe"""
        return self.class_counts[class_label] / self.total_samples
    
    def _calculate_categorical_likelihood(self, feature_idx, feature_value, class_label):
        """Calcula likelihood para feature categórica usando suavização de Laplace"""
        # Conta de ocorrências da feature_value na classe
        feature_count = self.feature_counts[feature_idx][class_label][feature_value]
        
        # Total de amostras na classe
        class_total = self.class_counts[class_label]
        
        # Número de valores únicos para esta feature
        all_values = set()
        for label in self.classes:
            all_values.update(self.feature_counts[feature_idx][label].keys())
        num_unique_values = len(all_values)
        
        # Suavização de Laplace para evitar probabilidade zero
        return (feature_count + 1) / (class_total + num_unique_values)
    
    def _calculate_gaussian_likelihood(self, feature_idx, feature_value, class_label):
        """Calcula likelihood para feature contínua usando distribuição Gaussiana"""
        try:
            numeric_value = float(feature_value)
        except (ValueError, TypeError):
            return 1e-10  # Probabilidade muito baixa para valores inválidos
        
        stats = self.feature_stats[feature_idx][class_label]
        
        if stats['count'] == 0:
            return 1e-10
        
        # Calcula média e variância
        mean = stats['sum'] / stats['count']
        if stats['count'] > 1:
            variance = (stats['sum_sq'] - (stats['sum'] ** 2) / stats['count']) / (stats['count'] - 1)
            variance = max(variance, 1e-10)  # Evita variância zero
        else:
            variance = 1.0  # Variância padrão para uma única amostra
        
        # Calcula densidade da distribuição Gaussiana
        std_dev = math.sqrt(variance)
        exponent = -((numeric_value - mean) ** 2) / (2 * variance)
        coefficient = 1 / (std_dev * math.sqrt(2 * math.pi))
        
        return coefficient * math.exp(exponent)
    
    def predict_proba(self, sample):
        """
        Calcula probabilidades para cada classe
        
        Args:
            sample (list): Amostra para classificar
        
        Returns:
            dict: Probabilidades para cada classe
        """
        if not self.trained:
            raise ValueError("Modelo deve ser treinado antes de fazer predições")
        
        class_probabilities = {}
        
        for class_label in self.classes:
            # Probabilidade a priori
            log_prob = math.log(self._calculate_prior(class_label))
            
            # Multiplica likelihoods (soma em log-space)
            for feature_idx, feature_value in enumerate(sample):
                if self.feature_types[feature_idx] == 'categorical':
                    likelihood = self._calculate_categorical_likelihood(feature_idx, feature_value, class_label)
                else:
                    likelihood = self._calculate_gaussian_likelihood(feature_idx, feature_value, class_label)
                
                # Evita log(0)
                likelihood = max(likelihood, 1e-10)
                log_prob += math.log(likelihood)
            
            class_probabilities[class_label] = log_prob
        
        # Converte de log-space para probabilidades normalizadas
        max_log_prob = max(class_probabilities.values())
        exp_probs = {}
        total_prob = 0
        
        for class_label, log_prob in class_probabilities.items():
            exp_prob = math.exp(log_prob - max_log_prob)
            exp_probs[class_label] = exp_prob
            total_prob += exp_prob
        
        # Normaliza
        normalized_probs = {}
        for class_label, exp_prob in exp_probs.items():
            normalized_probs[class_label] = exp_prob / total_prob
        
        return normalized_probs
    
    def predict(self, sample):
        """
        Faz predição para uma amostra
        
        Args:
            sample (list): Amostra para classificar
        
        Returns:
            tuple: (classe_predita, confiança)
        """
        probabilities = self.predict_proba(sample)
        predicted_class = max(probabilities, key=probabilities.get)
        confidence = probabilities[predicted_class]
        
        return predicted_class, confidence
    
    def predict_batch(self, X):
        """
        Faz predições para múltiplas amostras
        
        Args:
            X (list): Lista de amostras
        
        Returns:
            list: Lista de predições
        """
        predictions = []
        for sample in X:
            predicted_class, confidence = self.predict(sample)
            predictions.append({'class': predicted_class, 'confidence': confidence})
        
        return predictions
    
    def get_feature_importance(self):
        """Retorna importância das features baseada na variância entre classes"""
        if not self.trained:
            raise ValueError("Modelo deve ser treinado primeiro")
        
        importance = {}
        
        for feature_idx in self.feature_types:
            if self.feature_types[feature_idx] == 'continuous':
                # Para features contínuas, usa diferença de médias entre classes
                means = []
                for class_label in self.classes:
                    stats = self.feature_stats[feature_idx][class_label]
                    if stats['count'] > 0:
                        mean = stats['sum'] / stats['count']
                        means.append(mean)
                
                if len(means) > 1:
                    # Variância das médias como medida de importância
                    mean_of_means = sum(means) / len(means)
                    variance = sum((m - mean_of_means) ** 2 for m in means) / len(means)
                    importance[f'feature_{feature_idx}'] = variance
                else:
                    importance[f'feature_{feature_idx}'] = 0.0
            else:
                # Para features categóricas, usa entropia
                total_entropy = 0
                for class_label in self.classes:
                    class_counts = self.feature_counts[feature_idx][class_label]
                    if class_counts:
                        total_count = sum(class_counts.values())
                        entropy = 0
                        for count in class_counts.values():
                            if count > 0:
                                p = count / total_count
                                entropy -= p * math.log2(p)
                        total_entropy += entropy
                
                importance[f'feature_{feature_idx}'] = total_entropy
        
        return importance


def load_iris_dataset():
    """Carrega um dataset sintético similar ao Iris para demonstração"""
    # Dataset sintético com 3 classes e 4 features
    data = [
        # Classe: setosa (features: sepal_length, sepal_width, petal_length, petal_width)
        [5.1, 3.5, 1.4, 0.2, 'setosa'],
        [4.9, 3.0, 1.4, 0.2, 'setosa'],
        [4.7, 3.2, 1.3, 0.2, 'setosa'],
        [4.6, 3.1, 1.5, 0.2, 'setosa'],
        [5.0, 3.6, 1.4, 0.2, 'setosa'],
        [5.4, 3.9, 1.7, 0.4, 'setosa'],
        [4.6, 3.4, 1.4, 0.3, 'setosa'],
        [5.0, 3.4, 1.5, 0.2, 'setosa'],
        
        # Classe: versicolor
        [7.0, 3.2, 4.7, 1.4, 'versicolor'],
        [6.4, 3.2, 4.5, 1.5, 'versicolor'],
        [6.9, 3.1, 4.9, 1.5, 'versicolor'],
        [5.5, 2.3, 4.0, 1.3, 'versicolor'],
        [6.5, 2.8, 4.6, 1.5, 'versicolor'],
        [5.7, 2.8, 4.5, 1.3, 'versicolor'],
        [6.3, 3.3, 4.7, 1.6, 'versicolor'],
        [4.9, 2.4, 3.3, 1.0, 'versicolor'],
        
        # Classe: virginica
        [6.3, 3.3, 6.0, 2.5, 'virginica'],
        [5.8, 2.7, 5.1, 1.9, 'virginica'],
        [7.1, 3.0, 5.9, 2.1, 'virginica'],
        [6.3, 2.9, 5.6, 1.8, 'virginica'],
        [6.5, 3.0, 5.8, 2.2, 'virginica'],
        [7.6, 3.0, 6.6, 2.1, 'virginica'],
        [4.9, 2.5, 4.5, 1.7, 'virginica'],
        [7.3, 2.9, 6.3, 1.8, 'virginica'],
    ]
    
    X = [row[:-1] for row in data]  # Features
    y = [row[-1] for row in data]   # Classes
    
    return X, y


def load_text_classification_dataset():
    """Carrega dataset sintético para classificação de texto"""
    # Dataset com features categóricas para classificação de sentimento
    data = [
        # [palavra1, palavra2, palavra3, classe]
        ['bom', 'excelente', 'perfeito', 'positivo'],
        ['ruim', 'terrível', 'horrível', 'negativo'],
        ['ótimo', 'maravilhoso', 'fantástico', 'positivo'],
        ['péssimo', 'detestável', 'insuportável', 'negativo'],
        ['legal', 'bacana', 'interessante', 'positivo'],
        ['chato', 'entediante', 'monótono', 'negativo'],
        ['incrível', 'espetacular', 'sensacional', 'positivo'],
        ['frustrante', 'decepcionante', 'irritante', 'negativo'],
        ['agradável', 'prazeroso', 'satisfatório', 'positivo'],
        ['desagradável', 'incômodo', 'perturbador', 'negativo'],
    ]
    
    X = [row[:-1] for row in data]  # Features
    y = [row[-1] for row in data]   # Classes
    
    return X, y


# Exemplo de uso
if __name__ == "__main__":
    print("=== Classificador Naive Bayes ===")
    
    # Teste 1: Dataset numérico (tipo Iris)
    print("\n=== Teste 1: Classificação com Features Numéricas ===")
    
    X_iris, y_iris = load_iris_dataset()
    
    # Divide em treino e teste (80/20)
    split_idx = int(0.8 * len(X_iris))
    X_train, X_test = X_iris[:split_idx], X_iris[split_idx:]
    y_train, y_test = y_iris[:split_idx], y_iris[split_idx:]
    
    # Treina classificador
    nb_classifier = NaiveBayesClassifier()
    nb_classifier.fit(X_train, y_train)
    
    print(f"Dados de treino: {len(X_train)} amostras")
    print(f"Dados de teste: {len(X_test)} amostras")
    print(f"Classes: {sorted(nb_classifier.classes)}")
    
    # Testa predições
    correct_predictions = 0
    total_predictions = len(X_test)
    
    print(f"\nResultados das predições:")
    for i, (sample, true_label) in enumerate(zip(X_test, y_test)):
        predicted_class, confidence = nb_classifier.predict(sample)
        is_correct = predicted_class == true_label
        
        if is_correct:
            correct_predictions += 1
        
        print(f"  Amostra {i+1}: {sample}")
        print(f"    Verdadeiro: {true_label}")
        print(f"    Predito: {predicted_class} (confiança: {confidence:.3f})")
        print(f"    Correto: {'✓' if is_correct else '✗'}")
        
        # Mostra todas as probabilidades
        probabilities = nb_classifier.predict_proba(sample)
        print(f"    Probabilidades: {', '.join(f'{k}: {v:.3f}' for k, v in probabilities.items())}")
        print()
    
    accuracy = correct_predictions / total_predictions
    print(f"Acurácia: {accuracy:.3f} ({correct_predictions}/{total_predictions})")
    
    # Teste 2: Dataset categórico (classificação de texto)
    print("\n=== Teste 2: Classificação com Features Categóricas ===")
    
    X_text, y_text = load_text_classification_dataset()
    
    # Treina novo classificador
    nb_text = NaiveBayesClassifier()
    nb_text.fit(X_text, y_text)
    
    print(f"Dataset de texto: {len(X_text)} amostras")
    print(f"Classes: {sorted(nb_text.classes)}")
    
    # Testa com amostras sintéticas
    test_samples = [
        ['bom', 'legal', 'interessante'],
        ['ruim', 'chato', 'terrível'],
        ['ótimo', 'incrível', 'fantástico'],
        ['péssimo', 'frustrante', 'horrível']
    ]
    
    print(f"\nTeste com amostras sintéticas:")
    for i, sample in enumerate(test_samples):
        predicted_class, confidence = nb_text.predict(sample)
        probabilities = nb_text.predict_proba(sample)
        
        print(f"  Amostra {i+1}: {sample}")
        print(f"    Predição: {predicted_class} (confiança: {confidence:.3f})")
        print(f"    Probabilidades: {', '.join(f'{k}: {v:.3f}' for k, v in probabilities.items())}")
    
    # Análise de importância das features
    print(f"\n=== Importância das Features ===")
    
    # Para o dataset numérico
    importance_iris = nb_classifier.get_feature_importance()
    print(f"Dataset Iris:")
    feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    for i, (feature, importance) in enumerate(importance_iris.items()):
        feature_name = feature_names[i] if i < len(feature_names) else feature
        print(f"  {feature_name}: {importance:.4f}")
    
    # Para o dataset categórico
    importance_text = nb_text.get_feature_importance()
    print(f"\nDataset de Texto:")
    word_positions = ['palavra_1', 'palavra_2', 'palavra_3']
    for i, (feature, importance) in enumerate(importance_text.items()):
        position_name = word_positions[i] if i < len(word_positions) else feature
        print(f"  {position_name}: {importance:.4f}")
    
    # Demonstração de tipos de features detectados
    print(f"\n=== Tipos de Features Detectados ===")
    print(f"Dataset Iris:")
    for idx, feature_type in nb_classifier.feature_types.items():
        feature_name = feature_names[idx] if idx < len(feature_names) else f'feature_{idx}'
        print(f"  {feature_name}: {feature_type}")
    
    print(f"\nDataset de Texto:")
    for idx, feature_type in nb_text.feature_types.items():
        position_name = word_positions[idx] if idx < len(word_positions) else f'feature_{idx}'
        print(f"  {position_name}: {feature_type}")
    
    # Estatísticas do modelo
    print(f"\n=== Estatísticas dos Modelos ===")
    print(f"Modelo Iris:")
    print(f"  Total de amostras: {nb_classifier.total_samples}")
    print(f"  Número de classes: {len(nb_classifier.classes)}")
    print(f"  Número de features: {len(nb_classifier.feature_types)}")
    
    print(f"\nModelo Texto:")
    print(f"  Total de amostras: {nb_text.total_samples}")
    print(f"  Número de classes: {len(nb_text.classes)}")
    print(f"  Número de features: {len(nb_text.feature_types)}")
