package main

import (
	"container/list"
	"fmt"
	"math"
	"strings"
	"time"
)

// SlidingWindowAlgorithms implementa algoritmos usando a técnica de sliding window
type SlidingWindowAlgorithms struct {
	operationsCount  int
	comparisonsCount int
}

// NewSlidingWindowAlgorithms cria uma nova instância
func NewSlidingWindowAlgorithms() *SlidingWindowAlgorithms {
	return &SlidingWindowAlgorithms{}
}

// ResetCounters reset dos contadores de performance
func (sw *SlidingWindowAlgorithms) ResetCounters() {
	sw.operationsCount = 0
	sw.comparisonsCount = 0
}

// MaxSumSubarrayFixed encontra a soma máxima de um subarray de tamanho k
// Complexidade: O(n) tempo, O(1) espaço
func (sw *SlidingWindowAlgorithms) MaxSumSubarrayFixed(nums []int, k int) int {
	sw.ResetCounters()

	if len(nums) == 0 || k <= 0 || k > len(nums) {
		return 0
	}

	// Calcular soma da primeira janela
	windowSum := 0
	for i := 0; i < k; i++ {
		windowSum += nums[i]
		sw.operationsCount++
	}

	maxSum := windowSum

	// Deslizar janela
	for i := k; i < len(nums); i++ {
		// Remover elemento que sai, adicionar que entra
		windowSum = windowSum - nums[i-k] + nums[i]
		maxSum = int(math.Max(float64(maxSum), float64(windowSum)))
		sw.operationsCount += 2
		sw.comparisonsCount++
	}

	return maxSum
}

// LongestSubstringWithoutRepeating encontra o comprimento da maior substring sem caracteres repetidos
// Complexidade: O(n) tempo, O(min(m,n)) espaço
func (sw *SlidingWindowAlgorithms) LongestSubstringWithoutRepeating(s string) int {
	sw.ResetCounters()

	if len(s) == 0 {
		return 0
	}

	charSet := make(map[rune]bool)
	left := 0
	maxLength := 0

	for right, char := range s {
		// Contrair janela enquanto há repetição
		for charSet[char] {
			delete(charSet, rune(s[left]))
			left++
			sw.operationsCount += 2
		}

		// Expandir janela
		charSet[char] = true
		maxLength = int(math.Max(float64(maxLength), float64(right-left+1)))
		sw.operationsCount++
		sw.comparisonsCount++
	}

	return maxLength
}

// MinWindowSubstring encontra a menor janela em s que contém todos os caracteres de t
// Complexidade: O(|s| + |t|) tempo, O(|s| + |t|) espaço
func (sw *SlidingWindowAlgorithms) MinWindowSubstring(s, t string) string {
	sw.ResetCounters()

	if len(s) == 0 || len(t) == 0 {
		return ""
	}

	// Contar caracteres necessários
	dictT := make(map[rune]int)
	for _, char := range t {
		dictT[char]++
	}

	required := len(dictT)
	left := 0
	formed := 0

	// Dicionário para contar caracteres na janela atual
	windowCounts := make(map[rune]int)

	// Resultado: (comprimento da janela, left, right)
	ans := []int{math.MaxInt32, 0, 0}

	for right, character := range s {
		// Adicionar um caractere do lado direito da janela
		windowCounts[character]++
		sw.operationsCount++

		// Se a frequência do caractere atual na janela
		// iguala à frequência desejada em t, incrementar formed
		if count, exists := dictT[character]; exists && windowCounts[character] == count {
			formed++
			sw.comparisonsCount++
		}

		// Tentar contrair a janela até que ela deixe de ser 'desejável'
		for left <= right && formed == required {
			character := rune(s[left])

			// Salvar a menor janela até agora
			if right-left+1 < ans[0] {
				ans[0] = right - left + 1
				ans[1] = left
				ans[2] = right
				sw.comparisonsCount++
			}

			// O caractere no início da janela não faz mais parte da janela
			windowCounts[character]--
			if count, exists := dictT[character]; exists && windowCounts[character] < count {
				formed--
				sw.comparisonsCount++
			}

			// Mover ponteiro esquerdo para a frente
			left++
			sw.operationsCount++
		}
	}

	if ans[0] == math.MaxInt32 {
		return ""
	}
	return s[ans[1] : ans[2]+1]
}

