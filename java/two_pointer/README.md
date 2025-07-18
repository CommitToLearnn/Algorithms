<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=F39C12&height=120&section=header&text=Two%20Pointer%20-%20Java&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Implementação%20em%20Java%20da%20Técnica%20de%20Dois%20Ponteiros&descAlignY=65&descSize=16">

</div>

# Two Pointer - Implementação em Java

## Descrição

Esta implementação em Java demonstra a técnica de dois ponteiros através de 6 algoritmos fundamentais. Java oferece robustez, orientação a objetos e excelente ecosystem para implementar estes algoritmos de forma eficiente e escalável.

## Algoritmos Implementados

### 1. Two Sum em Array Ordenado
```java
public int[] twoSumSorted(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    
    while (left < right) {
        operationsCount++;
        int currentSum = nums[left] + nums[right];
        
        if (currentSum == target) {
            return new int[]{left, right};
        } else if (currentSum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    return new int[]{}; // Não encontrado
}
```

### 2. Verificação de Palíndromo
```java
public boolean isPalindrome(String s) {
    if (s == null || s.length() <= 1) {
        return true;
    }
    
    int left = 0;
    int right = s.length() - 1;
    
    while (left < right) {
        comparisonsCount++;
        if (s.charAt(left) != s.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    
    return true;
}
```

### 3. Remoção de Duplicatas
```java
public int removeDuplicates(int[] nums) {
    if (nums.length <= 1) {
        return nums.length;
    }
    
    int writePos = 1;
    
    for (int readPos = 1; readPos < nums.length; readPos++) {
        operationsCount++;
        if (nums[readPos] != nums[readPos - 1]) {
            nums[writePos] = nums[readPos];
            writePos++;
        }
    }
    
    return writePos;
}
```

### 4. Container com Mais Água
```java
public int containerWithMostWater(int[] heights) {
    int left = 0;
    int right = heights.length - 1;
    int maxArea = 0;
    
    while (left < right) {
        operationsCount++;
        int width = right - left;
        int height = Math.min(heights[left], heights[right]);
        int area = width * height;
        
        maxArea = Math.max(maxArea, area);
        
        if (heights[left] < heights[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxArea;
}
```

### 5. Three Sum
```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> result = new ArrayList<>();
    
    for (int i = 0; i < nums.length - 2; i++) {
        // Pular duplicatas para o primeiro número
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        
        int left = i + 1;
        int right = nums.length - 1;
        
        while (left < right) {
            operationsCount++;
            int currentSum = nums[i] + nums[left] + nums[right];
            
            if (currentSum == 0) {
                result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                
                // Pular duplicatas
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;
                
                left++;
                right--;
            } else if (currentSum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    return result;
}
```

### 6. Sort Colors (Dutch National Flag)
```java
public void sortColors(int[] nums) {
    int low = 0;
    int mid = 0;
    int high = nums.length - 1;
    
    while (mid <= high) {
        operationsCount++;
        switch (nums[mid]) {
            case 0:
                swap(nums, low, mid);
                low++;
                mid++;
                break;
            case 1:
                mid++;
                break;
            case 2:
                swap(nums, mid, high);
                high--;
                // Não incrementar mid aqui
                break;
        }
    }
}

private void swap(int[] nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
```

## Características da Implementação Java

### ☕ Orientação a Objetos
- **Encapsulamento**: Métodos e campos privados bem definidos
- **Reutilização**: Classe `TwoPointerBasico` instanciável
- **Extensibilidade**: Interface clara para novos algoritmos
- **Type Safety**: Tipagem forte com generics

### 📊 Monitoramento de Performance
```java
public class TwoPointerBasico {
    private int operationsCount;
    private int comparisonsCount;
    private long executionTime;
    
    public void resetCounters() {
        this.operationsCount = 0;
        this.comparisonsCount = 0;
        this.executionTime = 0;
    }
    
    public PerformanceStats getStats() {
        return new PerformanceStats(operationsCount, comparisonsCount, executionTime);
    }
}
```

### 🧪 Demonstração Completa
```java
public static void main(String[] args) {
    TwoPointerBasico tp = new TwoPointerBasico();
    
    System.out.println("=== Demonstração de Two Pointer em Java ===");
    
    // Two Sum
    int[] nums = {2, 7, 11, 15};
    long startTime = System.nanoTime();
    int[] result = tp.twoSumSorted(nums, 9);
    long endTime = System.nanoTime();
    
    System.out.printf("Two Sum: %s%n", Arrays.toString(result));
    System.out.printf("Tempo: %.2f ms%n", (endTime - startTime) / 1_000_000.0);
    System.out.printf("Operações: %d%n", tp.operationsCount);
}
```

## Compilação e Execução

