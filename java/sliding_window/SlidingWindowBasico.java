import java.util.*;

/**
 * Implementação de algoritmos usando a técnica de Sliding Window (Janela Deslizante)
 * 
 * Esta classe implementa várias técnicas de sliding window:
 * 1. Maximum Sum Subarray (Soma Máxima de Subarray)
 * 2. Longest Substring Without Repeating Characters (Maior Substring Sem Repetições)
 * 3. Minimum Window Substring (Menor Janela Contendo Substring)
 * 4. Sliding Window Maximum (Máximo em Janela Deslizante)
 * 5. Find All Anagrams (Encontrar Todos os Anagramas)
 * 6. Longest Subarray with K Distinct (Maior Subarray com K Elementos Distintos)
 * 
 * Autor: matheussricardoo
 */
public class SlidingWindowBasico {
    
    private int operationsCount;
    private int comparisonsCount;
    
    public SlidingWindowBasico() {
        resetCounters();
    }
    
    /**
     * Reset dos contadores de performance
     */
    public void resetCounters() {
        this.operationsCount = 0;
        this.comparisonsCount = 0;
    }
    
    /**
     * Encontra a soma máxima de um subarray de tamanho k
     * 
     * @param nums Lista de números
     * @param k Tamanho da janela
     * @return Soma máxima do subarray de tamanho k
     * 
     * Complexidade: O(n) tempo, O(1) espaço
     */
    public int maxSumSubarrayFixed(int[] nums, int k) {
        resetCounters();
        
        if (nums.length == 0 || k <= 0 || k > nums.length) {
            return 0;
        }
        
        // Calcular soma da primeira janela
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
            operationsCount++;
        }
        
        int maxSum = windowSum;
        
        // Deslizar janela
        for (int i = k; i < nums.length; i++) {
            // Remover elemento que sai, adicionar que entra
            windowSum = windowSum - nums[i - k] + nums[i];
            maxSum = Math.max(maxSum, windowSum);
            operationsCount += 2;
            comparisonsCount++;
        }
        
