package main

import (
	"fmt"
	"strings"
	"time"
)

// BacktrackingAlgorithms implementa algoritmos usando a técnica de backtracking
type BacktrackingAlgorithms struct {
	recursionCount int
	backtrackCount int
}

// NewBacktrackingAlgorithms cria uma nova instância
func NewBacktrackingAlgorithms() *BacktrackingAlgorithms {
	return &BacktrackingAlgorithms{}
}

// ResetCounters reset dos contadores de performance
func (bt *BacktrackingAlgorithms) ResetCounters() {
	bt.recursionCount = 0
	bt.backtrackCount = 0
}

// NQueens resolve o problema das N-Rainhas
// Complexidade: O(N!) tempo, O(N) espaço
func (bt *BacktrackingAlgorithms) NQueens(n int) [][]string {
	bt.ResetCounters()
	result := [][]string{}
	board := make([]string, n)

	// Inicializar tabuleiro
	for i := range board {
		board[i] = strings.Repeat(".", n)
	}

	var backtrack func(int)
	backtrack = func(row int) {
		bt.recursionCount++

		if row == n {
			// Solução encontrada
			solution := make([]string, n)
			copy(solution, board)
			result = append(result, solution)
			return
		}

		for col := 0; col < n; col++ {
			if bt.isSafe(board, row, col, n) {
				// Colocar rainha
				runes := []rune(board[row])
				runes[col] = 'Q'
				board[row] = string(runes)

				// Recursão
				backtrack(row + 1)

				// Backtrack (remover rainha)
				runes[col] = '.'
				board[row] = string(runes)
				bt.backtrackCount++
			}
		}
	}

	backtrack(0)
	return result
}

// isSafe verifica se é seguro colocar rainha na posição (row, col)
func (bt *BacktrackingAlgorithms) isSafe(board []string, row, col, n int) bool {
	// Verificar coluna
	for i := 0; i < row; i++ {
		if board[i][col] == 'Q' {
			return false
		}
	}

	// Verificar diagonal principal
	for i, j := row-1, col-1; i >= 0 && j >= 0; i, j = i-1, j-1 {
		if board[i][j] == 'Q' {
			return false
		}
	}

	// Verificar diagonal secundária
	for i, j := row-1, col+1; i >= 0 && j < n; i, j = i-1, j+1 {
		if board[i][j] == 'Q' {
			return false
		}
	}

	return true
}

// SolveSudoku resolve um puzzle de Sudoku
// Complexidade: O(9^(n*n)) tempo, O(1) espaço extra
func (bt *BacktrackingAlgorithms) SolveSudoku(board [][]string) bool {
	bt.ResetCounters()

	var solve func() bool
	solve = func() bool {
		bt.recursionCount++

		for i := 0; i < 9; i++ {
			for j := 0; j < 9; j++ {
				if board[i][j] == "." {
					for num := "1"; num <= "9"; num = string(rune(num[0] + 1)) {
						if bt.isValidSudoku(board, i, j, num) {
							board[i][j] = num

							if solve() {
								return true
							}

							// Backtrack
							board[i][j] = "."
							bt.backtrackCount++
						}
					}
					return false
				}
			}
		}
		return true
	}

	return solve()
}

// isValidSudoku verifica se é válido colocar o número na posição
func (bt *BacktrackingAlgorithms) isValidSudoku(board [][]string, row, col int, num string) bool {
	// Verificar linha
	for x := 0; x < 9; x++ {
		if board[row][x] == num {
			return false
		}
	}

	// Verificar coluna
	for x := 0; x < 9; x++ {
		if board[x][col] == num {
			return false
		}
	}

	// Verificar quadrante 3x3
	startRow, startCol := 3*(row/3), 3*(col/3)
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if board[i+startRow][j+startCol] == num {
				return false
			}
		}
	}

	return true
}

// GeneratePermutations gera todas as permutações de uma lista de números
// Complexidade: O(N! * N) tempo, O(N) espaço
func (bt *BacktrackingAlgorithms) GeneratePermutations(nums []int) [][]int {
	bt.ResetCounters()
	result := [][]int{}

	var backtrack func([]int)
	backtrack = func(currentPermutation []int) {
		bt.recursionCount++

		if len(currentPermutation) == len(nums) {
			perm := make([]int, len(currentPermutation))
			copy(perm, currentPermutation)
			result = append(result, perm)
			return
		}

		for _, num := range nums {
			if !bt.contains(currentPermutation, num) {
				currentPermutation = append(currentPermutation, num)
				backtrack(currentPermutation)
				currentPermutation = currentPermutation[:len(currentPermutation)-1] // Backtrack
				bt.backtrackCount++
			}
		}
	}

	backtrack([]int{})
	return result
}

