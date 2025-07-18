import java.util.*;

/**
 * Implementação de algoritmos usando a técnica de Two Pointer (Dois Ponteiros)
 * 
 * Esta classe implementa várias técnicas de dois ponteiros:
 * 1. Two Sum em Array Ordenado
 * 2. Verificação de Palíndromo
 * 3. Remoção de Duplicatas
 * 4. Container com Mais Água
 * 5. Three Sum
 * 6. Sort Colors (Dutch National Flag)
 * 
 * Autor: matheussricardoo
 */
public class TwoPointerBasico {
    
    private int operationsCount;
    private int comparisonsCount;
    
    public TwoPointerBasico() {
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
     * Encontra dois números em array ordenado que somam target
     * 
     * @param nums Array ordenado de números
     * @param target Valor alvo da soma
     * @return Array com os índices dos dois números, ou array vazio se não encontrado
     * 
     * Complexidade: O(n) tempo, O(1) espaço
     */
    public int[] twoSumSorted(int[] nums, int target) {
        resetCounters();
        
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            int currentSum = nums[left] + nums[right];
            operationsCount++;
            comparisonsCount++;
            
            if (currentSum == target) {
                return new int[]{left, right};
            } else if (currentSum < target) {
                left++;
            } else {
                right--;
            }
            operationsCount++;
        }
        
        return new int[]{}; // Não encontrado
    }
    
    /**
     * Verifica se uma string é palíndromo
     * 
     * @param s String a ser verificada
     * @return true se é palíndromo, false caso contrário
     * 
     * Complexidade: O(n) tempo, O(1) espaço
     */
    public boolean isPalindrome(String s) {
        resetCounters();
        
        int left = 0, right = s.length() - 1;
        
        while (left < right) {
            comparisonsCount++;
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
            operationsCount += 2;
        }
        
        return true;
    }
    
    /**
     * Remove duplicatas de array ordenado in-place
     * 
     * @param nums Array ordenado de números
     * @return Novo comprimento do array sem duplicatas
     * 
     * Complexidade: O(n) tempo, O(1) espaço
     */
    public int removeDuplicates(int[] nums) {
        resetCounters();
        
        if (nums.length <= 1) {
            return nums.length;
        }
        
        int writePos = 1;
        
        for (int readPos = 1; readPos < nums.length; readPos++) {
            comparisonsCount++;
            if (nums[readPos] != nums[readPos - 1]) {
                nums[writePos] = nums[readPos];
                writePos++;
                operationsCount++;
            }
            operationsCount++;
        }
        
        return writePos;
    }
    
    /**
     * Encontra o container que pode reter mais água
     * 
     * @param heights Array com alturas das paredes
     * @return Área máxima que pode ser contida
     * 
     * Complexidade: O(n) tempo, O(1) espaço
     */
    public int containerWithMostWater(int[] heights) {
        resetCounters();
        
        int left = 0, right = heights.length - 1;
        int maxArea = 0;
        
        while (left < right) {
            // Calcular área atual
            int width = right - left;
            int height = Math.min(heights[left], heights[right]);
            int area = width * height;
            
            maxArea = Math.max(maxArea, area);
            operationsCount += 3;
            comparisonsCount++;
            
            // Mover ponteiro da altura menor
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
            comparisonsCount++;
            operationsCount++;
        }
        
        return maxArea;
    }
    
