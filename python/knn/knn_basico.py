"""
K-Nearest Neighbors (KNN) - Implementação Básica
================================================

Algoritmo de classificação que classifica um ponto baseado na classe
dos K vizinhos mais próximos.

Complexidade:
- Tempo: O(n * d) para cada predição, onde n é o número de pontos e d é a dimensão
- Espaço: O(n * d) para armazenar os dados de treino

Casos de uso:
- Classificação de imagens
- Sistemas de recomendação
- Diagnóstico médico
- Reconhecimento de padrões
"""

import math
from typing import List, Tuple, Any
from collections import Counter


class KNNBasico:
    """
    Implementação básica do algoritmo K-Nearest Neighbors.
    
    Esta implementação é focada na clareza e entendimento,
    utilizando estruturas simples e comentários extensos.
    """
    
    def __init__(self, k: int = 3):
        """
        Inicializa o classificador KNN.
        
        Args:
            k (int): Número de vizinhos mais próximos a considerar
        """
        self.k = k
        self.dados_treino = []  # Lista para armazenar (ponto, classe)
        print(f"🎯 KNN Básico inicializado com k={k}")
    
    def calcular_distancia_euclidiana(self, ponto1: List[float], ponto2: List[float]) -> float:
        """
        Calcula a distância euclidiana entre dois pontos.
        
        Fórmula: √(Σ(xi - yi)²)
        
        Args:
            ponto1: Primeiro ponto (lista de coordenadas)
            ponto2: Segundo ponto (lista de coordenadas)
            
        Returns:
            float: Distância euclidiana entre os pontos
        """
        if len(ponto1) != len(ponto2):
            raise ValueError("Os pontos devem ter a mesma dimensão")
        
        # Calcula a soma dos quadrados das diferenças
        soma_quadrados = 0
        for i in range(len(ponto1)):
            diferenca = ponto1[i] - ponto2[i]
            soma_quadrados += diferenca * diferenca
            print(f"   Dimensão {i+1}: ({ponto1[i]} - {ponto2[i]})² = {diferenca * diferenca}")
        
        distancia = math.sqrt(soma_quadrados)
        print(f"   Distância euclidiana: √{soma_quadrados} = {distancia:.3f}")
        return distancia
    
    def treinar(self, dados: List[Tuple[List[float], Any]]):
        """
        Treina o modelo KNN (apenas armazena os dados).
        
        No KNN, o "treinamento" é simplesmente armazenar os dados,
        pois é um algoritmo de aprendizado lazy (preguiçoso).
        
        Args:
            dados: Lista de tuplas (ponto, classe)
        """
        self.dados_treino = dados.copy()
        print(f"📚 Modelo treinado com {len(self.dados_treino)} exemplos")
        
        # Mostra estatísticas dos dados
        classes = [classe for _, classe in dados]
        contador_classes = Counter(classes)
        print(f"📊 Distribuição das classes: {dict(contador_classes)}")
    
    def encontrar_k_vizinhos(self, ponto_consulta: List[float]) -> List[Tuple[float, Any]]:
        """
        Encontra os k vizinhos mais próximos de um ponto.
        
        Args:
            ponto_consulta: Ponto para o qual queremos encontrar vizinhos
            
        Returns:
            Lista com os k vizinhos mais próximos (distancia, classe)
        """
        print(f"\n🔍 Buscando {self.k} vizinhos mais próximos para {ponto_consulta}")
        
        # Calcula distância para todos os pontos de treino
        distancias = []
        for i, (ponto_treino, classe) in enumerate(self.dados_treino):
            print(f"\n📏 Calculando distância para ponto {i+1}: {ponto_treino} (classe: {classe})")
            distancia = self.calcular_distancia_euclidiana(ponto_consulta, ponto_treino)
            distancias.append((distancia, classe))
        
        # Ordena por distância (menor primeiro)
        distancias.sort(key=lambda x: x[0])
        
        # Retorna os k primeiros
        k_vizinhos = distancias[:self.k]
        
        print(f"\n🎯 {self.k} vizinhos mais próximos:")
        for i, (dist, classe) in enumerate(k_vizinhos):
            print(f"   {i+1}º vizinho: distância={dist:.3f}, classe={classe}")
        
        return k_vizinhos
    
    def classificar(self, ponto_consulta: List[float]) -> Any:
        """
        Classifica um ponto baseado nos k vizinhos mais próximos.
        
        Args:
            ponto_consulta: Ponto a ser classificado
            
        Returns:
            Classe prevista (mais frequente entre os k vizinhos)
        """
        if not self.dados_treino:
            raise ValueError("Modelo não foi treinado. Chame treinar() primeiro.")
        
        # Encontra os k vizinhos mais próximos
        k_vizinhos = self.encontrar_k_vizinhos(ponto_consulta)
        
        # Conta a frequência de cada classe
        classes = [classe for _, classe in k_vizinhos]
        contador_classes = Counter(classes)
        
        print(f"\n📊 Contagem de classes nos vizinhos: {dict(contador_classes)}")
        
        # Retorna a classe mais frequente
        classe_prevista = contador_classes.most_common(1)[0][0]
        confianca = contador_classes[classe_prevista] / self.k
        
        print(f"🎯 Classe prevista: {classe_prevista}")
        print(f"🔢 Confiança: {confianca:.1%} ({contador_classes[classe_prevista]}/{self.k} vizinhos)")
        
        return classe_prevista


