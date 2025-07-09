package main

import (
	"container/list"
	"fmt"
)

// OptimizedGraph representa um grafo usando lista de adjacência
type OptimizedGraph struct {
	vertices int
	adjList  [][]int // Lista de adjacência (mais eficiente que matriz)
}

// NewOptimizedGraph cria um novo grafo otimizado
func NewOptimizedGraph(vertices int) *OptimizedGraph {
	return &OptimizedGraph{
		vertices: vertices,
		adjList:  make([][]int, vertices),
	}
}

// AddEdge adiciona uma aresta (não direcionada)
func (g *OptimizedGraph) AddEdge(src, dest int) {
	g.adjList[src] = append(g.adjList[src], dest)
	g.adjList[dest] = append(g.adjList[dest], src) // Grafo não direcionado
}

// BFS executa busca em largura otimizada
// Retorna: slice com ordem de visitação, distâncias, e predecessores
func (g *OptimizedGraph) BFS(startVertex int) ([]int, []int, []int) {
	visited := make([]bool, g.vertices)
	distances := make([]int, g.vertices)
	predecessors := make([]int, g.vertices)
	visitOrder := make([]int, 0, g.vertices)

	// Inicializa distâncias e predecessores
	for i := 0; i < g.vertices; i++ {
		distances[i] = -1    // -1 indica não alcançado
		predecessors[i] = -1 // -1 indica sem predecessor
	}

	// Usa container/list para fila eficiente (O(1) para push/pop)
	queue := list.New()
	queue.PushBack(startVertex)
	visited[startVertex] = true
	distances[startVertex] = 0

	fmt.Printf("🚀 BFS otimizado a partir do vértice %d:\n", startVertex)

	for queue.Len() > 0 {
		// Remove da frente da fila (O(1))
		element := queue.Front()
		current := element.Value.(int)
		queue.Remove(element)

		visitOrder = append(visitOrder, current)
		fmt.Printf("   Visitando vértice %d (distância: %d)\n", current, distances[current])

		// Visita todos os vizinhos
		for _, neighbor := range g.adjList[current] {
			if !visited[neighbor] {
				visited[neighbor] = true
				distances[neighbor] = distances[current] + 1
				predecessors[neighbor] = current
				queue.PushBack(neighbor)
				fmt.Printf("     → Descoberto vizinho %d (distância: %d)\n",
					neighbor, distances[neighbor])
			}
		}
	}

	return visitOrder, distances, predecessors
}

// BFSPath encontra o caminho mais curto entre dois vértices
func (g *OptimizedGraph) BFSPath(start, target int) ([]int, bool) {
	if start == target {
		return []int{start}, true
	}

	visited := make([]bool, g.vertices)
	predecessors := make([]int, g.vertices)

	for i := 0; i < g.vertices; i++ {
		predecessors[i] = -1
	}

	queue := list.New()
	queue.PushBack(start)
	visited[start] = true

	for queue.Len() > 0 {
		element := queue.Front()
		current := element.Value.(int)
		queue.Remove(element)

		// Se encontrou o alvo, reconstrói o caminho
		if current == target {
			path := make([]int, 0)
			for curr := target; curr != -1; curr = predecessors[curr] {
				path = append([]int{curr}, path...)
			}
			return path, true
		}

		for _, neighbor := range g.adjList[current] {
			if !visited[neighbor] {
				visited[neighbor] = true
				predecessors[neighbor] = current
				queue.PushBack(neighbor)
			}
		}
	}

	return nil, false // Caminho não encontrado
}

// BFSLevels organiza vértices por níveis de distância
func (g *OptimizedGraph) BFSLevels(startVertex int) [][]int {
	visited := make([]bool, g.vertices)
	levels := make([][]int, 0)

	queue := list.New()
	queue.PushBack(startVertex)
	visited[startVertex] = true

	for queue.Len() > 0 {
		levelSize := queue.Len()
		currentLevel := make([]int, 0, levelSize)

		// Processa todos os vértices do nível atual
		for i := 0; i < levelSize; i++ {
			element := queue.Front()
			current := element.Value.(int)
			queue.Remove(element)

			currentLevel = append(currentLevel, current)

			// Adiciona vizinhos não visitados à próxima camada
			for _, neighbor := range g.adjList[current] {
				if !visited[neighbor] {
					visited[neighbor] = true
					queue.PushBack(neighbor)
				}
			}
		}

		levels = append(levels, currentLevel)
	}

	return levels
}

// IsConnected verifica se o grafo é conectado usando BFS
func (g *OptimizedGraph) IsConnected() bool {
	if g.vertices == 0 {
		return true
	}

	visited := make([]bool, g.vertices)
	queue := list.New()
	queue.PushBack(0)
	visited[0] = true
	visitedCount := 1

	for queue.Len() > 0 {
		element := queue.Front()
		current := element.Value.(int)
		queue.Remove(element)

		for _, neighbor := range g.adjList[current] {
			if !visited[neighbor] {
				visited[neighbor] = true
				visitedCount++
				queue.PushBack(neighbor)
			}
		}
	}

	return visitedCount == g.vertices
}