// SlidingWindowMaximum encontra o máximo em cada janela de tamanho k
// Complexidade: O(n) tempo, O(k) espaço
func (sw *SlidingWindowAlgorithms) SlidingWindowMaximum(nums []int, k int) []int {
	sw.ResetCounters()

	if len(nums) == 0 || k <= 0 {
		return []int{}
	}

	if k == 1 {
		return nums
	}

	// Lista para armazenar índices
	// Manteremos elementos em ordem decrescente
	dq := list.New()
	result := []int{}

	for i := 0; i < len(nums); i++ {
		// Remover elementos fora da janela atual
		for dq.Len() > 0 && dq.Front().Value.(int) <= i-k {
			dq.Remove(dq.Front())
			sw.operationsCount++
		}

		// Remover elementos menores que o atual
		// (eles nunca serão o máximo)
		for dq.Len() > 0 && nums[dq.Back().Value.(int)] < nums[i] {
			dq.Remove(dq.Back())
			sw.operationsCount++
			sw.comparisonsCount++
		}

		// Adicionar elemento atual
		dq.PushBack(i)
		sw.operationsCount++

		// Adicionar máximo ao resultado (se janela está completa)
		if i >= k-1 {
			result = append(result, nums[dq.Front().Value.(int)])
			sw.operationsCount++
		}
	}

	return result
}

// FindAnagrams encontra todos os índices de anagramas de p em s
// Complexidade: O(|s|) tempo, O(1) espaço
func (sw *SlidingWindowAlgorithms) FindAnagrams(s, p string) []int {
	sw.ResetCounters()

	if len(p) > len(s) {
		return []int{}
	}

	// Arrays de frequência para p e janela atual
	pCount := make([]int, 26)
	windowCount := make([]int, 26)

	// Contar frequências em p
	for _, char := range p {
		pCount[char-'a']++
		sw.operationsCount++
	}

	result := []int{}
	windowSize := len(p)

	for i, char := range s {
		// Adicionar caractere à janela
		windowCount[char-'a']++
		sw.operationsCount++

		// Remover caractere se janela excede tamanho
		if i >= windowSize {
			windowCount[rune(s[i-windowSize])-'a']--
			sw.operationsCount++
		}

		// Verificar se é anagrama (janela tem tamanho correto)
		if i >= windowSize-1 {
			if sw.arraysEqual(windowCount, pCount) {
				result = append(result, i-windowSize+1)
				sw.comparisonsCount++
			}
		}
	}

	return result
}

