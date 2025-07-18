<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=27AE60&height=120&section=header&text=Sliding%20Window&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Técnica%20de%20Janela%20Deslizante%20para%20Otimização&descAlignY=65&descSize=16">

</div>

# Sliding Window - Técnica de Janela Deslizante

## Descrição

A técnica de Sliding Window (Janela Deslizante) é uma abordagem algorítmica que mantém um subconjunto de elementos de uma estrutura de dados linear (array, string, lista) e "desliza" esta janela através da estrutura para resolver problemas de otimização de forma eficiente. É especialmente útil para problemas que envolvem subarrays ou substrings contíguas.

## Como Funciona

A técnica utiliza dois ponteiros para definir uma "janela" que se move através dos dados:

1. **Janela Fixa**: O tamanho da janela permanece constante
2. **Janela Variável**: O tamanho da janela muda baseado em condições

### Padrão de Janela Fixa
```python
def sliding_window_fixed(array, k):
    window_sum = sum(array[:k])  # Soma inicial
    max_sum = window_sum
    
    for i in range(k, len(array)):
        # Deslizar: remover primeiro, adicionar novo
        window_sum = window_sum - array[i-k] + array[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Padrão de Janela Variável
```python
def sliding_window_variable(array, condition):
    left = 0
    result = 0
    
    for right in range(len(array)):
        # Expandir janela
        # ... processar array[right] ...
        
        # Contrair janela se necessário
        while not condition_met():
            # ... processar array[left] ...
            left += 1
        
        # Atualizar resultado
        result = update_result(left, right)
    
    return result
```

## Complexidade

| Operação | Complexidade | Observações |
|----------|--------------|-------------|
| **Tempo** | O(n) | Um passe através dos dados |
| **Espaço** | O(1) - O(k) | Dependendo do problema |
| **Sem otimização** | O(n²) ou O(n×k) | Força bruta |
| **Com sliding window** | O(n) | Otimização significativa |

## Algoritmos Implementados

### 1. Maximum Sum Subarray (Janela Fixa)
```python
def max_sum_subarray_fixed(nums, k):
    if len(nums) < k:
        return 0
    
    # Calcular soma da primeira janela
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Deslizar janela
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

**Aplicação**: Encontrar subarray de tamanho k com maior soma
**Complexidade**: O(n) tempo, O(1) espaço

### 2. Longest Substring Without Repeating
```python
def longest_substring_without_repeating(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Contrair até remover duplicata
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Expandir janela
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

**Aplicação**: Maior substring sem caracteres repetidos
**Complexidade**: O(n) tempo, O(min(m,n)) espaço

### 3. Minimum Window Substring
```python
def min_window_substring(s, t):
    if not s or not t:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    left = 0
    formed = 0
    window_counts = {}
    
    ans = float("inf"), None, None
    
    for right in range(len(s)):
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) + 1
        
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        
        # Contrair janela
        while left <= right and formed == required:
            character = s[left]
            
            # Atualizar resultado
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
```

**Aplicação**: Menor janela contendo todos caracteres de um padrão
**Complexidade**: O(|s| + |t|) tempo, O(|s| + |t|) espaço

### 4. Sliding Window Maximum
```python
def sliding_window_maximum(nums, k):
    from collections import deque
    
    if not nums or k <= 0:
        return []
    
    dq = deque()  # Armazena índices
    result = []
    
    for i in range(len(nums)):
        # Remove elementos fora da janela
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove elementos menores (nunca serão máximo)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Adiciona máximo ao resultado
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

**Aplicação**: Máximo em cada janela de tamanho k
**Complexidade**: O(n) tempo, O(k) espaço

### 5. Find All Anagrams
```python
def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    
    p_count = [0] * 26
    window_count = [0] * 26
    
    # Contar frequências em p
    for char in p:
        p_count[ord(char) - ord('a')] += 1
    
    result = []
    
    for i in range(len(s)):
        # Adicionar à janela
        window_count[ord(s[i]) - ord('a')] += 1
        
        # Remover se janela excede tamanho
        if i >= len(p):
            window_count[ord(s[i - len(p)]) - ord('a')] -= 1
        
        # Verificar anagrama
        if i >= len(p) - 1 and window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result
```

**Aplicação**: Encontrar anagramas de um padrão em uma string
**Complexidade**: O(|s|) tempo, O(1) espaço