def demonstracao_knn_basico():
    """
    Demonstração do algoritmo KNN com exemplo prático.
    """
    print("=" * 60)
    print("🤖 DEMONSTRAÇÃO: K-Nearest Neighbors (KNN) - Versão Básica")
    print("=" * 60)
    
    # Criando dados de exemplo: flores com duas características
    # [comprimento_petala, largura_petala] -> especie
    dados_flores = [
        ([2.0, 1.0], "setosa"),
        ([2.2, 1.1], "setosa"),
        ([1.8, 0.9], "setosa"),
        ([5.0, 3.0], "versicolor"),
        ([4.8, 2.8], "versicolor"),
        ([5.2, 3.2], "versicolor"),
        ([6.5, 4.0], "virginica"),
        ([6.8, 4.2], "virginica"),
        ([6.3, 3.8], "virginica"),
    ]
    
    print(f"🌸 Dataset: Classificação de flores com {len(dados_flores)} exemplos")
    print("📊 Características: [comprimento_pétala, largura_pétala]")
    
    # Inicializa o classificador
    knn = KNNBasico(k=3)
    
    # Treina o modelo
    knn.treinar(dados_flores)
    
    # Testa com diferentes pontos
    pontos_teste = [
        [2.1, 1.0],  # Deve ser setosa
        [5.1, 3.1],  # Deve ser versicolor
        [6.6, 4.1],  # Deve ser virginica
        [4.0, 2.0],  # Caso ambíguo
    ]
    
    print("\n" + "=" * 40)
    print("🧪 TESTANDO CLASSIFICAÇÕES")
    print("=" * 40)
    
    for i, ponto in enumerate(pontos_teste):
        print(f"\n🔍 TESTE {i+1}: Classificando ponto {ponto}")
        print("-" * 40)
        
        classe_prevista = knn.classificar(ponto)
        
        print(f"✅ Resultado final: {ponto} → {classe_prevista}")


def exemplo_diferentes_k():
    """
    Demonstra como diferentes valores de k afetam a classificação.
    """
    print("\n" + "=" * 60)
    print("📈 COMPARAÇÃO: Efeito de diferentes valores de K")
    print("=" * 60)
    
    # Dados simples para demonstração
    dados = [
        ([1, 1], "A"), ([1, 2], "A"), ([2, 1], "A"),
        ([5, 5], "B"), ([5, 6], "B"), ([6, 5], "B"),
        ([3, 3], "A"),  # Ponto intermediário
    ]
    
    ponto_teste = [3, 4]
    
    for k in [1, 3, 5]:
        print(f"\n🎯 Testando com k={k}")
        print("-" * 30)
        
        knn = KNNBasico(k=k)
        knn.treinar(dados)
        
        resultado = knn.classificar(ponto_teste)
        print(f"📊 Com k={k}: {ponto_teste} → {resultado}")


if __name__ == "__main__":
    # Executa as demonstrações
    demonstracao_knn_basico()
    exemplo_diferentes_k()
    
    print("\n" + "=" * 60)
    print("🎓 EXERCÍCIOS SUGERIDOS:")
    print("=" * 60)
    print("1. Implemente outras métricas de distância (Manhattan, Minkowski)")
    print("2. Adicione validação cruzada para escolher o melhor k")
    print("3. Teste com datasets de mais dimensões")
    print("4. Implemente KNN para regressão (prever valores numéricos)")
    print("5. Adicione visualização dos resultados com matplotlib")
