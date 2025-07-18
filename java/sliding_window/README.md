<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E67E22&height=120&section=header&text=Sliding%20Window%20-%20Java&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Implementação%20em%20Java%20da%20Técnica%20de%20Janela%20Deslizante&descAlignY=65&descSize=16">

</div>

# Sliding Window - Implementação em Java

## Descrição

Esta implementação em Java demonstra a técnica de janela deslizante através de 7 algoritmos fundamentais. Java oferece Collections Framework robusto e orientação a objetos que tornam esta técnica especialmente poderosa para processar grandes volumes de dados de forma eficiente.

## Algoritmos Implementados

### 1. Maximum Sum Subarray (Fixed Window)
```java
public int maxSumSubarray(int[] nums, int k) {
    if (nums.length < k) {
        throw new IllegalArgumentException("Array menor que o tamanho da janela");
    }
    
    // Calcular soma da primeira janela
    int windowSum = 0;
    for (int i = 0; i < k; i++) {
        windowSum += nums[i];
        operationsCount++;
    }
    
    int maxSum = windowSum;
    
    // Deslizar a janela
    for (int i = k; i < nums.length; i++) {
        windowSum += nums[i] - nums[i - k];
        operationsCount += 2;
        maxSum = Math.max(maxSum, windowSum);
        windowAdjustments++;
    }
    
    maxWindowSize = Math.max(maxWindowSize, k);
    return maxSum;
}
```

### 2. Longest Substring Without Repeating Characters
```java
public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> charIndexMap = new HashMap<>();
    int left = 0;
    int maxLength = 0;
    
    for (int right = 0; right < s.length(); right++) {
        operationsCount++;
        char currentChar = s.charAt(right);
        
        if (charIndexMap.containsKey(currentChar) && 
            charIndexMap.get(currentChar) >= left) {
            left = charIndexMap.get(currentChar) + 1;
            windowAdjustments++;
        }
        
        charIndexMap.put(currentChar, right);
        int currentLength = right - left + 1;
        maxLength = Math.max(maxLength, currentLength);
        maxWindowSize = Math.max(maxWindowSize, currentLength);
    }
    
    return maxLength;
}
```

### 3. Minimum Window Substring
```java
public String minimumWindowSubstring(String s, String t) {
    if (s.length() < t.length()) {
        return "";
    }
    
    Map<Character, Integer> tCount = new HashMap<>();
    for (char c : t.toCharArray()) {
        tCount.put(c, tCount.getOrDefault(c, 0) + 1);
    }
    
    int required = tCount.size();
    int formed = 0;
    Map<Character, Integer> windowCounts = new HashMap<>();
    
    int left = 0;
    int minLen = Integer.MAX_VALUE;
    int minStart = 0;
    
    for (int right = 0; right < s.length(); right++) {
        operationsCount++;
        char rightChar = s.charAt(right);
        windowCounts.put(rightChar, windowCounts.getOrDefault(rightChar, 0) + 1);
        
        if (tCount.containsKey(rightChar) && 
            windowCounts.get(rightChar).intValue() == tCount.get(rightChar).intValue()) {
            formed++;
        }
        
        while (left <= right && formed == required) {
            windowAdjustments++;
            
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }
            
            char leftChar = s.charAt(left);
            windowCounts.put(leftChar, windowCounts.get(leftChar) - 1);
            
            if (tCount.containsKey(leftChar) && 
                windowCounts.get(leftChar) < tCount.get(leftChar)) {
                formed--;
            }
            left++;
        }
    }
    
    return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
}
```

### 4. Sliding Window Maximum
```java
public int[] slidingWindowMaximum(int[] nums, int k) {
    if (nums.length == 0 || k == 0) {
        return new int[0];
    }
    
    Deque<Integer> deque = new ArrayDeque<>();
    int[] result = new int[nums.length - k + 1];
    int resultIndex = 0;
    
    for (int i = 0; i < nums.length; i++) {
        operationsCount++;
        
        // Remove elementos fora da janela atual
        while (!deque.isEmpty() && deque.peekFirst() <= i - k) {
            deque.pollFirst();
        }
        
        // Remove elementos menores que o atual (não serão máximo)
        while (!deque.isEmpty() && nums[deque.peekLast()] <= nums[i]) {
            deque.pollLast();
        }
        
        deque.offerLast(i);
        
        // Adicionar máximo ao resultado quando janela estiver completa
        if (i >= k - 1) {
            result[resultIndex++] = nums[deque.peekFirst()];
            windowAdjustments++;
        }
    }
    
    maxWindowSize = Math.max(maxWindowSize, k);
    return result;
}
```

