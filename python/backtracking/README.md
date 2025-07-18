<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=8E44AD&height=120&section=header&text=Backtracking&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Algoritmos%20de%20Retrocesso%20e%20Busca%20Exaustiva&descAlignY=65&descSize=16">

</div>

# Backtracking - Algoritmos de Retrocesso

## Descrição

Backtracking é uma técnica algorítmica sistemática para encontrar todas (ou algumas) soluções para problemas computacionais. Constrói candidatos para as soluções incrementalmente e abandona cada candidato parcial ("backtracks") assim que determina que não pode ser completado para uma solução válida.

## Como Funciona

O backtracking utiliza um padrão recursivo que segue três etapas principais:

1. **Escolha**: Fazer uma escolha entre as opções disponíveis
2. **Exploração**: Explorar recursivamente as consequências da escolha
3. **Desfazer**: Se a exploração não leva a uma solução, desfazer a escolha (backtrack)

### Padrão Básico
```python
def backtrack(candidate):
    if is_solution(candidate):
        process_solution(candidate)
        return
    
    for next_choice in get_choices(candidate):
        if is_valid(next_choice):
            make_choice(next_choice)
            backtrack(candidate)
            unmake_choice(next_choice)  # BACKTRACK
```

### Estrutura de Decisão
```python
def solve_problem():
    def backtrack(state):
        # Caso base: solução encontrada
        if is_complete(state):
            solutions.append(state.copy())
            return
        
        # Explorar todas as possibilidades
        for choice in get_possible_choices(state):
            if is_valid_choice(choice, state):
                # Fazer escolha
                state.add(choice)
                
                # Recursão
                backtrack(state)
                
                # Desfazer escolha (backtrack)
                state.remove(choice)
```

## Complexidade

| Operação | Complexidade | Observações |
|----------|--------------|-------------|
| **Tempo** | O(b^d) | b = fator de ramificação, d = profundidade |
| **Espaço** | O(d) | Profundidade da recursão |
| **Melhor caso** | O(1) | Solução encontrada imediatamente |
| **Pior caso** | O(k^n) | Exploração completa do espaço |

## Algoritmos Implementados

### 1. N-Queens Problem
```python
def n_queens(n):
    board = ['.' * n for _ in range(n)]
    
    def is_safe(row, col):
        # Verificar coluna e diagonais
        for i in range(row):
            if (board[i][col] == 'Q' or 
                (col-(row-i) >= 0 and board[i][col-(row-i)] == 'Q') or
                (col+(row-i) < n and board[i][col+(row-i)] == 'Q')):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                backtrack(row + 1)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
```

**Aplicação**: Colocar N rainhas em tabuleiro NxN sem ataques
**Complexidade**: O(N!) tempo, O(N) espaço

### 2. Sudoku Solver
```python
def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # Verificar linha, coluna e quadrante 3x3
        for x in range(9):
            if (board[row][x] == num or 
                board[x][col] == num or
                board[3*(row//3) + x//3][3*(col//3) + x%3] == num):
                return False
        return True
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False
        return True
```

**Aplicação**: Resolver puzzles de Sudoku 9x9
**Complexidade**: O(9^(n²)) tempo, O(1) espaço extra

### 3. Generate Permutations
```python
def generate_permutations(nums):
    result = []
    
    def backtrack(current_permutation):
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])
            return
        
        for num in nums:
            if num not in current_permutation:
                current_permutation.append(num)
                backtrack(current_permutation)
                current_permutation.pop()  # Backtrack
```

**Aplicação**: Gerar todas as permutações de uma lista
**Complexidade**: O(N! × N) tempo, O(N) espaço

### 4. Generate Combinations
```python
def generate_combinations(n, k):
    result = []
    
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            result.append(current_combination[:])
            return
        
        for i in range(start, n + 1):
            current_combination.append(i)
            backtrack(i + 1, current_combination)
            current_combination.pop()  # Backtrack
```

**Aplicação**: Gerar combinações de k elementos de 1 a n
**Complexidade**: O(C(n,k) × k) tempo, O(k) espaço

