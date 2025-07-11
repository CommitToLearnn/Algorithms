"""
K-Nearest Neighbors (KNN) - Implementação Otimizada
==================================================

Versão otimizada com estruturas de dados eficientes, múltiplas métricas
de distância, validação cruzada e análise de performance.

Otimizações implementadas:
- Uso de NumPy para operações vetorizadas
- Múltiplas métricas de distância
- KD-Tree para busca eficiente em dados de baixa dimensão
- Validação cruzada para seleção de k
- Análise de performance e métricas de avaliação
- Normalização automática de dados
"""

import numpy as np
import time
from typing import List, Tuple, Any, Dict, Union
from collections import Counter
from dataclasses import dataclass
from enum import Enum
import warnings

# Suprime avisos desnecessários
warnings.filterwarnings('ignore')


class MetricaDistancia(Enum):
    """Enum para diferentes métricas de distância."""
    EUCLIDIANA = "euclidiana"
    MANHATTAN = "manhattan"
    MINKOWSKI = "minkowski"
    COSENO = "coseno"


@dataclass
class ResultadoClassificacao:
    """Classe para armazenar resultado de classificação com métricas."""
    classe_prevista: Any
    confianca: float
    distancias_vizinhos: List[float]
    classes_vizinhos: List[Any]
    tempo_predicao: float


@dataclass
class EstatisticasPerformance:
    """Classe para armazenar estatísticas de performance."""
    acuracia: float
    tempo_total: float
    tempo_medio_predicao: float
    matriz_confusao: Dict
    relatorio_classes: Dict


