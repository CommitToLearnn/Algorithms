/**
 * BFS Básico para Árvores - Implementação Educacional
 * ====================================================
 *
 * Esta implementação demonstra a busca em largura (BFS) aplicada a estruturas de árvore.
 * Foco no entendimento do algoritmo com visualização e exemplos práticos.
 *
 * Características:
 * - Implementação simples e didática
 * - Estrutura de árvore hierárquica
 * - Visualização da travessia
 * - Exemplos práticos de uso
 * - Análise de complexidade incluída
 *
 * Uso: go run bfs_basico_arvore.go
 *
 * @author matheussricardoo
 * @version 1.0
 * @since Julho 2025
 */

package main

import (
	"fmt"
)

// Node representa um nó na árvore
type Node struct {
	Value    int     // Valor armazenado no nó
	Children []*Node // Lista de nós filhos
}

// NewNode cria um novo nó com o valor especificado
// Complexidade: O(1)
func NewNode(value int) *Node {
	return &Node{
		Value:    value,
		Children: make([]*Node, 0),
	}
}

// AddChild adiciona um nó filho ao nó atual
// Complexidade: O(1)
func (n *Node) AddChild(child *Node) {
	n.Children = append(n.Children, child)
}

// BFS executa busca em largura em uma árvore
// Algoritmo: visita nós nível por nível, da esquerda para direita
// Complexidade de Tempo: O(n) onde n é o número de nós
// Complexidade de Espaço: O(w) onde w é a largura máxima da árvore
func BFS(root *Node) {
	if root == nil {
		fmt.Println("⚠️  Árvore vazia!")
		return
	}

	// Fila para armazenar os nós a serem visitados (FIFO)
	queue := []*Node{root}

	// Controle de nós visitados (previne loops em grafos)
	visited := make(map[*Node]bool)

	fmt.Print("🔍 BFS Traversal: ")

	for len(queue) > 0 {
		// Remove o primeiro nó da fila (FIFO - First In, First Out)
		current := queue[0]
		queue = queue[1:]

		// Verifica se o nó já foi visitado
		if visited[current] {
			continue
		}

		// Marca o nó como visitado
		visited[current] = true

		// Processa o nó atual
		fmt.Printf("%d ", current.Value)

		// Adiciona todos os filhos não visitados à fila
		for _, child := range current.Children {
			if !visited[child] {
				queue = append(queue, child)
			}
		}
	}

	fmt.Println()
}

// DisplayTree mostra a estrutura da árvore de forma visual
// Útil para compreender a hierarquia antes da travessia
func DisplayTree(root *Node, level int) {
	if root == nil {
		return
	}

	// Indentação baseada no nível da árvore
	for i := 0; i < level; i++ {
		fmt.Print("  ")
	}
	fmt.Printf("└─ %d\n", root.Value)

	// Recursivamente mostra os filhos
	for _, child := range root.Children {
		DisplayTree(child, level+1)
	}
}

// CountNodes conta o número total de nós na árvore
// Complexidade: O(n)
func CountNodes(root *Node) int {
	if root == nil {
		return 0
	}

	count := 1 // Conta o nó atual
	for _, child := range root.Children {
		count += CountNodes(child)
	}
	return count
}

// GetHeight calcula a altura da árvore
// Complexidade: O(n)
func GetHeight(root *Node) int {
	if root == nil {
		return 0
	}

	maxChildHeight := 0
	for _, child := range root.Children {
		childHeight := GetHeight(child)
		if childHeight > maxChildHeight {
			maxChildHeight = childHeight
		}
	}

	return maxChildHeight + 1
}

func main() {
	fmt.Println("╔════════════════════════════════════════╗")
	fmt.Println("║        BFS Básico para Árvores         ║")
	fmt.Println("║      Implementação Educacional         ║")
	fmt.Println("╚════════════════════════════════════════╝")
	fmt.Println()

	// Criação de uma árvore de exemplo
	// Estrutura da árvore:
	//        1
	//       /|\
	//      2 3 4
	//     /| |  |\
	//    5 6 7  8 9
	//      |
	//     10

	fmt.Println("📊 Construindo árvore de exemplo...")

	// Criação dos nós
	node1 := NewNode(1)   // Raiz
	node2 := NewNode(2)   // Nível 1
	node3 := NewNode(3)   // Nível 1
	node4 := NewNode(4)   // Nível 1
	node5 := NewNode(5)   // Nível 2
	node6 := NewNode(6)   // Nível 2
	node7 := NewNode(7)   // Nível 2
	node8 := NewNode(8)   // Nível 2
	node9 := NewNode(9)   // Nível 2
	node10 := NewNode(10) // Nível 3

	// Construção da hierarquia
	node1.AddChild(node2)
	node1.AddChild(node3)
	node1.AddChild(node4)
	node2.AddChild(node5)
	node2.AddChild(node6)
	node3.AddChild(node7)
	node4.AddChild(node8)
	node4.AddChild(node9)
	node6.AddChild(node10)

	// Mostrar estrutura da árvore
	fmt.Println("🌳 Estrutura da Árvore:")
	DisplayTree(node1, 0)
	fmt.Println()

	// Informações sobre a árvore
	fmt.Printf("📈 Número de nós: %d\n", CountNodes(node1))
	fmt.Printf("📏 Altura da árvore: %d\n", GetHeight(node1))
	fmt.Println()

	// Executar BFS
	fmt.Println("🚀 Executando Busca em Largura (BFS):")
	BFS(node1)

	fmt.Println()
	fmt.Println("✅ Ordem esperada: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10")
	fmt.Println("   (visitação nível por nível, da esquerda para a direita)")

	fmt.Println()
	fmt.Println("📋 Análise de Complexidade:")
	fmt.Println("   • Tempo: O(n) - visita cada nó exatamente uma vez")
	fmt.Println("   • Espaço: O(w) - onde w é a largura máxima da árvore")
	fmt.Println()
	fmt.Println("💡 Casos de Uso:")
	fmt.Println("   • Busca de caminho mais curto em árvores")
	fmt.Println("   • Travessia por níveis")
	fmt.Println("   • Algoritmos de busca em estruturas hierárquicas")
}
