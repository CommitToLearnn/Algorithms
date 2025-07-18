<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E74C3C&height=120&section=header&text=Two%20Pointer%20-%20Go&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Implementação%20em%20Go%20da%20Técnica%20de%20Dois%20Ponteiros&descAlignY=65&descSize=16">

</div>

# Two Pointer - Implementação em Go

## Descrição

Esta implementação em Go demonstra a técnica de dois ponteiros através de 6 algoritmos fundamentais. A linguagem Go oferece excelente performance e sintaxe clara para implementar estes algoritmos de forma eficiente.

## Algoritmos Implementados

### 1. Two Sum em Array Ordenado
```go
func (tp *TwoPointerAlgorithms) TwoSumSorted(nums []int, target int) []int {
    left, right := 0, len(nums)-1
    
    for left < right {
        currentSum := nums[left] + nums[right]
        if currentSum == target {
            return []int{left, right}
        } else if currentSum < target {
            left++
        } else {
            right--
        }
    }
    return []int{}
}
```

### 2. Verificação de Palíndromo
```go
func (tp *TwoPointerAlgorithms) IsPalindrome(s string) bool {
    left, right := 0, len(s)-1
    
    for left < right {
        if s[left] != s[right] {
            return false
        }
        left++
        right--
    }
    return true
}
```

### 3. Remoção de Duplicatas
```go
func (tp *TwoPointerAlgorithms) RemoveDuplicates(nums []int) int {
    if len(nums) <= 1 {
        return len(nums)
    }
    
    writePos := 1
    for readPos := 1; readPos < len(nums); readPos++ {
        if nums[readPos] != nums[readPos-1] {
            nums[writePos] = nums[readPos]
            writePos++
        }
    }
    return writePos
}
```

### 4. Container com Mais Água
```go
func (tp *TwoPointerAlgorithms) ContainerWithMostWater(heights []int) int {
    left, right := 0, len(heights)-1
    maxArea := 0
    
    for left < right {
        width := right - left
        height := int(math.Min(float64(heights[left]), float64(heights[right])))
        area := width * height
        maxArea = int(math.Max(float64(maxArea), float64(area)))
        
        if heights[left] < heights[right] {
            left++
        } else {
            right--
        }
    }
    return maxArea
}
```

### 5. Three Sum
```go
func (tp *TwoPointerAlgorithms) ThreeSum(nums []int) [][]int {
    sort.Ints(nums)
    result := [][]int{}
    
    for i := 0; i < len(nums)-2; i++ {
        if i > 0 && nums[i] == nums[i-1] {
            continue // Pular duplicatas
        }
        
        left, right := i+1, len(nums)-1
        for left < right {
            currentSum := nums[i] + nums[left] + nums[right]
            if currentSum == 0 {
                result = append(result, []int{nums[i], nums[left], nums[right]})
                // Pular duplicatas...
                left++
                right--
            } else if currentSum < 0 {
                left++
            } else {
                right--
            }
        }
    }
    return result
}
```

### 6. Sort Colors (Dutch National Flag)
```go
func (tp *TwoPointerAlgorithms) SortColors(nums []int) {
    low, mid, high := 0, 0, len(nums)-1
    
    for mid <= high {
        switch nums[mid] {
        case 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low++
            mid++
        case 1:
            mid++
        case 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high--
        }
    }
}
```

## Características da Implementação Go

### 🚀 Performance
- **Compilação nativa**: Binário otimizado
- **Garbage Collection eficiente**: Baixa latência
- **Concorrência nativa**: Goroutines (se necessário)
- **Tipos nativos**: `int`, `[]int`, `string`

### 📊 Monitoramento
```go
type TwoPointerAlgorithms struct {
    operationsCount  int
    comparisonsCount int
}

func (tp *TwoPointerAlgorithms) ResetCounters() {
    tp.operationsCount = 0
    tp.comparisonsCount = 0
}
```

### 🧪 Demonstração Completa
```go
func demonstrarTwoPointer() {
    tp := NewTwoPointerAlgorithms()
    
    // Exemplos práticos com medição de tempo
    start := time.Now()
    result := tp.TwoSumSorted([]int{2, 7, 11, 15}, 9)
    duration := time.Since(start)
    
    fmt.Printf("Resultado: %v\n", result)
    fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)
}
```

## Compilação e Execução

### Executar Localmente
```bash
cd go/two_pointer
go run two_pointer_basico.go
```

### Compilar Binário
```bash
go build -o two_pointer two_pointer_basico.go
./two_pointer
```

### Executar com Profiling
```bash
go run -race two_pointer_basico.go  # Detectar race conditions
go run -cpuprofile=cpu.prof two_pointer_basico.go  # CPU profiling
```

## Vantagens da Implementação Go

### ✅ Benefícios
- **Performance nativa**: Velocidade comparável a C/C++
- **Sintaxe limpa**: Código legível e mantível
- **Tipagem estática**: Detecção de erros em tempo de compilação
- **Padrões idiomáticos**: Seguindo convenções Go
- **Gerenciamento de memória**: GC automático eficiente

