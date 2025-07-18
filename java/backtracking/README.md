<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=9B59B6&height=120&section=header&text=Backtracking%20-%20Java&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Implementação%20em%20Java%20de%20Algoritmos%20de%20Backtracking&descAlignY=65&descSize=16">

</div>

# Backtracking - Implementação em Java

## Descrição

Esta implementação em Java demonstra a técnica de backtracking através de 6 algoritmos fundamentais. Java oferece robustez, orientação a objetos e excelente suporte para recursão, tornando-se ideal para implementar algoritmos de backtracking complexos de forma escalável.

## Algoritmos Implementados

### 1. N-Queens Problem
```java
public List<List<String>> nQueens(int n) {
    List<List<String>> result = new ArrayList<>();
    char[][] board = new char[n][n];
    
    // Inicializar tabuleiro
    for (int i = 0; i < n; i++) {
        Arrays.fill(board[i], '.');
    }
    
    backtrackQueens(board, 0, result);
    return result;
}

private void backtrackQueens(char[][] board, int row, List<List<String>> result) {
    recursionCount++;
    
    if (row == board.length) {
        result.add(constructSolution(board));
        solutionsFound++;
        return;
    }
    
    for (int col = 0; col < board.length; col++) {
        if (isQueenSafe(board, row, col)) {
            board[row][col] = 'Q';  // Fazer escolha
            backtrackQueens(board, row + 1, result);
            board[row][col] = '.';  // Desfazer escolha (backtrack)
            backtrackCount++;
        }
    }
}
```

### 2. Sudoku Solver
```java
public boolean solveSudoku(char[][] board) {
    return backtrackSudoku(board);
}

private boolean backtrackSudoku(char[][] board) {
    recursionCount++;
    
    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            if (board[row][col] == '.') {
                for (char num = '1'; num <= '9'; num++) {
                    if (isValidSudoku(board, row, col, num)) {
                        board[row][col] = num;  // Fazer escolha
                        
                        if (backtrackSudoku(board)) {
                            return true;
                        }
                        
                        board[row][col] = '.';  // Desfazer escolha
                        backtrackCount++;
                    }
                }
                return false;  // Nenhum número válido encontrado
            }
        }
    }
    return true;  // Tabuleiro completo
}
```

### 3. Generate Permutations
```java
public List<List<Integer>> permutations(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    List<Integer> current = new ArrayList<>();
    boolean[] used = new boolean[nums.length];
    
    backtrackPermutations(nums, current, used, result);
    return result;
}

private void backtrackPermutations(int[] nums, List<Integer> current, 
                                 boolean[] used, List<List<Integer>> result) {
    recursionCount++;
    
    if (current.size() == nums.length) {
        result.add(new ArrayList<>(current));
        solutionsFound++;
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        if (!used[i]) {
            current.add(nums[i]);      // Fazer escolha
            used[i] = true;
            
            backtrackPermutations(nums, current, used, result);
            
            current.remove(current.size() - 1);  // Desfazer escolha
            used[i] = false;
            backtrackCount++;
        }
    }
}
```

### 4. Generate Combinations
```java
public List<List<Integer>> combinations(int n, int k) {
    List<List<Integer>> result = new ArrayList<>();
    List<Integer> current = new ArrayList<>();
    
    backtrackCombinations(1, n, k, current, result);
    return result;
}

private void backtrackCombinations(int start, int n, int k, 
                                 List<Integer> current, List<List<Integer>> result) {
    recursionCount++;
    
    if (current.size() == k) {
        result.add(new ArrayList<>(current));
        solutionsFound++;
        return;
    }
    
    for (int i = start; i <= n; i++) {
        current.add(i);  // Fazer escolha
        backtrackCombinations(i + 1, n, k, current, result);
        current.remove(current.size() - 1);  // Desfazer escolha
        backtrackCount++;
    }
}
```