### 5. Word Search
```python
def word_search(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        if index == len(word):
            return True  # Palavra encontrada
        
        if (row < 0 or row >= rows or col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False
        
        # Marcar como visitado
        temp = board[row][col]
        board[row][col] = '#'
        
        # Explorar 4 direções
        found = any(backtrack(row + dr, col + dc, index + 1)
                   for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)])
        
        # Backtrack
        board[row][col] = temp
        return found
```

**Aplicação**: Buscar palavras em grade de letras
**Complexidade**: O(M×N×4^L) tempo, O(L) espaço

### 6. Subset Sum
```python
def subset_sum(nums, target):
    result = []
    nums.sort()  # Para otimização
    
    def backtrack(start, current_subset, current_sum):
        if current_sum == target:
            result.append(current_subset[:])
            return
        
        if current_sum > target:
            return  # Poda
        
        for i in range(start, len(nums)):
            # Pular duplicatas
            if i > start and nums[i] == nums[i-1]:
                continue
            
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset, current_sum + nums[i])
            current_subset.pop()  # Backtrack
```

**Aplicação**: Encontrar subconjuntos que somam valor alvo
**Complexidade**: O(2^N × N) tempo, O(N) espaço

## Técnicas de Otimização

### 1. Poda (Pruning)
```python
def backtrack_with_pruning(state):
    if not is_promising(state):
        return  # Poda: não explorar este ramo
    
    if is_solution(state):
        process_solution(state)
        return
    
    for choice in get_choices(state):
        make_choice(choice)
        backtrack_with_pruning(state)
        unmake_choice(choice)
```

### 2. Ordenação Estratégica
```python
# Ordenar candidatos por heurística
def get_sorted_choices(state):
    choices = get_all_choices(state)
    return sorted(choices, key=lambda x: heuristic_value(x))
```

### 3. Memoização
```python
memo = {}

def backtrack_with_memo(state):
    state_key = get_state_key(state)
    if state_key in memo:
        return memo[state_key]
    
    # ... lógica de backtracking ...
    
    memo[state_key] = result
    return result
```

## Vantagens e Limitações

### ✅ Vantagens
- **Completude**: Encontra todas as soluções se existirem
- **Sistematização**: Explora o espaço de busca de forma organizada
- **Flexibilidade**: Aplicável a muitos tipos de problemas
- **Poda**: Elimina ramos inválidos cedo

### ❌ Limitações
- **Complexidade**: Crescimento exponencial no pior caso
- **Memória**: Pode usar muita memória com recursão profunda
- **Tempo**: Pode ser muito lento para problemas grandes
- **Implementação**: Pode ser complexo para alguns problemas

## Casos de Uso

### 1. Problemas de Decisão
- **N-Queens**: Colocação de rainhas
- **Sudoku**: Preenchimento de grade
- **Graph Coloring**: Coloração de grafos
- **Knight's Tour**: Movimentos do cavalo no xadrez

### 2. Problemas de Otimização
- **Knapsack**: Seleção de itens
- **Traveling Salesman**: Menor caminho
- **Subset Sum**: Soma de subconjuntos
- **Partition Problem**: Divisão de conjuntos

### 3. Problemas de Enumeração
- **Permutações**: Arranjos de elementos
- **Combinações**: Seleções de elementos
- **Subconjuntos**: Todos os subconjuntos possíveis
- **Palavras**: Geração de sequências válidas

### 4. Problemas de Busca
- **Maze Solving**: Encontrar caminho em labirinto
- **Word Search**: Busca de palavras em grade
- **Pattern Matching**: Correspondência de padrões
- **Parsing**: Análise sintática

## Padrões de Implementação

### 1. Template Básico
```python
def solve_problem():
    solutions = []
    
    def backtrack(state):
        if is_complete(state):
            solutions.append(get_solution(state))
            return
        
        for choice in get_choices(state):
            if is_valid(choice, state):
                make_choice(choice, state)
                backtrack(state)
                unmake_choice(choice, state)
    
    initial_state = create_initial_state()
    backtrack(initial_state)
    return solutions
```

