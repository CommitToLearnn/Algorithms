#!/usr/bin/env python3
"""
BFS Otimizado - Implementação eficiente para produção em Python
Múltiplas variações e otimizações avançadas
"""

from collections import deque, defaultdict
from typing import List, Tuple, Optional, Dict

class OptimizedGraph:
    """Grafo otimizado usando lista de adjacência"""
    
    def __init__(self, vertices: int):
        """
        Inicializa grafo otimizado
        
        Args:
            vertices: Número de vértices do grafo
        """
        self.vertices = vertices
        # Lista de adjacência - mais eficiente que matriz para grafos esparsos
        self.adj_list = defaultdict(list)
    
    def add_edge(self, src: int, dest: int):
        """Adiciona aresta não direcionada"""
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)
    
    def bfs_complete(self, start_vertex: int) -> Tuple[List[int], List[int], List[int]]:
        """
        BFS completo que retorna visitação, distâncias e predecessores
        
        Args:
            start_vertex: Vértice inicial
            
        Returns:
            Tuple com (ordem_visitacao, distancias, predecessores)
        """
        visited = [False] * self.vertices
        distances = [-1] * self.vertices
        predecessors = [-1] * self.vertices
        visit_order = []
        
        queue = deque([start_vertex])
        visited[start_vertex] = True
        distances[start_vertex] = 0
        
        print(f"🚀 BFS otimizado a partir do vértice {start_vertex}:")
        
        while queue:
            current = queue.popleft()
            visit_order.append(current)
            
            print(f"   Visitando {current} (distância: {distances[current]})")
            
            # Itera apenas sobre vizinhos reais (otimização)
            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distances[neighbor] = distances[current] + 1
                    predecessors[neighbor] = current
                    queue.append(neighbor)
                    print(f"     → Descoberto {neighbor} (distância: {distances[neighbor]})")
        
        return visit_order, distances, predecessors
    
    def bfs_path(self, start: int, target: int) -> Optional[List[int]]:
        """
        Encontra caminho mais curto entre dois vértices (early termination)
        
        Args:
            start: Vértice inicial
            target: Vértice alvo
            
        Returns:
            Caminho mais curto ou None se não existe
        """
        if start == target:
            return [start]
        
        visited = [False] * self.vertices
        predecessors = [-1] * self.vertices
        
        queue = deque([start])
        visited[start] = True
        
        while queue:
            current = queue.popleft()
            
            # Early termination - para quando encontra o alvo
            if current == target:
                # Reconstrói caminho
                path = []
                curr = target
                while curr != -1:
                    path.append(curr)
                    curr = predecessors[curr]
                return path[::-1]  # Inverte o caminho
            
            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    predecessors[neighbor] = current
                    queue.append(neighbor)
        
        return None  # Caminho não encontrado
    
    def bfs_levels(self, start_vertex: int) -> List[List[int]]:
        """
        Organiza vértices por níveis de distância
        
        Returns:
            Lista de listas, onde cada sublista contém vértices do mesmo nível
        """
        if start_vertex >= self.vertices:
            return []
        
        visited = [False] * self.vertices
        levels = []
        
        queue = deque([start_vertex])
        visited[start_vertex] = True
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Processa todos os vértices do nível atual
            for _ in range(level_size):
                current = queue.popleft()
                current_level.append(current)
                
                # Adiciona vizinhos ao próximo nível
                for neighbor in self.adj_list[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            levels.append(current_level)
        
        return levels
    
    def is_connected(self) -> bool:
        """Verifica se o grafo é conectado usando BFS"""
        if self.vertices == 0:
            return True
        
        visited = [False] * self.vertices
        queue = deque([0])
        visited[0] = True
        visited_count = 1
        
        while queue:
            current = queue.popleft()
            
            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    visited_count += 1
                    queue.append(neighbor)
        
        return visited_count == self.vertices
    
    def find_components(self) -> List[List[int]]:
        """Encontra todos os componentes conectados"""
        visited = [False] * self.vertices
        components = []
        
        for vertex in range(self.vertices):
            if not visited[vertex]:
                component = []
                queue = deque([vertex])
                visited[vertex] = True
                
                while queue:
                    current = queue.popleft()
                    component.append(current)
                    
                    for neighbor in self.adj_list[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                components.append(sorted(component))
        
        return components
    
    def bfs_bipartite_check(self) -> Tuple[bool, List[int]]:
        """
        Verifica se o grafo é bipartido usando BFS
        
        Returns:
            Tuple (é_bipartido, coloração)
        """
        color = [-1] * self.vertices
        
        for start in range(self.vertices):
            if color[start] == -1:
                queue = deque([start])
                color[start] = 0
                
                while queue:
                    current = queue.popleft()
                    
                    for neighbor in self.adj_list[current]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False, color
        
        return True, color
    
    def shortest_paths_all(self, start: int) -> Dict[int, List[int]]:
        """
        Encontra caminhos mais curtos para todos os vértices alcançáveis
        
        Returns:
            Dicionário {destino: caminho}
        """
        _, distances, predecessors = self.bfs_complete(start)
        paths = {}
        
        for vertex in range(self.vertices):
            if distances[vertex] != -1:  # Vértice alcançável
                path = []
                current = vertex
                while current != -1:
                    path.append(current)
                    current = predecessors[current]
                paths[vertex] = path[::-1]
        
        return paths
    
    def get_stats(self) -> Dict:
        """Retorna estatísticas do grafo"""
        total_edges = sum(len(neighbors) for neighbors in self.adj_list.values()) // 2
        components = self.find_components()
        is_bipartite, _ = self.bfs_bipartite_check()
        
        return {
            'vertices': self.vertices,
            'edges': total_edges,
            'density': total_edges / (self.vertices * (self.vertices - 1) / 2) if self.vertices > 1 else 0,
            'connected': self.is_connected(),
            'components': len(components),
            'component_sizes': [len(comp) for comp in components],
            'bipartite': is_bipartite,
            'avg_degree': (2 * total_edges) / self.vertices if self.vertices > 0 else 0
        }
    
    def display_adjacency_list(self):
        """Exibe lista de adjacência"""
        print("📊 Lista de Adjacência:")
        for vertex in range(self.vertices):
            neighbors = self.adj_list[vertex] if vertex in self.adj_list else []
            print(f"   Vértice {vertex}: {sorted(neighbors)}")
        print()


def benchmark_comparison():
    """Demonstra diferenças de performance entre implementações"""
    print("⚡ Comparação de Performance:")
    
    # Cria grafo maior para demonstrar eficiência
    g = OptimizedGraph(10)
    
    # Adiciona muitas arestas
    edges = [
        (0, 1), (0, 2), (0, 3),
        (1, 4), (1, 5),
        (2, 6), (2, 7),
        (3, 8), (3, 9),
        (4, 5), (6, 7), (8, 9)
    ]
    
    for src, dest in edges:
        g.add_edge(src, dest)
    
    print(f"   Grafo com {g.vertices} vértices e {len(edges)} arestas")
    
    # Demonstra diferentes operações
    print(f"   Conectado: {g.is_connected()}")
    
    components = g.find_components()
    print(f"   Componentes: {len(components)}")
    
    is_bip, _ = g.bfs_bipartite_check()
    print(f"   Bipartido: {is_bip}")
    
    levels = g.bfs_levels(0)
    print(f"   Níveis a partir de 0: {len(levels)}")
    
    return g


def main():
    """Função principal com demonstrações avançadas"""
    print("=" * 60)
    print("         BFS OTIMIZADO EM PYTHON")
    print("=" * 60)
    
    # Criar grafo de exemplo
    print("\n🏗️  Construindo grafo otimizado...")
    g = OptimizedGraph(8)
    
    edges = [
        (0, 1), (0, 2),
        (1, 3), (2, 4),
        (3, 5), (4, 5),
        (5, 6), (6, 7)
    ]
    
    for src, dest in edges:
        g.add_edge(src, dest)
        print(f"   Aresta {src} ↔ {dest}")
    
    g.display_adjacency_list()
    
    # Estatísticas do grafo
    stats = g.get_stats()
    print("📈 Estatísticas:")
    for key, value in stats.items():
        print(f"   {key}: {value}")
    print()
    
    # 1. BFS completo
    print("1️⃣  BFS Completo:")
    visit_order, distances, _ = g.bfs_complete(0)
    print(f"   Ordem: {visit_order}")
    print(f"   Distâncias: {distances}")
    print()
    
    # 2. Busca de caminho otimizada
    print("2️⃣  Busca de Caminho (Early Termination):")
    path = g.bfs_path(0, 7)
    if path:
        print(f"   Caminho 0→7: {' → '.join(map(str, path))} (comprimento: {len(path)-1})")
    print()
    
    # 3. Organização por níveis
    print("3️⃣  Vértices por Níveis:")
    levels = g.bfs_levels(0)
    for i, level in enumerate(levels):
        print(f"   Nível {i}: {level}")
    print()
    
    # 4. Análise de componentes
    print("4️⃣  Análise de Componentes:")
    components = g.find_components()
    for i, comp in enumerate(components):
        print(f"   Componente {i+1}: {comp}")
    print()
    
    # 5. Verificação bipartida
    print("5️⃣  Verificação de Grafo Bipartido:")
    is_bipartite, coloring = g.bfs_bipartite_check()
    print(f"   É bipartido: {is_bipartite}")
    if is_bipartite:
        set_a = [i for i, color in enumerate(coloring) if color == 0 and i < len(coloring)]
        set_b = [i for i, color in enumerate(coloring) if color == 1 and i < len(coloring)]
        print(f"   Conjunto A: {set_a}")
        print(f"   Conjunto B: {set_b}")
    print()
    
    # 6. Benchmark
    print("6️⃣  Teste de Performance:")
    benchmark_comparison()
    print()
    
    print("=" * 60)
    print("✅ Otimizações Implementadas:")
    print("• Lista de adjacência (O(V+E) vs O(V²) espaço)")
    print("• deque para fila eficiente (O(1) append/popleft)")
    print("• Early termination para busca de caminhos")
    print("• Type hints para melhor legibilidade")
    print("• Múltiplas variações especializadas")
    print("• Análise avançada de propriedades do grafo")
    print("=" * 60)


if __name__ == "__main__":
    main()