### 6. Longest Subarray with K Distinct
```python
def longest_subarray_k_distinct(nums, k):
    if not nums or k <= 0:
        return 0
    
    left = 0
    max_length = 0
    count_map = {}
    
    for right in range(len(nums)):
        # Expandir janela
        count_map[nums[right]] = count_map.get(nums[right], 0) + 1
        
        # Contrair se mais de k distintos
        while len(count_map) > k:
            count_map[nums[left]] -= 1
            if count_map[nums[left]] == 0:
                del count_map[nums[left]]
            left += 1
        
        # Atualizar máximo
        if len(count_map) == k:
            max_length = max(max_length, right - left + 1)
    
    return max_length
```

**Aplicação**: Maior subarray com exatamente k elementos distintos
**Complexidade**: O(n) tempo, O(k) espaço

## Tipos de Janela

### 1. Janela Fixa
- **Características**: Tamanho constante
- **Uso**: Problemas com restrição de tamanho específico
- **Exemplos**: Média móvel, soma máxima de k elementos

```python
# Template para janela fixa
def fixed_window_template(array, k):
    if len(array) < k:
        return None
    
    # Inicializar primeira janela
    window_value = process_initial_window(array[:k])
    result = window_value
    
    # Deslizar janela
    for i in range(k, len(array)):
        # Remover elemento que sai
        window_value = remove_element(window_value, array[i-k])
        # Adicionar elemento que entra
        window_value = add_element(window_value, array[i])
        # Atualizar resultado
        result = update_result(result, window_value)
    
    return result
```

### 2. Janela Variável
- **Características**: Tamanho dinâmico baseado em condições
- **Uso**: Problemas de otimização com restrições
- **Exemplos**: Substring mais longa, janela mínima

```python
# Template para janela variável
def variable_window_template(array, condition):
    left = 0
    result = initialize_result()
    
    for right in range(len(array)):
        # Expandir janela
        update_window_state(array[right])
        
        # Contrair janela se necessário
        while not condition_satisfied():
            update_window_state_remove(array[left])
            left += 1
        
        # Atualizar resultado
        result = update_result(result, left, right)
    
    return result
```

## Vantagens e Limitações

### ✅ Vantagens
- **Eficiência**: Reduz complexidade de O(n²) para O(n)
- **Simplicidade**: Implementação direta e intuitiva
- **Versatilidade**: Aplicável a muitos tipos de problemas
- **Otimização**: Elimina recálculos desnecessários

### ❌ Limitações
- **Problemas específicos**: Nem todos se adequam à técnica
- **Dados contíguos**: Requer elementos adjacentes
- **Estado da janela**: Pode ser complexo manter estado
- **Estruturas específicas**: Funciona melhor com arrays/strings

## Casos de Uso

### 1. Problemas de Otimização
- **Maximum/Minimum**: Subarray com soma máxima/mínima
- **Longest/Shortest**: Substring com propriedades específicas
- **Count**: Número de subarrays válidos

### 2. Análise de Dados
- **Média Móvel**: Análise de tendências em séries temporais
- **Detecção de Padrões**: Identificação de sequências específicas
- **Filtragem**: Suavização de sinais e dados

### 3. Processamento de Texto
- **Busca de Padrões**: Encontrar substrings com características
- **Análise Linguística**: Processamento de n-gramas
- **Compressão**: Identificação de sequências repetitivas

### 4. Problemas de Sistemas
- **Rate Limiting**: Controle de taxa de requisições
- **Buffer Management**: Gerenciamento de janelas de dados
- **Network Protocols**: Controle de fluxo e congestionamento

## Padrões de Aplicação

### Quando Usar Sliding Window:
1. **Problema envolve subarrays/substrings** contíguas
2. **Busca por otimização** (máximo, mínimo, contagem)
3. **Dados são processados sequencialmente**
4. **Recálculo completo seria ineficiente**

### Como Identificar:
- Palavras-chave: "subarray", "substring", "janela", "contíguo"
- Problemas de soma, média, máximo/mínimo em sequências
- Busca por propriedades em intervalos
- Otimização que envolve elementos adjacentes

## Variações da Técnica

### 1. Two Pointers (Fast/Slow)
```python
def two_pointers_pattern(array):
    slow = fast = 0
    
    while fast < len(array):
        # Lógica específica
        if condition:
            slow += 1
        fast += 1
```

### 2. Sliding Window com Hash Map
```python
def sliding_window_with_map(array):
    left = 0
    char_map = {}
    
    for right in range(len(array)):
        char_map[array[right]] = char_map.get(array[right], 0) + 1
        
        while violates_condition(char_map):
            char_map[array[left]] -= 1
            if char_map[array[left]] == 0:
                del char_map[array[left]]
            left += 1
```

