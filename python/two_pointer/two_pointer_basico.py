"""
=== Two Pointer - Técnica de Dois Ponteiros ===

A técnica de dois ponteiros é uma abordagem eficiente para resolver problemas
que envolvem arrays ou listas ordenadas. Utiliza dois ponteiros que se movem
através da estrutura de dados para encontrar soluções em tempo linear.

Autor: matheussricardoo
Data: 2025
"""

def two_sum_sorted(nums, target):
    """
    Encontra dois números em um array ordenado que somam ao target.
    
    Args:
        nums: Lista de números inteiros ordenados
        target: Valor alvo da soma
    
    Returns:
        Tuple com os índices dos dois números ou None se não encontrar
    
    Complexidade: O(n) tempo, O(1) espaço
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

def is_palindrome(s):
    """
    Verifica se uma string é um palíndromo (ignora espaços e maiúsculas).
    
    Args:
        s: String para verificar
    
    Returns:
        Boolean indicando se é palíndromo
    
    Complexidade: O(n) tempo, O(1) espaço
    """
    # Limpar string: apenas caracteres alfanuméricos em minúsculo
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

def remove_duplicates(nums):
    """
    Remove duplicatas de um array ordenado in-place.
    
    Args:
        nums: Lista ordenada com possíveis duplicatas
    
    Returns:
        Comprimento do array sem duplicatas
    
    Complexidade: O(n) tempo, O(1) espaço
    """
    if not nums:
        return 0
    
    # Ponteiro para posição do próximo elemento único
    write_pos = 1
    
    for read_pos in range(1, len(nums)):
        if nums[read_pos] != nums[read_pos - 1]:
            nums[write_pos] = nums[read_pos]
            write_pos += 1
    
    return write_pos

def container_with_most_water(heights):
    """
    Encontra o container que pode armazenar mais água.
    
    Args:
        heights: Lista de alturas das paredes
    
    Returns:
        Área máxima de água que pode ser armazenada
    
    Complexidade: O(n) tempo, O(1) espaço
    """
    if len(heights) < 2:
        return 0
    
    left = 0
    right = len(heights) - 1
    max_area = 0
    
    while left < right:
        # Área = largura × altura mínima
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        
        max_area = max(max_area, area)
        
        # Move o ponteiro da menor altura
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

def three_sum(nums):
    """
    Encontra todos os triplets únicos que somam zero.
    
    Args:
        nums: Lista de números inteiros
    
    Returns:
        Lista de triplets que somam zero
    
    Complexidade: O(n²) tempo, O(1) espaço extra
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Pular duplicatas para o primeiro número
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Pular duplicatas
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result

def sort_colors(nums):
    """
    Ordena array com apenas 0s, 1s e 2s (Dutch National Flag Problem).
    
    Args:
        nums: Lista com apenas valores 0, 1, 2
    
    Modifica a lista in-place
    
    Complexidade: O(n) tempo, O(1) espaço
    """
    # Três ponteiros: low (0s), mid (atual), high (2s)
    low = mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Não incrementar mid porque precisamos verificar o valor trocado

def demonstrate_two_pointer():
    """Demonstra todos os algoritmos de Two Pointer."""
    print("=== Demonstração - Two Pointer ===\n")
    
    # 1. Two Sum em array ordenado
    print("1. Two Sum em Array Ordenado")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum_sorted(nums, target)
    print(f"Array: {nums}, Target: {target}")
    print(f"Índices que somam {target}: {result}")
    if result:
        print(f"Valores: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
    print()
    
    # 2. Verificação de Palíndromo
    print("2. Verificação de Palíndromo")
    test_strings = [
        "A man a plan a canal Panama",
        "race a car",
        "Madam",
        "Was it a car or a cat I saw?"
    ]
    
    for s in test_strings:
        is_pal = is_palindrome(s)
        print(f"'{s}' → {'É palíndromo' if is_pal else 'Não é palíndromo'}")
    print()
    
    # 3. Remoção de Duplicatas
    print("3. Remoção de Duplicatas")
    nums_dup = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5]
    original = nums_dup.copy()
    new_length = remove_duplicates(nums_dup)
    print(f"Original: {original}")
    print(f"Sem duplicatas: {nums_dup[:new_length]} (comprimento: {new_length})")
    print()
    
    # 4. Container com Mais Água
    print("4. Container com Mais Água")
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_water = container_with_most_water(heights)
    print(f"Alturas: {heights}")
    print(f"Área máxima de água: {max_water}")
    print()
    
    # 5. Three Sum
    print("5. Three Sum (triplets que somam zero)")
    nums_three = [-1, 0, 1, 2, -1, -4]
    triplets = three_sum(nums_three.copy())
    print(f"Array: {nums_three}")
    print(f"Triplets que somam zero: {triplets}")
    print()
    
    # 6. Sort Colors (Dutch National Flag)
    print("6. Sort Colors (0s, 1s, 2s)")
    colors = [2, 0, 2, 1, 1, 0]
    original_colors = colors.copy()
    sort_colors(colors)
    print(f"Original: {original_colors}")
    print(f"Ordenado: {colors}")
    print()
    
    # Estatísticas
    print("=== Estatísticas da Técnica ===")
    print("• Complexidade temporal típica: O(n)")
    print("• Complexidade espacial: O(1)")
    print("• Ideal para: arrays ordenados, problemas de soma")
    print("• Vantagem: eficiente em espaço e tempo")
    print("• Aplicações: algoritmos de busca, ordenação, strings")

if __name__ == "__main__":
    demonstrate_two_pointer()