### 5. Find All Anagrams
```java
public List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();
    
    if (s.length() < p.length()) {
        return result;
    }
    
    Map<Character, Integer> pCount = new HashMap<>();
    for (char c : p.toCharArray()) {
        pCount.put(c, pCount.getOrDefault(c, 0) + 1);
    }
    
    Map<Character, Integer> windowCount = new HashMap<>();
    int windowSize = p.length();
    
    for (int i = 0; i < s.length(); i++) {
        operationsCount++;
        char currentChar = s.charAt(i);
        windowCount.put(currentChar, windowCount.getOrDefault(currentChar, 0) + 1);
        
        // Se janela maior que p, remover character da esquerda
        if (i >= windowSize) {
            char leftChar = s.charAt(i - windowSize);
            int count = windowCount.get(leftChar) - 1;
            if (count == 0) {
                windowCount.remove(leftChar);
            } else {
                windowCount.put(leftChar, count);
            }
            windowAdjustments++;
        }
        
        // Verificar se é anagrama
        if (i >= windowSize - 1 && windowCount.equals(pCount)) {
            result.add(i - windowSize + 1);
        }
    }
    
    maxWindowSize = Math.max(maxWindowSize, windowSize);
    return result;
}
```

### 6. Longest Substring with At Most K Distinct Characters
```java
public int lengthOfLongestSubstringKDistinct(String s, int k) {
    if (k == 0) {
        return 0;
    }
    
    Map<Character, Integer> charCount = new HashMap<>();
    int left = 0;
    int maxLength = 0;
    
    for (int right = 0; right < s.length(); right++) {
        operationsCount++;
        char rightChar = s.charAt(right);
        charCount.put(rightChar, charCount.getOrDefault(rightChar, 0) + 1);
        
        while (charCount.size() > k) {
            char leftChar = s.charAt(left);
            int count = charCount.get(leftChar) - 1;
            if (count == 0) {
                charCount.remove(leftChar);
            } else {
                charCount.put(leftChar, count);
            }
            left++;
            windowAdjustments++;
        }
        
        int currentLength = right - left + 1;
        maxLength = Math.max(maxLength, currentLength);
        maxWindowSize = Math.max(maxWindowSize, currentLength);
    }
    
    return maxLength;
}
```

### 7. Subarray Product Less Than K
```java
public int numSubarrayProductLessThanK(int[] nums, int k) {
    if (k <= 1) {
        return 0;
    }
    
    int left = 0;
    int product = 1;
    int count = 0;
    
    for (int right = 0; right < nums.length; right++) {
        operationsCount++;
        product *= nums[right];
        
        while (product >= k) {
            product /= nums[left];
            left++;
            windowAdjustments++;
        }
        
        count += right - left + 1;
    }
    
    return count;
}
```

## Características da Implementação Java

### ☕ Collections Framework Avançado
- **HashMap/LinkedHashMap**: Mapeamento eficiente de caracteres
- **ArrayDeque**: Implementação eficiente de deque para sliding window maximum
- **ArrayList**: Lista dinâmica para resultados
- **StringBuilder**: Construção eficiente de strings