// FindComponentes encontra todos os componentes conectados
func (g *OptimizedGraph) FindComponents() [][]int {
	visited := make([]bool, g.vertices)
	components := make([][]int, 0)

	for v := 0; v < g.vertices; v++ {
		if !visited[v] {
			component := make([]int, 0)
			queue := list.New()
			queue.PushBack(v)
			visited[v] = true

			for queue.Len() > 0 {
				element := queue.Front()
				current := element.Value.(int)
				queue.Remove(element)

				component = append(component, current)

				for _, neighbor := range g.adjList[current] {
					if !visited[neighbor] {
						visited[neighbor] = true
						queue.PushBack(neighbor)
					}
				}
			}

			components = append(components, component)
		}
	}

	return components
}

// Display mostra a lista de adjacência
func (g *OptimizedGraph) Display() {
	fmt.Println("📊 Lista de Adjacência:")
	for i := 0; i < g.vertices; i++ {
		fmt.Printf("   Vértice %d: %v\n", i, g.adjList[i])
	}
	fmt.Println()
}

// GetStats retorna estatísticas do grafo
func (g *OptimizedGraph) GetStats() map[string]interface{} {
	totalEdges := 0
	for _, adj := range g.adjList {
		totalEdges += len(adj)
	}
	totalEdges /= 2 // Cada aresta é contada duas vezes (grafo não direcionado)

	components := g.FindComponents()

	return map[string]interface{}{
		"vertices":   g.vertices,
		"edges":      totalEdges,
		"density":    float64(totalEdges) / float64(g.vertices*(g.vertices-1)/2),
		"connected":  g.IsConnected(),
		"components": len(components),
		"component_sizes": func() []int {
			sizes := make([]int, len(components))
			for i, comp := range components {
				sizes[i] = len(comp)
			}
			return sizes
		}(),
	}
}

// Exemplo e benchmark
func main() {
	fmt.Println("=== BFS Otimizado ===\n")

	// Cria um grafo maior para demonstrar otimizações
	g := NewOptimizedGraph(8)

	// Adiciona arestas para formar um grafo interessante
	edges := [][]int{
		{0, 1}, {0, 2}, {1, 3}, {2, 4}, {3, 5}, {4, 5}, {5, 6}, {6, 7},
	}

	fmt.Println("🏗️  Construindo grafo:")
	for _, edge := range edges {
		g.AddEdge(edge[0], edge[1])
		fmt.Printf("   Aresta %d ↔ %d\n", edge[0], edge[1])
	}

	g.Display()

	// Estatísticas do grafo
	stats := g.GetStats()
	fmt.Printf("📈 Estatísticas do Grafo:\n")
	fmt.Printf("   Vértices: %d\n", stats["vertices"])
	fmt.Printf("   Arestas: %d\n", stats["edges"])
	fmt.Printf("   Densidade: %.3f\n", stats["density"])
	fmt.Printf("   Conectado: %t\n", stats["connected"])
	fmt.Printf("   Componentes: %d\n", stats["components"])
	fmt.Println()

	// 1. BFS básico com informações detalhadas
	fmt.Println("1️⃣  BFS Completo:")
	visitOrder, distances, predecessors := g.BFS(0)
	fmt.Printf("   Ordem de visitação: %v\n", visitOrder)
	fmt.Printf("   Distâncias: %v\n", distances)
	fmt.Printf("   Predecessores: %v\n\n", predecessors)

	// 2. Busca de caminho específico
	fmt.Println("2️⃣  Busca de Caminho:")
	if path, found := g.BFSPath(0, 6); found {
		fmt.Printf("   Caminho de 0 para 6: %v (comprimento: %d)\n", path, len(path)-1)
	} else {
		fmt.Println("   Caminho não encontrado")
	}

	if path, found := g.BFSPath(1, 7); found {
		fmt.Printf("   Caminho de 1 para 7: %v (comprimento: %d)\n", path, len(path)-1)
	} else {
		fmt.Println("   Caminho não encontrado")
	}
	fmt.Println()

	// 3. Organização por níveis
	fmt.Println("3️⃣  Vértices por Níveis:")
	levels := g.BFSLevels(0)
	for i, level := range levels {
		fmt.Printf("   Nível %d: %v\n", i, level)
	}
	fmt.Println()

	// 4. Análise de componentes
	fmt.Println("4️⃣  Componentes Conectados:")
	components := g.FindComponents()
	for i, comp := range components {
		fmt.Printf("   Componente %d: %v\n", i+1, comp)
	}
	fmt.Println()

	// 5. Demonstração com grafo desconectado
	fmt.Println("5️⃣  Testando Grafo Desconectado:")
	g2 := NewOptimizedGraph(6)
	g2.AddEdge(0, 1)
	g2.AddEdge(1, 2)
	g2.AddEdge(3, 4)
	// Vértice 5 fica isolado

	fmt.Printf("   Conectado: %t\n", g2.IsConnected())
	components2 := g2.FindComponents()
	fmt.Printf("   Componentes: %d\n", len(components2))
	for i, comp := range components2 {
		fmt.Printf("     Componente %d: %v\n", i+1, comp)
	}

	fmt.Println("\n=== Otimizações Implementadas ===")
	fmt.Println("✅ Lista de adjacência (O(V+E) vs O(V²) espaço)")
	fmt.Println("✅ Fila eficiente com container/list")
	fmt.Println("✅ Múltiplas variações de BFS especializadas")
	fmt.Println("✅ Análise de componentes e conectividade")
	fmt.Println("✅ Busca de caminhos específicos")
	fmt.Println("✅ Estatísticas detalhadas do grafo")
}
