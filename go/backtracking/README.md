<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=C0392B&height=120&section=header&text=Backtracking%20-%20Go&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Implementação%20em%20Go%20de%20Algoritmos%20de%20Backtracking&descAlignY=65&descSize=16">

</div>

# Backtracking - Implementação em Go

## Descrição

Esta implementação em Go demonstra a técnica de backtracking através de 6 algoritmos fundamentais. Go oferece excelente performance para algoritmos recursivos e permite implementações elegantes com suas estruturas de dados nativas.

## Algoritmos Implementados

### 1. N-Queens Problem
```go
func (ba *BacktrackingAlgorithms) NQueens(n int) [][]string {
    result := [][]string{}
    board := make([][]rune, n)
    for i := range board {
        board[i] = make([]rune, n)
        for j := range board[i] {
            board[i][j] = '.'
        }
    }
    
    var backtrack func(row int)
    backtrack = func(row int) {
        ba.recursionCount++
        if row == n {
            solution := []string{}
            for _, rowRunes := range board {
                solution = append(solution, string(rowRunes))
            }
            result = append(result, solution)
            return
        }
        
        for col := 0; col < n; col++ {
            if ba.isQueenSafe(board, row, col, n) {
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.' // Backtrack
            }
        }
    }
    
    backtrack(0)
    return result
}
```

### 2. Sudoku Solver
```go
func (ba *BacktrackingAlgorithms) SolveSudoku(board [][]rune) bool {
    return ba.solveSudokuHelper(board)
}

func (ba *BacktrackingAlgorithms) solveSudokuHelper(board [][]rune) bool {
    ba.recursionCount++
    
    for row := 0; row < 9; row++ {
        for col := 0; col < 9; col++ {
            if board[row][col] == '.' {
                for num := '1'; num <= '9'; num++ {
                    if ba.isValidSudoku(board, row, col, num) {
                        board[row][col] = num
                        if ba.solveSudokuHelper(board) {
                            return true
                        }
                        board[row][col] = '.' // Backtrack
                    }
                }
                return false
            }
        }
    }
    return true
}
```

### 3. Generate Permutations
```go
func (ba *BacktrackingAlgorithms) Permutations(nums []int) [][]int {
    result := [][]int{}
    
    var backtrack func(current []int)
    backtrack = func(current []int) {
        ba.recursionCount++
        if len(current) == len(nums) {
            perm := make([]int, len(current))
            copy(perm, current)
            result = append(result, perm)
            return
        }
        
        for _, num := range nums {
            if !contains(current, num) {
                current = append(current, num)
                backtrack(current)
                current = current[:len(current)-1] // Backtrack
            }
        }
    }
    
    backtrack([]int{})
    return result
}
```

### 4. Generate Combinations
```go
func (ba *BacktrackingAlgorithms) Combinations(n, k int) [][]int {
    result := [][]int{}
    
    var backtrack func(start int, current []int)
    backtrack = func(start int, current []int) {
        ba.recursionCount++
        if len(current) == k {
            comb := make([]int, len(current))
            copy(comb, current)
            result = append(result, comb)
            return
        }
        
        for i := start; i <= n; i++ {
            current = append(current, i)
            backtrack(i+1, current)
            current = current[:len(current)-1] // Backtrack
        }
    }
    
    backtrack(1, []int{})
    return result
}
```

### 5. Word Search
```go
func (ba *BacktrackingAlgorithms) WordSearch(board [][]rune, word string) bool {
    rows, cols := len(board), len(board[0])
    
    var dfs func(row, col, index int) bool
    dfs = func(row, col, index int) bool {
        ba.recursionCount++
        if index == len(word) {
            return true
        }
        
        if row < 0 || row >= rows || col < 0 || col >= cols || 
           board[row][col] != rune(word[index]) {
            return false
        }
        
        temp := board[row][col]
        board[row][col] = '#' // Marcar como visitado
        
        found := dfs(row+1, col, index+1) ||
                dfs(row-1, col, index+1) ||
                dfs(row, col+1, index+1) ||
                dfs(row, col-1, index+1)
        
        board[row][col] = temp // Backtrack
        return found
    }
    
    for row := 0; row < rows; row++ {
        for col := 0; col < cols; col++ {
            if dfs(row, col, 0) {
                return true
            }
        }
    }
    return false
}
```

