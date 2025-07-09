/**
 * BFS Básico - Implementação Educacional para Grafos
 * ==================================================
 *
 * Esta implementação demonstra a busca em largura (BFS) aplicada a grafos simples.
 * Foco no entendimento do algoritmo com matriz de adjacência.
 *
 * Características:
 * - Implementação simples e didática
 * - Uso de matriz de adjacência
 * - Comentários explicativos detalhados
 * - Exemplos práticos de uso
 * - Análise de complexidade incluída
 *
 * Nota: Para executar sem conflitos, use: go run bfs_basico.go
 *
 * @author matheussricardoo
 * @version 1.0
 * @since Julho 2025
 */

package main

import (
	"fmt"
)

// Graph representa um grafo simples usando matriz de adjacência
// Adequado para grafos pequenos e densos
type Graph struct {
	vertices  int      // Número de vértices
	adjMatrix [][]bool // Matriz de adjacência
}

// NewGraph cria um novo grafo com o número especificado de vértices
// Complexidade: O(V²) onde V é o número de vértices
func NewGraph(vertices int) *Graph {
	adjMatrix := make([][]bool, vertices)
	for i := range adjMatrix {
		adjMatrix[i] = make([]bool, vertices)
	}

	return &Graph{
		vertices:  vertices,
		adjMatrix: adjMatrix,
	}
}

// AddEdge adiciona uma aresta não direcionada entre dois vértices
// Complexidade: O(1)
func (g *Graph) AddEdge(src, dest int) {
	if src < 0 || src >= g.vertices || dest < 0 || dest >= g.vertices {
		fmt.Printf("❌ Erro: Vértices inválidos (%d, %d)\n", src, dest)
		return
	}

	g.adjMatrix[src][dest] = true
	g.adjMatrix[dest][src] = true // Grafo não direcionado
	fmt.Printf("✅ Aresta adicionada: %d ↔ %d\n", src, dest)
}

// BFS executa busca em largura básica a partir de um vértice
// Algoritmo: explora vértices nível por nível
// Complexidade de Tempo: O(V²) devido à matriz de adjacência
// Complexidade de Espaço: O(V) para a fila e array de visitados
func (g *Graph) BFS(startVertex int) {
	if startVertex < 0 || startVertex >= g.vertices {
		fmt.Printf("❌ Erro: Vértice inicial inválido (%d)\n", startVertex)
		return
	}

	// Array para marcar vértices visitados
	visited := make([]bool, g.vertices)

	// Fila simples usando slice (FIFO)
	queue := []int{startVertex}
	visited[startVertex] = true

	fmt.Printf("🔍 BFS a partir do vértice %d: ", startVertex)

	for len(queue) > 0 {
		// Remove o primeiro elemento da fila (FIFO)
		current := queue[0]
		queue = queue[1:]

		fmt.Printf("%d ", current)

		// Visita todos os vizinhos não visitados
		for neighbor := 0; neighbor < g.vertices; neighbor++ {
			if g.adjMatrix[current][neighbor] && !visited[neighbor] {
				visited[neighbor] = true
				queue = append(queue, neighbor)
			}
		}
	}

	fmt.Println()
}

// Display mostra a matriz de adjacência de forma legível
func (g *Graph) Display() {
	fmt.Println("📊 Matriz de Adjacência:")
	fmt.Print("    ")
	for j := 0; j < g.vertices; j++ {
		fmt.Printf("%d ", j)
	}
	fmt.Println()

	for i := 0; i < g.vertices; i++ {
		fmt.Printf("%d   ", i)
		for j := 0; j < g.vertices; j++ {
			if g.adjMatrix[i][j] {
				fmt.Print("1 ")
			} else {
				fmt.Print("0 ")
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func main() {
	fmt.Println("╔════════════════════════════════════════╗")
	fmt.Println("║          BFS Básico - Grafos           ║")
	fmt.Println("║      Implementação Educacional         ║")
	fmt.Println("╚════════════════════════════════════════╝")
	fmt.Println()

	// Criar um grafo pequeno para demonstração
	fmt.Println("📊 Criando grafo de exemplo com 5 vértices...")
	g := NewGraph(5)

	// Adicionar arestas para formar a estrutura:
	// 0 --- 1 --- 3
	// |     |
	// 2 --- 4
	fmt.Println("🔗 Adicionando arestas:")
	g.AddEdge(0, 1)
	g.AddEdge(0, 2)
	g.AddEdge(1, 3)
	g.AddEdge(1, 4)
	g.AddEdge(2, 4)

	fmt.Println()

	// Mostrar estrutura do grafo
	g.Display()

	// Executar BFS a partir de diferentes vértices
	fmt.Println("🚀 Executando BFS:")
	g.BFS(0)
	g.BFS(2)

	fmt.Println()
	fmt.Println("📋 Análise de Complexidade:")
	fmt.Println("   • Tempo: O(V²) - devido à matriz de adjacência")
	fmt.Println("   • Espaço: O(V) - para fila e array de visitados")
	fmt.Println()
	fmt.Println("💡 Casos de Uso:")
	fmt.Println("   • Busca de caminho mais curto (grafos não ponderados)")
	fmt.Println("   • Verificação de conectividade")
	fmt.Println("   • Análise de componentes conectados")
	fmt.Println()
	fmt.Println("⚡ Otimização: Para grafos esparsos, use lista de adjacência")
}