### 📊 Monitoramento Empresarial
```java
public class SlidingWindowBasico {
    private int operationsCount;
    private int windowAdjustments;
    private int maxWindowSize;
    private long totalExecutionTime;
    
    public void resetCounters() {
        this.operationsCount = 0;
        this.windowAdjustments = 0;
        this.maxWindowSize = 0;
        this.totalExecutionTime = 0;
    }
    
    public SlidingWindowStats getStats() {
        return SlidingWindowStats.builder()
            .operationsCount(operationsCount)
            .windowAdjustments(windowAdjustments)
            .maxWindowSize(maxWindowSize)
            .totalExecutionTime(totalExecutionTime)
            .efficiency(calculateEfficiency())
            .build();
    }
    
    private double calculateEfficiency() {
        return operationsCount > 0 ? 
            (double) windowAdjustments / operationsCount : 0.0;
    }
}

@Data
@Builder
public class SlidingWindowStats {
    private final int operationsCount;
    private final int windowAdjustments;
    private final int maxWindowSize;
    private final long totalExecutionTime;
    private final double efficiency;
    
    public double getAverageOperationsPerAdjustment() {
        return windowAdjustments > 0 ? 
            (double) operationsCount / windowAdjustments : 0.0;
    }
    
    public double getThroughput() {
        return totalExecutionTime > 0 ? 
            (operationsCount * 1000.0) / totalExecutionTime : 0.0;
    }
}
```

### 🧪 Demonstração Completa
```java
public static void main(String[] args) {
    SlidingWindowBasico sw = new SlidingWindowBasico();
    
    System.out.println("=== Demonstração de Sliding Window em Java ===");
    
    // Maximum Sum Subarray
    int[] nums = {2, 1, 5, 1, 3, 2};
    long startTime = System.nanoTime();
    int maxSum = sw.maxSumSubarray(nums, 3);
    long endTime = System.nanoTime();
    
    System.out.printf("Max Sum (k=3): %d%n", maxSum);
    System.out.printf("Tempo: %.2f μs%n", (endTime - startTime) / 1000.0);
    
    SlidingWindowStats stats = sw.getStats();
    System.out.printf("Operações: %d%n", stats.getOperationsCount());
    System.out.printf("Ajustes de janela: %d%n", stats.getWindowAdjustments());
    System.out.printf("Eficiência: %.2f%%%n", stats.getEfficiency() * 100);
}
```

## Compilação e Execução

### Compilar e Executar
```bash
cd java/sliding_window
javac SlidingWindowBasico.java
java SlidingWindowBasico
```

### Executar com Memory Tuning
```bash
java -Xms512m -Xmx2g SlidingWindowBasico        # Configurar heap
java -XX:+UseStringDeduplication SlidingWindowBasico  # Otimizar strings
java -XX:+UseCompressedOops SlidingWindowBasico       # Comprimir object pointers
```

### Profiling com JVisualVM
```bash
java -Dcom.sun.management.jmxremote=true SlidingWindowBasico
# Conectar via JVisualVM para monitoramento
```

## Vantagens da Implementação Java

### ✅ Benefícios Empresariais
- **Collections otimizadas**: HashMap, ArrayDeque com performance O(1)
- **Garbage Collection**: Gerenciamento automático de memória
- **Type Safety**: Generics previnem erros de tipo
- **Ecosystem maduro**: Frameworks, libraries, tools
- **Escalabilidade**: Suporte para Big Data (Spark, Hadoop)

### 🎯 Casos de Uso Corporativos
- **Stream Analytics**: Processamento de dados em tempo real
- **Log Analysis**: Análise de logs de aplicação
- **Financial Trading**: Análise de séries temporais
- **IoT Data Processing**: Processamento de dados de sensores
- **Web Analytics**: Análise de comportamento de usuários

## Complexidade e Performance

| Algoritmo | Tempo | Espaço | Estruturas Java |
|-----------|-------|--------|-----------------|
| **Max Sum Subarray** | O(n) | O(1) | Arrays primitivos |
| **Longest Substring** | O(n) | O(min(m,n)) | HashMap<Character, Integer> |
| **Minimum Window** | O(n+m) | O(m) | HashMap com contadores |
| **Sliding Window Max** | O(n) | O(k) | ArrayDeque<Integer> |
| **Find Anagrams** | O(n+m) | O(m) | HashMap comparisons |
| **K Distinct Chars** | O(n) | O(k) | HashMap dinâmico |
| **Product Less Than K** | O(n) | O(1) | Variables primitivas |

## Design Patterns para Sliding Window

