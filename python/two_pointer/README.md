<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E74C3C&height=120&section=header&text=Two%20Pointer&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Técnica%20de%20Dois%20Ponteiros%20para%20Algoritmos%20Eficientes&descAlignY=65&descSize=16">

</div>

# Two Pointer - Técnica de Dois Ponteiros

## Descrição

A técnica de dois ponteiros é uma abordagem algorítmica que utiliza dois ponteiros para percorrer uma estrutura de dados (geralmente arrays ou strings) de forma eficiente. Esta técnica é especialmente útil para problemas que envolvem busca de pares, verificação de propriedades ou manipulação de sequências ordenadas.

## Como Funciona

A técnica utiliza dois ponteiros que se movem através da estrutura de dados:

1. **Ponteiros Opostos**: Começam nas extremidades e se movem em direção ao centro
2. **Ponteiros Sequenciais**: Começam juntos e se movem com velocidades diferentes
3. **Ponteiro Rápido/Lento**: Um se move mais rápido que o outro

### Padrões Principais

#### 1. Ponteiros nas Extremidades
```python
left = 0
right = len(array) - 1
while left < right:
    # Lógica de processamento
    if condition:
        left += 1
    else:
        right -= 1
```

#### 2. Sliding Window com Dois Ponteiros
```python
left = 0
for right in range(len(array)):
    # Expandir janela
    while condition_violated:
        # Contrair janela
        left += 1
```

## Complexidade

| Operação | Complexidade | Observações |
|----------|--------------|-------------|
| **Tempo** | O(n) | Um único passe através dos dados |
| **Espaço** | O(1) | Apenas variáveis auxiliares |
| **Casos especiais** | O(n log n) | Quando requer ordenação prévia |

## Algoritmos Implementados

### 1. Two Sum em Array Ordenado
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

**Aplicação**: Encontrar pares que somam um valor específico
**Complexidade**: O(n) tempo, O(1) espaço

### 2. Verificação de Palíndromo
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

**Aplicação**: Verificar se string é igual quando lida de trás para frente
**Complexidade**: O(n) tempo, O(1) espaço

### 3. Remoção de Duplicatas
```python
def remove_duplicates(nums):
    write_pos = 1
    for read_pos in range(1, len(nums)):
        if nums[read_pos] != nums[read_pos - 1]:
            nums[write_pos] = nums[read_pos]
            write_pos += 1
    return write_pos
```

**Aplicação**: Remover elementos duplicados in-place
**Complexidade**: O(n) tempo, O(1) espaço

### 4. Container com Mais Água
```python
def container_with_most_water(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area
```

**Aplicação**: Problema clássico de otimização
**Complexidade**: O(n) tempo, O(1) espaço

### 5. Three Sum
```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Pular duplicatas...
```

**Aplicação**: Encontrar triplets que somam zero
**Complexidade**: O(n²) tempo, O(1) espaço extra

### 6. Dutch National Flag (Sort Colors)
```python
def sort_colors(nums):
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

**Aplicação**: Ordenar array com 3 valores distintos
**Complexidade**: O(n) tempo, O(1) espaço

## Vantagens e Limitações

### ✅ Vantagens
- **Eficiência**: Complexidade O(n) para muitos problemas
- **Espaço**: Uso mínimo de memória O(1)
- **Simplicidade**: Implementação direta e intuitiva
- **Versatilidade**: Aplicável a muitos tipos de problemas

### ❌ Limitações
- **Ordenação**: Muitos casos requerem dados pré-ordenados
- **Problemas específicos**: Nem todos os problemas se adequam
- **Complexidade**: Pode ser difícil identificar quando usar

## Casos de Uso

### 1. Problemas de Soma
- Two Sum, Three Sum, Four Sum
- Encontrar pares/triplets com propriedades específicas
- Problemas de subsequência

### 2. Manipulação de Strings
- Verificação de palíndromos
- Remoção de caracteres específicos
- Comparação de strings

### 3. Problemas de Array
- Remoção de duplicatas
- Particionamento de arrays
- Merge de arrays ordenados

### 4. Otimização
- Container com mais água
- Máximo/mínimo com restrições
- Problemas de janela deslizante

## Padrões de Aplicação

### Quando Usar Two Pointer:
1. **Array/String ordenada** e você precisa encontrar pares
2. **Verificação de propriedades** que dependem de elementos nas extremidades
3. **Problemas de particionamento** ou divisão de dados
4. **Otimização** onde você precisa maximizar/minimizar algo

### Como Identificar:
- Palavras-chave: "par", "soma", "palíndromo", "ordenado"
- Necessidade de comparar elementos distantes
- Problemas que podem ser resolvidos com força bruta O(n²)

## Variações da Técnica

### 1. Ponteiros Fixos
```python
# Distância fixa entre ponteiros
left = 0
right = k  # k é fixo
while right < len(array):
    # Processar janela [left, right]
    left += 1
    right += 1