### 5. Word Search
```java
public boolean wordSearch(char[][] board, String word) {
    int rows = board.length;
    int cols = board[0].length;
    
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (dfsWordSearch(board, word, row, col, 0)) {
                return true;
            }
        }
    }
    return false;
}

private boolean dfsWordSearch(char[][] board, String word, int row, int col, int index) {
    recursionCount++;
    
    if (index == word.length()) {
        return true;
    }
    
    if (row < 0 || row >= board.length || col < 0 || col >= board[0].length ||
        board[row][col] != word.charAt(index)) {
        return false;
    }
    
    char temp = board[row][col];
    board[row][col] = '#';  // Marcar como visitado
    
    boolean found = dfsWordSearch(board, word, row + 1, col, index + 1) ||
                   dfsWordSearch(board, word, row - 1, col, index + 1) ||
                   dfsWordSearch(board, word, row, col + 1, index + 1) ||
                   dfsWordSearch(board, word, row, col - 1, index + 1);
    
    board[row][col] = temp;  // Restaurar (backtrack)
    backtrackCount++;
    
    return found;
}
```

### 6. Subset Sum
```java
public boolean subsetSum(int[] nums, int target) {
    return backtrackSubsetSum(nums, 0, 0, target);
}

private boolean backtrackSubsetSum(int[] nums, int index, int currentSum, int target) {
    recursionCount++;
    
    if (currentSum == target) {
        return true;
    }
    
    if (index >= nums.length || currentSum > target) {
        return false;
    }
    
    // Incluir o número atual
    if (backtrackSubsetSum(nums, index + 1, currentSum + nums[index], target)) {
        return true;
    }
    
    // Excluir o número atual
    return backtrackSubsetSum(nums, index + 1, currentSum, target);
}
```

## Características da Implementação Java

### ☕ Orientação a Objetos Avançada
- **Encapsulamento**: Métodos auxiliares privados bem definidos
- **Collections Framework**: ArrayList, List para flexibilidade
- **Generic Types**: Type safety com `List<List<Integer>>`
- **Method Overloading**: Múltiplas assinaturas para flexibilidade

### 📊 Monitoramento Abrangente
```java
public class BacktrackingBasico {
    private int recursionCount;
    private int backtrackCount;
    private int solutionsFound;
    private long executionTime;
    
    public void resetCounters() {
        this.recursionCount = 0;
        this.backtrackCount = 0;
        this.solutionsFound = 0;
        this.executionTime = 0;
    }
    
    public BacktrackingStats getStats() {
        return new BacktrackingStats(
            recursionCount, backtrackCount, solutionsFound, executionTime
        );
    }
}

public class BacktrackingStats {
    private final int recursions;
    private final int backtracks;
    private final int solutions;
    private final long executionTimeNs;
    
    // Getters e métodos de cálculo...
    public double getBacktrackRatio() {
        return recursions > 0 ? (double) backtracks / recursions : 0.0;
    }
    
    public double getSolutionEfficiency() {
        return recursions > 0 ? (double) solutions / recursions : 0.0;
    }
}
```

### 🧪 Demonstração Completa
```java
public static void main(String[] args) {
    BacktrackingBasico bt = new BacktrackingBasico();
    
    System.out.println("=== Demonstração de Backtracking em Java ===");
    
    // N-Queens
    long startTime = System.nanoTime();
    List<List<String>> queens = bt.nQueens(4);
    long endTime = System.nanoTime();
    
    System.out.printf("4-Queens: %d soluções encontradas%n", queens.size());
    System.out.printf("Tempo: %.2f ms%n", (endTime - startTime) / 1_000_000.0);
    
    BacktrackingStats stats = bt.getStats();
    System.out.printf("Recursões: %d%n", stats.getRecursions());
    System.out.printf("Backtracks: %d%n", stats.getBacktracks());
    System.out.printf("Eficiência: %.2f%%%n", stats.getSolutionEfficiency() * 100);
}
```

## Compilação e Execução

### Compilar e Executar
```bash
cd java/backtracking
javac BacktrackingBasico.java
java BacktrackingBasico
```

### Executar com JVM Tuning
```bash
java -Xms1g -Xmx4g BacktrackingBasico           # Aumentar heap para problemas grandes
java -XX:+UseG1GC BacktrackingBasico            # Usar G1GC para melhor latência
java -XX:+PrintGCDetails BacktrackingBasico     # Debug GC para análise
```