### 1. Template Method Pattern
```java
public abstract class SlidingWindowTemplate<T, R> {
    protected int operationsCount = 0;
    protected int windowAdjustments = 0;
    
    public final R solve(T input, Object... params) {
        initializeWindow(input, params);
        R result = createResult();
        
        int left = 0;
        for (int right = 0; right < getInputSize(input); right++) {
            operationsCount++;
            
            expandWindow(input, right, params);
            
            while (shouldContractWindow(input, left, right, params)) {
                contractWindow(input, left, params);
                left++;
                windowAdjustments++;
            }
            
            updateResult(result, input, left, right, params);
        }
        
        return finalizeResult(result);
    }
    
    // Métodos abstratos que subclasses devem implementar
    protected abstract void initializeWindow(T input, Object... params);
    protected abstract int getInputSize(T input);
    protected abstract void expandWindow(T input, int right, Object... params);
    protected abstract boolean shouldContractWindow(T input, int left, int right, Object... params);
    protected abstract void contractWindow(T input, int left, Object... params);
    protected abstract R createResult();
    protected abstract void updateResult(R result, T input, int left, int right, Object... params);
    protected abstract R finalizeResult(R result);
}
```

### 2. Strategy Pattern para Different Window Types
```java
public interface WindowStrategy<T, R> {
    R execute(T input, Object... params);
    SlidingWindowStats getStats();
}

public class FixedWindowStrategy implements WindowStrategy<int[], Integer> {
    private final SlidingWindowBasico slidingWindow = new SlidingWindowBasico();
    
    @Override
    public Integer execute(int[] input, Object... params) {
        int k = (Integer) params[0];
        return slidingWindow.maxSumSubarray(input, k);
    }
    
    @Override
    public SlidingWindowStats getStats() {
        return slidingWindow.getStats();
    }
}

public class VariableWindowStrategy implements WindowStrategy<String, Integer> {
    private final SlidingWindowBasico slidingWindow = new SlidingWindowBasico();
    
    @Override
    public Integer execute(String input, Object... params) {
        return slidingWindow.lengthOfLongestSubstring(input);
    }
    
    @Override
    public SlidingWindowStats getStats() {
        return slidingWindow.getStats();
    }
}

public class SlidingWindowContext {
    private WindowStrategy<?, ?> strategy;
    
    public <T, R> void setStrategy(WindowStrategy<T, R> strategy) {
        this.strategy = strategy;
    }
    
    @SuppressWarnings("unchecked")
    public <T, R> R solve(T input, Object... params) {
        return ((WindowStrategy<T, R>) strategy).execute(input, params);
    }
}
```

### 3. Builder Pattern para Window Configuration
```java
@Builder
public class WindowConfiguration {
    private final int fixedSize;
    private final int maxSize;
    private final boolean allowShrinking;
    private final boolean trackMaximum;
    private final boolean enableMetrics;
    
    public static class WindowConfigurationBuilder {
        public WindowConfigurationBuilder forFixedWindow(int size) {
            this.fixedSize = size;
            this.allowShrinking = false;
            return this;
        }
        
        public WindowConfigurationBuilder forVariableWindow(int maxSize) {
            this.maxSize = maxSize;
            this.allowShrinking = true;
            return this;
        }
        
        public WindowConfigurationBuilder withMetrics() {
            this.enableMetrics = true;
            return this;
        }
    }
}

public class ConfigurableSlidingWindow {
    private final WindowConfiguration config;
    private final SlidingWindowBasico algorithm;
    
    public ConfigurableSlidingWindow(WindowConfiguration config) {
        this.config = config;
        this.algorithm = new SlidingWindowBasico();
    }
    
    public <T, R> R solve(T input, WindowProcessor<T, R> processor) {
        if (config.isEnableMetrics()) {
            algorithm.resetCounters();
        }
        
        return processor.process(input, config, algorithm);
    }
}
```

## Testing Avançado