### 6. Subset Sum
```go
func (ba *BacktrackingAlgorithms) SubsetSum(nums []int, target int) bool {
    var backtrack func(index, currentSum int) bool
    backtrack = func(index, currentSum int) bool {
        ba.recursionCount++
        if currentSum == target {
            return true
        }
        if index >= len(nums) || currentSum > target {
            return false
        }
        
        // Incluir o número atual
        if backtrack(index+1, currentSum+nums[index]) {
            return true
        }
        
        // Excluir o número atual
        return backtrack(index+1, currentSum)
    }
    
    return backtrack(0, 0)
}
```

## Características da Implementação Go

### 🚀 Performance e Recursão
- **Stack nativo**: Recursão eficiente com stack do sistema
- **Garbage Collection**: Gerenciamento automático de memória
- **Closures**: Funções aninhadas para backtracking elegante
- **Slices dinâmicos**: Estruturas de dados flexíveis

### 📊 Monitoramento de Performance
```go
type BacktrackingAlgorithms struct {
    recursionCount   int
    backtrackCount   int
    solutionsFound   int
}

func (ba *BacktrackingAlgorithms) ResetCounters() {
    ba.recursionCount = 0
    ba.backtrackCount = 0
    ba.solutionsFound = 0
}

func (ba *BacktrackingAlgorithms) GetStats() (int, int, int) {
    return ba.recursionCount, ba.backtrackCount, ba.solutionsFound
}
```

### 🧪 Demonstração Completa
```go
func demonstrarBacktracking() {
    ba := NewBacktrackingAlgorithms()
    
    fmt.Println("=== Demonstração de Backtracking em Go ===")
    
    // N-Queens
    start := time.Now()
    queens := ba.NQueens(4)
    duration := time.Since(start)
    
    fmt.Printf("4-Queens: %d soluções encontradas\n", len(queens))
    fmt.Printf("Tempo: %.2fms\n", float64(duration.Nanoseconds())/1e6)
    fmt.Printf("Recursões: %d\n", ba.recursionCount)
}
```

## Compilação e Execução

### Executar Localmente
```bash
cd go/backtracking
go run backtracking_basico.go
```

### Compilar com Otimizações
```bash
go build -ldflags="-s -w" -o backtracking_optimized backtracking_basico.go
./backtracking_optimized
```

### Executar com Profiling
```bash
go run -race backtracking_basico.go  # Detectar race conditions
go run -cpuprofile=cpu.prof backtracking_basico.go  # CPU profiling
```

## Vantagens da Implementação Go

### ✅ Benefícios
- **Recursão eficiente**: Stack nativo otimizado
- **Sintaxe clara**: Closures e funções aninhadas elegantes
- **Performance nativa**: Velocidade comparável a C/C++
- **Garbage Collection**: Sem vazamentos de memória
- **Concorrência**: Goroutines para paralelização (quando aplicável)

### 🎯 Casos de Uso Ideais
- **Solvers de puzzle**: Sudoku, N-Queens, etc.
- **Otimização combinatorial**
- **Geração de permutações/combinações**
- **Problemas de busca em grafos**
- **AI e algoritmos de decisão**

## Complexidade dos Algoritmos

| Algoritmo | Tempo | Espaço | Características |
|-----------|-------|--------|-----------------|
| **N-Queens** | O(N!) | O(N²) | Exponencial - todas as permutações |
| **Sudoku Solver** | O(9^(n²)) | O(n²) | Pior caso - todas as possibilidades |
| **Permutations** | O(N!) | O(N) | Fatorial - todas as ordenações |
| **Combinations** | O(2^N) | O(k) | Exponencial - todos os subconjuntos |
| **Word Search** | O(N*M*4^L) | O(L) | L = comprimento da palavra |
| **Subset Sum** | O(2^N) | O(N) | Todos os subconjuntos possíveis |