### 🎯 Casos de Uso Ideais
- **Sistemas de alto desempenho**
- **Microserviços**
- **Processamento de dados em larga escala**
- **APIs REST de alta throughput**
- **Ferramentas de linha de comando**

## Complexidade dos Algoritmos

| Algoritmo | Tempo | Espaço | Observações |
|-----------|-------|--------|-------------|
| **Two Sum Sorted** | O(n) | O(1) | Array deve estar ordenado |
| **Is Palindrome** | O(n) | O(1) | Verificação linear |
| **Remove Duplicates** | O(n) | O(1) | Modificação in-place |
| **Container Water** | O(n) | O(1) | Otimização greedy |
| **Three Sum** | O(n²) | O(1) | Sem espaço extra para solução |
| **Sort Colors** | O(n) | O(1) | Particionamento em 3 vias |

## Comparação de Performance

### Go vs Outras Linguagens
```go
// Teste com 1M elementos
largeArray := make([]int, 1000000)
for i := range largeArray {
    largeArray[i] = i * 2
}

start := time.Now()
result := tp.TwoSumSorted(largeArray, 1999998)
duration := time.Since(start)

// Go típico: ~1-2ms
// Python típico: ~10-20ms  
// Java típico: ~2-5ms
```

## Patterns Idiomáticos Go

### 1. Error Handling
```go
func (tp *TwoPointerAlgorithms) TwoSumSortedSafe(nums []int, target int) ([]int, error) {
    if len(nums) < 2 {
        return nil, fmt.Errorf("array deve ter pelo menos 2 elementos")
    }
    
    result := tp.TwoSumSorted(nums, target)
    if len(result) == 0 {
        return nil, fmt.Errorf("nenhum par encontrado que soma %d", target)
    }
    
    return result, nil
}
```

### 2. Interface Design
```go
type TwoPointerSolver interface {
    TwoSumSorted([]int, int) []int
    IsPalindrome(string) bool
    RemoveDuplicates([]int) int
}

// Implementação automática
var _ TwoPointerSolver = (*TwoPointerAlgorithms)(nil)
```

### 3. Benchmarking
```go
func BenchmarkTwoSum(b *testing.B) {
    tp := NewTwoPointerAlgorithms()
    nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        tp.TwoSumSorted(nums, 15)
    }
}
```

## Testing em Go

### Unit Tests
```bash
# Criar arquivo two_pointer_test.go
go test ./...                 # Executar todos os testes
go test -v                    # Verbose output
go test -bench=.              # Executar benchmarks
go test -race                 # Detectar race conditions
go test -cover                # Coverage report
```

### Exemplo de Teste
```go
func TestTwoSumSorted(t *testing.T) {
    tp := NewTwoPointerAlgorithms()
    
    tests := []struct {
        nums   []int
        target int
        want   []int
    }{
        {[]int{2, 7, 11, 15}, 9, []int{0, 1}},
        {[]int{1, 2, 3, 4}, 7, []int{2, 3}},
        {[]int{1, 2}, 5, []int{}},
    }
    
    for _, tt := range tests {
        got := tp.TwoSumSorted(tt.nums, tt.target)
        if !reflect.DeepEqual(got, tt.want) {
            t.Errorf("TwoSumSorted(%v, %d) = %v, want %v", 
                tt.nums, tt.target, got, tt.want)
        }
    }
}
```

## Aplicações Práticas em Go

### 1. HTTP Handler
```go
func twoSumHandler(w http.ResponseWriter, r *http.Request) {
    var req struct {
        Numbers []int `json:"numbers"`
        Target  int   `json:"target"`
    }
    
    json.NewDecoder(r.Body).Decode(&req)
    
    tp := NewTwoPointerAlgorithms()
    result := tp.TwoSumSorted(req.Numbers, req.Target)
    
    json.NewEncoder(w).Encode(map[string]interface{}{
        "indices": result,
        "found":   len(result) > 0,
    })
}
```

### 2. CLI Tool
```go
func main() {
    if len(os.Args) < 3 {
        fmt.Println("Uso: two_pointer <números> <target>")
        os.Exit(1)
    }
    
    // Parse argumentos e executar algoritmo
    tp := NewTwoPointerAlgorithms()
    // ... implementação CLI
}
```

### 3. Concurrent Processing
```go
func processBatch(nums [][]int, targets []int) <-chan []int {
    results := make(chan []int, len(nums))
    
    for i, arr := range nums {
        go func(arr []int, target int) {
            tp := NewTwoPointerAlgorithms()
            result := tp.TwoSumSorted(arr, target)
            results <- result
        }(arr, targets[i])
    }
    
    return results
}
```

## Recursos Avançados

### Memory Profiling
```bash
go run -memprofile=mem.prof two_pointer_basico.go
go tool pprof mem.prof
```

### CPU Profiling
```bash
go run -cpuprofile=cpu.prof two_pointer_basico.go
go tool pprof cpu.prof
```

### Build Optimization
```bash
go build -ldflags="-s -w" -o two_pointer_optimized  # Strip debug info
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
  <i>🐹 "Simplicidade é a sofisticação suprema em Go"</i>
  <br>
  <i>🐹 "Simplicity is the ultimate sophistication in Go"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E74C3C&height=120&section=footer"/>

</div>