### Compilar e Executar
```bash
cd java/two_pointer
javac TwoPointerBasico.java
java TwoPointerBasico
```

### Executar com Diferentes JVM Options
```bash
java -Xms512m -Xmx2g TwoPointerBasico          # Configurar heap
java -XX:+UseG1GC TwoPointerBasico             # Usar G1 Garbage Collector
java -XX:+PrintGCDetails TwoPointerBasico      # Debug GC
```

### Executar com JProfiler/VisualVM
```bash
java -Dcom.sun.management.jmxremote TwoPointerBasico
# Conectar via JProfiler ou VisualVM para profiling
```

## Vantagens da Implementação Java

### ✅ Benefícios
- **Write Once, Run Anywhere**: Portabilidade total
- **Garbage Collection**: Gerenciamento automático de memória
- **Biblioteca rica**: Collections Framework robusto
- **Tooling avançado**: IDEs, debuggers, profilers
- **Concorrência**: Excelente suporte para threading

### 🎯 Casos de Uso Ideais
- **Aplicações empresariais**
- **Sistemas web de grande escala**
- **Microserviços**
- **Processamento batch**
- **APIs REST robustas**

## Complexidade dos Algoritmos

| Algoritmo | Tempo | Espaço | Estruturas Java |
|-----------|-------|--------|-----------------|
| **Two Sum Sorted** | O(n) | O(1) | Arrays primitivos |
| **Is Palindrome** | O(n) | O(1) | String charAt() |
| **Remove Duplicates** | O(n) | O(1) | Array in-place |
| **Container Water** | O(n) | O(1) | Math.min/max |
| **Three Sum** | O(n²) | O(1) | ArrayList, Arrays.sort |
| **Sort Colors** | O(n) | O(1) | Array swap operations |

## Patterns Java para Two Pointer

### 1. Generic Two Pointer Template
```java
public abstract class TwoPointerTemplate<T> {
    protected int operationsCount = 0;
    
    public abstract boolean shouldMoveLeft(T[] array, int left, int right, T target);
    public abstract boolean shouldMoveRight(T[] array, int left, int right, T target);
    public abstract boolean isValidSolution(T[] array, int left, int right, T target);
    
    public int[] solve(T[] array, T target) {
        int left = 0;
        int right = array.length - 1;
        
        while (left < right) {
            operationsCount++;
            
            if (isValidSolution(array, left, right, target)) {
                return new int[]{left, right};
            } else if (shouldMoveLeft(array, left, right, target)) {
                left++;
            } else if (shouldMoveRight(array, left, right, target)) {
                right--;
            }
        }
        
        return new int[]{};
    }
}
```

### 2. Interface para Problemas Two Pointer
```java
public interface TwoPointerSolver {
    int[] twoSumSorted(int[] nums, int target);
    boolean isPalindrome(String s);
    int removeDuplicates(int[] nums);
    int containerWithMostWater(int[] heights);
    List<List<Integer>> threeSum(int[] nums);
    void sortColors(int[] nums);
    
    // Métodos de monitoramento
    void resetCounters();
    PerformanceStats getStats();
}

// Implementação
public class TwoPointerBasico implements TwoPointerSolver {
    // ... implementações dos métodos
}
```

### 3. Exception Handling e Validation
```java
public int[] twoSumSortedSafe(int[] nums, int target) throws IllegalArgumentException {
    if (nums == null) {
        throw new IllegalArgumentException("Array não pode ser null");
    }
    if (nums.length < 2) {
        throw new IllegalArgumentException("Array deve ter pelo menos 2 elementos");
    }
    
    // Verificar se array está ordenado
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i-1]) {
            throw new IllegalArgumentException("Array deve estar ordenado");
        }
    }
    
    int[] result = twoSumSorted(nums, target);
    if (result.length == 0) {
        throw new NoSuchElementException(
            String.format("Nenhum par encontrado que soma %d", target)
        );
    }
    
    return result;
}
```

## Testing e Frameworks

### JUnit 5 Tests
```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import static org.junit.jupiter.api.Assertions.*;

class TwoPointerBasicoTest {
    private TwoPointerBasico twoPointer;
    
    @BeforeEach
    void setUp() {
        twoPointer = new TwoPointerBasico();
    }
    
    @Test
    @DisplayName("Two Sum deve retornar índices corretos")
    void testTwoSumSorted() {
        int[] nums = {2, 7, 11, 15};
        int[] expected = {0, 1};
        int[] result = twoPointer.twoSumSorted(nums, 9);
        
        assertArrayEquals(expected, result);
    }
    
    @ParameterizedTest
    @ValueSource(strings = {"racecar", "level", "noon"})
    @DisplayName("Deve reconhecer palíndromos válidos")
    void testValidPalindromes(String s) {
        assertTrue(twoPointer.isPalindrome(s));
    }
    
    @Test
    @DisplayName("Remove duplicates deve manter apenas elementos únicos")
    void testRemoveDuplicates() {
        int[] nums = {1, 1, 2, 2, 3, 4, 4};
        int newLength = twoPointer.removeDuplicates(nums);
        
        assertEquals(4, newLength);
        assertArrayEquals(new int[]{1, 2, 3, 4}, Arrays.copyOf(nums, newLength));
    }
}
```