## Patterns Idiomáticos Go

### 1. Function Closures para Backtracking
```go
func (ba *BacktrackingAlgorithms) solveWithBacktrack(problem interface{}) interface{} {
    var backtrack func(state interface{}) bool
    backtrack = func(state interface{}) bool {
        ba.recursionCount++
        
        if isComplete(state) {
            return true
        }
        
        for _, choice := range getChoices(state) {
            makeChoice(state, choice)
            if backtrack(state) {
                return true
            }
            undoChoice(state, choice) // Backtrack
        }
        
        return false
    }
    
    return backtrack(initialState(problem))
}
```

### 2. Interface para Problemas de Backtracking
```go
type BacktrackProblem interface {
    IsComplete() bool
    GetChoices() []interface{}
    MakeChoice(choice interface{})
    UndoChoice(choice interface{})
    IsValid() bool
}

func SolveGeneric(problem BacktrackProblem) bool {
    if problem.IsComplete() {
        return true
    }
    
    for _, choice := range problem.GetChoices() {
        problem.MakeChoice(choice)
        if problem.IsValid() && SolveGeneric(problem) {
            return true
        }
        problem.UndoChoice(choice)
    }
    
    return false
}
```

### 3. Error Handling e Validation
```go
func (ba *BacktrackingAlgorithms) NQueensSafe(n int) ([][]string, error) {
    if n <= 0 {
        return nil, fmt.Errorf("n deve ser positivo, recebido: %d", n)
    }
    if n > 20 {
        return nil, fmt.Errorf("n muito grande (%d), pode causar timeout", n)
    }
    
    result := ba.NQueens(n)
    if len(result) == 0 {
        return nil, fmt.Errorf("nenhuma solução encontrada para n=%d", n)
    }
    
    return result, nil
}
```

## Testing e Benchmarking

### Unit Tests
```go
func TestNQueens(t *testing.T) {
    ba := NewBacktrackingAlgorithms()
    
    tests := []struct {
        n        int
        expected int
    }{
        {1, 1},
        {4, 2},
        {8, 92},
    }
    
    for _, tt := range tests {
        t.Run(fmt.Sprintf("n=%d", tt.n), func(t *testing.T) {
            result := ba.NQueens(tt.n)
            if len(result) != tt.expected {
                t.Errorf("NQueens(%d) = %d soluções, esperado %d", 
                    tt.n, len(result), tt.expected)
            }
        })
    }
}
```

### Benchmarks
```go
func BenchmarkNQueens(b *testing.B) {
    ba := NewBacktrackingAlgorithms()
    
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        ba.NQueens(8)
        ba.ResetCounters()
    }
}

func BenchmarkPermutations(b *testing.B) {
    ba := NewBacktrackingAlgorithms()
    nums := []int{1, 2, 3, 4, 5}
    
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        ba.Permutations(nums)
        ba.ResetCounters()
    }
}
```

## Otimizações Específicas Go

### 1. Memory Pool para Reutilização
```go
var solutionPool = sync.Pool{
    New: func() interface{} {
        return make([][]int, 0, 1000)
    },
}

func (ba *BacktrackingAlgorithms) PermutationsPooled(nums []int) [][]int {
    result := solutionPool.Get().([][]int)
    defer solutionPool.Put(result[:0])
    
    // ... implementação usando result
    
    finalResult := make([][]int, len(result))
    copy(finalResult, result)
    return finalResult
}
```

