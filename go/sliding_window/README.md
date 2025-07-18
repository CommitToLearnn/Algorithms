<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=8E44AD&height=120&section=header&text=Sliding%20Window%20-%20Go&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Implementação%20em%20Go%20da%20Técnica%20de%20Janela%20Deslizante&descAlignY=65&descSize=16">

</div>

# Sliding Window - Implementação em Go

## Descrição

Esta implementação em Go demonstra a técnica de janela deslizante através de 7 algoritmos fundamentais. Go oferece estruturas de dados eficientes e sintaxe clara para otimizar problemas de array e string usando esta técnica.

## Algoritmos Implementados

### 1. Maximum Sum Subarray (Fixed Window)
```go
func (sw *SlidingWindowAlgorithms) MaxSumSubarray(nums []int, k int) int {
    if len(nums) < k {
        return 0
    }
    
    // Calcular soma da primeira janela
    windowSum := 0
    for i := 0; i < k; i++ {
        windowSum += nums[i]
        sw.operationsCount++
    }
    
    maxSum := windowSum
    
    // Deslizar a janela
    for i := k; i < len(nums); i++ {
        windowSum += nums[i] - nums[i-k]
        sw.operationsCount += 2
        if windowSum > maxSum {
            maxSum = windowSum
        }
    }
    
    return maxSum
}
```

### 2. Longest Substring Without Repeating Characters
```go
func (sw *SlidingWindowAlgorithms) LengthOfLongestSubstring(s string) int {
    charMap := make(map[rune]int)
    left := 0
    maxLength := 0
    
    for right, char := range s {
        sw.operationsCount++
        
        if lastIndex, exists := charMap[char]; exists && lastIndex >= left {
            left = lastIndex + 1
        }
        
        charMap[char] = right
        currentLength := right - left + 1
        if currentLength > maxLength {
            maxLength = currentLength
        }
    }
    
    return maxLength
}
```

### 3. Minimum Window Substring
```go
func (sw *SlidingWindowAlgorithms) MinimumWindowSubstring(s, t string) string {
    if len(s) < len(t) {
        return ""
    }
    
    tCount := make(map[rune]int)
    for _, char := range t {
        tCount[char]++
    }
    
    required := len(tCount)
    formed := 0
    windowCounts := make(map[rune]int)
    
    left := 0
    minLen := math.MaxInt32
    minStart := 0
    
    for right, char := range s {
        sw.operationsCount++
        windowCounts[char]++
        
        if count, exists := tCount[char]; exists && windowCounts[char] == count {
            formed++
        }
        
        for left <= right && formed == required {
            if right-left+1 < minLen {
                minLen = right - left + 1
                minStart = left
            }
            
            leftChar := rune(s[left])
            windowCounts[leftChar]--
            if count, exists := tCount[leftChar]; exists && windowCounts[leftChar] < count {
                formed--
            }
            left++
        }
    }
    
    if minLen == math.MaxInt32 {
        return ""
    }
    return s[minStart : minStart+minLen]
}
```

### 4. Sliding Window Maximum
```go
func (sw *SlidingWindowAlgorithms) SlidingWindowMaximum(nums []int, k int) []int {
    if len(nums) == 0 || k == 0 {
        return []int{}
    }
    
    deque := list.New()
    result := []int{}
    
    for i, num := range nums {
        sw.operationsCount++
        
        // Remove elementos fora da janela atual
        for deque.Len() > 0 && deque.Front().Value.(int) <= i-k {
            deque.Remove(deque.Front())
        }
        
        // Remove elementos menores que o atual (não serão máximo)
        for deque.Len() > 0 && nums[deque.Back().Value.(int)] <= num {
            deque.Remove(deque.Back())
        }
        
        deque.PushBack(i)
        
        // Adicionar máximo ao resultado quando janela estiver completa
        if i >= k-1 {
            result = append(result, nums[deque.Front().Value.(int)])
        }
    }
    
    return result
}
```

### 5. Find All Anagrams
```go
func (sw *SlidingWindowAlgorithms) FindAnagrams(s, p string) []int {
    if len(s) < len(p) {
        return []int{}
    }
    
    pCount := make(map[rune]int)
    for _, char := range p {
        pCount[char]++
    }
    
    windowCount := make(map[rune]int)
    result := []int{}
    windowSize := len(p)
    
    for i, char := range s {
        sw.operationsCount++
        windowCount[char]++
        
        // Se janela maior que p, remover character da esquerda
        if i >= windowSize {
            leftChar := rune(s[i-windowSize])
            windowCount[leftChar]--
            if windowCount[leftChar] == 0 {
                delete(windowCount, leftChar)
            }
        }
        
        // Verificar se é anagrama
        if i >= windowSize-1 && mapsEqual(windowCount, pCount) {
            result = append(result, i-windowSize+1)
        }
    }
    
    return result
}
```