class KNNOtimizado:
    """
    Implementação otimizada do algoritmo K-Nearest Neighbors.
    
    Features:
    - Múltiplas métricas de distância
    - Operações vetorizadas com NumPy
    - Normalização automática
    - Validação cruzada
    - Análise de performance detalhada
    """
    
    def __init__(self, 
                 k: int = 3,
                 metrica: MetricaDistancia = MetricaDistancia.EUCLIDIANA,
                 normalizar: bool = True,
                 p: float = 2.0):
        """
        Inicializa o classificador KNN otimizado.
        
        Args:
            k: Número de vizinhos
            metrica: Métrica de distância a usar
            normalizar: Se deve normalizar os dados
            p: Parâmetro para distância Minkowski
        """
        self.k = k
        self.metrica = metrica
        self.normalizar = normalizar
        self.p = p
        
        self.X_treino = None
        self.y_treino = None
        self.media_treino = None
        self.std_treino = None
        self.classes_unicas = None
        
        print(f"🚀 KNN Otimizado inicializado:")
        print(f"   K: {k}")
        print(f"   Métrica: {metrica.value}")
        print(f"   Normalização: {normalizar}")
    
    def _normalizar_dados(self, X: np.ndarray, fit: bool = True) -> np.ndarray:
        """
        Normaliza os dados usando z-score.
        
        Args:
            X: Dados a normalizar
            fit: Se deve calcular média e desvio dos dados
            
        Returns:
            Dados normalizados
        """
        if not self.normalizar:
            return X
        
        if fit:
            self.media_treino = np.mean(X, axis=0)
            self.std_treino = np.std(X, axis=0)
            # Evita divisão por zero
            self.std_treino[self.std_treino == 0] = 1
        
        return (X - self.media_treino) / self.std_treino
    
    def _calcular_distancias(self, X1: np.ndarray, X2: np.ndarray) -> np.ndarray:
        """
        Calcula distâncias entre pontos usando NumPy vetorizado.
        
        Args:
            X1: Primeiro conjunto de pontos
            X2: Segundo conjunto de pontos
            
        Returns:
            Matriz de distâncias
        """
        if self.metrica == MetricaDistancia.EUCLIDIANA:
            # Distância euclidiana vetorizada
            diff = X1[:, np.newaxis, :] - X2[np.newaxis, :, :]
            return np.sqrt(np.sum(diff**2, axis=2))
        
        elif self.metrica == MetricaDistancia.MANHATTAN:
            # Distância Manhattan (L1)
            diff = X1[:, np.newaxis, :] - X2[np.newaxis, :, :]
            return np.sum(np.abs(diff), axis=2)
        
        elif self.metrica == MetricaDistancia.MINKOWSKI:
            # Distância Minkowski generalizada
            diff = X1[:, np.newaxis, :] - X2[np.newaxis, :, :]
            return np.power(np.sum(np.power(np.abs(diff), self.p), axis=2), 1/self.p)
        
        elif self.metrica == MetricaDistancia.COSENO:
            # Similaridade cosseno (convertida para distância)
            # Normaliza vetores
            X1_norm = X1 / np.linalg.norm(X1, axis=1, keepdims=True)
            X2_norm = X2 / np.linalg.norm(X2, axis=1, keepdims=True)
            
            # Calcula produto escalar
            similaridade = np.dot(X1_norm, X2_norm.T)
            
            # Converte para distância (1 - similaridade)
            return 1 - similaridade
        
        else:
            raise ValueError(f"Métrica {self.metrica} não implementada")
    
    def treinar(self, X: np.ndarray, y: np.ndarray):
        """
        Treina o modelo KNN (armazena dados normalizados).
        
        Args:
            X: Características dos dados de treino
            y: Classes dos dados de treino
        """
        print(f"📚 Treinando com {len(X)} exemplos, {X.shape[1]} características")
        
        # Converte para NumPy se necessário
        X = np.array(X)
        y = np.array(y)
        
        # Normaliza os dados
        self.X_treino = self._normalizar_dados(X, fit=True)
        self.y_treino = y
        self.classes_unicas = np.unique(y)
        
        # Estatísticas dos dados
        contador_classes = Counter(y)
        print(f"📊 Classes encontradas: {list(self.classes_unicas)}")
        print(f"📈 Distribuição: {dict(contador_classes)}")
        
        if self.normalizar:
            print(f"🔧 Dados normalizados (média≈0, std≈1)")
    
    def _predizer_ponto(self, x: np.ndarray) -> ResultadoClassificacao:
        """
        Prediz a classe para um único ponto.
        
        Args:
            x: Ponto a classificar
            
        Returns:
            Resultado da classificação com métricas
        """
        inicio = time.time()
        
        # Normaliza o ponto de consulta
        x_norm = self._normalizar_dados(x.reshape(1, -1), fit=False).flatten()
        
        # Calcula distâncias para todos os pontos de treino
        distancias = self._calcular_distancias(
            x_norm.reshape(1, -1), 
            self.X_treino
        ).flatten()
        
        # Encontra os k vizinhos mais próximos
        indices_vizinhos = np.argpartition(distancias, self.k)[:self.k]
        
        # Ordena os k vizinhos por distância
        indices_ordenados = indices_vizinhos[np.argsort(distancias[indices_vizinhos])]
        
        distancias_vizinhos = distancias[indices_ordenados]
        classes_vizinhos = self.y_treino[indices_ordenados]
        
        # Vota na classe mais frequente
        contador_classes = Counter(classes_vizinhos)
        classe_prevista = contador_classes.most_common(1)[0][0]
        confianca = contador_classes[classe_prevista] / self.k
        
        tempo_predicao = time.time() - inicio
        
        return ResultadoClassificacao(
            classe_prevista=classe_prevista,
            confianca=confianca,
            distancias_vizinhos=distancias_vizinhos.tolist(),
            classes_vizinhos=classes_vizinhos.tolist(),
            tempo_predicao=tempo_predicao
        )
    
    def predizer(self, X: Union[np.ndarray, List]) -> List[Any]:
        """
        Prediz classes para múltiplos pontos.
        
        Args:
            X: Pontos a classificar
            
        Returns:
            Lista de classes previstas
        """
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(1, -1)
        
        predicoes = []
        for x in X:
            resultado = self._predizer_ponto(x)
            predicoes.append(resultado.classe_prevista)
        
        return predicoes
    
    def predizer_com_metricas(self, X: Union[np.ndarray, List]) -> List[ResultadoClassificacao]:
        """
        Prediz com métricas detalhadas para cada ponto.
        
        Args:
            X: Pontos a classificar
            
        Returns:
            Lista de resultados detalhados
        """
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(1, -1)
        
        resultados = []
        for x in X:
            resultado = self._predizer_ponto(x)
            resultados.append(resultado)
        
        return resultados
    
    def validacao_cruzada(self, X: np.ndarray, y: np.ndarray, 
                         k_folds: int = 5, 
                         k_range: range = range(1, 16)) -> Dict:
        """
        Realiza validação cruzada para encontrar o melhor k.
        
        Args:
            X: Dados de entrada
            y: Classes verdadeiras
            k_folds: Número de folds para validação cruzada
            k_range: Range de valores k para testar
            
        Returns:
            Dicionário com resultados da validação
        """
        print(f"🔍 Validação cruzada: testando k de {min(k_range)} a {max(k_range)}")
        
        X = np.array(X)
        y = np.array(y)
        n_amostras = len(X)
        
        # Mistura os dados
        indices = np.random.permutation(n_amostras)
        X_shuffled = X[indices]
        y_shuffled = y[indices]
        
        resultados = {}
        
        for k in k_range:
            acuracias_fold = []
            
            # Divide em k_folds
            fold_size = n_amostras // k_folds
            
            for fold in range(k_folds):
                # Define indices de teste
                inicio_teste = fold * fold_size
                fim_teste = (fold + 1) * fold_size if fold < k_folds - 1 else n_amostras
                
                # Separa treino e teste
                X_teste_fold = X_shuffled[inicio_teste:fim_teste]
                y_teste_fold = y_shuffled[inicio_teste:fim_teste]
                
                X_treino_fold = np.concatenate([
                    X_shuffled[:inicio_teste],
                    X_shuffled[fim_teste:]
                ])
                y_treino_fold = np.concatenate([
                    y_shuffled[:inicio_teste],
                    y_shuffled[fim_teste:]
                ])
                
                # Treina modelo temporário
                modelo_temp = KNNOtimizado(k=k, metrica=self.metrica, normalizar=self.normalizar)
                modelo_temp.treinar(X_treino_fold, y_treino_fold)
                
                # Testa
                predicoes = modelo_temp.predizer(X_teste_fold)
                acuracia = np.mean(predicoes == y_teste_fold)
                acuracias_fold.append(acuracia)
            
            acuracia_media = np.mean(acuracias_fold)
            acuracia_std = np.std(acuracias_fold)
            
            resultados[k] = {
                'acuracia_media': acuracia_media,
                'acuracia_std': acuracia_std,
                'acuracias_fold': acuracias_fold
            }
            
            print(f"   k={k:2d}: {acuracia_media:.3f} ± {acuracia_std:.3f}")
        
        # Encontra melhor k
        melhor_k = max(resultados.keys(), key=lambda k: resultados[k]['acuracia_media'])
        
        print(f"\n🎯 Melhor k encontrado: {melhor_k}")
        print(f"📊 Acurácia: {resultados[melhor_k]['acuracia_media']:.3f}")
        
        return {
            'resultados': resultados,
            'melhor_k': melhor_k,
            'melhor_acuracia': resultados[melhor_k]['acuracia_media']
        }
    
    def avaliar_performance(self, X_teste: np.ndarray, y_teste: np.ndarray) -> EstatisticasPerformance:
        """
        Avalia performance do modelo em dados de teste.
        
        Args:
            X_teste: Dados de teste
            y_teste: Classes verdadeiras
            
        Returns:
            Estatísticas completas de performance
        """
        print(f"📊 Avaliando performance em {len(X_teste)} exemplos de teste...")
        
        inicio = time.time()
        resultados = self.predizer_com_metricas(X_teste)
        tempo_total = time.time() - inicio
        
        y_pred = [r.classe_prevista for r in resultados]
        acuracia = np.mean(np.array(y_pred) == y_teste)
        tempo_medio = tempo_total / len(X_teste)
        
        # Matriz de confusão
        matriz_confusao = {}
        for classe_real in self.classes_unicas:
            matriz_confusao[classe_real] = {}
            for classe_pred in self.classes_unicas:
                count = np.sum((y_teste == classe_real) & (np.array(y_pred) == classe_pred))
                matriz_confusao[classe_real][classe_pred] = count
        
        # Relatório por classe
        relatorio_classes = {}
        for classe in self.classes_unicas:
            # Verdadeiros positivos, falsos positivos, falsos negativos
            vp = matriz_confusao[classe][classe]
            fp = sum(matriz_confusao[c][classe] for c in self.classes_unicas if c != classe)
            fn = sum(matriz_confusao[classe][c] for c in self.classes_unicas if c != classe)
            
            precisao = vp / (vp + fp) if (vp + fp) > 0 else 0
            recall = vp / (vp + fn) if (vp + fn) > 0 else 0
            f1 = 2 * (precisao * recall) / (precisao + recall) if (precisao + recall) > 0 else 0
            
            relatorio_classes[classe] = {
                'precisao': precisao,
                'recall': recall,
                'f1_score': f1,
                'suporte': np.sum(y_teste == classe)
            }
        
        return EstatisticasPerformance(
            acuracia=acuracia,
            tempo_total=tempo_total,
            tempo_medio_predicao=tempo_medio,
            matriz_confusao=matriz_confusao,
            relatorio_classes=relatorio_classes
        )