### Profiling com JProfiler
```bash
java -agentpath:/path/to/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849 BacktrackingBasico
```

## Vantagens da Implementação Java

### ✅ Benefícios Empresariais
- **Escalabilidade**: Suporte robusto para problemas grandes
- **Manutenibilidade**: Código bem estruturado e legível
- **Testabilidade**: Frameworks de teste maduros (JUnit, TestNG)
- **Debugging**: Ferramentas avançadas de debugging
- **Monitoramento**: JMX, profilers, APM tools

### 🎯 Casos de Uso Corporativos
- **Sistemas de otimização**
- **Engines de scheduling**
- **Solvers para puzzles corporativos**
- **Algoritmos de decisão em IA**
- **Sistemas de configuração automática**

## Complexidade e Performance

| Algoritmo | Tempo | Espaço | Características Java |
|-----------|-------|--------|---------------------|
| **N-Queens** | O(N!) | O(N²) | Arrays 2D, recursão profunda |
| **Sudoku Solver** | O(9^(n²)) | O(n²) | char[][] para eficiência |
| **Permutations** | O(N!) | O(N) | ArrayList dinâmico |
| **Combinations** | O(2^N) | O(k) | Recursão com poda |
| **Word Search** | O(N*M*4^L) | O(L) | DFS com backtrack |
| **Subset Sum** | O(2^N) | O(N) | Recursão binary choice |

## Design Patterns para Backtracking

### 1. Template Method Pattern
```java
public abstract class BacktrackingTemplate<T> {
    protected int recursionCount = 0;
    protected int backtrackCount = 0;
    
    public final List<T> solve(Object problem) {
        List<T> solutions = new ArrayList<>();
        T initialState = createInitialState(problem);
        backtrack(initialState, solutions);
        return solutions;
    }
    
    protected final void backtrack(T state, List<T> solutions) {
        recursionCount++;
        
        if (isComplete(state)) {
            solutions.add(cloneState(state));
            return;
        }
        
        for (Object choice : getChoices(state)) {
            if (isValid(state, choice)) {
                makeChoice(state, choice);
                backtrack(state, solutions);
                undoChoice(state, choice);
                backtrackCount++;
            }
        }
    }
    
    // Métodos abstratos que subclasses devem implementar
    protected abstract T createInitialState(Object problem);
    protected abstract boolean isComplete(T state);
    protected abstract List<Object> getChoices(T state);
    protected abstract boolean isValid(T state, Object choice);
    protected abstract void makeChoice(T state, Object choice);
    protected abstract void undoChoice(T state, Object choice);
    protected abstract T cloneState(T state);
}
```

### 2. Strategy Pattern para Diferentes Algoritmos
```java
public interface BacktrackingStrategy<T> {
    List<T> solve(Object problem);
    BacktrackingStats getStats();
}

public class NQueensStrategy implements BacktrackingStrategy<List<String>> {
    private final BacktrackingBasico solver = new BacktrackingBasico();
    
    @Override
    public List<List<String>> solve(Object problem) {
        Integer n = (Integer) problem;
        return solver.nQueens(n);
    }
    
    @Override
    public BacktrackingStats getStats() {
        return solver.getStats();
    }
}

public class BacktrackingContext {
    private BacktrackingStrategy<?> strategy;
    
    public void setStrategy(BacktrackingStrategy<?> strategy) {
        this.strategy = strategy;
    }
    
    public Object solve(Object problem) {
        return strategy.solve(problem);
    }
}
```