// contains verifica se um slice contém um valor
func (bt *BacktrackingAlgorithms) contains(slice []int, val int) bool {
	for _, item := range slice {
		if item == val {
			return true
		}
	}
	return false
}

// GenerateCombinations gera todas as combinações de k elementos de 1 a n
// Complexidade: O(C(n,k) * k) tempo, O(k) espaço
func (bt *BacktrackingAlgorithms) GenerateCombinations(n, k int) [][]int {
	bt.ResetCounters()
	result := [][]int{}

	var backtrack func(int, []int)
	backtrack = func(start int, currentCombination []int) {
		bt.recursionCount++

		if len(currentCombination) == k {
			comb := make([]int, len(currentCombination))
			copy(comb, currentCombination)
			result = append(result, comb)
			return
		}

		for i := start; i <= n; i++ {
			currentCombination = append(currentCombination, i)
			backtrack(i+1, currentCombination)
			currentCombination = currentCombination[:len(currentCombination)-1] // Backtrack
			bt.backtrackCount++
		}
	}

	backtrack(1, []int{})
	return result
}

// WordSearch busca uma palavra em uma matriz de caracteres
// Complexidade: O(M*N*4^L) tempo, O(L) espaço
func (bt *BacktrackingAlgorithms) WordSearch(board [][]string, word string) bool {
	bt.ResetCounters()

	if len(board) == 0 || len(board[0]) == 0 || len(word) == 0 {
		return false
	}

	rows, cols := len(board), len(board[0])

	var backtrack func(int, int, int) bool
	backtrack = func(row, col, index int) bool {
		bt.recursionCount++

		if index == len(word) {
			return true // Palavra encontrada
		}

		if row < 0 || row >= rows || col < 0 || col >= cols ||
			board[row][col] != string(word[index]) {
			return false
		}

		// Marcar célula como visitada
		temp := board[row][col]
		board[row][col] = "#"

		// Explorar 4 direções
		directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
		found := false

		for _, dir := range directions {
			if backtrack(row+dir[0], col+dir[1], index+1) {
				found = true
				break
			}
		}

		// Backtrack (restaurar célula)
		board[row][col] = temp
		if !found {
			bt.backtrackCount++
		}

		return found
	}

	// Tentar começar de cada posição
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if backtrack(i, j, 0) {
				return true
			}
		}
	}

	return false
}

// SubsetSum encontra todos os subconjuntos que somam um valor alvo
// Complexidade: O(2^N * N) tempo, O(N) espaço
func (bt *BacktrackingAlgorithms) SubsetSum(nums []int, target int) [][]int {
	bt.ResetCounters()
	result := [][]int{}

	var backtrack func(int, []int, int)
	backtrack = func(start int, currentSubset []int, currentSum int) {
		bt.recursionCount++

		if currentSum == target {
			subset := make([]int, len(currentSubset))
			copy(subset, currentSubset)
			result = append(result, subset)
			return
		}

		if currentSum > target {
			return // Poda: soma já excedeu o alvo
		}

		for i := start; i < len(nums); i++ {
			currentSubset = append(currentSubset, nums[i])
			backtrack(i+1, currentSubset, currentSum+nums[i])
			currentSubset = currentSubset[:len(currentSubset)-1] // Backtrack
			bt.backtrackCount++
		}
	}

	backtrack(0, []int{}, 0)
	return result
}

