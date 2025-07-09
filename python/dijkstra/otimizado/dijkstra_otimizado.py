"""
Implementação Otimizada do Algoritmo de Dijkstra
===============================================

Esta implementação utiliza uma heap (fila de prioridade) para otimizar
a busca pelo vértice com menor distância, resultando em melhor performance.

Características desta versão:
- Usa heapq para fila de prioridade eficiente
- Complexidade: O((V + E) log V) onde V = vértices, E = arestas
- Mais eficiente para grafos grandes
- Parada antecipada quando destino é alcançado

Autor: Algorithms Repository
Data: Julho 2025
"""

import heapq
import sys
from typing import Dict, List, Tuple

class GrafoDijkstraOtimizado:
    """
    Classe que representa um grafo para o algoritmo de Dijkstra otimizado.
    """
    
    def __init__(self):
        """
        Inicializa um grafo vazio.
        """
        self.vertices = {}  # Dicionário de adjacências: {vertice: [(vizinho, peso), ...]}
        
    def adicionar_vertice(self, vertice: str) -> None:
        """
        Adiciona um vértice ao grafo.
        
        Args:
            vertice: Nome do vértice a ser adicionado
        """
        if vertice not in self.vertices:
            self.vertices[vertice] = []
            
    def adicionar_aresta(self, origem: str, destino: str, peso: float) -> None:
        """
        Adiciona uma aresta ponderada ao grafo.
        
        Args:
            origem: Vértice de origem
            destino: Vértice de destino
            peso: Peso da aresta (deve ser não-negativo)
        """
        if peso < 0:
            raise ValueError("O algoritmo de Dijkstra não funciona com pesos negativos")
            
        # Garante que ambos os vértices existem
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        
        # Adiciona a aresta (grafo direcionado)
        self.vertices[origem].append((destino, peso))
        
    def dijkstra_otimizado(self, origem: str, destino: str) -> Tuple[float, List[str]]:
        """
        Executa o algoritmo de Dijkstra otimizado com heap.
        
        Args:
            origem: Vértice de origem
            destino: Vértice de destino
            
        Returns:
            Tupla contendo (distância_total, caminho)
            
        Raises:
            ValueError: Se origem ou destino não existirem no grafo
        """
        if origem not in self.vertices:
            raise ValueError(f"Vértice de origem '{origem}' não existe no grafo")
        if destino not in self.vertices:
            raise ValueError(f"Vértice de destino '{destino}' não existe no grafo")
            
        # Inicialização
        distancias = {vertice: sys.maxsize for vertice in self.vertices}
        distancias[origem] = 0
        
        # Para reconstruir o caminho
        predecessores = {vertice: None for vertice in self.vertices}
        
        # Heap para fila de prioridade: (distância, vértice)
        heap = [(0, origem)]
        
        # Conjunto de vértices processados
        processados = set()
        
        print(f"Iniciando Dijkstra Otimizado de '{origem}' para '{destino}'")
        print("Usando heap para fila de prioridade")
        
        # Algoritmo principal
        while heap:
            # Obtém o vértice com menor distância
            distancia_atual, atual = heapq.heappop(heap)
            
            # Se já processamos este vértice, ignora
            if atual in processados:
                continue
                
            # Marca como processado
            processados.add(atual)
            
            print(f"\nProcessando vértice: {atual} (distância: {distancia_atual})")
            
            # Se chegamos ao destino, podemos parar (otimização)
            if atual == destino:
                print("Destino alcançado! Parando busca.")
                break
                
            # Relaxa todas as arestas do vértice atual
            for vizinho, peso in self.vertices[atual]:
                if vizinho not in processados:
                    nova_distancia = distancia_atual + peso
                    
                    if nova_distancia < distancias[vizinho]:
                        print(f"  Relaxando {vizinho}: {distancias[vizinho]} -> {nova_distancia}")
                        distancias[vizinho] = nova_distancia
                        predecessores[vizinho] = atual
                        
                        # Adiciona à heap com nova distância
                        heapq.heappush(heap, (nova_distancia, vizinho))
                        
        # Reconstrói o caminho
        caminho = []
        if distancias[destino] != sys.maxsize:
            atual = destino
            while atual is not None:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            
        return distancias[destino], caminho
        
    def dijkstra_todos_caminhos(self, origem: str) -> Dict[str, Tuple[float, List[str]]]:
        """
        Calcula os caminhos mais curtos da origem para todos os outros vértices.
        
        Args:
            origem: Vértice de origem
            
        Returns:
            Dicionário com {destino: (distância, caminho)} para todos os vértices
        """
        if origem not in self.vertices:
            raise ValueError(f"Vértice de origem '{origem}' não existe no grafo")
            
        # Inicialização
        distancias = {vertice: sys.maxsize for vertice in self.vertices}
        distancias[origem] = 0
        
        # Para reconstruir os caminhos
        predecessores = {vertice: None for vertice in self.vertices}
        
        # Heap para fila de prioridade
        heap = [(0, origem)]
        processados = set()
        
        print(f"Calculando todos os caminhos a partir de '{origem}'")
        
        # Algoritmo principal
        while heap:
            distancia_atual, atual = heapq.heappop(heap)
            
            if atual in processados:
                continue
                
            processados.add(atual)
            
            # Relaxa todas as arestas
            for vizinho, peso in self.vertices[atual]:
                if vizinho not in processados:
                    nova_distancia = distancia_atual + peso
                    
                    if nova_distancia < distancias[vizinho]:
                        distancias[vizinho] = nova_distancia
                        predecessores[vizinho] = atual
                        heapq.heappush(heap, (nova_distancia, vizinho))
                        
        # Reconstrói todos os caminhos
        resultados = {}
        for destino in self.vertices:
            if destino != origem:
                caminho = []
                if distancias[destino] != sys.maxsize:
                    atual = destino
                    while atual is not None:
                        caminho.append(atual)
                        atual = predecessores[atual]
                    caminho.reverse()
                    
                resultados[destino] = (distancias[destino], caminho)
                
        return resultados
        
    def imprimir_grafo(self) -> None:
        """
        Imprime uma representação do grafo.
        """
        print("Representação do Grafo:")
        for vertice in sorted(self.vertices.keys()):
            vizinhos = ", ".join([f"{v}({p})" for v, p in self.vertices[vertice]])
            print(f"  {vertice} -> {vizinhos if vizinhos else 'sem conexões'}")