    /**
     * Encontra todos os triplets únicos que somam zero
     * 
     * @param nums Array de números
     * @return Lista de triplets que somam zero
     * 
     * Complexidade: O(n²) tempo, O(1) espaço extra
     */
    public List<List<Integer>> threeSum(int[] nums) {
        resetCounters();
        
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; i++) {
            // Pular duplicatas para o primeiro número
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int left = i + 1, right = nums.length - 1;
            
            while (left < right) {
                int currentSum = nums[i] + nums[left] + nums[right];
                operationsCount++;
                comparisonsCount++;
                
                if (currentSum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Pular duplicatas
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                        operationsCount++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                        operationsCount++;
                    }
                    
                    left++;
                    right--;
                    operationsCount += 2;
                } else if (currentSum < 0) {
                    left++;
                    operationsCount++;
                } else {
                    right--;
                    operationsCount++;
                }
            }
        }
        
        return result;
    }
    
    /**
     * Ordena array com valores 0, 1, 2 (Dutch National Flag)
     * 
     * @param nums Array a ser ordenado
     * 
     * Complexidade: O(n) tempo, O(1) espaço
     */
    public void sortColors(int[] nums) {
        resetCounters();
        
        int low = 0, mid = 0, high = nums.length - 1;
        
        while (mid <= high) {
            comparisonsCount++;
            switch (nums[mid]) {
                case 0:
                    swap(nums, low, mid);
                    low++;
                    mid++;
                    operationsCount += 3;
                    break;
                case 1:
                    mid++;
                    operationsCount++;
                    break;
                case 2:
                    swap(nums, mid, high);
                    high--;
                    operationsCount += 2;
                    break;
            }
        }
    }
    
    /**
     * Método auxiliar para trocar elementos no array
     */
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
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
    public static void demonstrarTwoPointer() {
        TwoPointerBasico tp = new TwoPointerBasico();
        
        System.out.println("=".repeat(80));
        System.out.println("DEMONSTRAÇÃO: Algoritmos de Two Pointer");
        System.out.println("=".repeat(80));
        
        // 1. Two Sum em Array Ordenado
        System.out.println("\n1. TWO SUM EM ARRAY ORDENADO");
        System.out.println("-".repeat(40));
        int[] nums1 = {2, 7, 11, 15};
        int target = 9;
        
        System.out.printf("Array: %s\n", Arrays.toString(nums1));
        System.out.printf("Target: %d\n", target);
        
        long start = System.nanoTime();
        int[] result = tp.twoSumSorted(nums1, target);
        long duration = System.nanoTime() - start;
        
        System.out.printf("Índices encontrados: %s\n", Arrays.toString(result));
        if (result.length == 2) {
            System.out.printf("Valores: [%d, %d]\n", nums1[result[0]], nums1[result[1]]);
        }
        System.out.printf("Operações: %d\n", tp.getOperationsCount());
        System.out.printf("Comparações: %d\n", tp.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 2. Verificação de Palíndromo
        System.out.println("\n2. VERIFICAÇÃO DE PALÍNDROMO");
        System.out.println("-".repeat(40));
        String testString = "racecar";
        
        System.out.printf("String: '%s'\n", testString);
        
        start = System.nanoTime();
        boolean isPalin = tp.isPalindrome(testString);
        duration = System.nanoTime() - start;
        
        System.out.printf("É palíndromo: %b\n", isPalin);
        System.out.printf("Operações: %d\n", tp.getOperationsCount());
        System.out.printf("Comparações: %d\n", tp.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 3. Remoção de Duplicatas
        System.out.println("\n3. REMOÇÃO DE DUPLICATAS");
        System.out.println("-".repeat(40));
        int[] nums2 = {1, 1, 2, 2, 3, 4, 4, 5};
        int[] original = nums2.clone();
        
        System.out.printf("Array original: %s\n", Arrays.toString(original));
        
        start = System.nanoTime();
        int newLength = tp.removeDuplicates(nums2);
        duration = System.nanoTime() - start;
        
        System.out.printf("Array após remoção: %s\n", Arrays.toString(Arrays.copyOf(nums2, newLength)));
        System.out.printf("Novo comprimento: %d\n", newLength);
        System.out.printf("Operações: %d\n", tp.getOperationsCount());
        System.out.printf("Comparações: %d\n", tp.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 4. Container com Mais Água
        System.out.println("\n4. CONTAINER COM MAIS ÁGUA");
        System.out.println("-".repeat(40));
        int[] heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        
        System.out.printf("Alturas: %s\n", Arrays.toString(heights));
        
        start = System.nanoTime();
        int maxArea = tp.containerWithMostWater(heights);
        duration = System.nanoTime() - start;
        
        System.out.printf("Área máxima: %d\n", maxArea);
        System.out.printf("Operações: %d\n", tp.getOperationsCount());
        System.out.printf("Comparações: %d\n", tp.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 5. Three Sum
        System.out.println("\n5. THREE SUM");
        System.out.println("-".repeat(40));
        int[] nums3 = {-1, 0, 1, 2, -1, -4};
        
        System.out.printf("Array: %s\n", Arrays.toString(nums3));
        
        start = System.nanoTime();
        List<List<Integer>> triplets = tp.threeSum(nums3);
        duration = System.nanoTime() - start;
        
        System.out.printf("Triplets que somam zero: %s\n", triplets);
        System.out.printf("Número de triplets: %d\n", triplets.size());
        System.out.printf("Operações: %d\n", tp.getOperationsCount());
        System.out.printf("Comparações: %d\n", tp.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 6. Sort Colors (Dutch National Flag)
        System.out.println("\n6. SORT COLORS (DUTCH NATIONAL FLAG)");
        System.out.println("-".repeat(40));
        int[] colors = {2, 0, 2, 1, 1, 0};
        int[] original2 = colors.clone();
        
        System.out.printf("Array original: %s\n", Arrays.toString(original2));
        
        start = System.nanoTime();
        tp.sortColors(colors);
        duration = System.nanoTime() - start;
        
        System.out.printf("Array ordenado: %s\n", Arrays.toString(colors));
        System.out.printf("Operações: %d\n", tp.getOperationsCount());
        System.out.printf("Comparações: %d\n", tp.getComparisonsCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // Análise de Performance
        System.out.println("\n" + "=".repeat(80));
        System.out.println("ANÁLISE DE PERFORMANCE");
        System.out.println("=".repeat(80));
        
        // Teste com array grande
        int[] largeArray = new int[10000];
        for (int i = 0; i < largeArray.length; i++) {
            largeArray[i] = i * 2; // Array ordenado
        }
        
        System.out.printf("Teste com array de %d elementos\n", largeArray.length);
        
        // Two Sum
        start = System.nanoTime();
        tp.twoSumSorted(largeArray, 19998); // Procurar últimos dois elementos
        long twoSumTime = System.nanoTime() - start;
        
        System.out.printf("Two Sum - Tempo: %.2fms, Operações: %d\n", 
            twoSumTime / 1e6, tp.getOperationsCount());
        
        // Verificação de eficiência vs força bruta
        System.out.println("\nComparação com Força Bruta (simulação):");
        
        // Simulação força bruta O(n²)
        int n = largeArray.length;
        long bruteForceOps = ((long)n * (n - 1)) / 2; // Número de comparações em força bruta
        
        System.out.printf("Força Bruta (O(n²)): %d operações estimadas\n", bruteForceOps);
        System.out.printf("Two Pointer (O(n)): %d operações reais\n", tp.getOperationsCount());
        System.out.printf("Melhoria: %.1fx mais eficiente\n", (double)bruteForceOps / tp.getOperationsCount());
        
        // Estatísticas finais
        System.out.println("\n" + "=".repeat(80));
        System.out.println("RESUMO DA TÉCNICA DE TWO POINTER");
        System.out.println("=".repeat(80));
        System.out.println("✓ Reduz complexidade de O(n²) para O(n)");
        System.out.println("✓ Uso eficiente de memória O(1)");
        System.out.println("✓ Ideal para arrays/strings ordenadas");
        System.out.println("✓ Padrões: opostos, sequenciais, rápido/lento");
        System.out.println("✓ Aplicações: busca, verificação, otimização");
        
        System.out.println("\nAlgoritmos implementados:");
        System.out.println("• Two Sum em array ordenado");
        System.out.println("• Verificação de palíndromo");
        System.out.println("• Remoção de duplicatas");
        System.out.println("• Container com mais água");
        System.out.println("• Three Sum");
        System.out.println("• Dutch National Flag (Sort Colors)");
    }
    
    public static void main(String[] args) {
        demonstrarTwoPointer();
    }
}