### 3. Observer Pattern para Monitoramento
```java
public interface BacktrackingObserver {
    void onRecursionStart(int depth, Object state);
    void onRecursionEnd(int depth, Object state);
    void onBacktrack(int depth, Object state);
    void onSolutionFound(Object solution);
}

public class BacktrackingSubject {
    private final List<BacktrackingObserver> observers = new ArrayList<>();
    
    public void addObserver(BacktrackingObserver observer) {
        observers.add(observer);
    }
    
    protected void notifyRecursionStart(int depth, Object state) {
        observers.forEach(obs -> obs.onRecursionStart(depth, state));
    }
    
    protected void notifyBacktrack(int depth, Object state) {
        observers.forEach(obs -> obs.onBacktrack(depth, state));
    }
    
    // ... outros métodos de notificação
}

public class PerformanceObserver implements BacktrackingObserver {
    private int maxDepth = 0;
    private long startTime;
    
    @Override
    public void onRecursionStart(int depth, Object state) {
        if (depth == 0) startTime = System.nanoTime();
        maxDepth = Math.max(maxDepth, depth);
    }
    
    @Override
    public void onSolutionFound(Object solution) {
        long elapsedTime = System.nanoTime() - startTime;
        System.out.printf("Solução encontrada em %.2f ms (profundidade máxima: %d)%n",
            elapsedTime / 1_000_000.0, maxDepth);
    }
    
    // ... outros métodos
}
```

## Testing Avançado

### JUnit 5 com Parameterized Tests
```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.junit.jupiter.params.provider.MethodSource;
import static org.junit.jupiter.api.Assertions.*;

class BacktrackingBasicoTest {
    private BacktrackingBasico backtracking;
    
    @BeforeEach
    void setUp() {
        backtracking = new BacktrackingBasico();
    }
    
    @ParameterizedTest
    @ValueSource(ints = {1, 4, 8})
    @DisplayName("N-Queens deve encontrar soluções válidas")
    void testNQueens(int n) {
        List<List<String>> solutions = backtracking.nQueens(n);
        
        assertFalse(solutions.isEmpty(), "Deve encontrar pelo menos uma solução");
        
        for (List<String> solution : solutions) {
            assertEquals(n, solution.size(), "Solução deve ter " + n + " linhas");
            assertTrue(isValidQueensSolution(solution), "Solução deve ser válida");
        }
    }
    
    @Test
    @DisplayName("Sudoku solver deve resolver puzzles válidos")
    void testSudokuSolver() {
        char[][] board = {
            {'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
        };
        
        assertTrue(backtracking.solveSudoku(board));
        assertTrue(isValidSudokuSolution(board));
    }
    
    @ParameterizedTest
    @MethodSource("providePermutationInputs")
    @DisplayName("Permutations deve gerar todas as permutações")
    void testPermutations(int[] input, int expectedCount) {
        List<List<Integer>> permutations = backtracking.permutations(input);
        
        assertEquals(expectedCount, permutations.size());
        assertTrue(areAllPermutationsUnique(permutations));
        assertTrue(areAllPermutationsValid(permutations, input));
    }
    
    static Stream<Arguments> providePermutationInputs() {
        return Stream.of(
            Arguments.of(new int[]{1}, 1),
            Arguments.of(new int[]{1, 2}, 2),
            Arguments.of(new int[]{1, 2, 3}, 6),
            Arguments.of(new int[]{1, 2, 3, 4}, 24)
        );
    }
}
```

### Performance Testing com JMH
```java
import org.openjdk.jmh.annotations.*;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Benchmark)
@Fork(1)
@Warmup(iterations = 3, time = 1)
@Measurement(iterations = 5, time = 1)
public class BacktrackingBenchmark {
    
    private BacktrackingBasico backtracking;
    
    @Setup
    public void setup() {
        backtracking = new BacktrackingBasico();
    }
    
    @Benchmark
    public List<List<String>> benchmarkNQueens4() {
        backtracking.resetCounters();
        return backtracking.nQueens(4);
    }
    
    @Benchmark
    public List<List<String>> benchmarkNQueens8() {
        backtracking.resetCounters();
        return backtracking.nQueens(8);
    }
    
    @Benchmark
    public List<List<Integer>> benchmarkPermutations() {
        backtracking.resetCounters();
        return backtracking.permutations(new int[]{1, 2, 3, 4, 5});
    }
    
    @Benchmark
    public List<List<Integer>> benchmarkCombinations() {
        backtracking.resetCounters();
        return backtracking.combinations(10, 3);
    }
}
```

## Integração Spring Framework