// arraysEqual compara dois arrays de inteiros
func (sw *SlidingWindowAlgorithms) arraysEqual(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

// LongestSubarrayKDistinct encontra o comprimento do maior subarray com exatamente k elementos distintos
// Complexidade: O(n) tempo, O(k) espaço
func (sw *SlidingWindowAlgorithms) LongestSubarrayKDistinct(nums []int, k int) int {
	sw.ResetCounters()

	if len(nums) == 0 || k <= 0 {
		return 0
	}

	left := 0
	maxLength := 0
	countMap := make(map[int]int)

	for right := 0; right < len(nums); right++ {
		// Adicionar elemento à janela
		countMap[nums[right]]++
		sw.operationsCount++

		// Contrair janela se tiver mais de k elementos distintos
		for len(countMap) > k {
			countMap[nums[left]]--
			if countMap[nums[left]] == 0 {
				delete(countMap, nums[left])
			}
			left++
			sw.operationsCount += 2
			sw.comparisonsCount++
		}

		// Atualizar máximo se janela tem exatamente k elementos distintos
		if len(countMap) == k {
			maxLength = int(math.Max(float64(maxLength), float64(right-left+1)))
			sw.comparisonsCount++
		}
	}

	return maxLength
}

// MaxSumSubarrayVariable encontra a soma máxima de subarray com soma <= target
// Complexidade: O(n) tempo, O(1) espaço
func (sw *SlidingWindowAlgorithms) MaxSumSubarrayVariable(nums []int, target int) int {
	sw.ResetCounters()

	if len(nums) == 0 || target <= 0 {
		return 0
	}

	left := 0
	currentSum := 0
	maxSum := 0

	for right := 0; right < len(nums); right++ {
		// Expandir janela
		currentSum += nums[right]
		sw.operationsCount++

		// Contrair janela se soma excede target
		for currentSum > target && left <= right {
			currentSum -= nums[left]
			left++
			sw.operationsCount += 2
			sw.comparisonsCount++
		}

		// Atualizar máximo
		maxSum = int(math.Max(float64(maxSum), float64(currentSum)))
		sw.comparisonsCount++
	}

	return maxSum
}

// Função para demonstrar o uso dos algoritmos
func demonstrarSlidingWindow() {
	sw := NewSlidingWindowAlgorithms()

	fmt.Println(strings.Repeat("=", 80))
	fmt.Println("DEMONSTRAÇÃO: Algoritmos de Sliding Window")
	fmt.Println(strings.Repeat("=", 80))

	// 1. Maximum Sum Subarray (Fixed Window)
	fmt.Println("\n1. MAXIMUM SUM SUBARRAY - JANELA FIXA")
	fmt.Println(strings.Repeat("-", 50))
	nums1 := []int{1, 4, 2, 9, 5, 10, 13, 8, 5}
	k := 3

	fmt.Printf("Array: %v\n", nums1)
	fmt.Printf("Tamanho da janela: %d\n", k)

	start := time.Now()
	maxSum := sw.MaxSumSubarrayFixed(nums1, k)
	duration := time.Since(start)

	fmt.Printf("Soma máxima: %d\n", maxSum)
	fmt.Printf("Operações: %d\n", sw.operationsCount)
	fmt.Printf("Comparações: %d\n", sw.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 2. Longest Substring Without Repeating Characters
	fmt.Println("\n2. LONGEST SUBSTRING WITHOUT REPEATING")
	fmt.Println(strings.Repeat("-", 50))
	s1 := "abcabcbb"

	fmt.Printf("String: '%s'\n", s1)

	start = time.Now()
	length := sw.LongestSubstringWithoutRepeating(s1)
	duration = time.Since(start)

	fmt.Printf("Comprimento da maior substring: %d\n", length)
	fmt.Printf("Operações: %d\n", sw.operationsCount)
	fmt.Printf("Comparações: %d\n", sw.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 3. Minimum Window Substring
	fmt.Println("\n3. MINIMUM WINDOW SUBSTRING")
	fmt.Println(strings.Repeat("-", 50))
	s2 := "ADOBECODEBANC"
	t := "ABC"

	fmt.Printf("String principal: '%s'\n", s2)
	fmt.Printf("Padrão: '%s'\n", t)

	start = time.Now()
	minWindow := sw.MinWindowSubstring(s2, t)
	duration = time.Since(start)

	fmt.Printf("Menor janela: '%s'\n", minWindow)
	fmt.Printf("Operações: %d\n", sw.operationsCount)
	fmt.Printf("Comparações: %d\n", sw.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 4. Sliding Window Maximum
	fmt.Println("\n4. SLIDING WINDOW MAXIMUM")
	fmt.Println(strings.Repeat("-", 50))
	nums2 := []int{1, 3, -1, -3, 5, 3, 6, 7}
	k2 := 3

	fmt.Printf("Array: %v\n", nums2)
	fmt.Printf("Tamanho da janela: %d\n", k2)

	start = time.Now()
	maximums := sw.SlidingWindowMaximum(nums2, k2)
	duration = time.Since(start)

	fmt.Printf("Máximos: %v\n", maximums)
	fmt.Printf("Operações: %d\n", sw.operationsCount)
	fmt.Printf("Comparações: %d\n", sw.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 5. Find All Anagrams
	fmt.Println("\n5. FIND ALL ANAGRAMS")
	fmt.Println(strings.Repeat("-", 50))
	s3 := "abab"
	p := "ab"

	fmt.Printf("String principal: '%s'\n", s3)
	fmt.Printf("Padrão: '%s'\n", p)

	start = time.Now()
	anagrams := sw.FindAnagrams(s3, p)
	duration = time.Since(start)

	fmt.Printf("Índices de anagramas: %v\n", anagrams)
	fmt.Printf("Operações: %d\n", sw.operationsCount)
	fmt.Printf("Comparações: %d\n", sw.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 6. Longest Subarray with K Distinct
	fmt.Println("\n6. LONGEST SUBARRAY WITH K DISTINCT")
	fmt.Println(strings.Repeat("-", 50))
	nums3 := []int{1, 2, 1, 2, 3}
	k3 := 2

	fmt.Printf("Array: %v\n", nums3)
	fmt.Printf("K (elementos distintos): %d\n", k3)

	start = time.Now()
	longest := sw.LongestSubarrayKDistinct(nums3, k3)
	duration = time.Since(start)

	fmt.Printf("Comprimento do maior subarray: %d\n", longest)
	fmt.Printf("Operações: %d\n", sw.operationsCount)
	fmt.Printf("Comparações: %d\n", sw.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// 7. Maximum Sum Subarray (Variable Window)
	fmt.Println("\n7. MAXIMUM SUM SUBARRAY - JANELA VARIÁVEL")
	fmt.Println(strings.Repeat("-", 50))
	nums4 := []int{1, 2, 3, 4, 5}
	target := 8

	fmt.Printf("Array: %v\n", nums4)
	fmt.Printf("Target (soma máxima): %d\n", target)

	start = time.Now()
	maxSumVar := sw.MaxSumSubarrayVariable(nums4, target)
	duration = time.Since(start)

	fmt.Printf("Soma máxima <= %d: %d\n", target, maxSumVar)
	fmt.Printf("Operações: %d\n", sw.operationsCount)
	fmt.Printf("Comparações: %d\n", sw.comparisonsCount)
	fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)

	// Análise comparativa
	fmt.Println("\n" + strings.Repeat("=", 80))
	fmt.Println("ANÁLISE COMPARATIVA: Sliding Window vs Força Bruta")
	fmt.Println(strings.Repeat("=", 80))

	// Exemplo: Maximum Sum Subarray
	testArray := make([]int, 1000)
	for i := range testArray {
		testArray[i] = i
	}
	windowSize := 100

	fmt.Printf("Array de teste: %d elementos\n", len(testArray))
	fmt.Printf("Tamanho da janela: %d\n", windowSize)

	// Sliding Window
	start = time.Now()
	resultSW := sw.MaxSumSubarrayFixed(testArray, windowSize)
	timeSW := time.Since(start)

	fmt.Printf("\nSliding Window:\n")
	fmt.Printf("  Resultado: %d\n", resultSW)
	fmt.Printf("  Tempo: %.2fms\n", float64(timeSW.Nanoseconds())/1e6)
	fmt.Printf("  Complexidade: O(n)\n")

	// Força Bruta (simulação)
	start = time.Now()
	maxSumBF := 0
	for i := 0; i <= len(testArray)-windowSize; i++ {
		currentSum := 0
		for j := i; j < i+windowSize; j++ {
			currentSum += testArray[j]
		}
		if currentSum > maxSumBF {
			maxSumBF = currentSum
		}
	}
	timeBF := time.Since(start)

	fmt.Printf("\nForça Bruta:\n")
	fmt.Printf("  Resultado: %d\n", maxSumBF)
	fmt.Printf("  Tempo: %.2fms\n", float64(timeBF.Nanoseconds())/1e6)
	fmt.Printf("  Complexidade: O(n*k)\n")

	improvement := float64(timeBF.Nanoseconds()) / float64(timeSW.Nanoseconds())
	fmt.Printf("\nMelhoria de performance: %.1fx mais rápido\n", improvement)

	// Estatísticas finais
	fmt.Println("\n" + strings.Repeat("=", 80))
	fmt.Println("RESUMO DA TÉCNICA DE SLIDING WINDOW")
	fmt.Println(strings.Repeat("=", 80))
	fmt.Println("✓ Otimiza problemas de subarray/substring")
	fmt.Println("✓ Reduz complexidade de O(n²) para O(n)")
	fmt.Println("✓ Duas variações: janela fixa e janela variável")
	fmt.Println("✓ Útil para problemas de otimização e busca")
	fmt.Println("✓ Elimina recálculos desnecessários")

	fmt.Println("\nTipos de problemas resolvidos:")
	fmt.Println("• Maximum/Minimum em subarrays")
	fmt.Println("• Substrings com propriedades específicas")
	fmt.Println("• Problemas de contagem e frequência")
	fmt.Println("• Otimização com restrições")
	fmt.Println("• Análise de sequências temporais")
}

func main() {
	demonstrarSlidingWindow()
}