### 6. Longest Substring with At Most K Distinct Characters
```go
func (sw *SlidingWindowAlgorithms) LengthOfLongestSubstringKDistinct(s string, k int) int {
    if k == 0 {
        return 0
    }
    
    charCount := make(map[rune]int)
    left := 0
    maxLength := 0
    
    for right, char := range s {
        sw.operationsCount++
        charCount[char]++
        
        for len(charCount) > k {
            leftChar := rune(s[left])
            charCount[leftChar]--
            if charCount[leftChar] == 0 {
                delete(charCount, leftChar)
            }
            left++
        }
        
        currentLength := right - left + 1
        if currentLength > maxLength {
            maxLength = currentLength
        }
    }
    
    return maxLength
}
```

### 7. Subarray Product Less Than K
```go
func (sw *SlidingWindowAlgorithms) NumSubarrayProductLessThanK(nums []int, k int) int {
    if k <= 1 {
        return 0
    }
    
    left := 0
    product := 1
    count := 0
    
    for right, num := range nums {
        sw.operationsCount++
        product *= num
        
        for product >= k {
            product /= nums[left]
            left++
        }
        
        count += right - left + 1
    }
    
    return count
}
```

## Características da Implementação Go

### 🚀 Performance e Estruturas de Dados
- **Maps nativos**: `map[rune]int` para contagem eficiente
- **Slices dinâmicos**: Crescimento automático e eficiente
- **container/list**: Deque para sliding window maximum
- **Strings otimizadas**: Operações Unicode-aware
- **Memory efficiency**: Garbage collection otimizada

### 📊 Monitoramento de Performance
```go
type SlidingWindowAlgorithms struct {
    operationsCount    int
    windowAdjustments  int
    maxWindowSize      int
}

func (sw *SlidingWindowAlgorithms) ResetCounters() {
    sw.operationsCount = 0
    sw.windowAdjustments = 0
    sw.maxWindowSize = 0
}

func (sw *SlidingWindowAlgorithms) GetStats() (int, int, int) {
    return sw.operationsCount, sw.windowAdjustments, sw.maxWindowSize
}
```

### 🧪 Demonstração Completa
```go
func demonstrarSlidingWindow() {
    sw := NewSlidingWindowAlgorithms()
    
    fmt.Println("=== Demonstração de Sliding Window em Go ===")
    
    // Maximum Sum Subarray
    nums := []int{2, 1, 5, 1, 3, 2}
    start := time.Now()
    maxSum := sw.MaxSumSubarray(nums, 3)
    duration := time.Since(start)
    
    fmt.Printf("Max Sum (k=3): %d\n", maxSum)
    fmt.Printf("Tempo: %.2fμs\n", float64(duration.Nanoseconds())/1e3)
    fmt.Printf("Operações: %d\n", sw.operationsCount)
}
```

## Compilação e Execução

### Executar Localmente
```bash
cd go/sliding_window
go run sliding_window_basico.go
```

### Compilar com Otimizações
```bash
go build -ldflags="-s -w" -o sliding_window_optimized sliding_window_basico.go
./sliding_window_optimized
```

### Executar com Profiling
```bash
go run -race sliding_window_basico.go  # Detectar race conditions
go run -cpuprofile=cpu.prof sliding_window_basico.go  # CPU profiling
```

## Vantagens da Implementação Go

### ✅ Benefícios
- **Maps eficientes**: Hash tables otimizadas nativas
- **Slices performáticos**: Arrays dinâmicos com baixo overhead
- **Strings Unicode**: Suporte nativo para UTF-8
- **Memory management**: GC automático eficiente
- **Tipagem forte**: Detecção de erros em compile-time

### 🎯 Casos de Uso Ideais
- **Stream processing**: Processamento de dados em tempo real
- **String algorithms**: Análise de texto e patterns
- **Time series analysis**: Análise de séries temporais
- **Network monitoring**: Análise de tráfego de rede
- **Financial algorithms**: Análise de dados financeiros

## Complexidade dos Algoritmos

| Algoritmo | Tempo | Espaço | Tipo de Janela |
|-----------|-------|--------|----------------|
| **Max Sum Subarray** | O(n) | O(1) | Tamanho fixo |
| **Longest Substring** | O(n) | O(min(m,n)) | Tamanho variável |
| **Minimum Window** | O(n+m) | O(m) | Tamanho variável |
| **Sliding Window Max** | O(n) | O(k) | Tamanho fixo |
| **Find Anagrams** | O(n+m) | O(m) | Tamanho fixo |
| **K Distinct Chars** | O(n) | O(k) | Tamanho variável |
| **Product Less Than K** | O(n) | O(1) | Tamanho variável |

