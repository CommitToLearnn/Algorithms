import java.util.*;

/**
 * Implementação de algoritmos usando a técnica de Backtracking (Retrocesso)
 * 
 * Esta classe implementa várias técnicas de backtracking:
 * 1. N-Queens Problem (Problema das N-Rainhas)
 * 2. Sudoku Solver (Resolvedor de Sudoku)
 * 3. Generate Permutations (Gerar Permutações)
 * 4. Generate Combinations (Gerar Combinações)
 * 5. Word Search (Busca de Palavras)
 * 6. Subset Sum (Soma de Subconjuntos)
 * 
 * Autor: matheussricardoo
 */
public class BacktrackingBasico {
    
    private int recursionCount;
    private int backtrackCount;
    
    public BacktrackingBasico() {
        resetCounters();
    }
    
    /**
     * Reset dos contadores de performance
     */
    public void resetCounters() {
        this.recursionCount = 0;
        this.backtrackCount = 0;
    }
    
    /**
     * Resolve o problema das N-Rainhas
     * 
     * @param n Tamanho do tabuleiro (NxN)
     * @return Lista de soluções, cada uma representando uma configuração válida
     * 
     * Complexidade: O(N!) tempo, O(N) espaço
     */
    public List<List<String>> nQueens(int n) {
        resetCounters();
        List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];
        
        // Inicializar tabuleiro
        for (int i = 0; i < n; i++) {
            Arrays.fill(board[i], '.');
        }
        
