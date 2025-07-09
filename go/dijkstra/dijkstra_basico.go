package main

import (
	"fmt"
	"math"
)

// SimpleGraph representa um grafo simples com matriz de adjacência
type SimpleGraph struct {
	vertices int
	matrix   [][]int // Matriz de adjacência com pesos (0 = sem conexão)
}

// NewSimpleGraph cria um novo grafo simples
func NewSimpleGraph(vertices int) *SimpleGraph {
	matrix := make([][]int, vertices)
	for i := range matrix {
		matrix[i] = make([]int, vertices)
	}

	return &SimpleGraph{
		vertices: vertices,
		matrix:   matrix,
	}
}

// AddEdge adiciona uma aresta com peso
func (g *SimpleGraph) AddEdge(from, to, weight int) {
	g.matrix[from][to] = weight
}

// DijkstraBasico implementa o algoritmo de Dijkstra de forma didática
// Complexidade: O(V²) onde V é o número de vértices
func (g *SimpleGraph) DijkstraBasico(start int) ([]int, []int) {
	const INF = math.MaxInt32 // Representa infinito

	// Arrays para armazenar resultados
	distances := make([]int, g.vertices) // Menor distância até cada vértice
	previous := make([]int, g.vertices)  // Vértice anterior no caminho mais curto
	visited := make([]bool, g.vertices)  // Controla quais vértices já foram processados

	// Inicialização
	fmt.Println("=== Inicialização ===")
	for i := 0; i < g.vertices; i++ {
		distances[i] = INF // Todas as distâncias começam como infinito
		previous[i] = -1   // Nenhum vértice anterior inicialmente
		visited[i] = false // Nenhum vértice foi visitado
	}
	distances[start] = 0 // Distância do vértice inicial para ele mesmo é 0

	fmt.Printf("Vértice inicial: %d\n", start)
	fmt.Printf("Distâncias iniciais: %v\n\n", distances)

	// Algoritmo principal: processa cada vértice
	for count := 0; count < g.vertices; count++ {
		fmt.Printf("=== Iteração %d ===\n", count+1)

		// Encontra o vértice não visitado com menor distância
		minDistance := INF
		minVertex := -1

		for v := 0; v < g.vertices; v++ {
			if !visited[v] && distances[v] < minDistance {
				minDistance = distances[v]
				minVertex = v
			}
		}

		// Se não encontrou vértice alcançável, termina
		if minVertex == -1 {
			fmt.Println("Não há mais vértices alcançáveis")
			break
		}

		fmt.Printf("Processando vértice %d (distância: %d)\n", minVertex, distances[minVertex])

		// Marca como visitado
		visited[minVertex] = true

		// Relaxa todas as arestas saindo do vértice atual
		fmt.Printf("Verificando vizinhos de %d:\n", minVertex)
		for neighbor := 0; neighbor < g.vertices; neighbor++ {
			// Se existe aresta e o vizinho não foi visitado
			if g.matrix[minVertex][neighbor] > 0 && !visited[neighbor] {
				// Calcula nova distância passando pelo vértice atual
				newDistance := distances[minVertex] + g.matrix[minVertex][neighbor]

				fmt.Printf("  Vizinho %d: distância atual = %d, nova = %d",
					neighbor, distances[neighbor], newDistance)

				// Se a nova distância é melhor, atualiza
				if newDistance < distances[neighbor] {
					distances[neighbor] = newDistance
					previous[neighbor] = minVertex
					fmt.Printf(" -> ATUALIZADO!")
				}
				fmt.Println()
			}
		}

		fmt.Printf("Distâncias após iteração: %v\n\n", distances)
	}

	return distances, previous
}

// GetPath reconstrói o caminho mais curto do start ao end
func (g *SimpleGraph) GetPath(previous []int, start, end int) []int {
	// Se não há caminho para o destino
	if previous[end] == -1 && start != end {
		return nil
	}

	// Reconstrói o caminho de trás para frente
	path := make([]int, 0)
	current := end

	for current != -1 {
		path = append([]int{current}, path...) // Adiciona no início
		current = previous[current]
	}

	return path
}

// DisplayMatrix exibe a matriz de adjacência
func (g *SimpleGraph) DisplayMatrix() {
	fmt.Println("\nMatriz de Adjacência:")
	fmt.Print("     ")
	for i := 0; i < g.vertices; i++ {
		fmt.Printf("%3d ", i)
	}
	fmt.Println()

	for i := 0; i < g.vertices; i++ {
		fmt.Printf("%3d: ", i)
		for j := 0; j < g.vertices; j++ {
			if g.matrix[i][j] == 0 {
				fmt.Print("  - ")
			} else {
				fmt.Printf("%3d ", g.matrix[i][j])
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

// Exemplo de uso
func main() {
	fmt.Println("=== Algoritmo de Dijkstra - Versão Básica ===")

	// Cria um grafo com 5 vértices
	g := NewSimpleGraph(5)

	// Adiciona arestas (origem, destino, peso)
	g.AddEdge(0, 1, 10)
	g.AddEdge(0, 4, 5)
	g.AddEdge(1, 2, 1)
	g.AddEdge(1, 4, 2)
	g.AddEdge(2, 3, 4)
	g.AddEdge(3, 2, 6)
	g.AddEdge(3, 0, 7)
	g.AddEdge(4, 1, 3)
	g.AddEdge(4, 2, 9)
	g.AddEdge(4, 3, 2)

	g.DisplayMatrix()

	// Executa Dijkstra a partir do vértice 0
	distances, previous := g.DijkstraBasico(0)

	// Exibe resultados
	fmt.Println("=== RESULTADOS FINAIS ===")
	fmt.Printf("Vértice de origem: 0\n\n")

	for i := 0; i < g.vertices; i++ {
		if distances[i] == math.MaxInt32 {
			fmt.Printf("Vértice %d: INALCANÇÁVEL\n", i)
		} else {
			path := g.GetPath(previous, 0, i)
			fmt.Printf("Vértice %d: distância = %d, caminho = %v\n",
				i, distances[i], path)
		}
	}

	fmt.Println("\n=== Explicação do Algoritmo ===")
	fmt.Println("1. Inicializa todas as distâncias como infinito, exceto a origem (0)")
	fmt.Println("2. Em cada iteração, escolhe o vértice não visitado com menor distância")
	fmt.Println("3. Para cada vizinho deste vértice, tenta 'relaxar' a aresta:")
	fmt.Println("   - Se (distância atual + peso da aresta) < distância do vizinho:")
	fmt.Println("   - Atualiza a distância do vizinho")
	fmt.Println("4. Marca o vértice como visitado e repete até todos serem processados")
}