## Patterns Idiomáticos Go

### 1. Generic Sliding Window Template
```go
func (sw *SlidingWindowAlgorithms) SlidingWindowTemplate(s string, pattern string) []int {
    if len(s) < len(pattern) {
        return []int{}
    }
    
    // Inicializar contadores
    patternCount := make(map[rune]int)
    for _, char := range pattern {
        patternCount[char]++
    }
    
    windowCount := make(map[rune]int)
    result := []int{}
    required := len(patternCount)
    formed := 0
    
    left := 0
    for right, char := range s {
        // Expandir janela
        windowCount[char]++
        if count, exists := patternCount[char]; exists && windowCount[char] == count {
            formed++
        }
        
        // Contrair janela se necessário
        for formed == required && left <= right {
            // Processar resultado válido
            if right-left+1 == len(pattern) {
                result = append(result, left)
            }
            
            leftChar := rune(s[left])
            windowCount[leftChar]--
            if count, exists := patternCount[leftChar]; exists && windowCount[leftChar] < count {
                formed--
            }
            left++
        }
    }
    
    return result
}
```

### 2. Interface para Sliding Window Problems
```go
type SlidingWindowProblem interface {
    IsValid(window interface{}) bool
    ShouldExpand(window interface{}) bool
    ShouldContract(window interface{}) bool
    ProcessResult(window interface{}) interface{}
}

func SolveGeneric(data []interface{}, problem SlidingWindowProblem) []interface{} {
    left := 0
    window := make([]interface{}, 0)
    results := []interface{}{}
    
    for right, element := range data {
        window = append(window, element)
        
        for !problem.ShouldExpand(window) && left <= right {
            if problem.IsValid(window) {
                results = append(results, problem.ProcessResult(window))
            }
            window = window[1:]
            left++
        }
    }
    
    return results
}
```

### 3. Error Handling e Validation
```go
func (sw *SlidingWindowAlgorithms) MaxSumSubarraySafe(nums []int, k int) (int, error) {
    if len(nums) == 0 {
        return 0, fmt.Errorf("array não pode estar vazio")
    }
    if k <= 0 {
        return 0, fmt.Errorf("k deve ser positivo, recebido: %d", k)
    }
    if k > len(nums) {
        return 0, fmt.Errorf("k (%d) maior que tamanho do array (%d)", k, len(nums))
    }
    
    result := sw.MaxSumSubarray(nums, k)
    return result, nil
}
```

## Testing e Benchmarking

### Unit Tests
```go
func TestMaxSumSubarray(t *testing.T) {
    sw := NewSlidingWindowAlgorithms()
    
    tests := []struct {
        nums     []int
        k        int
        expected int
    }{
        {[]int{2, 1, 5, 1, 3, 2}, 3, 9},
        {[]int{1, 2, 3, 4, 5}, 2, 9},
        {[]int{5}, 1, 5},
    }
    
    for _, tt := range tests {
        t.Run(fmt.Sprintf("nums=%v,k=%d", tt.nums, tt.k), func(t *testing.T) {
            result := sw.MaxSumSubarray(tt.nums, tt.k)
            if result != tt.expected {
                t.Errorf("MaxSumSubarray(%v, %d) = %d, esperado %d", 
                    tt.nums, tt.k, result, tt.expected)
            }
        })
    }
}
```

### Benchmarks
```go
func BenchmarkLongestSubstring(b *testing.B) {
    sw := NewSlidingWindowAlgorithms()
    s := strings.Repeat("abcdefghijklmnopqrstuvwxyz", 1000)
    
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        sw.LengthOfLongestSubstring(s)
        sw.ResetCounters()
    }
}

func BenchmarkSlidingWindowMaximum(b *testing.B) {
    sw := NewSlidingWindowAlgorithms()
    nums := make([]int, 10000)
    for i := range nums {
        nums[i] = rand.Intn(1000)
    }
    
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        sw.SlidingWindowMaximum(nums, 100)
        sw.ResetCounters()
    }
}
```

## Otimizações Específicas Go

### 1. Memory Pool para Strings
```go
var stringPool = sync.Pool{
    New: func() interface{} {
        return make([]rune, 0, 1000)
    },
}

func (sw *SlidingWindowAlgorithms) LongestSubstringPooled(s string) int {
    chars := stringPool.Get().([]rune)
    defer stringPool.Put(chars[:0])
    
    // Usar chars como buffer reutilizável
    return sw.processWithBuffer(s, chars)
}
```