// Função para demonstrar o uso dos algoritmos
func demonstrarBacktracking() {
	bt := NewBacktrackingAlgorithms()

	fmt.Println(strings.Repeat("=", 80))
	fmt.Println("DEMONSTRAÇÃO: Algoritmos de Backtracking")
	fmt.Println(strings.Repeat("=", 80))

	// 1. N-Queens Problem
	fmt.Println("\n1. N-QUEENS PROBLEM (N=4)")
	fmt.Println(strings.Repeat("-", 40))
	start := time.Now()
	solutions := bt.NQueens(4)
	duration := time.Since(start)

	fmt.Printf("Número de soluções encontradas: %d\n", len(solutions))
	fmt.Println("Primeira solução:")
	for _, row := range solutions[0] {
		fmt.Printf("  %s\n", row)
	}
	fmt.Printf("Recursões: %d\n", bt.recursionCount)
	fmt.Printf("Backtracks: %d\n", bt.backtrackCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 2. Sudoku Solver
	fmt.Println("\n2. SUDOKU SOLVER")
	fmt.Println(strings.Repeat("-", 40))
	sudokuBoard := [][]string{
		{"5", "3", ".", ".", "7", ".", ".", ".", "."},
		{"6", ".", ".", "1", "9", "5", ".", ".", "."},
		{".", "9", "8", ".", ".", ".", ".", "6", "."},
		{"8", ".", ".", ".", "6", ".", ".", ".", "3"},
		{"4", ".", ".", "8", ".", "3", ".", ".", "1"},
		{"7", ".", ".", ".", "2", ".", ".", ".", "6"},
		{".", "6", ".", ".", ".", ".", "2", "8", "."},
		{".", ".", ".", "4", "1", "9", ".", ".", "5"},
		{".", ".", ".", ".", "8", ".", ".", "7", "9"},
	}

	fmt.Println("Tabuleiro original:")
	for _, row := range sudokuBoard {
		fmt.Printf("  %s\n", strings.Join(row, " "))
	}

	start = time.Now()
	solved := bt.SolveSudoku(sudokuBoard)
	duration = time.Since(start)

	if solved {
		fmt.Println("\nSolução encontrada:")
		for _, row := range sudokuBoard {
			fmt.Printf("  %s\n", strings.Join(row, " "))
		}
	} else {
		fmt.Println("\nNenhuma solução encontrada!")
	}

	fmt.Printf("Recursões: %d\n", bt.recursionCount)
	fmt.Printf("Backtracks: %d\n", bt.backtrackCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 3. Generate Permutations
	fmt.Println("\n3. GENERATE PERMUTATIONS ([1,2,3])")
	fmt.Println(strings.Repeat("-", 40))
	start = time.Now()
	perms := bt.GeneratePermutations([]int{1, 2, 3})
	duration = time.Since(start)

	fmt.Printf("Permutações: %v\n", perms)
	fmt.Printf("Total de permutações: %d\n", len(perms))
	fmt.Printf("Recursões: %d\n", bt.recursionCount)
	fmt.Printf("Backtracks: %d\n", bt.backtrackCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 4. Generate Combinations
	fmt.Println("\n4. GENERATE COMBINATIONS (n=4, k=2)")
	fmt.Println(strings.Repeat("-", 40))
	start = time.Now()
	combs := bt.GenerateCombinations(4, 2)
	duration = time.Since(start)

	fmt.Printf("Combinações: %v\n", combs)
	fmt.Printf("Total de combinações: %d\n", len(combs))
	fmt.Printf("Recursões: %d\n", bt.recursionCount)
	fmt.Printf("Backtracks: %d\n", bt.backtrackCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 5. Word Search
	fmt.Println("\n5. WORD SEARCH")
	fmt.Println(strings.Repeat("-", 40))
	wordBoard := [][]string{
		{"A", "B", "C", "E"},
		{"S", "F", "C", "S"},
		{"A", "D", "E", "E"},
	}
	word := "ABCCED"

	fmt.Println("Tabuleiro:")
	for _, row := range wordBoard {
		fmt.Printf("  %v\n", row)
	}
	fmt.Printf("Palavra procurada: '%s'\n", word)

	start = time.Now()
	found := bt.WordSearch(wordBoard, word)
	duration = time.Since(start)

	fmt.Printf("Palavra encontrada: %t\n", found)
	fmt.Printf("Recursões: %d\n", bt.recursionCount)
	fmt.Printf("Backtracks: %d\n", bt.backtrackCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 6. Subset Sum
	fmt.Println("\n6. SUBSET SUM ([1,2,3,4,5], target=5)")
	fmt.Println(strings.Repeat("-", 40))
	nums := []int{1, 2, 3, 4, 5}
	target := 5

	start = time.Now()
	subsets := bt.SubsetSum(nums, target)
	duration = time.Since(start)

	fmt.Printf("Números: %v\n", nums)
	fmt.Printf("Alvo: %d\n", target)
	fmt.Printf("Subconjuntos que somam %d: %v\n", target, subsets)
	fmt.Printf("Total de subconjuntos: %d\n", len(subsets))
	fmt.Printf("Recursões: %d\n", bt.recursionCount)
	fmt.Printf("Backtracks: %d\n", bt.backtrackCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// Estatísticas finais
	fmt.Println("\n" + strings.Repeat("=", 80))
	fmt.Println("RESUMO DA TÉCNICA DE BACKTRACKING")
	fmt.Println(strings.Repeat("=", 80))
	fmt.Println("✓ Explora sistematicamente todas as possibilidades")
	fmt.Println("✓ Remove candidatos inválidos (poda)")
	fmt.Println("✓ Retrocede quando atinge beco sem saída")
	fmt.Println("✓ Útil para problemas de decisão e otimização")
	fmt.Println("✓ Complexidade exponencial, mas eficiente com poda")

	fmt.Println("\nProblemas clássicos de backtracking:")
	fmt.Println("• N-Queens Problem")
	fmt.Println("• Sudoku Solver")
	fmt.Println("• Permutações e Combinações")
	fmt.Println("• Word Search")
	fmt.Println("• Subset Sum")
	fmt.Println("• Graph Coloring")
	fmt.Println("• Knapsack Problem")
	fmt.Println("• Maze Solving")
}

func main() {
	demonstrarBacktracking()
}