### JUnit 5 com Parameterized Tests
```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.MethodSource;
import static org.junit.jupiter.api.Assertions.*;

class SlidingWindowBasicoTest {
    private SlidingWindowBasico slidingWindow;
    
    @BeforeEach
    void setUp() {
        slidingWindow = new SlidingWindowBasico();
    }
    
    @ParameterizedTest
    @CsvSource({
        "'2,1,5,1,3,2', 3, 9",
        "'1,2,3,4,5', 2, 9",
        "'5', 1, 5"
    })
    @DisplayName("Max sum subarray deve retornar soma máxima correta")
    void testMaxSumSubarray(String arrayStr, int k, int expected) {
        int[] nums = Arrays.stream(arrayStr.split(","))
                          .mapToInt(Integer::parseInt)
                          .toArray();
        
        int result = slidingWindow.maxSumSubarray(nums, k);
        assertEquals(expected, result);
    }
    
    @ParameterizedTest
    @MethodSource("provideLongestSubstringInputs")
    @DisplayName("Longest substring deve encontrar maior substring sem repetição")
    void testLongestSubstring(String input, int expected) {
        int result = slidingWindow.lengthOfLongestSubstring(input);
        assertEquals(expected, result);
    }
    
    static Stream<Arguments> provideLongestSubstringInputs() {
        return Stream.of(
            Arguments.of("abcabcbb", 3),
            Arguments.of("bbbbb", 1),
            Arguments.of("pwwkew", 3),
            Arguments.of("", 0),
            Arguments.of("abcdef", 6)
        );
    }
    
    @Test
    @DisplayName("Sliding window maximum deve retornar máximos corretos")
    void testSlidingWindowMaximum() {
        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
        int[] expected = {3, 3, 5, 5, 6, 7};
        int[] result = slidingWindow.slidingWindowMaximum(nums, 3);
        
        assertArrayEquals(expected, result);
    }
    
    @Test
    @DisplayName("Performance deve estar dentro dos limites esperados")
    void testPerformance() {
        int[] largeArray = new int[100000];
        Arrays.fill(largeArray, 1);
        
        long startTime = System.currentTimeMillis();
        slidingWindow.maxSumSubarray(largeArray, 1000);
        long executionTime = System.currentTimeMillis() - startTime;
        
        assertTrue(executionTime < 100, "Execução deve ser menor que 100ms");
        
        SlidingWindowStats stats = slidingWindow.getStats();
        assertTrue(stats.getOperationsCount() > 0, "Deve registrar operações");
        assertTrue(stats.getEfficiency() >= 0, "Eficiência deve ser não-negativa");
    }
}
```

### Performance Testing com JMH
```java
import org.openjdk.jmh.annotations.*;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Benchmark)
@Fork(1)
@Warmup(iterations = 3, time = 1)
@Measurement(iterations = 5, time = 1)
public class SlidingWindowBenchmark {
    
    private SlidingWindowBasico slidingWindow;
    private int[] largeArray;
    private String longString;
    
    @Setup
    public void setup() {
        slidingWindow = new SlidingWindowBasico();
        
        largeArray = new int[10000];
        Random random = new Random(42);
        for (int i = 0; i < largeArray.length; i++) {
            largeArray[i] = random.nextInt(100);
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10000; i++) {
            sb.append((char) ('a' + random.nextInt(26)));
        }
        longString = sb.toString();
    }
    
    @Benchmark
    public int benchmarkMaxSumSubarray() {
        slidingWindow.resetCounters();
        return slidingWindow.maxSumSubarray(largeArray, 100);
    }
    
    @Benchmark
    public int benchmarkLongestSubstring() {
        slidingWindow.resetCounters();
        return slidingWindow.lengthOfLongestSubstring(longString);
    }
    
    @Benchmark
    public int[] benchmarkSlidingWindowMaximum() {
        slidingWindow.resetCounters();
        return slidingWindow.slidingWindowMaximum(largeArray, 50);
    }
    
    @Benchmark
    public List<Integer> benchmarkFindAnagrams() {
        slidingWindow.resetCounters();
        return slidingWindow.findAnagrams(longString, "abc");
    }
}
```

## Integração Spring Framework