```

### 2. Ponteiros com Diferentes Velocidades
```python
# Floyd's Cycle Detection
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        # Ciclo detectado
        break
```

### 3. Múltiplos Ponteiros
```python
# Três ou mais ponteiros
left = 0
mid = 0
right = len(array) - 1
# Lógica específica para cada ponteiro
```

## Comparação com Outras Técnicas

| Técnica | Tempo | Espaço | Quando Usar |
|---------|-------|--------|-------------|
| **Two Pointer** | O(n) | O(1) | Arrays ordenados, busca de pares |
| **Hash Table** | O(n) | O(n) | Busca rápida, dados não ordenados |
| **Binary Search** | O(log n) | O(1) | Busca em array ordenado |
| **Sliding Window** | O(n) | O(1) | Subarray com propriedades |

## Executar Exemplo

```bash
cd python/two_pointer
python two_pointer_basico.py
```

## Exercícios Sugeridos

### Iniciante
1. Verificar se array é palíndromo
2. Encontrar par que soma um valor
3. Remover elemento específico

### Intermediário
4. Four Sum (quatro números que somam target)
5. Trapping Rain Water
6. Sort Colors com mais cores

### Avançado
7. Minimum Window Substring
8. Longest Palindromic Substring
9. Container With Most Water (variações)

## Aplicações no Mundo Real

### 1. Sistemas de Busca
```python
# Busca de produtos em faixa de preço
def products_in_price_range(products, min_price, max_price):
    # products está ordenado por preço
    left = find_first_gte(products, min_price)
    right = find_last_lte(products, max_price)
    return products[left:right+1]
```

### 2. Análise de Dados
```python
# Encontrar período com soma específica
def find_period_sum(daily_sales, target_sum):
    left = 0
    current_sum = 0
    for right in range(len(daily_sales)):
        current_sum += daily_sales[right]
        while current_sum > target_sum:
            current_sum -= daily_sales[left]
            left += 1
        if current_sum == target_sum:
            return (left, right)
```

### 3. Processamento de Texto
```python
# Verificar anagramas
def is_anagram_sorted(s1, s2):
    return sorted(s1) == sorted(s2)

# Versão two-pointer para strings já ordenadas
def is_anagram_two_pointer(s1, s2):
    if len(s1) != len(s2):
        return False
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            return False
    return True
```

## Referências

- [Two Pointers Technique - GeeksforGeeks](https://www.geeksforgeeks.org/two-pointers-technique/)
- [LeetCode Two Pointers Problems](https://leetcode.com/tag/two-pointers/)
- [Algorithms by Robert Sedgewick](https://algs4.cs.princeton.edu/home/)
- [Introduction to Algorithms - CLRS](https://mitpress.mit.edu/books/introduction-algorithms)

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
  <i>↔️ "A eficiência está na simplicidade dos movimentos precisos"</i>
  <br>
  <i>↔️ "Efficiency lies in the simplicity of precise movements"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E74C3C&height=120&section=footer"/>

</div>