### Spring Service
```java
@Service
@Transactional
public class BacktrackingService {
    
    private final BacktrackingBasico backtracking;
    private final BacktrackingMetrics metrics;
    
    @Autowired
    public BacktrackingService(BacktrackingBasico backtracking, 
                             BacktrackingMetrics metrics) {
        this.backtracking = backtracking;
        this.metrics = metrics;
    }
    
    @Async
    public CompletableFuture<NQueensResponse> solveNQueensAsync(int n) {
        long startTime = System.currentTimeMillis();
        
        try {
            List<List<String>> solutions = backtracking.nQueens(n);
            long executionTime = System.currentTimeMillis() - startTime;
            
            BacktrackingStats stats = backtracking.getStats();
            metrics.recordExecution("nqueens", stats.getRecursions(), executionTime);
            
            return CompletableFuture.completedFuture(
                NQueensResponse.builder()
                    .solutions(solutions)
                    .count(solutions.size())
                    .executionTimeMs(executionTime)
                    .stats(stats)
                    .build()
            );
        } catch (Exception e) {
            return CompletableFuture.failedFuture(e);
        }
    }
    
    @Cacheable(value = "combinations", key = "#n + '_' + #k")
    public List<List<Integer>> getCombinations(int n, int k) {
        return backtracking.combinations(n, k);
    }
}
```

### REST Controller
```java
@RestController
@RequestMapping("/api/backtracking")
@Validated
public class BacktrackingController {
    
    @Autowired
    private BacktrackingService backtrackingService;
    
    @PostMapping("/nqueens/{n}")
    public ResponseEntity<NQueensResponse> solveNQueens(
            @PathVariable @Min(1) @Max(12) int n) {
        
        try {
            CompletableFuture<NQueensResponse> future = 
                backtrackingService.solveNQueensAsync(n);
            
            NQueensResponse response = future.get(30, TimeUnit.SECONDS);
            return ResponseEntity.ok(response);
            
        } catch (TimeoutException e) {
            return ResponseEntity.status(HttpStatus.REQUEST_TIMEOUT)
                .body(NQueensResponse.builder()
                    .error("Timeout: problema muito complexo")
                    .build());
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(NQueensResponse.builder()
                    .error("Erro interno: " + e.getMessage())
                    .build());
        }
    }
    
    @PostMapping("/sudoku")
    public ResponseEntity<SudokuResponse> solveSudoku(
            @RequestBody @Valid SudokuRequest request) {
        
        char[][] board = convertToCharArray(request.getBoard());
        long startTime = System.currentTimeMillis();
        
        boolean solved = backtrackingService.solveSudoku(board);
        long executionTime = System.currentTimeMillis() - startTime;
        
        return ResponseEntity.ok(
            SudokuResponse.builder()
                .solved(solved)
                .board(convertToStringArray(board))
                .executionTimeMs(executionTime)
                .build()
        );
    }
}
```

## Aplicações Empresariais

### 1. Scheduling System
```java
@Component
public class EmployeeScheduler {
    private final BacktrackingBasico backtracking;
    
    public List<Schedule> generateSchedules(List<Employee> employees, 
                                          List<Shift> shifts, 
                                          List<Constraint> constraints) {
        
        ScheduleProblem problem = new ScheduleProblem(employees, shifts, constraints);
        return backtrackingService.solveScheduling(problem);
    }
}

public class ScheduleProblem {
    private final List<Employee> employees;
    private final List<Shift> shifts;
    private final List<Constraint> constraints;
    
    public boolean isValidAssignment(Employee employee, Shift shift) {
        return constraints.stream()
            .allMatch(constraint -> constraint.isValid(employee, shift));
    }
}
```