### Spring Service
```java
@Service
@Transactional
public class SlidingWindowService {
    
    private final SlidingWindowBasico slidingWindow;
    private final SlidingWindowMetrics metrics;
    
    @Autowired
    public SlidingWindowService(SlidingWindowBasico slidingWindow,
                              SlidingWindowMetrics metrics) {
        this.slidingWindow = slidingWindow;
        this.metrics = metrics;
    }
    
    @Async
    public CompletableFuture<MaxSumResponse> findMaxSumAsync(int[] array, int k) {
        long startTime = System.currentTimeMillis();
        
        try {
            int maxSum = slidingWindow.maxSumSubarray(array, k);
            long executionTime = System.currentTimeMillis() - startTime;
            
            SlidingWindowStats stats = slidingWindow.getStats();
            metrics.recordExecution("maxsum", stats.getOperationsCount(), executionTime);
            
            return CompletableFuture.completedFuture(
                MaxSumResponse.builder()
                    .maxSum(maxSum)
                    .windowSize(k)
                    .arrayLength(array.length)
                    .executionTimeMs(executionTime)
                    .stats(stats)
                    .build()
            );
        } catch (Exception e) {
            return CompletableFuture.failedFuture(e);
        }
    }
    
    @Cacheable(value = "anagrams", key = "#text + '_' + #pattern")
    public List<Integer> findAnagrams(String text, String pattern) {
        return slidingWindow.findAnagrams(text, pattern);
    }
    
    @EventListener
    public void handleDataStream(DataStreamEvent event) {
        int[] data = event.getData();
        int windowSize = event.getWindowSize();
        
        int maxSum = slidingWindow.maxSumSubarray(data, windowSize);
        
        // Publicar resultado
        applicationEventPublisher.publishEvent(
            new SlidingWindowResultEvent(maxSum, event.getStreamId())
        );
    }
}
```

### REST Controller
```java
@RestController
@RequestMapping("/api/sliding-window")
@Validated
public class SlidingWindowController {
    
    @Autowired
    private SlidingWindowService slidingWindowService;
    
    @PostMapping("/max-sum")
    public ResponseEntity<MaxSumResponse> findMaxSum(
            @RequestBody @Valid MaxSumRequest request) {
        
        try {
            CompletableFuture<MaxSumResponse> future = 
                slidingWindowService.findMaxSumAsync(
                    request.getArray(), 
                    request.getWindowSize()
                );
            
            MaxSumResponse response = future.get(5, TimeUnit.SECONDS);
            return ResponseEntity.ok(response);
            
        } catch (TimeoutException e) {
            return ResponseEntity.status(HttpStatus.REQUEST_TIMEOUT)
                .body(MaxSumResponse.builder()
                    .error("Timeout: array muito grande")
                    .build());
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(MaxSumResponse.builder()
                    .error("Erro interno: " + e.getMessage())
                    .build());
        }
    }
    
    @GetMapping("/longest-substring")
    public ResponseEntity<LongestSubstringResponse> findLongestSubstring(
            @RequestParam String text) {
        
        long startTime = System.currentTimeMillis();
        int length = slidingWindowService.lengthOfLongestSubstring(text);
        long executionTime = System.currentTimeMillis() - startTime;
        
        return ResponseEntity.ok(
            LongestSubstringResponse.builder()
                .length(length)
                .inputLength(text.length())
                .executionTimeMs(executionTime)
                .build()
        );
    }
    
    @PostMapping("/stream/analyze")
    public ResponseEntity<StreamAnalysisResponse> analyzeStream(
            @RequestBody @Valid StreamAnalysisRequest request) {
        
        List<StreamResult> results = new ArrayList<>();
        
        for (StreamWindow window : request.getWindows()) {
            int maxSum = slidingWindowService.maxSumSubarray(
                window.getData(), 
                window.getSize()
            );
            
            results.add(StreamResult.builder()
                .windowId(window.getId())
                .maxSum(maxSum)
                .timestamp(System.currentTimeMillis())
                .build());
        }
        
        return ResponseEntity.ok(
            StreamAnalysisResponse.builder()
                .results(results)
                .totalWindows(results.size())
                .build()
        );
    }
}
```

## Aplicações Empresariais

