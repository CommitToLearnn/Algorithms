"""
Sliding Window - Algoritmos Básicos
Implementação de algoritmos fundamentais usando a técnica de janela deslizante.

Este módulo implementa várias técnicas de sliding window:
1. Maximum Sum Subarray (Soma Máxima de Subarray)
2. Longest Substring Without Repeating Characters (Maior Substring Sem Repetições)
3. Minimum Window Substring (Menor Janela Contendo Substring)
4. Sliding Window Maximum (Máximo em Janela Deslizante)
5. Find All Anagrams (Encontrar Todos os Anagramas)
6. Longest Subarray with K Distinct (Maior Subarray com K Elementos Distintos)

Autor: matheussricardoo
"""

import time
from collections import defaultdict, deque
from typing import List, Dict, Optional


class SlidingWindowAlgorithms:
    """Classe que implementa algoritmos fundamentais de sliding window."""
    
    def __init__(self):
        """Inicializa a classe com contadores de performance."""
        self.operations_count = 0
        self.comparisons_count = 0
    
    def reset_counters(self):
        """Reset dos contadores de performance."""
        self.operations_count = 0
        self.comparisons_count = 0
    
    def max_sum_subarray_fixed(self, nums: List[int], k: int) -> int:
        """
        Encontra a soma máxima de um subarray de tamanho k.
        
        Utiliza janela fixa deslizante para evitar recálculo.
        
        Args:
            nums: Lista de números
            k: Tamanho da janela
            
        Returns:
            Soma máxima do subarray de tamanho k
            
        Complexidade:
            Tempo: O(n) onde n é o tamanho da lista
            Espaço: O(1)
        """
        self.reset_counters()
        
        if not nums or k <= 0 or k > len(nums):
            return 0
        
        # Calcular soma da primeira janela
        window_sum = sum(nums[:k])
        max_sum = window_sum
        self.operations_count += k
        
        # Deslizar janela
        for i in range(k, len(nums)):
            # Remover elemento que sai da janela, adicionar que entra
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
            self.operations_count += 2
            self.comparisons_count += 1
        
        return max_sum
    
    def longest_substring_without_repeating(self, s: str) -> int:
        """
        Encontra o comprimento da maior substring sem caracteres repetidos.
        
        Utiliza janela variável com hash set para tracking.
        
        Args:
            s: String de entrada
            
        Returns:
            Comprimento da maior substring sem repetições
            
        Complexidade:
            Tempo: O(n) onde n é o comprimento da string
            Espaço: O(min(m,n)) onde m é o tamanho do charset
        """
        self.reset_counters()
        
        if not s:
            return 0
        
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Contrair janela enquanto há repetição
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                self.operations_count += 2
            
            # Expandir janela
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            self.operations_count += 1
            self.comparisons_count += 1
        
        return max_length
    
    def min_window_substring(self, s: str, t: str) -> str:
        """
        Encontra a menor janela em s que contém todos os caracteres de t.
        
        Utiliza janela variável com hash maps para tracking.
        
        Args:
            s: String principal
            t: String padrão
            
        Returns:
            Menor substring de s que contém todos caracteres de t
            
        Complexidade:
            Tempo: O(|s| + |t|)
            Espaço: O(|s| + |t|)
        """
        self.reset_counters()
        
        if not s or not t:
            return ""
        
        # Contar caracteres necessários
        dict_t = defaultdict(int)
        for char in t:
            dict_t[char] += 1
        
        required = len(dict_t)
        left = 0
        formed = 0
        
        # Dicionário para contar caracteres na janela atual
        window_counts = defaultdict(int)
        
        # Resultado: (comprimento da janela, left, right)
        ans = float("inf"), None, None
        
        for right in range(len(s)):
            # Adicionar um caractere do lado direito da janela
            character = s[right]
            window_counts[character] += 1
            self.operations_count += 1
            
            # Se a frequência do caractere atual na janela
            # iguala à frequência desejada em t, incrementar formed
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
                self.comparisons_count += 1
            
            # Tentar contrair a janela até que ela deixe de ser 'desejável'
            while left <= right and formed == required:
                character = s[left]
                
                # Salvar a menor janela até agora
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                    self.comparisons_count += 1
                
                # O caractere no início da janela não faz mais parte da janela
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                    self.comparisons_count += 1
                
                # Mover ponteiro esquerdo para a frente
                left += 1
                self.operations_count += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
    
    def sliding_window_maximum(self, nums: List[int], k: int) -> List[int]:
        """
        Encontra o máximo em cada janela de tamanho k.
        
        Utiliza deque para manter elementos em ordem decrescente.
        
        Args:
            nums: Lista de números
            k: Tamanho da janela
            
        Returns:
            Lista com o máximo de cada janela
            
        Complexidade:
            Tempo: O(n) onde n é o tamanho da lista
            Espaço: O(k) para o deque
        """
        self.reset_counters()
        
        if not nums or k <= 0:
            return []
        
        if k == 1:
            return nums
        
        # Deque para armazenar índices
        # Manteremos elementos em ordem decrescente
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            # Remover elementos fora da janela atual
            while dq and dq[0] <= i - k:
                dq.popleft()
                self.operations_count += 1
            
            # Remover elementos menores que o atual
            # (eles nunca serão o máximo)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                self.operations_count += 1
                self.comparisons_count += 1
            
            # Adicionar elemento atual
            dq.append(i)
            self.operations_count += 1
            
            # Adicionar máximo ao resultado (se janela está completa)
            if i >= k - 1:
                result.append(nums[dq[0]])
                self.operations_count += 1
        
        return result
    
    def find_anagrams(self, s: str, p: str) -> List[int]:
        """
        Encontra todos os índices de anagramas de p em s.
        
        Utiliza janela fixa com comparação de frequências.
        
        Args:
            s: String principal
            p: String padrão
            
        Returns:
            Lista de índices onde anagramas de p começam em s
            
        Complexidade:
            Tempo: O(|s|) 
            Espaço: O(1) já que usa arrays de tamanho fixo (26 letras)
        """
        self.reset_counters()
        
        if len(p) > len(s):
            return []
        
        # Arrays de frequência para p e janela atual
        p_count = [0] * 26
        window_count = [0] * 26
        
        # Contar frequências em p
        for char in p:
            p_count[ord(char) - ord('a')] += 1
            self.operations_count += 1
        
        result = []
        window_size = len(p)
        
        for i in range(len(s)):
            # Adicionar caractere à janela
            window_count[ord(s[i]) - ord('a')] += 1
            self.operations_count += 1
            
            # Remover caractere se janela excede tamanho
            if i >= window_size:
                window_count[ord(s[i - window_size]) - ord('a')] -= 1
                self.operations_count += 1
            
            # Verificar se é anagrama (janela tem tamanho correto)
            if i >= window_size - 1:
                if window_count == p_count:
                    result.append(i - window_size + 1)
                    self.comparisons_count += 1
        
        return result
    
    def longest_subarray_k_distinct(self, nums: List[int], k: int) -> int:
        """
        Encontra o comprimento do maior subarray com exatamente k elementos distintos.
        
        Utiliza janela variável com hash map para tracking.
        
        Args:
            nums: Lista de números
            k: Número de elementos distintos desejados
            
        Returns:
            Comprimento do maior subarray com k elementos distintos
            
        Complexidade:
            Tempo: O(n) onde n é o tamanho da lista
            Espaço: O(k) para o hash map
        """
        self.reset_counters()
        
        if not nums or k <= 0:
            return 0
        
        left = 0
        max_length = 0
        count_map = defaultdict(int)
        
        for right in range(len(nums)):
            # Adicionar elemento à janela
            count_map[nums[right]] += 1
            self.operations_count += 1
            
            # Contrair janela se tiver mais de k elementos distintos
            while len(count_map) > k:
                count_map[nums[left]] -= 1
                if count_map[nums[left]] == 0:
                    del count_map[nums[left]]
                left += 1
                self.operations_count += 2
                self.comparisons_count += 1
            
            # Atualizar máximo se janela tem exatamente k elementos distintos
            if len(count_map) == k:
                max_length = max(max_length, right - left + 1)
                self.comparisons_count += 1
        
        return max_length
    
    def max_sum_subarray_variable(self, nums: List[int], target: int) -> int:
        """
        Encontra a soma máxima de subarray com soma <= target.
        
        Utiliza janela variável para encontrar subarrays válidos.
        
        Args:
            nums: Lista de números positivos
            target: Soma alvo máxima
            
        Returns:
            Soma máxima de subarray que não excede target
            
        Complexidade:
            Tempo: O(n) onde n é o tamanho da lista
            Espaço: O(1)
        """
        self.reset_counters()
        
        if not nums or target <= 0:
            return 0
        
        left = 0
        current_sum = 0
        max_sum = 0
        
        for right in range(len(nums)):
            # Expandir janela
            current_sum += nums[right]
            self.operations_count += 1
            
            # Contrair janela se soma excede target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                self.operations_count += 2
                self.comparisons_count += 1
            
            # Atualizar máximo
            max_sum = max(max_sum, current_sum)
            self.comparisons_count += 1
        
        return max_sum