def exemplo_performance():
    """
    Exemplo demonstrando a performance da versão otimizada.
    """
    print("=== Exemplo de Performance - Dijkstra Otimizado ===\n")
    
    # Cria um grafo maior para demonstrar a eficiência
    grafo = GrafoDijkstraOtimizado()
    
    # Cria uma estrutura de grafo em grade
    tamanho = 5
    for i in range(tamanho):
        for j in range(tamanho):
            vertice = f"v{i}{j}"
            
            # Conecta com vizinhos (direita e baixo)
            if j < tamanho - 1:  # Conecta à direita
                grafo.adicionar_aresta(vertice, f"v{i}{j+1}", 1)
            if i < tamanho - 1:  # Conecta para baixo
                grafo.adicionar_aresta(vertice, f"v{i+1}{j}", 1)
                
    # Adiciona algumas arestas diagonais com peso maior
    for i in range(tamanho - 1):
        for j in range(tamanho - 1):
            grafo.adicionar_aresta(f"v{i}{j}", f"v{i+1}{j+1}", 1.5)
            
    print(f"Grafo criado com {len(grafo.vertices)} vértices")
    
    # Teste de caminho específico
    origem = "v00"
    destino = "v44"
    
    print(f"\nBuscando caminho de {origem} para {destino}:")
    print("=" * 50)
    
    distancia, caminho = grafo.dijkstra_otimizado(origem, destino)
    
    print("\nResultado:")
    if caminho:
        print(f"Caminho: {' -> '.join(caminho)}")
        print(f"Distância total: {distancia}")
    else:
        print("Não há caminho entre os vértices.")


def exemplo_todos_caminhos():
    """
    Exemplo demonstrando o cálculo de todos os caminhos.
    """
    print("\n" + "="*60)
    print("=== Exemplo - Todos os Caminhos ===")
    print("="*60 + "\n")
    
    # Cria um grafo pequeno para demonstrar
    grafo = GrafoDijkstraOtimizado()
    
    # Adiciona um hub central
    grafo.adicionar_aresta("Hub", "A", 2)
    grafo.adicionar_aresta("Hub", "B", 1)
    grafo.adicionar_aresta("Hub", "C", 3)
    grafo.adicionar_aresta("A", "D", 1)
    grafo.adicionar_aresta("B", "D", 2)
    grafo.adicionar_aresta("C", "D", 1)
    grafo.adicionar_aresta("A", "E", 4)
    grafo.adicionar_aresta("B", "E", 3)
    grafo.adicionar_aresta("D", "E", 1)
    
    grafo.imprimir_grafo()
    
    # Calcula todos os caminhos a partir do Hub
    origem = "Hub"
    todos_caminhos = grafo.dijkstra_todos_caminhos(origem)
    
    print(f"\nTodos os caminhos mais curtos a partir de '{origem}':")
    print("-" * 50)
    
    for destino, (distancia, caminho) in todos_caminhos.items():
        if caminho:
            print(f"{destino}: {' -> '.join(caminho)} (distância: {distancia})")
        else:
            print(f"{destino}: sem caminho")


def comparacao_algoritmos():
    """
    Demonstra a diferença entre as versões básica e otimizada.
    """
    print("\n" + "="*60)
    print("=== Comparação: Básico vs Otimizado ===")
    print("="*60)
    
    print("\nCaracterísticas da versão BÁSICA:")
    print("- Usa lista simples para encontrar vértice com menor distância")
    print("- Complexidade: O(V²)")
    print("- Mais didática e fácil de entender")
    print("- Processa todos os vértices")
    
    print("\nCaracterísticas da versão OTIMIZADA:")
    print("- Usa heap (fila de prioridade) para eficiência")
    print("- Complexidade: O((V + E) log V)")
    print("- Mais eficiente para grafos grandes")
    print("- Parada antecipada quando destino é encontrado")
    print("- Função adicional para todos os caminhos")
    
    print("\nRecomendação:")
    print("- Use a versão BÁSICA para aprender os conceitos")
    print("- Use a versão OTIMIZADA em aplicações reais")


if __name__ == "__main__":
    exemplo_performance()
    exemplo_todos_caminhos()
    comparacao_algoritmos()