### 1. Real-time Analytics Service
```java
@Service
public class RealTimeAnalyticsService {
    
    private final SlidingWindowBasico slidingWindow;
    private final CircularBuffer<DataPoint> dataBuffer;
    
    @EventListener
    public void processDataPoint(DataPointEvent event) {
        DataPoint dataPoint = event.getDataPoint();
        dataBuffer.add(dataPoint);
        
        if (dataBuffer.isFull()) {
            int[] values = dataBuffer.getValues();
            
            // Calcular métricas com sliding window
            int maxSum = slidingWindow.maxSumSubarray(values, 10);
            int maxProduct = slidingWindow.numSubarrayProductLessThanK(values, 1000);
            
            // Publicar alertas se necessário
            if (maxSum > threshold) {
                alertService.publishAlert(new HighValueAlert(maxSum, dataPoint.getTimestamp()));
            }
        }
    }
}

@Component
public class CircularBuffer<T> {
    private final Object[] buffer;
    private final int capacity;
    private int size = 0;
    private int writeIndex = 0;
    
    public CircularBuffer(int capacity) {
        this.capacity = capacity;
        this.buffer = new Object[capacity];
    }
    
    public synchronized void add(T item) {
        buffer[writeIndex] = item;
        writeIndex = (writeIndex + 1) % capacity;
        
        if (size < capacity) {
            size++;
        }
    }
    
    public synchronized boolean isFull() {
        return size == capacity;
    }
    
    @SuppressWarnings("unchecked")
    public synchronized int[] getValues() {
        int[] values = new int[size];
        int readIndex = (writeIndex - size + capacity) % capacity;
        
        for (int i = 0; i < size; i++) {
            DataPoint dp = (DataPoint) buffer[readIndex];
            values[i] = dp.getValue();
            readIndex = (readIndex + 1) % capacity;
        }
        
        return values;
    }
}
```

### 2. Log Analysis System
```java
@Service
public class LogAnalysisService {
    
    private final SlidingWindowBasico slidingWindow;
    
    public LogAnalysisResult analyzeLogPattern(List<LogEntry> logs, String pattern) {
        String logText = logs.stream()
            .map(LogEntry::getMessage)
            .collect(Collectors.joining(" "));
        
        List<Integer> occurrences = slidingWindow.findAnagrams(logText, pattern);
        
        return LogAnalysisResult.builder()
            .pattern(pattern)
            .occurrences(occurrences)
            .totalLogs(logs.size())
            .matchRate((double) occurrences.size() / logs.size())
            .build();
    }
    
    public ErrorRateAnalysis analyzeErrorRate(List<LogEntry> logs, Duration windowDuration) {
        Map<Long, Integer> errorCounts = new HashMap<>();
        long windowSizeMs = windowDuration.toMillis();
        
        // Agrupar logs por janelas de tempo
        logs.stream()
            .filter(log -> log.getLevel() == LogLevel.ERROR)
            .forEach(log -> {
                long windowStart = (log.getTimestamp() / windowSizeMs) * windowSizeMs;
                errorCounts.merge(windowStart, 1, Integer::sum);
            });
        
        int[] errorRates = errorCounts.values().stream()
            .mapToInt(Integer::intValue)
            .toArray();
        
        int maxErrorRate = slidingWindow.maxSumSubarray(errorRates, 3);
        
        return ErrorRateAnalysis.builder()
            .maxErrorRate(maxErrorRate)
            .windowDuration(windowDuration)
            .totalWindows(errorRates.length)
            .build();
    }
}
```