### Performance Benchmarks com JMH
```java
import org.openjdk.jmh.annotations.*;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Benchmark)
public class TwoPointerBenchmark {
    
    private TwoPointerBasico twoPointer;
    private int[] largeArray;
    
    @Setup
    public void setup() {
        twoPointer = new TwoPointerBasico();
        largeArray = new int[100000];
        for (int i = 0; i < largeArray.length; i++) {
            largeArray[i] = i * 2;
        }
    }
    
    @Benchmark
    public int[] benchmarkTwoSum() {
        return twoPointer.twoSumSorted(largeArray, 199998);
    }
    
    @Benchmark
    public boolean benchmarkPalindrome() {
        return twoPointer.isPalindrome("abcdefghijklmnopqrstuvwxyz");
    }
}
```

## Integração com Spring Framework

### Spring Service
```java
@Service
@Component
public class TwoPointerService {
    private final TwoPointerBasico twoPointer;
    
    @Autowired
    public TwoPointerService() {
        this.twoPointer = new TwoPointerBasico();
    }
    
    public TwoSumResponse findTwoSum(int[] numbers, int target) {
        long startTime = System.currentTimeMillis();
        int[] result = twoPointer.twoSumSorted(numbers, target);
        long executionTime = System.currentTimeMillis() - startTime;
        
        return TwoSumResponse.builder()
            .indices(result)
            .found(result.length > 0)
            .executionTimeMs(executionTime)
            .operationsCount(twoPointer.getOperationsCount())
            .build();
    }
}
```

### REST Controller
```java
@RestController
@RequestMapping("/api/algorithms/two-pointer")
public class TwoPointerController {
    
    @Autowired
    private TwoPointerService twoPointerService;
    
    @PostMapping("/two-sum")
    public ResponseEntity<TwoSumResponse> twoSum(@RequestBody TwoSumRequest request) {
        try {
            TwoSumResponse response = twoPointerService.findTwoSum(
                request.getNumbers(), 
                request.getTarget()
            );
            return ResponseEntity.ok(response);
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().build();
        }
    }
    
    @PostMapping("/palindrome")
    public ResponseEntity<PalindromeResponse> checkPalindrome(@RequestBody String text) {
        boolean isPalindrome = twoPointerService.isPalindrome(text);
        return ResponseEntity.ok(new PalindromeResponse(isPalindrome, text));
    }
}
```

## Concorrência e Paralelização

### CompletableFuture para Async Processing
```java
public class AsyncTwoPointerService {
    private final ExecutorService executor = ForkJoinPool.commonPool();
    
    public CompletableFuture<int[]> twoSumAsync(int[] nums, int target) {
        return CompletableFuture.supplyAsync(() -> {
            TwoPointerBasico tp = new TwoPointerBasico();
            return tp.twoSumSorted(nums, target);
        }, executor);
    }
    
    public CompletableFuture<List<Boolean>> checkMultiplePalindromes(List<String> strings) {
        List<CompletableFuture<Boolean>> futures = strings.stream()
            .map(s -> CompletableFuture.supplyAsync(() -> {
                TwoPointerBasico tp = new TwoPointerBasico();
                return tp.isPalindrome(s);
            }, executor))
            .collect(Collectors.toList());
        
        return CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
            .thenApply(v -> futures.stream()
                .map(CompletableFuture::join)
                .collect(Collectors.toList()));
    }
}
```

### Parallel Streams
```java
public class ParallelTwoPointerProcessor {
    
    public Map<String, Boolean> checkPalindromes(List<String> strings) {
        return strings.parallelStream()
            .collect(Collectors.toConcurrentMap(
                s -> s,
                s -> {
                    TwoPointerBasico tp = new TwoPointerBasico();
                    return tp.isPalindrome(s);
                }
            ));
    }
    
    public List<int[]> processTwoSumBatch(List<TwoSumTask> tasks) {
        return tasks.parallelStream()
            .map(task -> {
                TwoPointerBasico tp = new TwoPointerBasico();
                return tp.twoSumSorted(task.getNumbers(), task.getTarget());
            })
            .collect(Collectors.toList());
    }
}
```

## Aplicações Práticas