        backtrackNQueens(board, 0, result);
        return result;
    }
    
    private void backtrackNQueens(char[][] board, int row, List<List<String>> result) {
        recursionCount++;
        
        if (row == board.length) {
            // Solução encontrada
            List<String> solution = new ArrayList<>();
            for (char[] r : board) {
                solution.add(new String(r));
            }
            result.add(solution);
            return;
        }
        
        for (int col = 0; col < board.length; col++) {
            if (isSafeNQueens(board, row, col)) {
                // Colocar rainha
                board[row][col] = 'Q';
                
                // Recursão
                backtrackNQueens(board, row + 1, result);
                
                // Backtrack (remover rainha)
                board[row][col] = '.';
                backtrackCount++;
            }
        }
    }
    
    private boolean isSafeNQueens(char[][] board, int row, int col) {
        int n = board.length;
        
        // Verificar coluna
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }
        
        // Verificar diagonal principal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        // Verificar diagonal secundária
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        return true;
    }
    
    /**
     * Resolve um puzzle de Sudoku
     * 
     * @param board Matriz 9x9 representando o tabuleiro ('.' para célula vazia)
     * @return true se o Sudoku foi resolvido, false caso contrário
     * 
     * Complexidade: O(9^(n*n)) tempo, O(1) espaço extra
     */
    public boolean solveSudoku(char[][] board) {
        resetCounters();
        return backtrackSudoku(board);
    }
    
    private boolean backtrackSudoku(char[][] board) {
        recursionCount++;
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char num = '1'; num <= '9'; num++) {
                        if (isValidSudoku(board, i, j, num)) {
                            board[i][j] = num;
                            
                            if (backtrackSudoku(board)) {
                                return true;
                            }
                            
                            // Backtrack
                            board[i][j] = '.';
                            backtrackCount++;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    private boolean isValidSudoku(char[][] board, int row, int col, char num) {
        // Verificar linha
        for (int x = 0; x < 9; x++) {
            if (board[row][x] == num) {
                return false;
            }
        }
        
        // Verificar coluna
        for (int x = 0; x < 9; x++) {
            if (board[x][col] == num) {
                return false;
            }
        }
        
        // Verificar quadrante 3x3
        int startRow = 3 * (row / 3);
        int startCol = 3 * (col / 3);
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i + startRow][j + startCol] == num) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    /**
     * Gera todas as permutações de uma lista de números
     * 
     * @param nums Lista de números
     * @return Lista de todas as permutações possíveis
     * 
     * Complexidade: O(N! * N) tempo, O(N) espaço
     */
    public List<List<Integer>> generatePermutations(int[] nums) {
        resetCounters();
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentPermutation = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        
        backtrackPermutations(nums, currentPermutation, used, result);
        return result;
    }
    
    private void backtrackPermutations(int[] nums, List<Integer> currentPermutation, 
                                     boolean[] used, List<List<Integer>> result) {
        recursionCount++;
        
        if (currentPermutation.size() == nums.length) {
            result.add(new ArrayList<>(currentPermutation));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                currentPermutation.add(nums[i]);
                used[i] = true;
                
                backtrackPermutations(nums, currentPermutation, used, result);
                
                currentPermutation.remove(currentPermutation.size() - 1);
                used[i] = false;
                backtrackCount++;
            }
        }
    }
    
    /**
     * Gera todas as combinações de k elementos de 1 a n
     * 
     * @param n Número máximo
     * @param k Tamanho das combinações
     * @return Lista de todas as combinações possíveis
     * 
     * Complexidade: O(C(n,k) * k) tempo, O(k) espaço
     */
    public List<List<Integer>> generateCombinations(int n, int k) {
        resetCounters();
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentCombination = new ArrayList<>();
        
        backtrackCombinations(1, n, k, currentCombination, result);
        return result;
    }
    
    private void backtrackCombinations(int start, int n, int k, 
                                     List<Integer> currentCombination, 
                                     List<List<Integer>> result) {
        recursionCount++;
        
        if (currentCombination.size() == k) {
            result.add(new ArrayList<>(currentCombination));
            return;
        }
        
        for (int i = start; i <= n; i++) {
            currentCombination.add(i);
            backtrackCombinations(i + 1, n, k, currentCombination, result);
            currentCombination.remove(currentCombination.size() - 1);
            backtrackCount++;
        }
    }
    
    /**
     * Busca uma palavra em uma matriz de caracteres
     * 
     * @param board Matriz de caracteres
     * @param word Palavra a ser procurada
     * @return true se a palavra foi encontrada, false caso contrário
     * 
     * Complexidade: O(M*N*4^L) tempo, O(L) espaço
     */
    public boolean wordSearch(char[][] board, String word) {
        resetCounters();
        
        if (board.length == 0 || board[0].length == 0 || word.length() == 0) {
            return false;
        }
        
        int rows = board.length;
        int cols = board[0].length;
        
        // Tentar começar de cada posição
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (backtrackWordSearch(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    private boolean backtrackWordSearch(char[][] board, String word, int row, int col, int index) {
        recursionCount++;
        
        if (index == word.length()) {
            return true; // Palavra encontrada
        }
        
        if (row < 0 || row >= board.length || col < 0 || col >= board[0].length ||
            board[row][col] != word.charAt(index)) {
            return false;
        }
        
        // Marcar célula como visitada
        char temp = board[row][col];
        board[row][col] = '#';
        
        // Explorar 4 direções
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        boolean found = false;
        
        for (int[] dir : directions) {
            if (backtrackWordSearch(board, word, row + dir[0], col + dir[1], index + 1)) {
                found = true;
                break;
            }
        }
        
        // Backtrack (restaurar célula)
        board[row][col] = temp;
        if (!found) {
            backtrackCount++;
        }
        
        return found;
    }
    
    /**
     * Encontra todos os subconjuntos que somam um valor alvo
     * 
     * @param nums Lista de números
     * @param target Valor alvo da soma
     * @return Lista de subconjuntos que somam o valor alvo
     * 
     * Complexidade: O(2^N * N) tempo, O(N) espaço
     */
    public List<List<Integer>> subsetSum(int[] nums, int target) {
        resetCounters();
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentSubset = new ArrayList<>();
        
        backtrackSubsetSum(nums, 0, currentSubset, 0, target, result);
        return result;
    }
    
    private void backtrackSubsetSum(int[] nums, int start, List<Integer> currentSubset, 
                                  int currentSum, int target, List<List<Integer>> result) {
        recursionCount++;
        
        if (currentSum == target) {
            result.add(new ArrayList<>(currentSubset));
            return;
        }
        
        if (currentSum > target) {
            return; // Poda: soma já excedeu o alvo
        }
        
        for (int i = start; i < nums.length; i++) {
            currentSubset.add(nums[i]);
            backtrackSubsetSum(nums, i + 1, currentSubset, currentSum + nums[i], target, result);
            currentSubset.remove(currentSubset.size() - 1);
            backtrackCount++;
        }
    }
    
    /**
     * Getters para contadores de performance
     */
    public int getRecursionCount() {
        return recursionCount;
    }
    
    public int getBacktrackCount() {
        return backtrackCount;
    }
    
    /**
     * Método para demonstrar o uso dos algoritmos
     */
    public static void demonstrarBacktracking() {
        BacktrackingBasico bt = new BacktrackingBasico();
        
        System.out.println("=".repeat(80));
        System.out.println("DEMONSTRAÇÃO: Algoritmos de Backtracking");
        System.out.println("=".repeat(80));
        
        // 1. N-Queens Problem
        System.out.println("\n1. N-QUEENS PROBLEM (N=4)");
        System.out.println("-".repeat(40));
        long start = System.nanoTime();
        List<List<String>> solutions = bt.nQueens(4);
        long duration = System.nanoTime() - start;
        
        System.out.printf("Número de soluções encontradas: %d\n", solutions.size());
        System.out.println("Primeira solução:");
        for (String row : solutions.get(0)) {
            System.out.printf("  %s\n", row);
        }
        System.out.printf("Recursões: %d\n", bt.getRecursionCount());
        System.out.printf("Backtracks: %d\n", bt.getBacktrackCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 2. Sudoku Solver
        System.out.println("\n2. SUDOKU SOLVER");
        System.out.println("-".repeat(40));
        char[][] sudokuBoard = {
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        
        System.out.println("Tabuleiro original:");
        for (char[] row : sudokuBoard) {
            System.out.printf("  %s\n", Arrays.toString(row));
        }
        
        start = System.nanoTime();
        boolean solved = bt.solveSudoku(sudokuBoard);
        duration = System.nanoTime() - start;
        
        if (solved) {
            System.out.println("\nSolução encontrada:");
            for (char[] row : sudokuBoard) {
                System.out.printf("  %s\n", Arrays.toString(row));
            }
        } else {
            System.out.println("\nNenhuma solução encontrada!");
        }
        
        System.out.printf("Recursões: %d\n", bt.getRecursionCount());
        System.out.printf("Backtracks: %d\n", bt.getBacktrackCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 3. Generate Permutations
        System.out.println("\n3. GENERATE PERMUTATIONS ([1,2,3])");
        System.out.println("-".repeat(40));
        start = System.nanoTime();
        List<List<Integer>> perms = bt.generatePermutations(new int[]{1, 2, 3});
        duration = System.nanoTime() - start;
        
        System.out.printf("Permutações: %s\n", perms);
        System.out.printf("Total de permutações: %d\n", perms.size());
        System.out.printf("Recursões: %d\n", bt.getRecursionCount());
        System.out.printf("Backtracks: %d\n", bt.getBacktrackCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 4. Generate Combinations
        System.out.println("\n4. GENERATE COMBINATIONS (n=4, k=2)");
        System.out.println("-".repeat(40));
        start = System.nanoTime();
        List<List<Integer>> combs = bt.generateCombinations(4, 2);
        duration = System.nanoTime() - start;
        
        System.out.printf("Combinações: %s\n", combs);
        System.out.printf("Total de combinações: %d\n", combs.size());
        System.out.printf("Recursões: %d\n", bt.getRecursionCount());
        System.out.printf("Backtracks: %d\n", bt.getBacktrackCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 5. Word Search
        System.out.println("\n5. WORD SEARCH");
        System.out.println("-".repeat(40));
        char[][] wordBoard = {
            {'A', 'B', 'C', 'E'},
            {'S', 'F', 'C', 'S'},
            {'A', 'D', 'E', 'E'}
        };
        String word = "ABCCED";
        
        System.out.println("Tabuleiro:");
        for (char[] row : wordBoard) {
            System.out.printf("  %s\n", Arrays.toString(row));
        }
        System.out.printf("Palavra procurada: '%s'\n", word);
        
        start = System.nanoTime();
        boolean found = bt.wordSearch(wordBoard, word);
        duration = System.nanoTime() - start;
        
        System.out.printf("Palavra encontrada: %b\n", found);
        System.out.printf("Recursões: %d\n", bt.getRecursionCount());
        System.out.printf("Backtracks: %d\n", bt.getBacktrackCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // 6. Subset Sum
        System.out.println("\n6. SUBSET SUM ([1,2,3,4,5], target=5)");
        System.out.println("-".repeat(40));
        int[] nums = {1, 2, 3, 4, 5};
        int target = 5;
        
        start = System.nanoTime();
        List<List<Integer>> subsets = bt.subsetSum(nums, target);
        duration = System.nanoTime() - start;
        
        System.out.printf("Números: %s\n", Arrays.toString(nums));
        System.out.printf("Alvo: %d\n", target);
        System.out.printf("Subconjuntos que somam %d: %s\n", target, subsets);
        System.out.printf("Total de subconjuntos: %d\n", subsets.size());
        System.out.printf("Recursões: %d\n", bt.getRecursionCount());
        System.out.printf("Backtracks: %d\n", bt.getBacktrackCount());
        System.out.printf("Tempo: %.2fms\n", duration / 1e6);
        
        // Estatísticas finais
        System.out.println("\n" + "=".repeat(80));
        System.out.println("RESUMO DA TÉCNICA DE BACKTRACKING");
        System.out.println("=".repeat(80));
        System.out.println("✓ Explora sistematicamente todas as possibilidades");
        System.out.println("✓ Remove candidatos inválidos (poda)");
        System.out.println("✓ Retrocede quando atinge beco sem saída");
        System.out.println("✓ Útil para problemas de decisão e otimização");
        System.out.println("✓ Complexidade exponencial, mas eficiente com poda");
        
        System.out.println("\nProblemas clássicos de backtracking:");
        System.out.println("• N-Queens Problem");
        System.out.println("• Sudoku Solver");
        System.out.println("• Permutações e Combinações");
        System.out.println("• Word Search");
        System.out.println("• Subset Sum");
        System.out.println("• Graph Coloring");
        System.out.println("• Knapsack Problem");
        System.out.println("• Maze Solving");
    }
    
    public static void main(String[] args) {
        demonstrarBacktracking();
    }
}