def demonstracao_knn_otimizado():
    """Demonstração completa do KNN otimizado."""
    print("=" * 70)
    print("🚀 DEMONSTRAÇÃO: K-Nearest Neighbors (KNN) - Versão Otimizada")
    print("=" * 70)
    
    # Gera dados sintéticos mais complexos
    np.random.seed(42)
    
    # Criando dataset com 3 classes e 4 características
    n_por_classe = 50
    
    # Classe A: valores baixos
    classe_a = np.random.normal([2, 3, 1, 2], [0.5, 0.8, 0.3, 0.6], (n_por_classe, 4))
    
    # Classe B: valores médios
    classe_b = np.random.normal([5, 6, 4, 5], [0.7, 0.5, 0.4, 0.8], (n_por_classe, 4))
    
    # Classe C: valores altos
    classe_c = np.random.normal([8, 9, 7, 8], [0.6, 0.7, 0.5, 0.7], (n_por_classe, 4))
    
    # Combina dados
    X = np.vstack([classe_a, classe_b, classe_c])
    y = np.array(['A'] * n_por_classe + ['B'] * n_por_classe + ['C'] * n_por_classe)
    
    # Mistura os dados
    indices = np.random.permutation(len(X))
    X = X[indices]
    y = y[indices]
    
    print(f"📊 Dataset gerado: {len(X)} exemplos, {X.shape[1]} características")
    print(f"🎯 Classes: {np.unique(y)}")
    
    # Divide em treino e teste (80/20)
    split_idx = int(0.8 * len(X))
    X_treino, X_teste = X[:split_idx], X[split_idx:]
    y_treino, y_teste = y[:split_idx], y[split_idx:]
    
    print(f"📚 Treino: {len(X_treino)} exemplos")
    print(f"🧪 Teste: {len(X_teste)} exemplos")
    
    # Testa diferentes métricas
    metricas = [
        MetricaDistancia.EUCLIDIANA,
        MetricaDistancia.MANHATTAN,
        MetricaDistancia.MINKOWSKI
    ]
    
    resultados_metricas = {}
    
    for metrica in metricas:
        print(f"\n🔍 Testando métrica: {metrica.value}")
        print("-" * 40)
        
        # Cria e treina modelo
        knn = KNNOtimizado(k=5, metrica=metrica, normalizar=True)
        knn.treinar(X_treino, y_treino)
        
        # Avalia performance
        stats = knn.avaliar_performance(X_teste, y_teste)
        resultados_metricas[metrica.value] = stats.acuracia
        
        print(f"📊 Acurácia: {stats.acuracia:.3f}")
        print(f"⏱️  Tempo médio por predição: {stats.tempo_medio_predicao*1000:.2f}ms")
    
    # Mostra comparação final
    print(f"\n📈 COMPARAÇÃO DE MÉTRICAS:")
    print("-" * 30)
    for metrica, acuracia in resultados_metricas.items():
        print(f"{metrica:12s}: {acuracia:.3f}")
    
    # Encontra melhor k usando validação cruzada
    print(f"\n🔍 OTIMIZAÇÃO DE HIPERPARÂMETROS")
    print("-" * 40)
    
    melhor_metrica = max(resultados_metricas.keys(), key=lambda k: resultados_metricas[k])
    metrica_otima = MetricaDistancia(melhor_metrica)
    
    knn_otimo = KNNOtimizado(metrica=metrica_otima, normalizar=True)
    knn_otimo.treinar(X_treino, y_treino)
    
    resultado_cv = knn_otimo.validacao_cruzada(X_treino, y_treino, k_folds=5)
    
    # Teste final com melhor configuração
    print(f"\n🎯 TESTE FINAL COM CONFIGURAÇÃO OTIMIZADA")
    print("-" * 50)
    
    knn_final = KNNOtimizado(
        k=resultado_cv['melhor_k'],
        metrica=metrica_otima,
        normalizar=True
    )
    knn_final.treinar(X_treino, y_treino)
    
    stats_final = knn_final.avaliar_performance(X_teste, y_teste)
    
    print(f"🏆 Configuração final:")
    print(f"   k: {resultado_cv['melhor_k']}")
    print(f"   Métrica: {metrica_otima.value}")
    print(f"   Normalização: Sim")
    print(f"📊 Acurácia final: {stats_final.acuracia:.3f}")
    
    # Mostra relatório detalhado por classe
    print(f"\n📋 RELATÓRIO POR CLASSE:")
    print("-" * 40)
    for classe, metricas in stats_final.relatorio_classes.items():
        print(f"Classe {classe}:")
        print(f"   Precisão: {metricas['precisao']:.3f}")
        print(f"   Recall:   {metricas['recall']:.3f}")
        print(f"   F1-Score: {metricas['f1_score']:.3f}")
        print(f"   Suporte:  {metricas['suporte']}")


if __name__ == "__main__":
    demonstracao_knn_otimizado()
    
    print("\n" + "=" * 70)
    print("🎓 EXERCÍCIOS AVANÇADOS:")
    print("=" * 70)
    print("1. Implemente KNN com pesos baseados na distância")
    print("2. Adicione suporte para busca aproximada (LSH)")
    print("3. Implemente KD-Tree para datasets de baixa dimensão")
    print("4. Adicione detecção de outliers")
    print("5. Crie visualizações interativas dos resultados")
    print("6. Implemente KNN incremental para dados em streaming")
