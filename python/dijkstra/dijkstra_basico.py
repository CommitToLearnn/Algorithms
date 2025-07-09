"""
Implementação Básica do Algoritmo de Dijkstra
============================================

Esta é uma implementação didática do algoritmo de Dijkstra para encontrar
o caminho mais curto entre dois vértices em um grafo ponderado.

Características desta versão:
- Usa lista simples para a fila de prioridade
- Código mais legível e fácil de entender
- Ideal para aprendizado dos conceitos básicos
- Complexidade: O(V²) onde V é o número de vértices

Autor: Algorithms Repository
Data: Julho 2025
"""

import sys
from typing import Dict, List, Tuple, Optional

class GrafoDijkstra:
    """
    Classe que representa um grafo para o algoritmo de Dijkstra.
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
        
    def obter_vertice_menor_distancia(self, distancias: Dict[str, float], visitados: set) -> Optional[str]:
        """
        Encontra o vértice não visitado com menor distância.
        
        Args:
            distancias: Dicionário com as distâncias atuais
            visitados: Conjunto de vértices já visitados
            
        Returns:
            Vértice com menor distância ou None se todos foram visitados
        """
        menor_distancia = sys.maxsize
        vertice_escolhido = None
        
        for vertice in self.vertices:
            if vertice not in visitados and distancias[vertice] < menor_distancia:
                menor_distancia = distancias[vertice]
                vertice_escolhido = vertice
                
        return vertice_escolhido
        
    def dijkstra(self, origem: str, destino: str) -> Tuple[float, List[str]]:
        """
        Executa o algoritmo de Dijkstra para encontrar o caminho mais curto.
        
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
        
        # Conjunto de vértices visitados
        visitados = set()
        
        print(f"Iniciando Dijkstra de '{origem}' para '{destino}'")
        print(f"Distâncias iniciais: {distancias}")
        
        # Algoritmo principal
        while len(visitados) < len(self.vertices):
            # Encontra o vértice não visitado com menor distância
            atual = self.obter_vertice_menor_distancia(distancias, visitados)
            
            if atual is None or distancias[atual] == sys.maxsize:
                break  # Não há mais vértices alcançáveis
                
            visitados.add(atual)
            print(f"\nVisitando vértice: {atual} (distância: {distancias[atual]})")
            
            # Se chegamos ao destino, podemos parar
            if atual == destino:
                print("Destino alcançado!")
                break
                
            # Relaxa todas as arestas do vértice atual
            for vizinho, peso in self.vertices[atual]:
                if vizinho not in visitados:
                    nova_distancia = distancias[atual] + peso
                    
                    if nova_distancia < distancias[vizinho]:
                        print(f"  Relaxando {vizinho}: {distancias[vizinho]} -> {nova_distancia}")
                        distancias[vizinho] = nova_distancia
                        predecessores[vizinho] = atual
                        
        # Reconstrói o caminho
        caminho = []
        if distancias[destino] != sys.maxsize:
            atual = destino
            while atual is not None:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            
        return distancias[destino], caminho
        
    def imprimir_grafo(self) -> None:
        """
        Imprime uma representação do grafo.
        """
        print("Representação do Grafo:")
        for vertice in sorted(self.vertices.keys()):
            vizinhos = ", ".join([f"{v}({p})" for v, p in self.vertices[vertice]])
            print(f"  {vertice} -> {vizinhos if vizinhos else 'sem conexões'}")


def exemplo_basico():
    """
    Exemplo básico de uso do algoritmo de Dijkstra.
    """
    print("=== Exemplo Básico do Algoritmo de Dijkstra ===\n")
    
    # Cria o grafo
    grafo = GrafoDijkstra()
    
    # Adiciona as arestas (representando um mapa de cidades)
    grafo.adicionar_aresta("A", "B", 4)
    grafo.adicionar_aresta("A", "C", 2)
    grafo.adicionar_aresta("B", "C", 1)
    grafo.adicionar_aresta("B", "D", 5)
    grafo.adicionar_aresta("C", "D", 8)
    grafo.adicionar_aresta("C", "E", 10)
    grafo.adicionar_aresta("D", "E", 2)
    
    grafo.imprimir_grafo()
    
    # Executa o algoritmo
    origem = "A"
    destino = "E"
    
    print(f"\nBuscando o caminho mais curto de {origem} para {destino}:")
    print("=" * 50)
    
    distancia, caminho = grafo.dijkstra(origem, destino)
    
    print("\nResultado:")
    if caminho:
        print(f"Caminho: {' -> '.join(caminho)}")
        print(f"Distância total: {distancia}")
    else:
        print("Não há caminho entre os vértices.")


def exemplo_detalhado():
    """
    Exemplo mais detalhado com múltiplas consultas.
    """
    print("\n" + "="*60)
    print("=== Exemplo Detalhado - Rede de Computadores ===")
    print("="*60 + "\n")
    
    # Cria um grafo representando uma rede de computadores
    rede = GrafoDijkstra()
    
    # Adiciona conexões (latência em ms)
    rede.adicionar_aresta("Router1", "PC_A", 1)
    rede.adicionar_aresta("Router1", "Router2", 5)
    rede.adicionar_aresta("Router1", "Router3", 3)
    rede.adicionar_aresta("Router2", "PC_B", 2)
    rede.adicionar_aresta("Router2", "Server", 4)
    rede.adicionar_aresta("Router3", "PC_C", 1)
    rede.adicionar_aresta("Router3", "Server", 6)
    rede.adicionar_aresta("PC_A", "PC_B", 10)
    
    rede.imprimir_grafo()
    
    # Testa múltiplos caminhos
    testes = [
        ("Router1", "Server"),
        ("PC_A", "PC_C"),
        ("PC_B", "PC_C")
    ]
    
    for origem, destino in testes:
        print(f"\nCalculando rota de {origem} para {destino}:")
        print("-" * 40)
        
        distancia, caminho = rede.dijkstra(origem, destino)
        
        if caminho:
            print(f"Rota: {' -> '.join(caminho)}")
            print(f"Latência total: {distancia}ms")
        else:
            print("Sem conectividade entre os dispositivos.")


if __name__ == "__main__":
    exemplo_basico()
    exemplo_detalhado()
