package main

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

// TwoPointerAlgorithms implementa algoritmos usando a técnica de dois ponteiros
type TwoPointerAlgorithms struct {
	operationsCount  int
	comparisonsCount int
}

// NewTwoPointerAlgorithms cria uma nova instância
func NewTwoPointerAlgorithms() *TwoPointerAlgorithms {
	return &TwoPointerAlgorithms{}
}

// ResetCounters reset dos contadores de performance
func (tp *TwoPointerAlgorithms) ResetCounters() {
	tp.operationsCount = 0
	tp.comparisonsCount = 0
}

// TwoSumSorted encontra dois números em array ordenado que somam target
// Complexidade: O(n) tempo, O(1) espaço
func (tp *TwoPointerAlgorithms) TwoSumSorted(nums []int, target int) []int {
	tp.ResetCounters()

	left, right := 0, len(nums)-1

	for left < right {
		currentSum := nums[left] + nums[right]
		tp.operationsCount++
		tp.comparisonsCount++

		if currentSum == target {
			return []int{left, right}
		} else if currentSum < target {
			left++
		} else {
			right--
		}
		tp.operationsCount++
	}

	return []int{} // Não encontrado
}

// IsPalindrome verifica se uma string é palíndromo
// Complexidade: O(n) tempo, O(1) espaço
func (tp *TwoPointerAlgorithms) IsPalindrome(s string) bool {
	tp.ResetCounters()

	left, right := 0, len(s)-1

	for left < right {
		tp.comparisonsCount++
		if s[left] != s[right] {
			return false
		}
		left++
		right--
		tp.operationsCount += 2
	}

	return true
}

// RemoveDuplicates remove duplicatas de array ordenado in-place
// Complexidade: O(n) tempo, O(1) espaço
func (tp *TwoPointerAlgorithms) RemoveDuplicates(nums []int) int {
	tp.ResetCounters()

	if len(nums) <= 1 {
		return len(nums)
	}

	writePos := 1

	for readPos := 1; readPos < len(nums); readPos++ {
		tp.comparisonsCount++
		if nums[readPos] != nums[readPos-1] {
			nums[writePos] = nums[readPos]
			writePos++
			tp.operationsCount++
		}
		tp.operationsCount++
	}

	return writePos
}

// ContainerWithMostWater encontra o container que pode reter mais água
// Complexidade: O(n) tempo, O(1) espaço
func (tp *TwoPointerAlgorithms) ContainerWithMostWater(heights []int) int {
	tp.ResetCounters()

	left, right := 0, len(heights)-1
	maxArea := 0

	for left < right {
		// Calcular área atual
		width := right - left
		height := int(math.Min(float64(heights[left]), float64(heights[right])))
		area := width * height

		maxArea = int(math.Max(float64(maxArea), float64(area)))
		tp.operationsCount += 3
		tp.comparisonsCount += 1

		// Mover ponteiro da altura menor
		if heights[left] < heights[right] {
			left++
		} else {
			right--
		}
		tp.comparisonsCount++
		tp.operationsCount++
	}

	return maxArea
}

// ThreeSum encontra todos os triplets únicos que somam zero
// Complexidade: O(n²) tempo, O(1) espaço extra
func (tp *TwoPointerAlgorithms) ThreeSum(nums []int) [][]int {
	tp.ResetCounters()

	sort.Ints(nums)
	result := [][]int{}

	for i := 0; i < len(nums)-2; i++ {
		// Pular duplicatas para o primeiro número
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		left, right := i+1, len(nums)-1

		for left < right {
			currentSum := nums[i] + nums[left] + nums[right]
			tp.operationsCount++
			tp.comparisonsCount++

			if currentSum == 0 {
				result = append(result, []int{nums[i], nums[left], nums[right]})

				// Pular duplicatas
				for left < right && nums[left] == nums[left+1] {
					left++
					tp.operationsCount++
				}
				for left < right && nums[right] == nums[right-1] {
					right--
					tp.operationsCount++
				}

				left++
				right--
				tp.operationsCount += 2
			} else if currentSum < 0 {
				left++
				tp.operationsCount++
			} else {
				right--
				tp.operationsCount++
			}
		}
	}

	return result
}