### 2. Concurrent Processing
```go
func (sw *SlidingWindowAlgorithms) ProcessConcurrent(data [][]int, k int) <-chan int {
    results := make(chan int, len(data))
    
    var wg sync.WaitGroup
    for _, arr := range data {
        wg.Add(1)
        go func(nums []int) {
            defer wg.Done()
            result := sw.MaxSumSubarray(nums, k)
            results <- result
        }(arr)
    }
    
    go func() {
        wg.Wait()
        close(results)
    }()
    
    return results
}
```

### 3. Streaming Processing
```go
func (sw *SlidingWindowAlgorithms) ProcessStream(input <-chan int, k int) <-chan int {
    output := make(chan int)
    
    go func() {
        defer close(output)
        
        window := make([]int, 0, k)
        sum := 0
        
        for value := range input {
            window = append(window, value)
            sum += value
            
            if len(window) > k {
                sum -= window[0]
                window = window[1:]
            }
            
            if len(window) == k {
                output <- sum
            }
        }
    }()
    
    return output
}
```

## Aplicações Práticas

### 1. Log Analysis API
```go
func logAnalysisHandler(w http.ResponseWriter, r *http.Request) {
    var req struct {
        LogLines []string `json:"log_lines"`
        Pattern  string   `json:"pattern"`
    }
    
    json.NewDecoder(r.Body).Decode(&req)
    
    sw := NewSlidingWindowAlgorithms()
    
    // Encontrar todas as ocorrências do pattern
    results := []int{}
    for i, line := range req.LogLines {
        if sw.containsPattern(line, req.Pattern) {
            results = append(results, i)
        }
    }
    
    response := map[string]interface{}{
        "matches": results,
        "total":   len(results),
        "stats": map[string]int{
            "operations": sw.operationsCount,
        },
    }
    
    json.NewEncoder(w).Encode(response)
}
```

### 2. Real-time Monitoring
```go
func monitorDataStream() {
    sw := NewSlidingWindowAlgorithms()
    dataStream := make(chan int, 1000)
    
    // Simular stream de dados
    go func() {
        for {
            dataStream <- rand.Intn(100)
            time.Sleep(10 * time.Millisecond)
        }
    }()
    
    // Processar com sliding window
    windowSize := 10
    results := sw.ProcessStream(dataStream, windowSize)
    
    for avg := range results {
        if avg > 70 { // Threshold
            fmt.Printf("Alert: Average %.2f above threshold\n", float64(avg)/float64(windowSize))
        }
    }
}
```

### 3. File Processing CLI
```go
func main() {
    if len(os.Args) < 4 {
        fmt.Println("Uso: sliding_window <file> <algorithm> <parameter>")
        os.Exit(1)
    }
    
    filename := os.Args[1]
    algorithm := os.Args[2]
    param := os.Args[3]
    
    data := readDataFromFile(filename)
    sw := NewSlidingWindowAlgorithms()
    
    switch algorithm {
    case "maxsum":
        k, _ := strconv.Atoi(param)
        result := sw.MaxSumSubarray(data, k)
        fmt.Printf("Maximum sum: %d\n", result)
        
    case "distinct":
        k, _ := strconv.Atoi(param)
        content := readStringFromFile(filename)
        result := sw.LengthOfLongestSubstringKDistinct(content, k)
        fmt.Printf("Longest substring with %d distinct chars: %d\n", k, result)
    }
}
```

## Profiling e Otimização

### Memory Usage Analysis
```bash
go run -memprofile=mem.prof sliding_window_basico.go
go tool pprof mem.prof
(pprof) top10
(pprof) list SlidingWindowAlgorithms
```

### CPU Performance
```bash
go run -cpuprofile=cpu.prof sliding_window_basico.go
go tool pprof cpu.prof
(pprof) web  # Visualização gráfica
```

### Execution Tracing
```bash
go run -trace=trace.out sliding_window_basico.go
go tool trace trace.out
```

---

<div align="center">

## 👤 Autor | Author

<div align="center">
  <a href="https://github.com/matheussricardoo" target="_blank">
    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/matheus-ricardo-426452266/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn"/>
  </a>
</div>

## 📄 Licença | License

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../../LICENSE) para mais detalhes.

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

---

<div align="center">
  <i>🪟 "A janela deslizante em Go: eficiência que flui naturalmente"</i>
  <br>
  <i>🪟 "Sliding window in Go: efficiency that flows naturally"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=8E44AD&height=120&section=footer"/>

</div>