### 2. Resource Allocation System
```java
@Service
public class ResourceAllocationService {
    
    public List<AllocationPlan> optimizeResourceAllocation(
            List<Resource> resources, 
            List<Task> tasks, 
            OptimizationCriteria criteria) {
        
        AllocationProblem problem = new AllocationProblem(resources, tasks, criteria);
        return backtrackingService.findOptimalAllocations(problem);
    }
}

public class AllocationProblem extends BacktrackingTemplate<AllocationState> {
    
    @Override
    protected boolean isComplete(AllocationState state) {
        return state.getAllocatedTasks().size() == totalTasks;
    }
    
    @Override
    protected boolean isValid(AllocationState state, Object choice) {
        TaskAllocation allocation = (TaskAllocation) choice;
        return allocation.getResource().canHandle(allocation.getTask()) &&
               !state.hasConflict(allocation);
    }
    
    // ... implementação dos outros métodos abstratos
}
```

### 3. Configuration Management
```java
@Service
public class ConfigurationResolver {
    
    public List<Configuration> resolveConfigurations(
            List<Component> components,
            List<Dependency> dependencies,
            List<Rule> rules) {
        
        ConfigurationProblem problem = new ConfigurationProblem(
            components, dependencies, rules
        );
        
        return backtrackingService.findValidConfigurations(problem);
    }
}

public class ConfigurationProblem {
    
    public boolean isConfigurationValid(Configuration config) {
        return dependencies.stream().allMatch(dep -> dep.isSatisfied(config)) &&
               rules.stream().allMatch(rule -> rule.isCompliant(config));
    }
    
    public List<ConfigurationChoice> getNextChoices(Configuration partial) {
        return components.stream()
            .filter(comp -> !partial.contains(comp))
            .map(comp -> new ConfigurationChoice(comp, partial))
            .filter(this::isPotentiallyValid)
            .collect(Collectors.toList());
    }
}
```

## Monitoramento e Observabilidade

### Custom Metrics com Micrometer
```java
@Component
public class BacktrackingMetrics {
    
    private final Counter recursionCounter;
    private final Counter backtrackCounter;
    private final Timer executionTimer;
    private final Gauge maxDepthGauge;
    
    public BacktrackingMetrics(MeterRegistry meterRegistry) {
        this.recursionCounter = Counter.builder("backtracking.recursions.total")
            .description("Total number of recursive calls")
            .register(meterRegistry);
            
        this.backtrackCounter = Counter.builder("backtracking.backtracks.total")
            .description("Total number of backtrack operations")
            .register(meterRegistry);
            
        this.executionTimer = Timer.builder("backtracking.execution.time")
            .description("Execution time of backtracking algorithms")
            .register(meterRegistry);
            
        this.maxDepthGauge = Gauge.builder("backtracking.max.depth")
            .description("Maximum recursion depth reached")
            .register(meterRegistry, this, BacktrackingMetrics::getCurrentMaxDepth);
    }
    
    public void recordExecution(String algorithm, int recursions, long timeMs) {
        recursionCounter.increment(recursions);
        executionTimer.record(timeMs, TimeUnit.MILLISECONDS);
        
        Tags tags = Tags.of("algorithm", algorithm);
        // Record per-algorithm metrics...
    }
}
```

### Health Checks
```java
@Component
public class BacktrackingHealthIndicator implements HealthIndicator {
    
    private final BacktrackingService backtrackingService;
    
    @Override
    public Health health() {
        try {
            // Test simple N-Queens problem
            long startTime = System.currentTimeMillis();
            List<List<String>> result = backtrackingService.solveNQueens(4);
            long executionTime = System.currentTimeMillis() - startTime;
            
            if (result.size() == 2 && executionTime < 1000) {
                return Health.up()
                    .withDetail("algorithm", "nqueens")
                    .withDetail("solutions", result.size())
                    .withDetail("executionTimeMs", executionTime)
                    .build();
            } else {
                return Health.down()
                    .withDetail("reason", "Performance degradation detected")
                    .withDetail("executionTimeMs", executionTime)
                    .build();
            }
            
        } catch (Exception e) {
            return Health.down()
                .withDetail("error", e.getMessage())
                .build();
        }
    }
}
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
  <i>☕ "Backtracking em Java: onde a recursão encontra a arquitetura empresarial"</i>
  <br>
  <i>☕ "Backtracking in Java: where recursion meets enterprise architecture"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=9B59B6&height=120&section=footer"/>

</div>
