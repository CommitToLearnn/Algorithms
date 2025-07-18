"""
Backtracking - Algoritmos Básicos
Implementação de algoritmos fundamentais usando a técnica de backtracking.

Este módulo implementa várias técnicas de backtracking:
1. N-Queens Problem (Problema das N-Rainhas)
2. Sudoku Solver (Resolvedor de Sudoku)
3. Generate Permutations (Gerar Permutações)
4. Generate Combinations (Gerar Combinações)
5. Word Search (Busca de Palavras)
6. Subset Sum (Soma de Subconjuntos)

Autor: matheussricardoo
"""

import time
from typing import List


class BacktrackingAlgorithms:
    """Classe que implementa algoritmos fundamentais de backtracking."""
    
    def __init__(self):
        """Inicializa a classe com contadores de performance."""
        self.recursion_count = 0
        self.backtrack_count = 0
    
    def reset_counters(self):
        """Reset dos contadores de performance."""
        self.recursion_count = 0
        self.backtrack_count = 0
    
    def n_queens(self, n: int) -> List[List[str]]:
        """
        Resolve o problema das N-Rainhas.
        
        O problema consiste em colocar N rainhas em um tabuleiro NxN
        de forma que nenhuma rainha ataque outra.
        
        Args:
            n: Tamanho do tabuleiro (NxN)
            
        Returns:
            Lista de soluções, cada uma representando uma configuração válida
            
        Complexidade:
            Tempo: O(N!) no pior caso
            Espaço: O(N) para recursão
        """
        self.reset_counters()
        result = []
        board = ['.' * n for _ in range(n)]
        
        def is_safe(row: int, col: int) -> bool:
            """Verifica se é seguro colocar rainha na posição (row, col)."""
            # Verifica coluna
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Verifica diagonal principal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Verifica diagonal secundária
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        def backtrack(row: int):
            """Função recursiva de backtracking."""
            self.recursion_count += 1
            
            if row == n:
                # Solução encontrada
                result.append(board[:])
                return
            
            for col in range(n):
                if is_safe(row, col):
                    # Colocar rainha
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    
                    # Recursão
                    backtrack(row + 1)
                    
                    # Backtrack (remover rainha)
                    board[row] = board[row][:col] + '.' + board[row][col+1:]
                    self.backtrack_count += 1
        
        backtrack(0)
        return result
    
    def solve_sudoku(self, board: List[List[str]]) -> bool:
        """
        Resolve um puzzle de Sudoku usando backtracking.
        
        Args:
            board: Matriz 9x9 representando o tabuleiro ('.' para célula vazia)
            
        Returns:
            True se o Sudoku foi resolvido, False caso contrário
            
        Complexidade:
            Tempo: O(9^(n*n)) onde n é o número de células vazias
            Espaço: O(1) exceto stack de recursão
        """
        self.reset_counters()
        
        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
            """Verifica se é válido colocar o número na posição."""
            # Verificar linha
            for x in range(9):
                if board[row][x] == num:
                    return False
            
            # Verificar coluna
            for x in range(9):
                if board[x][col] == num:
                    return False
            
            # Verificar quadrante 3x3
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[i + start_row][j + start_col] == num:
                        return False
            
            return True
        
        def solve() -> bool:
            """Função recursiva de backtracking para resolver Sudoku."""
            self.recursion_count += 1
            
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                
                                if solve():
                                    return True
                                
                                # Backtrack
                                board[i][j] = '.'
                                self.backtrack_count += 1
                        
                        return False
            return True
        
        return solve()
    
    def generate_permutations(self, nums: List[int]) -> List[List[int]]:
        """
        Gera todas as permutações de uma lista de números.
        
        Args:
            nums: Lista de números
            
        Returns:
            Lista de todas as permutações possíveis
            
        Complexidade:
            Tempo: O(N! * N) onde N é o tamanho da lista
            Espaço: O(N) para recursão
        """
        self.reset_counters()
        result = []
        
        def backtrack(current_permutation: List[int]):
            """Função recursiva para gerar permutações."""
            self.recursion_count += 1
            
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])
                return
            
            for num in nums:
                if num not in current_permutation:
                    current_permutation.append(num)
                    backtrack(current_permutation)
                    current_permutation.pop()  # Backtrack
                    self.backtrack_count += 1
        
        backtrack([])
        return result
    
    def generate_combinations(self, n: int, k: int) -> List[List[int]]:
        """
        Gera todas as combinações de k elementos de 1 a n.
        
        Args:
            n: Número máximo
            k: Tamanho das combinações
            
        Returns:
            Lista de todas as combinações possíveis
            
        Complexidade:
            Tempo: O(C(n,k) * k) onde C(n,k) é o coeficiente binomial
            Espaço: O(k) para recursão
        """
        self.reset_counters()
        result = []
        
        def backtrack(start: int, current_combination: List[int]):
            """Função recursiva para gerar combinações."""
            self.recursion_count += 1
            
            if len(current_combination) == k:
                result.append(current_combination[:])
                return
            
            for i in range(start, n + 1):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()  # Backtrack
                self.backtrack_count += 1
        
        backtrack(1, [])
        return result
    
    def word_search(self, board: List[List[str]], word: str) -> bool:
        """
        Busca uma palavra em uma matriz de caracteres.
        
        A palavra pode ser formada por letras adjacentes (horizontal/vertical).
        Cada célula pode ser usada apenas uma vez.
        
        Args:
            board: Matriz de caracteres
            word: Palavra a ser procurada
            
        Returns:
            True se a palavra foi encontrada, False caso contrário
            
        Complexidade:
            Tempo: O(M*N*4^L) onde M,N são dimensões e L é o tamanho da palavra
            Espaço: O(L) para recursão
        """
        self.reset_counters()
        
        if not board or not board[0] or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def backtrack(row: int, col: int, index: int) -> bool:
            """Função recursiva para buscar palavra."""
            self.recursion_count += 1
            
            if index == len(word):
                return True  # Palavra encontrada
            
            if (row < 0 or row >= rows or col < 0 or col >= cols or
                board[row][col] != word[index]):
                return False
            
            # Marcar célula como visitada
            temp = board[row][col]
            board[row][col] = '#'
            
            # Explorar 4 direções
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            found = False
            
            for dr, dc in directions:
                if backtrack(row + dr, col + dc, index + 1):
                    found = True
                    break
            
            # Backtrack (restaurar célula)
            board[row][col] = temp
            if not found:
                self.backtrack_count += 1
            
            return found
        
        # Tentar começar de cada posição
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        
        return False
    
    def subset_sum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Encontra todos os subconjuntos que somam um valor alvo.
        
        Args:
            nums: Lista de números
            target: Valor alvo da soma
            
        Returns:
            Lista de subconjuntos que somam o valor alvo
            
        Complexidade:
            Tempo: O(2^N * N) onde N é o tamanho da lista
            Espaço: O(N) para recursão
        """
        self.reset_counters()
        result = []
        nums.sort()  # Ordenar para otimização
        
        def backtrack(start: int, current_subset: List[int], current_sum: int):
            """Função recursiva para encontrar subconjuntos."""
            self.recursion_count += 1
            
            if current_sum == target:
                result.append(current_subset[:])
                return
            
            if current_sum > target:
                return  # Poda: soma já excedeu o alvo
            
            for i in range(start, len(nums)):
                # Pular duplicatas
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset, current_sum + nums[i])
                current_subset.pop()  # Backtrack
                self.backtrack_count += 1
        
        backtrack(0, [], 0)
        return result


def demonstrar_backtracking():
    """Demonstra o uso dos algoritmos de backtracking."""
    bt = BacktrackingAlgorithms()
    
    print("=" * 80)
    print("DEMONSTRAÇÃO: Algoritmos de Backtracking")
    print("=" * 80)
    
    # 1. N-Queens Problem
    print("\n1. N-QUEENS PROBLEM (N=4)")
    print("-" * 40)
    start_time = time.time()
    solutions = bt.n_queens(4)
    end_time = time.time()
    
    print(f"Número de soluções encontradas: {len(solutions)}")
    print("Primeira solução:")
    for row in solutions[0]:
        print(f"  {row}")
    print(f"Recursões: {bt.recursion_count}")
    print(f"Backtracks: {bt.backtrack_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 2. Sudoku Solver
    print("\n2. SUDOKU SOLVER")
    print("-" * 40)
    sudoku_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    print("Tabuleiro original:")
    for row in sudoku_board:
        print("  " + " ".join(row))
    
    start_time = time.time()
    solved = bt.solve_sudoku(sudoku_board)
    end_time = time.time()
    
    if solved:
        print("\nSolução encontrada:")
        for row in sudoku_board:
            print("  " + " ".join(row))
    else:
        print("\nNenhuma solução encontrada!")
    
    print(f"Recursões: {bt.recursion_count}")
    print(f"Backtracks: {bt.backtrack_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 3. Generate Permutations
    print("\n3. GENERATE PERMUTATIONS ([1,2,3])")
    print("-" * 40)
    start_time = time.time()
    perms = bt.generate_permutations([1, 2, 3])
    end_time = time.time()
    
    print(f"Permutações: {perms}")
    print(f"Total de permutações: {len(perms)}")
    print(f"Recursões: {bt.recursion_count}")
    print(f"Backtracks: {bt.backtrack_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 4. Generate Combinations
    print("\n4. GENERATE COMBINATIONS (n=4, k=2)")
    print("-" * 40)
    start_time = time.time()
    combs = bt.generate_combinations(4, 2)
    end_time = time.time()
    
    print(f"Combinações: {combs}")
    print(f"Total de combinações: {len(combs)}")
    print(f"Recursões: {bt.recursion_count}")
    print(f"Backtracks: {bt.backtrack_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 5. Word Search
    print("\n5. WORD SEARCH")
    print("-" * 40)
    word_board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"
    
    print("Tabuleiro:")
    for row in word_board:
        print(f"  {row}")
    print(f"Palavra procurada: '{word}'")
    
    start_time = time.time()
    found = bt.word_search(word_board, word)
    end_time = time.time()
    
    print(f"Palavra encontrada: {found}")
    print(f"Recursões: {bt.recursion_count}")
    print(f"Backtracks: {bt.backtrack_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 6. Subset Sum
    print("\n6. SUBSET SUM ([1,2,3,4,5], target=5)")
    print("-" * 40)
    nums = [1, 2, 3, 4, 5]
    target = 5
    
    start_time = time.time()
    subsets = bt.subset_sum(nums, target)
    end_time = time.time()
    
    print(f"Números: {nums}")
    print(f"Alvo: {target}")
    print(f"Subconjuntos que somam {target}: {subsets}")
    print(f"Total de subconjuntos: {len(subsets)}")
    print(f"Recursões: {bt.recursion_count}")
    print(f"Backtracks: {bt.backtrack_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # Estatísticas finais
    print("\n" + "=" * 80)
    print("RESUMO DA TÉCNICA DE BACKTRACKING")
    print("=" * 80)
    print("✓ Explora sistematicamente todas as possibilidades")
    print("✓ Remove candidatos inválidos (poda)")
    print("✓ Retrocede quando atinge beco sem saída")
    print("✓ Útil para problemas de decisão e otimização")
    print("✓ Complexidade exponencial, mas eficiente com poda")
    
    print("\nProblemas clássicos de backtracking:")
    print("• N-Queens Problem")
    print("• Sudoku Solver")
    print("• Permutações e Combinações")
    print("• Word Search")
    print("• Subset Sum")
    print("• Graph Coloring")
    print("• Knapsack Problem")
    print("• Maze Solving")


if __name__ == "__main__":
    demonstrar_backtracking()