### 3. Financial Trading System
```java
@Service
public class TradingAnalysisService {
    
    private final SlidingWindowBasico slidingWindow;
    
    public TradingSignal analyzePriceMovement(List<PricePoint> prices, int windowSize) {
        int[] priceValues = prices.stream()
            .mapToInt(PricePoint::getPrice)
            .toArray();
        
        // Encontrar janela com maior soma (maior momentum)
        int maxSum = slidingWindow.maxSumSubarray(priceValues, windowSize);
        
        // Encontrar janela com maior variação
        int[] maxWindow = slidingWindow.slidingWindowMaximum(priceValues, windowSize);
        
        return TradingSignal.builder()
            .maxMomentum(maxSum)
            .maxVariation(Arrays.stream(maxWindow).max().orElse(0))
            .recommendation(calculateRecommendation(maxSum, maxWindow))
            .confidence(calculateConfidence(priceValues, windowSize))
            .build();
    }
    
    public VolatilityAnalysis analyzeVolatility(List<PricePoint> prices) {
        // Calcular diferenças percentuais
        List<Double> changes = new ArrayList<>();
        for (int i = 1; i < prices.size(); i++) {
            double change = ((double) prices.get(i).getPrice() - prices.get(i-1).getPrice()) 
                          / prices.get(i-1).getPrice() * 100;
            changes.add(Math.abs(change));
        }
        
        // Converter para int array para sliding window
        int[] volatilityData = changes.stream()
            .mapToInt(d -> (int) (d * 100))  // Scale para int
            .toArray();
        
        int avgVolatility = slidingWindow.maxSumSubarray(volatilityData, 5) / 5;
        
        return VolatilityAnalysis.builder()
            .averageVolatility(avgVolatility / 100.0)  // Scale back
            .highVolatilityPeriods(findHighVolatilityPeriods(volatilityData))
            .riskLevel(calculateRiskLevel(avgVolatility))
            .build();
    }
}
```

## Monitoramento e Observabilidade

### Custom Metrics com Micrometer
```java
@Component
public class SlidingWindowMetrics {
    
    private final Counter operationsCounter;
    private final Counter windowAdjustmentsCounter;
    private final Timer executionTimer;
    private final Gauge maxWindowSizeGauge;
    private final AtomicInteger currentMaxWindowSize = new AtomicInteger(0);
    
    public SlidingWindowMetrics(MeterRegistry meterRegistry) {
        this.operationsCounter = Counter.builder("sliding_window.operations.total")
            .description("Total number of sliding window operations")
            .register(meterRegistry);
            
        this.windowAdjustmentsCounter = Counter.builder("sliding_window.adjustments.total")
            .description("Total number of window adjustments")
            .register(meterRegistry);
            
        this.executionTimer = Timer.builder("sliding_window.execution.time")
            .description("Execution time of sliding window algorithms")
            .register(meterRegistry);
            
        this.maxWindowSizeGauge = Gauge.builder("sliding_window.max.size")
            .description("Maximum window size used")
            .register(meterRegistry, currentMaxWindowSize, AtomicInteger::get);
    }
    
    public void recordExecution(String algorithm, int operations, int adjustments, long timeMs) {
        operationsCounter.increment(operations);
        windowAdjustmentsCounter.increment(adjustments);
        executionTimer.record(timeMs, TimeUnit.MILLISECONDS);
        
        Tags tags = Tags.of("algorithm", algorithm);
        // Record per-algorithm metrics...
    }
    
    public void updateMaxWindowSize(int size) {
        currentMaxWindowSize.updateAndGet(current -> Math.max(current, size));
    }
}
```

### Health Checks
```java
@Component
public class SlidingWindowHealthIndicator implements HealthIndicator {
    
    private final SlidingWindowService slidingWindowService;
    
    @Override
    public Health health() {
        try {
            // Test simple sliding window operation
            int[] testArray = {1, 2, 3, 4, 5};
            long startTime = System.currentTimeMillis();
            
            int result = slidingWindowService.maxSumSubarray(testArray, 3);
            long executionTime = System.currentTimeMillis() - startTime;
            
            if (result == 12 && executionTime < 10) {
                return Health.up()
                    .withDetail("algorithm", "maxsum")
                    .withDetail("result", result)
                    .withDetail("executionTimeMs", executionTime)
                    .build();
            } else {
                return Health.down()
                    .withDetail("reason", "Performance degradation or incorrect result")
                    .withDetail("expected", 12)
                    .withDetail("actual", result)
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
  <i>☕ "Sliding Window em Java: onde a eficiência encontra a elegância empresarial"</i>
  <br>
  <i>☕ "Sliding Window in Java: where efficiency meets enterprise elegance"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E67E22&height=120&section=footer"/>

</div>
