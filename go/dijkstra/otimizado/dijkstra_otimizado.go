package main

import (
	"container/heap"
	"fmt"
	"math"
)

// Edge representa uma aresta com peso
type Edge struct {
	to     int
	weight int
}

// WeightedGraph representa um grafo ponderado usando lista de adjacência
type WeightedGraph struct {
	vertices int
	adjList  [][]Edge
}

// NewWeightedGraph cria um novo grafo ponderado
func NewWeightedGraph(vertices int) *WeightedGraph {
	return &WeightedGraph{
		vertices: vertices,
		adjList:  make([][]Edge, vertices),
	}
}

// AddEdge adiciona uma aresta ponderada
func (g *WeightedGraph) AddEdge(from, to, weight int) {
	g.adjList[from] = append(g.adjList[from], Edge{to, weight})
}

// PriorityQueue implementa uma fila de prioridade usando heap
// Otimização: O(log V) para inserção e remoção vs O(V) na versão básica
type PriorityQueue []*Item

type Item struct {
	vertex   int
	distance int
	index    int
}

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].distance < pq[j].distance
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

// Dijkstra encontra os caminhos mais curtos de um vértice para todos os outros
// Complexidade: O((V + E) log V) com heap vs O(V²) na versão básica
func (g *WeightedGraph) Dijkstra(start int) ([]int, []int) {
	const INF = math.MaxInt32

	distances := make([]int, g.vertices)
	previous := make([]int, g.vertices)
	visited := make([]bool, g.vertices)

	// Inicializa distâncias
	for i := 0; i < g.vertices; i++ {
		distances[i] = INF
		previous[i] = -1
	}
	distances[start] = 0

	// Cria fila de prioridade otimizada com heap
	pq := make(PriorityQueue, 0, g.vertices)
	heap.Init(&pq)
	heap.Push(&pq, &Item{vertex: start, distance: 0})

	for pq.Len() > 0 {
		// Extrai o vértice com menor distância (O(log V))
		current := heap.Pop(&pq).(*Item)
		currentVertex := current.vertex

		// Skip se já foi processado (pode haver duplicatas na fila)
		if visited[currentVertex] {
			continue
		}

		visited[currentVertex] = true

		// Relaxa todas as arestas adjacentes
		for _, edge := range g.adjList[currentVertex] {
			neighbor := edge.to
			newDistance := distances[currentVertex] + edge.weight

			// Relaxamento: tenta melhorar a distância
			if newDistance < distances[neighbor] {
				distances[neighbor] = newDistance
				previous[neighbor] = currentVertex
				// Adiciona à fila de prioridade (O(log V))
				heap.Push(&pq, &Item{vertex: neighbor, distance: newDistance})
			}
		}
	}

	return distances, previous
}

// DijkstraOptimized versão que para quando encontra o destino específico
// Útil quando só queremos o caminho para um vértice específico
func (g *WeightedGraph) DijkstraOptimized(start, end int) (int, []int) {
	const INF = math.MaxInt32

	if start == end {
		return 0, []int{start}
	}

	distances := make([]int, g.vertices)
	previous := make([]int, g.vertices)
	visited := make([]bool, g.vertices)

	for i := 0; i < g.vertices; i++ {
		distances[i] = INF
		previous[i] = -1
	}
	distances[start] = 0

	pq := make(PriorityQueue, 0, g.vertices)
	heap.Init(&pq)
	heap.Push(&pq, &Item{vertex: start, distance: 0})

	for pq.Len() > 0 {
		current := heap.Pop(&pq).(*Item)
		currentVertex := current.vertex

		if visited[currentVertex] {
			continue
		}

		visited[currentVertex] = true

		// Otimização: para quando encontra o destino
		if currentVertex == end {
			break
		}

		for _, edge := range g.adjList[currentVertex] {
			neighbor := edge.to
			newDistance := distances[currentVertex] + edge.weight

			if newDistance < distances[neighbor] {
				distances[neighbor] = newDistance
				previous[neighbor] = currentVertex
				heap.Push(&pq, &Item{vertex: neighbor, distance: newDistance})
			}
		}
	}

	path := g.GetPath(previous, start, end)
	return distances[end], path
}

// GetPath reconstrói o caminho de start para end
func (g *WeightedGraph) GetPath(previous []int, start, end int) []int {
	if previous[end] == -1 && start != end {
		return nil // Não há caminho
	}

	path := make([]int, 0)
	current := end

	for current != -1 {
		path = append([]int{current}, path...)
		current = previous[current]
	}

	return path
}

// DisplayGraph exibe a representação da lista de adjacência
func (g *WeightedGraph) DisplayGraph() {
	fmt.Println("Grafo (Lista de Adjacência):")
	for i := 0; i < g.vertices; i++ {
		fmt.Printf("Vértice %d: ", i)
		for _, edge := range g.adjList[i] {
			fmt.Printf("->(%d,%d) ", edge.to, edge.weight)
		}
		fmt.Println()
	}
	fmt.Println()
}

// BenchmarkComparison compara diferentes versões do algoritmo
func (g *WeightedGraph) BenchmarkComparison(start int) {
	fmt.Println("=== Comparação de Performance ===")

	fmt.Println("Executando Dijkstra otimizado...")
	distances, previous := g.Dijkstra(start)

	fmt.Printf("Resultados para vértice %d:\n", start)
	for i := 0; i < g.vertices; i++ {
		if distances[i] != math.MaxInt32 {
			path := g.GetPath(previous, start, i)
			fmt.Printf("  Para %d: distância %d, caminho %v\n", i, distances[i], path)
		} else {
			fmt.Printf("  Para %d: INALCANÇÁVEL\n", i)
		}
	}
}

// Exemplo de uso
func main() {
	fmt.Println("=== Algoritmo de Dijkstra - Versão Otimizada ===")

	// Cria um grafo maior para demonstrar as otimizações
	g := NewWeightedGraph(8)

	// Adiciona arestas para criar um grafo mais complexo
	g.AddEdge(0, 1, 4)
	g.AddEdge(0, 2, 2)
	g.AddEdge(1, 2, 1)
	g.AddEdge(1, 3, 5)
	g.AddEdge(2, 3, 8)
	g.AddEdge(2, 4, 10)
	g.AddEdge(3, 4, 2)
	g.AddEdge(3, 5, 6)
	g.AddEdge(4, 5, 3)
	g.AddEdge(0, 6, 8)
	g.AddEdge(6, 7, 1)
	g.AddEdge(5, 7, 4)

	g.DisplayGraph()

	fmt.Println("1. Dijkstra completo (todos os caminhos):")
	g.BenchmarkComparison(0)

	fmt.Println("\n2. Dijkstra otimizado (caminho específico):")
	distance, path := g.DijkstraOptimized(0, 7)
	fmt.Printf("De 0 para 7: distância = %d, caminho = %v\n", distance, path)

	fmt.Println("\n=== Otimizações Implementadas ===")
	fmt.Println("1. Lista de Adjacência: O(V + E) espaço vs O(V²) matriz")
	fmt.Println("2. Heap (Priority Queue): O(log V) vs O(V) para encontrar mínimo")
	fmt.Println("3. Early Termination: Para quando encontra destino específico")
	fmt.Println("4. Complexidade Total: O((V + E) log V) vs O(V²)")

	fmt.Println("\n=== Quando Usar Cada Versão ===")
	fmt.Println("Básica: Grafos pequenos, fins didáticos, todos os caminhos")
	fmt.Println("Otimizada: Grafos grandes, performance crítica, busca específica")
}
