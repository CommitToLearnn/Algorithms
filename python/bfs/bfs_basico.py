#!/usr/bin/env python3
"""
BFS Básico - Implementação simples e didática em Python
Foco no entendimento do algoritmo
"""

from collections import deque

class Graph:
    """Grafo simples usando matriz de adjacência"""
    
    def __init__(self, vertices):
        """Inicializa grafo com número de vértices especificado"""
        self.vertices = vertices
        # Matriz de adjacência inicializada com False
        self.adj_matrix = [[False for _ in range(vertices)] for _ in range(vertices)]
    
    def add_edge(self, src, dest):
        """Adiciona uma aresta não direcionada entre src e dest"""
        self.adj_matrix[src][dest] = True
        self.adj_matrix[dest][src] = True  # Grafo não direcionado
    
    def bfs(self, start_vertex):
        """
        Executa busca em largura básica a partir do vértice inicial
        
        Args:
            start_vertex: Vértice de onde iniciar a busca
            
        Returns:
            Lista com a ordem de visitação dos vértices
        """
        # Lista para marcar vértices visitados
        visited = [False] * self.vertices
        
        # Fila para BFS - usando deque para eficiência
        queue = deque([start_vertex])
        visited[start_vertex] = True
        
        # Lista para armazenar ordem de visitação
        visit_order = []
        
        print(f"🚀 BFS a partir do vértice {start_vertex}:")
        
        while queue:
            # Remove o primeiro elemento da fila (FIFO)
            current = queue.popleft()
            visit_order.append(current)
            
            print(f"   Visitando vértice {current}")
            
            # Verifica todos os possíveis vizinhos
            for neighbor in range(self.vertices):
                # Se existe aresta e o vizinho não foi visitado
                if self.adj_matrix[current][neighbor] and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    print(f"     → Adicionado à fila: {neighbor}")
        
        return visit_order
    
    def bfs_with_distances(self, start_vertex):
        """
        BFS que também calcula distâncias mínimas
        
        Returns:
            tuple: (ordem_visitacao, distancias, predecessores)
        """
        visited = [False] * self.vertices
        distances = [-1] * self.vertices  # -1 indica não alcançado
        predecessors = [-1] * self.vertices  # -1 indica sem predecessor
        
        queue = deque([start_vertex])
        visited[start_vertex] = True
        distances[start_vertex] = 0
        
        visit_order = []
        
        print(f"\n🔍 BFS com distâncias a partir do vértice {start_vertex}:")
        
        while queue:
            current = queue.popleft()
            visit_order.append(current)
            
            print(f"   Processando vértice {current} (distância: {distances[current]})")
            
            for neighbor in range(self.vertices):
                if self.adj_matrix[current][neighbor] and not visited[neighbor]:
                    visited[neighbor] = True
                    distances[neighbor] = distances[current] + 1
                    predecessors[neighbor] = current
                    queue.append(neighbor)
                    print(f"     → Descoberto {neighbor} (distância: {distances[neighbor]})")
        
        return visit_order, distances, predecessors
    
    def find_path(self, start, end):
        """
        Encontra caminho mais curto entre dois vértices usando BFS
        
        Returns:
            list: Caminho do start ao end, ou None se não existe
        """
        if start == end:
            return [start]
        
        _, _, predecessors = self.bfs_with_distances(start)
        
        # Se end não foi alcançado
        if predecessors[end] == -1:
            return None
        
        # Reconstrói o caminho de trás para frente
        path = []
        current = end
        while current != -1:
            path.append(current)
            current = predecessors[current]
        
        # Inverte para ter o caminho correto
        path.reverse()
        return path
    
    def display_matrix(self):
        """Exibe a matriz de adjacência de forma legível"""
        print("\n📊 Matriz de Adjacência:")
        print("     ", end="")
        for i in range(self.vertices):
            print(f"{i:3}", end="")
        print()
        
        for i in range(self.vertices):
            print(f"{i:3}: ", end="")
            for j in range(self.vertices):
                print("1  " if self.adj_matrix[i][j] else "0  ", end="")
            print()
        print()
    
    def get_neighbors(self, vertex):
        """Retorna lista de vizinhos de um vértice"""
        neighbors = []
        for i in range(self.vertices):
            if self.adj_matrix[vertex][i]:
                neighbors.append(i)
        return neighbors


def main():
    """Função principal com exemplo de uso"""
    print("=" * 50)
    print("    BFS BÁSICO EM PYTHON")
    print("=" * 50)
    
    # Criar um grafo pequeno para demonstração
    print("\n🏗️  Criando grafo com 6 vértices...")
    g = Graph(6)
    
    # Adicionar arestas para formar um grafo interessante
    edges = [
        (0, 1), (0, 2),
        (1, 3), (1, 4),
        (2, 4), (2, 5),
        (3, 4)
    ]
    
    print("   Adicionando arestas:")
    for src, dest in edges:
        g.add_edge(src, dest)
        print(f"     {src} ↔ {dest}")
    
    # Mostrar estrutura do grafo
    g.display_matrix()
    
    # Executar BFS básico
    print("1️⃣  BFS Básico:")
    visit_order = g.bfs(0)
    print(f"   Ordem de visitação: {visit_order}")
    
    # BFS com distâncias
    print("\n2️⃣  BFS com Distâncias:")
    _, distances, predecessors = g.bfs_with_distances(0)
    print(f"   Distâncias a partir de 0: {distances}")
    print(f"   Predecessores: {predecessors}")
    
    # Demonstrar busca de caminhos
    print("\n3️⃣  Busca de Caminhos:")
    test_paths = [(0, 5), (1, 5), (0, 3)]
    
    for start, end in test_paths:
        path = g.find_path(start, end)
        if path:
            print(f"   Caminho de {start} para {end}: {' → '.join(map(str, path))} (comprimento: {len(path)-1})")
        else:
            print(f"   Não há caminho de {start} para {end}")
    
    # Mostrar vizinhos de cada vértice
    print("\n4️⃣  Vizinhos de cada vértice:")
    for vertex in range(g.vertices):
        neighbors = g.get_neighbors(vertex)
        print(f"   Vértice {vertex}: {neighbors}")
    
    print("\n" + "=" * 50)
    print("💡 Conceitos Importantes:")
    print("• BFS usa FILA (FIFO) - primeiro a entrar, primeiro a sair")
    print("• Garante encontrar o CAMINHO MAIS CURTO em grafos não ponderados")
    print("• Explora vértices por NÍVEIS de distância")
    print("• Complexidade: O(V + E) onde V=vértices, E=arestas")
    print("• Útil para: pathfinding, análise de redes, componentes conectados")
    print("=" * 50)


if __name__ == "__main__":
    main()