### 3. Monotonic Deque
```python
from collections import deque

def monotonic_deque_pattern(array, k):
    dq = deque()
    result = []
    
    for i in range(len(array)):
        # Remove elementos fora da janela
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Manter propriedade monotônica
        while dq and array[dq[-1]] <= array[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(array[dq[0]])
```

## Comparação com Outras Técnicas

| Técnica | Tempo | Espaço | Quando Usar |
|---------|-------|--------|-------------|
| **Sliding Window** | O(n) | O(1)-O(k) | Subarrays contíguos, otimização |
| **Two Pointers** | O(n) | O(1) | Arrays ordenados, busca de pares |
| **Hash Table** | O(n) | O(n) | Busca rápida, dados não contíguos |
| **Dynamic Programming** | O(n²) | O(n²) | Subproblemas sobrepostos |

## Executar Exemplo

```bash
cd python/sliding_window
python sliding_window_basico.py
```

## Exercícios Sugeridos

### Iniciante
1. Média móvel de array
2. Maior soma de k elementos consecutivos
3. Menor subarray com soma >= target

### Intermediário
4. Longest Repeating Character Replacement
5. Permutation in String
6. Minimum Size Subarray Sum

### Avançado
7. Substring with Concatenation of All Words
8. Minimum Window Substring (múltiplos padrões)
9. Sliding Window Median

## Aplicações no Mundo Real

### 1. Análise Financeira
```python
# Média móvel de preços de ações
def moving_average(prices, window_size):
    if len(prices) < window_size:
        return []
    
    window_sum = sum(prices[:window_size])
    averages = [window_sum / window_size]
    
    for i in range(window_size, len(prices)):
        window_sum = window_sum - prices[i - window_size] + prices[i]
        averages.append(window_sum / window_size)
    
    return averages
```

### 2. Monitoramento de Sistema
```python
# Rate limiting com sliding window
class RateLimiter:
    def __init__(self, max_requests, window_size):
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests = deque()
    
    def is_allowed(self, timestamp):
        # Remove requisições fora da janela
        while self.requests and self.requests[0] <= timestamp - self.window_size:
            self.requests.popleft()
        
        # Verificar se pode adicionar nova requisição
        if len(self.requests) < self.max_requests:
            self.requests.append(timestamp)
            return True
        
        return False
```

### 3. Processamento de Sinais
```python
# Filtro passa-baixa usando média móvel
def low_pass_filter(signal, window_size):
    filtered_signal = []
    
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        end = i + 1
        
        window_avg = sum(signal[start:end]) / (end - start)
        filtered_signal.append(window_avg)
    
    return filtered_signal
```

### 4. Análise de Logs
```python
# Detectar picos de erro em logs
def detect_error_spikes(error_counts, threshold, window_size):
    spikes = []
    
    window_sum = sum(error_counts[:window_size])
    
    for i in range(window_size, len(error_counts)):
        if window_sum > threshold:
            spikes.append(i - window_size)
        
        window_sum = window_sum - error_counts[i - window_size] + error_counts[i]
    
    return spikes
```

## Otimizações Avançadas

### 1. Lazy Propagation
```python
# Atualizar estado da janela de forma preguiçosa
def lazy_sliding_window(array, k):
    pending_updates = 0
    
    for i in range(len(array)):
        # Aplicar atualizações pendentes apenas quando necessário
        if i % k == 0:
            apply_pending_updates(pending_updates)
            pending_updates = 0
        
        pending_updates += process_element(array[i])
```

### 2. Segment Tree para Janelas
```python
# Usar segment tree para consultas de range em janelas
class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.tree = [0] * (4 * self.n)
        self.build(array, 0, 0, self.n - 1)
    
    def query_range(self, left, right):
        return self.query(0, 0, self.n - 1, left, right)
```

## Referências

- [Sliding Window Technique - GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)
- [LeetCode Sliding Window Problems](https://leetcode.com/tag/sliding-window/)
- [Algorithms by Robert Sedgewick](https://algs4.cs.princeton.edu/home/)
- [The Algorithm Design Manual - Steven Skiena](http://www.algorist.com/)

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
  <i>🔄 "A eficiência flui como uma janela que desliza suavemente pelos dados"</i>
  <br>
  <i>🔄 "Efficiency flows like a window that slides smoothly through data"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=27AE60&height=120&section=footer"/>

</div>