        return maxSum;
    }
    
    /**
     * Encontra o comprimento da maior substring sem caracteres repetidos
     * 
     * @param s String de entrada
     * @return Comprimento da maior substring sem repetições
     * 
     * Complexidade: O(n) tempo, O(min(m,n)) espaço
     */
    public int longestSubstringWithoutRepeating(String s) {
        resetCounters();
        
        if (s.length() == 0) {
            return 0;
        }
        
        Set<Character> charSet = new HashSet<>();
        int left = 0;
        int maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);
            
            // Contrair janela enquanto há repetição
            while (charSet.contains(rightChar)) {
                charSet.remove(s.charAt(left));
                left++;
                operationsCount += 2;
            }
            
            // Expandir janela
            charSet.add(rightChar);
            maxLength = Math.max(maxLength, right - left + 1);
            operationsCount++;
            comparisonsCount++;
        }
        
        return maxLength;
    }
    
    /**
     * Encontra a menor janela em s que contém todos os caracteres de t
     * 
     * @param s String principal
     * @param t String padrão
     * @return Menor substring de s que contém todos caracteres de t
     * 
     * Complexidade: O(|s| + |t|) tempo, O(|s| + |t|) espaço
     */
    public String minWindowSubstring(String s, String t) {
        resetCounters();
        
        if (s.length() == 0 || t.length() == 0) {
            return "";
        }
        
        // Contar caracteres necessários
        Map<Character, Integer> dictT = new HashMap<>();
        for (char c : t.toCharArray()) {
            dictT.put(c, dictT.getOrDefault(c, 0) + 1);
        }
        
        int required = dictT.size();
        int left = 0;
        int formed = 0;
        
        // Dicionário para contar caracteres na janela atual
        Map<Character, Integer> windowCounts = new HashMap<>();
        
        // Resultado: [comprimento da janela, left, right]
        int[] ans = {Integer.MAX_VALUE, 0, 0};
        
        for (int right = 0; right < s.length(); right++) {
            // Adicionar um caractere do lado direito da janela
            char character = s.charAt(right);
            windowCounts.put(character, windowCounts.getOrDefault(character, 0) + 1);
            operationsCount++;
            
            // Se a frequência do caractere atual na janela
            // iguala à frequência desejada em t, incrementar formed
            if (dictT.containsKey(character) && 
                windowCounts.get(character).intValue() == dictT.get(character).intValue()) {
                formed++;
                comparisonsCount++;
            }
            
            // Tentar contrair a janela até que ela deixe de ser 'desejável'
            while (left <= right && formed == required) {
                character = s.charAt(left);
                
                // Salvar a menor janela até agora
                if (right - left + 1 < ans[0]) {
                    ans[0] = right - left + 1;
                    ans[1] = left;
                    ans[2] = right;
                    comparisonsCount++;
                }
                
                // O caractere no início da janela não faz mais parte da janela
                windowCounts.put(character, windowCounts.get(character) - 1);
                if (dictT.containsKey(character) && 
                    windowCounts.get(character).intValue() < dictT.get(character).intValue()) {
                    formed--;
                    comparisonsCount++;
                }
                
                // Mover ponteiro esquerdo para a frente
                left++;
                operationsCount++;
            }
        }
        
        return ans[0] == Integer.MAX_VALUE ? "" : s.substring(ans[1], ans[2] + 1);
    }
    
    /**
     * Encontra o máximo em cada janela de tamanho k
     * 
     * @param nums Lista de números
     * @param k Tamanho da janela
     * @return Lista com o máximo de cada janela
     * 
     * Complexidade: O(n) tempo, O(k) espaço
     */
    public int[] slidingWindowMaximum(int[] nums, int k) {
        resetCounters();
        
        if (nums.length == 0 || k <= 0) {
            return new int[0];
        }
        
        if (k == 1) {
            return nums;
        }
        
        // Deque para armazenar índices
        // Manteremos elementos em ordem decrescente
        Deque<Integer> dq = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];
        int resultIndex = 0;
        
        for (int i = 0; i < nums.length; i++) {
            // Remover elementos fora da janela atual
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.pollFirst();
                operationsCount++;
            }
            
            // Remover elementos menores que o atual
            // (eles nunca serão o máximo)
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) {
                dq.pollLast();
                operationsCount++;
                comparisonsCount++;
            }
            
            // Adicionar elemento atual
            dq.offerLast(i);
            operationsCount++;
            
            // Adicionar máximo ao resultado (se janela está completa)
            if (i >= k - 1) {
                result[resultIndex++] = nums[dq.peekFirst()];
                operationsCount++;
            }
        }
        
        return result;
    }
    
    /**
     * Encontra todos os índices de anagramas de p em s
     * 
     * @param s String principal
     * @param p String padrão
     * @return Lista de índices onde anagramas de p começam em s
     * 
     * Complexidade: O(|s|) tempo, O(1) espaço
     */
    public List<Integer> findAnagrams(String s, String p) {
        resetCounters();
        
        if (p.length() > s.length()) {
            return new ArrayList<>();
        }
        
        // Arrays de frequência para p e janela atual
        int[] pCount = new int[26];
        int[] windowCount = new int[26];
        
        // Contar frequências em p
        for (char c : p.toCharArray()) {
            pCount[c - 'a']++;
            operationsCount++;
        }
        
        List<Integer> result = new ArrayList<>();
        int windowSize = p.length();
        
        for (int i = 0; i < s.length(); i++) {
            // Adicionar caractere à janela
            windowCount[s.charAt(i) - 'a']++;
            operationsCount++;
            
            // Remover caractere se janela excede tamanho
            if (i >= windowSize) {
                windowCount[s.charAt(i - windowSize) - 'a']--;
                operationsCount++;
            }
            
            // Verificar se é anagrama (janela tem tamanho correto)
            if (i >= windowSize - 1) {
                if (Arrays.equals(windowCount, pCount)) {
                    result.add(i - windowSize + 1);
                    comparisonsCount++;
                }
            }
        }
        
        return result;
    }
    
    /**
     * Encontra o comprimento do maior subarray com exatamente k elementos distintos
     * 
     * @param nums Lista de números
     * @param k Número de elementos distintos desejados
     * @return Comprimento do maior subarray com k elementos distintos
     * 
     * Complexidade: O(n) tempo, O(k) espaço
     */
    public int longestSubarrayKDistinct(int[] nums, int k) {
        resetCounters();
        
        if (nums.length == 0 || k <= 0) {
            return 0;
        }
        
        int left = 0;
        int maxLength = 0;
        Map<Integer, Integer> countMap = new HashMap<>();
        
        for (int right = 0; right < nums.length; right++) {
            // Adicionar elemento à janela
            countMap.put(nums[right], countMap.getOrDefault(nums[right], 0) + 1);
            operationsCount++;
            
            // Contrair janela se tiver mais de k elementos distintos
            while (countMap.size() > k) {
                countMap.put(nums[left], countMap.get(nums[left]) - 1);
                if (countMap.get(nums[left]) == 0) {
                    countMap.remove(nums[left]);
                }
                left++;
                operationsCount += 2;
                comparisonsCount++;
            }
            
            // Atualizar máximo se janela tem exatamente k elementos distintos
            if (countMap.size() == k) {
                maxLength = Math.max(maxLength, right - left + 1);
                comparisonsCount++;
            }
        }
        
        return maxLength;
    }
    
    /**
     * Encontra a soma máxima de subarray com soma <= target
     * 
     * @param nums Lista de números positivos
     * @param target Soma alvo máxima
     * @return Soma máxima de subarray que não excede target
     * 
     * Complexidade: O(n) tempo, O(1) espaço
     */
    public int maxSumSubarrayVariable(int[] nums, int target) {
        resetCounters();
        
        if (nums.length == 0 || target <= 0) {
            return 0;
        }
        
        int left = 0;
        int currentSum = 0;
        int maxSum = 0;
        
        for (int right = 0; right < nums.length; right++) {
            // Expandir janela
            currentSum += nums[right];
            operationsCount++;
            
            // Contrair janela se soma excede target
            while (currentSum > target && left <= right) {
                currentSum -= nums[left];
                left++;
                operationsCount += 2;
                comparisonsCount++;
            }
            
            // Atualizar máximo
            maxSum = Math.max(maxSum, currentSum);
            comparisonsCount++;
        }
        
        return maxSum;
    }
    
    /**
     * Getters para contadores de performance
     */
    public int getOperationsCount() {
        return operationsCount;
    }
    
    public int getComparisonsCount() {
        return comparisonsCount;
    }
    
    /**
     * Método para demonstrar o uso dos algoritmos
     */
    public static void demonstrarSlidingWindow() {
        SlidingWindowBasico sw = new SlidingWindowBasico();
        
        System.out.println("=".repeat(80));
        System.out.println("DEMONSTRAÇÃO: Algoritmos de Sliding Window");
        System.out.println("=".repeat(80));
        
        // 1. Maximum Sum Subarray (Fixed Window)
        System.out.println("\n1. MAXIMUM SUM SUBARRAY - JANELA FIXA");
        System.out.println("-".repeat(50));
        int[] nums1 = {1, 4, 2, 9, 5, 10, 13, 8, 5};
        int k = 3;
        
        System.out.printf("Array: %s\n", Arrays.toString(nums1));
        System.out.printf("Tamanho da janela: %d\n", k);
        
        long start = System.nanoTime();
        int maxSum = sw.maxSumSubarrayFixed(nums1, k);
        long duration = System.nanoTime() - start;
        
        System.out.printf("Soma máxima: %d\n", maxSum);
        System.out.printf("Operações: %d\n", sw.getOperationsCount());
        System.out.printf("Comparações: %d\n", sw.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 2. Longest Substring Without Repeating Characters
        System.out.println("\n2. LONGEST SUBSTRING WITHOUT REPEATING");
        System.out.println("-".repeat(50));
        String s1 = "abcabcbb";
        
        System.out.printf("String: '%s'\n", s1);
        
        start = System.nanoTime();
        int length = sw.longestSubstringWithoutRepeating(s1);
        duration = System.nanoTime() - start;
        
        System.out.printf("Comprimento da maior substring: %d\n", length);
        System.out.printf("Operações: %d\n", sw.getOperationsCount());
        System.out.printf("Comparações: %d\n", sw.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 3. Minimum Window Substring
        System.out.println("\n3. MINIMUM WINDOW SUBSTRING");
        System.out.println("-".repeat(50));
        String s2 = "ADOBECODEBANC";
        String t = "ABC";
        
        System.out.printf("String principal: '%s'\n", s2);
        System.out.printf("Padrão: '%s'\n", t);
        
        start = System.nanoTime();
        String minWindow = sw.minWindowSubstring(s2, t);
        duration = System.nanoTime() - start;
        
        System.out.printf("Menor janela: '%s'\n", minWindow);
        System.out.printf("Operações: %d\n", sw.getOperationsCount());
        System.out.printf("Comparações: %d\n", sw.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 4. Sliding Window Maximum
        System.out.println("\n4. SLIDING WINDOW MAXIMUM");
        System.out.println("-".repeat(50));
        int[] nums2 = {1, 3, -1, -3, 5, 3, 6, 7};
        int k2 = 3;
        
        System.out.printf("Array: %s\n", Arrays.toString(nums2));
        System.out.printf("Tamanho da janela: %d\n", k2);
        
        start = System.nanoTime();
        int[] maximums = sw.slidingWindowMaximum(nums2, k2);
        duration = System.nanoTime() - start;
        
        System.out.printf("Máximos: %s\n", Arrays.toString(maximums));
        System.out.printf("Operações: %d\n", sw.getOperationsCount());
        System.out.printf("Comparações: %d\n", sw.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 5. Find All Anagrams
        System.out.println("\n5. FIND ALL ANAGRAMS");
        System.out.println("-".repeat(50));
        String s3 = "abab";
        String p = "ab";
        
        System.out.printf("String principal: '%s'\n", s3);
        System.out.printf("Padrão: '%s'\n", p);
        
        start = System.nanoTime();
        List<Integer> anagrams = sw.findAnagrams(s3, p);
        duration = System.nanoTime() - start;
        
        System.out.printf("Índices de anagramas: %s\n", anagrams);
        System.out.printf("Operações: %d\n", sw.getOperationsCount());
        System.out.printf("Comparações: %d\n", sw.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 6. Longest Subarray with K Distinct
        System.out.println("\n6. LONGEST SUBARRAY WITH K DISTINCT");
        System.out.println("-".repeat(50));
        int[] nums3 = {1, 2, 1, 2, 3};
        int k3 = 2;
        
        System.out.printf("Array: %s\n", Arrays.toString(nums3));
        System.out.printf("K (elementos distintos): %d\n", k3);
        
        start = System.nanoTime();
        int longest = sw.longestSubarrayKDistinct(nums3, k3);
        duration = System.nanoTime() - start;
        
        System.out.printf("Comprimento do maior subarray: %d\n", longest);
        System.out.printf("Operações: %d\n", sw.getOperationsCount());
        System.out.printf("Comparações: %d\n", sw.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 7. Maximum Sum Subarray (Variable Window)
        System.out.println("\n7. MAXIMUM SUM SUBARRAY - JANELA VARIÁVEL");
        System.out.println("-".repeat(50));
        int[] nums4 = {1, 2, 3, 4, 5};
        int target = 8;
        
        System.out.printf("Array: %s\n", Arrays.toString(nums4));
        System.out.printf("Target (soma máxima): %d\n", target);
        
        start = System.nanoTime();
        int maxSumVar = sw.maxSumSubarrayVariable(nums4, target);
        duration = System.nanoTime() - start;
        
        System.out.printf("Soma máxima <= %d: %d\n", target, maxSumVar);
        System.out.printf("Operações: %d\n", sw.getOperationsCount());
        System.out.printf("Comparações: %d\n", sw.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // Análise comparativa
        System.out.println("\n" + "=".repeat(80));
        System.out.println("ANÁLISE COMPARATIVA: Sliding Window vs Força Bruta");
        System.out.println("=".repeat(80));
        
        // Exemplo: Maximum Sum Subarray
        int[] testArray = new int[1000];
        for (int i = 0; i < testArray.length; i++) {
            testArray[i] = i;
        }
        int windowSize = 100;
        
        System.out.printf("Array de teste: %d elementos\n", testArray.length);
        System.out.printf("Tamanho da janela: %d\n", windowSize);
        
        // Sliding Window
        start = System.nanoTime();
        int resultSW = sw.maxSumSubarrayFixed(testArray, windowSize);
        long timeSW = System.nanoTime() - start;
        
        System.out.printf("\nSliding Window:\n");
        System.out.printf("  Resultado: %d\n", resultSW);
        System.out.printf("  Tempo: %.2fms\n", timeSW / 1e6);
        System.out.printf("  Complexidade: O(n)\n");
        
        // Força Bruta (simulação)
        start = System.nanoTime();
        int maxSumBF = 0;
        for (int i = 0; i <= testArray.length - windowSize; i++) {
            int currentSum = 0;
            for (int j = i; j < i + windowSize; j++) {
                currentSum += testArray[j];
            }
            maxSumBF = Math.max(maxSumBF, currentSum);
        }
        long timeBF = System.nanoTime() - start;
        
        System.out.printf("\nForça Bruta:\n");
        System.out.printf("  Resultado: %d\n", maxSumBF);
        System.out.printf("  Tempo: %.2fms\n", timeBF / 1e6);
        System.out.printf("  Complexidade: O(n*k)\n");
        
        double improvement = (double) timeBF / timeSW;
        System.out.printf("\nMelhoria de performance: %.1fx mais rápido\n", improvement);
        
        // Estatísticas finais
        System.out.println("\n" + "=".repeat(80));
        System.out.println("RESUMO DA TÉCNICA DE SLIDING WINDOW");
        System.out.println("=".repeat(80));
        System.out.println("✓ Otimiza problemas de subarray/substring");
        System.out.println("✓ Reduz complexidade de O(n²) para O(n)");
        System.out.println("✓ Duas variações: janela fixa e janela variável");
        System.out.println("✓ Útil para problemas de otimização e busca");
        System.out.println("✓ Elimina recálculos desnecessários");
        
        System.out.println("\nTipos de problemas resolvidos:");
        System.out.println("• Maximum/Minimum em subarrays");
        System.out.println("• Substrings com propriedades específicas");
        System.out.println("• Problemas de contagem e frequência");
        System.out.println("• Otimização com restrições");
        System.out.println("• Análise de sequências temporais");
    }
    
    public static void main(String[] args) {
        demonstrarSlidingWindow();
    }
}