### 1. Microservice Completo
```java
@SpringBootApplication
public class TwoPointerMicroservice {
    public static void main(String[] args) {
        SpringApplication.run(TwoPointerMicroservice.class, args);
    }
}

@Configuration
public class TwoPointerConfig {
    
    @Bean
    public TwoPointerBasico twoPointerAlgorithm() {
        return new TwoPointerBasico();
    }
    
    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(4);
        executor.setMaxPoolSize(8);
        executor.setQueueCapacity(100);
        executor.setThreadNamePrefix("TwoPointer-");
        executor.initialize();
        return executor;
    }
}
```

### 2. CLI Application
```java
public class TwoPointerCLI {
    private static final Scanner scanner = new Scanner(System.in);
    private static final TwoPointerBasico twoPointer = new TwoPointerBasico();
    
    public static void main(String[] args) {
        System.out.println("=== Two Pointer Algorithms CLI ===");
        
        while (true) {
            printMenu();
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    runTwoSum();
                    break;
                case 2:
                    runPalindromeCheck();
                    break;
                case 3:
                    runRemoveDuplicates();
                    break;
                case 0:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        }
    }
    
    private static void runTwoSum() {
        System.out.print("Digite o array (separado por espaços): ");
        scanner.nextLine(); // Consumir newline
        String[] input = scanner.nextLine().split(" ");
        int[] nums = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
        
        System.out.print("Digite o target: ");
        int target = scanner.nextInt();
        
        int[] result = twoPointer.twoSumSorted(nums, target);
        System.out.printf("Resultado: %s%n", Arrays.toString(result));
    }
}
```

### 3. Web Application com Thymeleaf
```java
@Controller
public class TwoPointerWebController {
    
    @GetMapping("/two-pointer")
    public String showTwoPointerPage(Model model) {
        model.addAttribute("algorithms", Arrays.asList(
            "Two Sum", "Palindrome Check", "Remove Duplicates", 
            "Container With Most Water", "Three Sum", "Sort Colors"
        ));
        return "two-pointer";
    }
    
    @PostMapping("/two-pointer/execute")
    public String executeTwoPointer(@RequestParam String algorithm,
                                  @RequestParam String input,
                                  @RequestParam(required = false) Integer target,
                                  Model model) {
        TwoPointerBasico tp = new TwoPointerBasico();
        String result = "";
        
        try {
            switch (algorithm) {
                case "Two Sum":
                    int[] nums = parseIntArray(input);
                    int[] indices = tp.twoSumSorted(nums, target);
                    result = "Índices: " + Arrays.toString(indices);
                    break;
                    
                case "Palindrome Check":
                    boolean isPalindrome = tp.isPalindrome(input);
                    result = "É palíndromo: " + isPalindrome;
                    break;
                    
                // ... outros casos
            }
        } catch (Exception e) {
            result = "Erro: " + e.getMessage();
        }
        
        model.addAttribute("result", result);
        model.addAttribute("algorithm", algorithm);
        return "two-pointer-result";
    }
}
```

## Performance e Monitoramento

### JVM Monitoring
```java
public class PerformanceMonitor {
    private final MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();
    private final RuntimeMXBean runtimeBean = ManagementFactory.getRuntimeMXBean();
    
    public void logPerformanceStats() {
        MemoryUsage heapUsage = memoryBean.getHeapMemoryUsage();
        
        System.out.printf("Heap Used: %.2f MB%n", 
            heapUsage.getUsed() / (1024.0 * 1024.0));
        System.out.printf("Heap Max: %.2f MB%n", 
            heapUsage.getMax() / (1024.0 * 1024.0));
        System.out.printf("Uptime: %d ms%n", runtimeBean.getUptime());
    }
}
```

### Custom Metrics
```java
public class TwoPointerMetrics {
    private final AtomicLong totalOperations = new AtomicLong(0);
    private final AtomicLong totalExecutions = new AtomicLong(0);
    private final AtomicLong totalExecutionTime = new AtomicLong(0);
    
    public void recordExecution(long operationsCount, long executionTimeNs) {
        totalOperations.addAndGet(operationsCount);
        totalExecutions.incrementAndGet();
        totalExecutionTime.addAndGet(executionTimeNs);
    }
    
    public double getAverageOperationsPerExecution() {
        long executions = totalExecutions.get();
        return executions == 0 ? 0 : (double) totalOperations.get() / executions;
    }
    
    public double getAverageExecutionTimeMs() {
        long executions = totalExecutions.get();
        return executions == 0 ? 0 : totalExecutionTime.get() / (executions * 1_000_000.0);
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
  <i>☕ "Dois ponteiros em Java: robustez empresarial encontra elegância algorítmica"</i>
  <br>
  <i>☕ "Two pointers in Java: enterprise robustness meets algorithmic elegance"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=F39C12&height=120&section=footer"/>

</div>