### 2. Com Otimização de Poda
```python
def solve_with_pruning():
    best_solution = None
    best_value = float('inf')
    
    def backtrack(state, current_value):
        nonlocal best_solution, best_value
        
        # Poda por limitante
        if current_value >= best_value:
            return
        
        if is_complete(state):
            if current_value < best_value:
                best_value = current_value
                best_solution = state.copy()
            return
        
        for choice in get_choices(state):
            if is_promising(choice, state, best_value):
                make_choice(choice, state)
                backtrack(state, current_value + get_cost(choice))
                unmake_choice(choice, state)
```

### 3. Iterativo com Stack
```python
def backtrack_iterative():
    stack = [initial_state]
    solutions = []
    
    while stack:
        state = stack.pop()
        
        if is_complete(state):
            solutions.append(get_solution(state))
            continue
        
        for choice in get_choices(state):
            if is_valid(choice, state):
                new_state = make_choice(choice, state.copy())
                stack.append(new_state)
    
    return solutions
```

## Executar Exemplo

```bash
cd python/backtracking
python backtracking_basico.py
```

## Exercícios Sugeridos

### Iniciante
1. Implementar busca em labirinto
2. Gerar todas as subsequências de uma string
3. Resolver problema das 8-Rainhas

### Intermediário
4. Implementar Knapsack com backtracking
5. Resolver Word Break Problem
6. Implementar Graph Coloring

### Avançado
7. Traveling Salesman Problem
8. Maximum Clique Problem
9. Hamiltonian Path Problem

## Aplicações no Mundo Real

### 1. Jogos e Puzzles
```python
# Solver para Sudoku online
def sudoku_ai_solver(puzzle):
    board = parse_puzzle(puzzle)
    if solve_sudoku(board):
        return format_solution(board)
    return "No solution found"
```

### 2. Otimização de Recursos
```python
# Alocação de tarefas
def task_allocation(tasks, workers, constraints):
    def backtrack(assignment):
        if len(assignment) == len(tasks):
            if is_valid_assignment(assignment, constraints):
                return assignment
            return None
        
        task_idx = len(assignment)
        for worker in workers:
            if can_assign(tasks[task_idx], worker, assignment):
                assignment.append(worker)
                result = backtrack(assignment)
                if result:
                    return result
                assignment.pop()
        
        return None
```

### 3. Análise Combinatória
```python
# Geração de casos de teste
def generate_test_cases(parameters, constraints):
    test_cases = []
    
    def backtrack(current_case):
        if len(current_case) == len(parameters):
            if satisfies_constraints(current_case, constraints):
                test_cases.append(current_case.copy())
            return
        
        param = parameters[len(current_case)]
        for value in param.possible_values:
            current_case.append(value)
            backtrack(current_case)
            current_case.pop()
```

## Comparação com Outras Técnicas

| Técnica | Tempo | Espaço | Quando Usar |
|---------|-------|--------|-------------|
| **Backtracking** | O(b^d) | O(d) | Busca exaustiva, problemas NP |
| **Dynamic Programming** | O(n²) | O(n²) | Subproblemas sobrepostos |
| **Greedy** | O(n log n) | O(1) | Escolha ótima local |
| **Branch and Bound** | O(b^d) | O(d) | Otimização com limitantes |

## Heurísticas de Melhoria

### 1. Most Constraining Variable
- Escolher variável com menos opções disponíveis
- Reduz fator de ramificação

### 2. Least Constraining Value
- Escolher valor que menos restringe outras variáveis
- Mantém mais opções futuras

### 3. Forward Checking
- Verificar consistência após cada atribuição
- Detectar falhas mais cedo

### 4. Arc Consistency
- Manter consistência entre pares de variáveis
- Reduzir domínios das variáveis

## Referências

- [Backtracking - GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Algorithm Design Manual - Skiena](http://www.algorist.com/)
- [Introduction to Algorithms - CLRS](https://mitpress.mit.edu/books/introduction-algorithms)
- [Artificial Intelligence: A Modern Approach - Russell & Norvig](http://aima.cs.berkeley.edu/)

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
  <i>🔄 "Na busca pela solução, cada passo atrás é um passo à frente na sabedoria"</i>
  <br>
  <i>🔄 "In the search for solution, every step back is a step forward in wisdom"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=8E44AD&height=120&section=footer"/>

</div>