### 2. Concurrent Backtracking
```go
func (ba *BacktrackingAlgorithms) NQueensConcurrent(n int) [][]string {
    solutions := make(chan []string, 1000)
    var wg sync.WaitGroup
    
    // Dividir problema por primeira linha
    for firstCol := 0; firstCol < n; firstCol++ {
        wg.Add(1)
        go func(col int) {
            defer wg.Done()
            // Resolver subproblema iniciando com rainha na posição (0, col)
            partialSolutions := ba.solveFromPosition(n, 0, col)
            for _, sol := range partialSolutions {
                solutions <- sol
            }
        }(firstCol)
    }
    
    go func() {
        wg.Wait()
        close(solutions)
    }()
    
    result := [][]string{}
    for sol := range solutions {
        result = append(result, sol)
    }
    
    return result
}
```

### 3. Iterative Deepening
```go
func (ba *BacktrackingAlgorithms) NQueensIterativeDeepening(n, maxDepth int) [][]string {
    for depth := 1; depth <= maxDepth; depth++ {
        ba.ResetCounters()
        solutions := ba.nQueensWithDepthLimit(n, depth)
        
        if len(solutions) > 0 {
            fmt.Printf("Soluções encontradas na profundidade %d\n", depth)
            return solutions
        }
    }
    return [][]string{}
}
```

## Aplicações Práticas

### 1. Solver Web API
```go
func sudokuHandler(w http.ResponseWriter, r *http.Request) {
    var req struct {
        Board [][]string `json:"board"`
    }
    
    json.NewDecoder(r.Body).Decode(&req)
    
    // Converter para [][]rune
    board := make([][]rune, 9)
    for i := range board {
        board[i] = make([]rune, 9)
        for j := range board[i] {
            if req.Board[i][j] == "" {
                board[i][j] = '.'
            } else {
                board[i][j] = rune(req.Board[i][j][0])
            }
        }
    }
    
    ba := NewBacktrackingAlgorithms()
    solved := ba.SolveSudoku(board)
    
    response := map[string]interface{}{
        "solved": solved,
        "board":  board,
        "stats": map[string]int{
            "recursions": ba.recursionCount,
        },
    }
    
    json.NewEncoder(w).Encode(response)
}
```

### 2. CLI Puzzle Solver
```go
func main() {
    if len(os.Args) < 2 {
        fmt.Println("Uso: solver <puzzle_type> [args...]")
        os.Exit(1)
    }
    
    ba := NewBacktrackingAlgorithms()
    
    switch os.Args[1] {
    case "nqueens":
        n, _ := strconv.Atoi(os.Args[2])
        solutions := ba.NQueens(n)
        fmt.Printf("Encontradas %d soluções para %d-Queens\n", len(solutions), n)
        
    case "sudoku":
        board := readSudokuFromFile(os.Args[2])
        if ba.SolveSudoku(board) {
            printSudoku(board)
        } else {
            fmt.Println("Sudoku não tem solução")
        }
    }
}
```

### 3. Performance Testing Framework
```go
func runPerformanceTests() {
    problems := []struct {
        name string
        fn   func() interface{}
    }{
        {"4-Queens", func() interface{} { return ba.NQueens(4) }},
        {"8-Queens", func() interface{} { return ba.NQueens(8) }},
        {"Permutations-5", func() interface{} { return ba.Permutations([]int{1,2,3,4,5}) }},
    }
    
    for _, problem := range problems {
        start := time.Now()
        result := problem.fn()
        duration := time.Since(start)
        
        fmt.Printf("%s: %.2fms\n", problem.name, float64(duration.Nanoseconds())/1e6)
    }
}
```

## Profiling e Otimização

### CPU Profiling
```bash
go run -cpuprofile=cpu.prof backtracking_basico.go
go tool pprof cpu.prof
```

### Memory Profiling
```bash
go run -memprofile=mem.prof backtracking_basico.go
go tool pprof mem.prof
```

### Trace Analysis
```bash
go run -trace=trace.out backtracking_basico.go
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
  <i>🔄 "No backtracking, cada passo para trás é um passo para frente em Go"</i>
  <br>
  <i>🔄 "In backtracking, every step back is a step forward in Go"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=C0392B&height=120&section=footer"/>

</div>