// SortColors ordena array com valores 0, 1, 2 (Dutch National Flag)
// Complexidade: O(n) tempo, O(1) espaço
func (tp *TwoPointerAlgorithms) SortColors(nums []int) {
	tp.ResetCounters()

	low, mid, high := 0, 0, len(nums)-1

	for mid <= high {
		tp.comparisonsCount++
		switch nums[mid] {
		case 0:
			nums[low], nums[mid] = nums[mid], nums[low]
			low++
			mid++
			tp.operationsCount += 3
		case 1:
			mid++
			tp.operationsCount++
		case 2:
			nums[mid], nums[high] = nums[high], nums[mid]
			high--
			tp.operationsCount += 2
		}
	}
}

// Função para demonstrar o uso dos algoritmos
func demonstrarTwoPointer() {
	tp := NewTwoPointerAlgorithms()

	fmt.Println(strings.Repeat("=", 80))
	fmt.Println("DEMONSTRAÇÃO: Algoritmos de Two Pointer")
	fmt.Println(strings.Repeat("=", 80))

	// 1. Two Sum em Array Ordenado
	fmt.Println("\n1. TWO SUM EM ARRAY ORDENADO")
	fmt.Println(strings.Repeat("-", 40))
	nums1 := []int{2, 7, 11, 15}
	target := 9

	fmt.Printf("Array: %v\n", nums1)
	fmt.Printf("Target: %d\n", target)

	start := time.Now()
	result := tp.TwoSumSorted(nums1, target)
	duration := time.Since(start)

	fmt.Printf("Índices encontrados: %v\n", result)
	if len(result) == 2 {
		fmt.Printf("Valores: [%d, %d]\n", nums1[result[0]], nums1[result[1]])
	}
	fmt.Printf("Operações: %d\n", tp.operationsCount)
	fmt.Printf("Comparações: %d\n", tp.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 2. Verificação de Palíndromo
	fmt.Println("\n2. VERIFICAÇÃO DE PALÍNDROMO")
	fmt.Println(strings.Repeat("-", 40))
	testString := "racecar"

	fmt.Printf("String: '%s'\n", testString)

	start = time.Now()
	isPalin := tp.IsPalindrome(testString)
	duration = time.Since(start)

	fmt.Printf("É palíndromo: %t\n", isPalin)
	fmt.Printf("Operações: %d\n", tp.operationsCount)
	fmt.Printf("Comparações: %d\n", tp.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 3. Remoção de Duplicatas
	fmt.Println("\n3. REMOÇÃO DE DUPLICATAS")
	fmt.Println(strings.Repeat("-", 40))
	nums2 := []int{1, 1, 2, 2, 3, 4, 4, 5}
	original := make([]int, len(nums2))
	copy(original, nums2)

	fmt.Printf("Array original: %v\n", original)

	start = time.Now()
	newLength := tp.RemoveDuplicates(nums2)
	duration = time.Since(start)

	fmt.Printf("Array após remoção: %v\n", nums2[:newLength])
	fmt.Printf("Novo comprimento: %d\n", newLength)
	fmt.Printf("Operações: %d\n", tp.operationsCount)
	fmt.Printf("Comparações: %d\n", tp.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 4. Container com Mais Água
	fmt.Println("\n4. CONTAINER COM MAIS ÁGUA")
	fmt.Println(strings.Repeat("-", 40))
	heights := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}

	fmt.Printf("Alturas: %v\n", heights)

	start = time.Now()
	maxArea := tp.ContainerWithMostWater(heights)
	duration = time.Since(start)

	fmt.Printf("Área máxima: %d\n", maxArea)
	fmt.Printf("Operações: %d\n", tp.operationsCount)
	fmt.Printf("Comparações: %d\n", tp.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 5. Three Sum
	fmt.Println("\n5. THREE SUM")
	fmt.Println(strings.Repeat("-", 40))
	nums3 := []int{-1, 0, 1, 2, -1, -4}

	fmt.Printf("Array: %v\n", nums3)

	start = time.Now()
	triplets := tp.ThreeSum(nums3)
	duration = time.Since(start)

	fmt.Printf("Triplets que somam zero: %v\n", triplets)
	fmt.Printf("Número de triplets: %d\n", len(triplets))
	fmt.Printf("Operações: %d\n", tp.operationsCount)
	fmt.Printf("Comparações: %d\n", tp.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 6. Sort Colors (Dutch National Flag)
	fmt.Println("\n6. SORT COLORS (DUTCH NATIONAL FLAG)")
	fmt.Println(strings.Repeat("-", 40))
	colors := []int{2, 0, 2, 1, 1, 0}
	original2 := make([]int, len(colors))
	copy(original2, colors)

	fmt.Printf("Array original: %v\n", original2)

	start = time.Now()
	tp.SortColors(colors)
	duration = time.Since(start)

	fmt.Printf("Array ordenado: %v\n", colors)
	fmt.Printf("Operações: %d\n", tp.operationsCount)
	fmt.Printf("Comparações: %d\n", tp.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// Análise de Performance
	fmt.Println("\n" + strings.Repeat("=", 80))
	fmt.Println("ANÁLISE DE PERFORMANCE")
	fmt.Println(strings.Repeat("=", 80))

	// Teste com array grande
	largeArray := make([]int, 10000)
	for i := range largeArray {
		largeArray[i] = i * 2 // Array ordenado
	}

	fmt.Printf("Teste com array de %d elementos\n", len(largeArray))

	// Two Sum
	start = time.Now()
	tp.TwoSumSorted(largeArray, 19998) // Procurar últimos dois elementos
	twoSumTime := time.Since(start)

	fmt.Printf("Two Sum - Tempo: %.2fms, Operações: %d\n",
		float64(twoSumTime.Nanoseconds())/1e6, tp.operationsCount)

	// Verificação de eficiência vs força bruta
	fmt.Println("\nComparação com Força Bruta (simulação):")

	// Simulação força bruta O(n²)
	n := len(largeArray)
	bruteForceOps := (n * (n - 1)) / 2 // Número de comparações em força bruta

	fmt.Printf("Força Bruta (O(n²)): %d operações estimadas\n", bruteForceOps)
	fmt.Printf("Two Pointer (O(n)): %d operações reais\n", tp.operationsCount)
	fmt.Printf("Melhoria: %.1fx mais eficiente\n", float64(bruteForceOps)/float64(tp.operationsCount))

	// Estatísticas finais
	fmt.Println("\n" + strings.Repeat("=", 80))
	fmt.Println("RESUMO DA TÉCNICA DE TWO POINTER")
	fmt.Println(strings.Repeat("=", 80))
	fmt.Println("✓ Reduz complexidade de O(n²) para O(n)")
	fmt.Println("✓ Uso eficiente de memória O(1)")
	fmt.Println("✓ Ideal para arrays/strings ordenadas")
	fmt.Println("✓ Padrões: opostos, sequenciais, rápido/lento")
	fmt.Println("✓ Aplicações: busca, verificação, otimização")

	fmt.Println("\nAlgoritmos implementados:")
	fmt.Println("• Two Sum em array ordenado")
	fmt.Println("• Verificação de palíndromo")
	fmt.Println("• Remoção de duplicatas")
	fmt.Println("• Container com mais água")
	fmt.Println("• Three Sum")
	fmt.Println("• Dutch National Flag (Sort Colors)")
}

func main() {
	demonstrarTwoPointer()
}