def demonstrar_sliding_window():
    """Demonstra o uso dos algoritmos de sliding window."""
    sw = SlidingWindowAlgorithms()
    
    print("=" * 80)
    print("DEMONSTRAÇÃO: Algoritmos de Sliding Window")
    print("=" * 80)
    
    # 1. Maximum Sum Subarray (Fixed Window)
    print("\n1. MAXIMUM SUM SUBARRAY - JANELA FIXA")
    print("-" * 50)
    nums1 = [1, 4, 2, 9, 5, 10, 13, 8, 5]
    k = 3
    
    print(f"Array: {nums1}")
    print(f"Tamanho da janela: {k}")
    
    start_time = time.time()
    max_sum = sw.max_sum_subarray_fixed(nums1, k)
    end_time = time.time()
    
    print(f"Soma máxima: {max_sum}")
    print(f"Operações: {sw.operations_count}")
    print(f"Comparações: {sw.comparisons_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 2. Longest Substring Without Repeating Characters
    print("\n2. LONGEST SUBSTRING WITHOUT REPEATING")
    print("-" * 50)
    s1 = "abcabcbb"
    
    print(f"String: '{s1}'")
    
    start_time = time.time()
    length = sw.longest_substring_without_repeating(s1)
    end_time = time.time()
    
    print(f"Comprimento da maior substring: {length}")
    print(f"Operações: {sw.operations_count}")
    print(f"Comparações: {sw.comparisons_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 3. Minimum Window Substring
    print("\n3. MINIMUM WINDOW SUBSTRING")
    print("-" * 50)
    s2 = "ADOBECODEBANC"
    t = "ABC"
    
    print(f"String principal: '{s2}'")
    print(f"Padrão: '{t}'")
    
    start_time = time.time()
    min_window = sw.min_window_substring(s2, t)
    end_time = time.time()
    
    print(f"Menor janela: '{min_window}'")
    print(f"Operações: {sw.operations_count}")
    print(f"Comparações: {sw.comparisons_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 4. Sliding Window Maximum
    print("\n4. SLIDING WINDOW MAXIMUM")
    print("-" * 50)
    nums2 = [1, 3, -1, -3, 5, 3, 6, 7]
    k2 = 3
    
    print(f"Array: {nums2}")
    print(f"Tamanho da janela: {k2}")
    
    start_time = time.time()
    maximums = sw.sliding_window_maximum(nums2, k2)
    end_time = time.time()
    
    print(f"Máximos: {maximums}")
    print(f"Operações: {sw.operations_count}")
    print(f"Comparações: {sw.comparisons_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 5. Find All Anagrams
    print("\n5. FIND ALL ANAGRAMS")
    print("-" * 50)
    s3 = "abab"
    p = "ab"
    
    print(f"String principal: '{s3}'")
    print(f"Padrão: '{p}'")
    
    start_time = time.time()
    anagrams = sw.find_anagrams(s3, p)
    end_time = time.time()
    
    print(f"Índices de anagramas: {anagrams}")
    print(f"Operações: {sw.operations_count}")
    print(f"Comparações: {sw.comparisons_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 6. Longest Subarray with K Distinct
    print("\n6. LONGEST SUBARRAY WITH K DISTINCT")
    print("-" * 50)
    nums3 = [1, 2, 1, 2, 3]
    k3 = 2
    
    print(f"Array: {nums3}")
    print(f"K (elementos distintos): {k3}")
    
    start_time = time.time()
    longest = sw.longest_subarray_k_distinct(nums3, k3)
    end_time = time.time()
    
    print(f"Comprimento do maior subarray: {longest}")
    print(f"Operações: {sw.operations_count}")
    print(f"Comparações: {sw.comparisons_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # 7. Maximum Sum Subarray (Variable Window)
    print("\n7. MAXIMUM SUM SUBARRAY - JANELA VARIÁVEL")
    print("-" * 50)
    nums4 = [1, 2, 3, 4, 5]
    target = 8
    
    print(f"Array: {nums4}")
    print(f"Target (soma máxima): {target}")
    
    start_time = time.time()
    max_sum_var = sw.max_sum_subarray_variable(nums4, target)
    end_time = time.time()
    
    print(f"Soma máxima <= {target}: {max_sum_var}")
    print(f"Operações: {sw.operations_count}")
    print(f"Comparações: {sw.comparisons_count}")
    print(f"Tempo: {(end_time - start_time)*1000:.2f}ms")
    
    # Análise comparativa
    print("\n" + "=" * 80)
    print("ANÁLISE COMPARATIVA: Sliding Window vs Força Bruta")
    print("=" * 80)
    
    # Exemplo: Maximum Sum Subarray
    test_array = list(range(1000))
    window_size = 100
    
    # Sliding Window
    start_time = time.time()
    result_sw = sw.max_sum_subarray_fixed(test_array, window_size)
    time_sw = time.time() - start_time
    
    # Força Bruta (simulação)
    start_time = time.time()
    max_sum_bf = 0
    for i in range(len(test_array) - window_size + 1):
        current_sum = sum(test_array[i:i + window_size])
        max_sum_bf = max(max_sum_bf, current_sum)
    time_bf = time.time() - start_time
    
    print(f"Array de teste: {len(test_array)} elementos")
    print(f"Tamanho da janela: {window_size}")
    print(f"\nSliding Window:")
    print(f"  Resultado: {result_sw}")
    print(f"  Tempo: {time_sw*1000:.2f}ms")
    print(f"  Complexidade: O(n)")
    print(f"\nForça Bruta:")
    print(f"  Resultado: {max_sum_bf}")
    print(f"  Tempo: {time_bf*1000:.2f}ms")
    print(f"  Complexidade: O(n*k)")
    print(f"\nMelhoria de performance: {time_bf/time_sw:.1f}x mais rápido")
    
    # Estatísticas finais
    print("\n" + "=" * 80)
    print("RESUMO DA TÉCNICA DE SLIDING WINDOW")
    print("=" * 80)
    print("✓ Otimiza problemas de subarray/substring")
    print("✓ Reduz complexidade de O(n²) para O(n)")
    print("✓ Duas variações: janela fixa e janela variável")
    print("✓ Útil para problemas de otimização e busca")
    print("✓ Elimina recálculos desnecessários")
    
    print("\nTipos de problemas resolvidos:")
    print("• Maximum/Minimum em subarrays")
    print("• Substrings com propriedades específicas")
    print("• Problemas de contagem e frequência")
    print("• Otimização com restrições")
    print("• Análise de sequências temporais")


if __name__ == "__main__":
    demonstrar_sliding_window()
