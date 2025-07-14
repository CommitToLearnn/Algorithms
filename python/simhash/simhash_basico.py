"""
SimHash - Algoritmo para detecção de documentos similares
Implementação básica que gera fingerprints de 64-bit para textos
"""

import hashlib
import re
from collections import defaultdict


class SimHash:
    def __init__(self, text, hash_bits=64):
        """
        Inicializa o SimHash com um texto
        
        Args:
            text (str): Texto para gerar o hash
            hash_bits (int): Número de bits do hash (padrão 64)
        """
        self.hash_bits = hash_bits
        self.hash_value = self._compute_simhash(text)
    
    def _tokenize(self, text):
        """Tokeniza o texto em palavras"""
        # Remove pontuação e converte para minúsculas
        text = re.sub(r'[^\w\s]', '', text.lower())
        return text.split()
    
    def _compute_simhash(self, text):
        """Computa o SimHash do texto"""
        tokens = self._tokenize(text)
        
        # Inicializa vetor de características
        vector = [0] * self.hash_bits
        
        for token in tokens:
            # Gera hash MD5 do token
            hash_obj = hashlib.md5(token.encode('utf-8'))
            hash_hex = hash_obj.hexdigest()
            
            # Converte para binário
            hash_int = int(hash_hex, 16)
            
            # Para cada bit do hash
            for i in range(self.hash_bits):
                bit = (hash_int >> i) & 1
                if bit == 1:
                    vector[i] += 1
                else:
                    vector[i] -= 1
        
        # Gera o fingerprint final
        fingerprint = 0
        for i in range(self.hash_bits):
            if vector[i] > 0:
                fingerprint |= (1 << i)
        
        return fingerprint
    
    def hamming_distance(self, other):
        """Calcula a distância de Hamming entre dois SimHashes"""
        if not isinstance(other, SimHash):
            raise ValueError("Comparação deve ser com outro objeto SimHash")
        
        xor_result = self.hash_value ^ other.hash_value
        distance = bin(xor_result).count('1')
        return distance
    
    def similarity(self, other):
        """Calcula similaridade como porcentagem (0-100)"""
        distance = self.hamming_distance(other)
        similarity = ((self.hash_bits - distance) / self.hash_bits) * 100
        return similarity
    
    def __str__(self):
        return f"SimHash({self.hash_value:0{self.hash_bits//4}x})"


# Exemplo de uso
if __name__ == "__main__":
    # Textos de exemplo
    text1 = "O gato subiu no telhado para pegar o rato"
    text2 = "O gato subiu no telhado para capturar o rato"
    text3 = "O cachorro latiu para o carteiro na rua"
    
    # Gera SimHashes
    hash1 = SimHash(text1)
    hash2 = SimHash(text2)
    hash3 = SimHash(text3)
    
    print("=== SimHash - Detecção de Similaridade ===")
    print(f"Texto 1: {text1}")
    print(f"Hash 1: {hash1}")
    print()
    
    print(f"Texto 2: {text2}")
    print(f"Hash 2: {hash2}")
    print()
    
    print(f"Texto 3: {text3}")
    print(f"Hash 3: {hash3}")
    print()
    
    # Calcula similaridades
    sim_1_2 = hash1.similarity(hash2)
    sim_1_3 = hash1.similarity(hash3)
    sim_2_3 = hash2.similarity(hash3)
    
    print("=== Resultados de Similaridade ===")
    print(f"Similaridade entre texto 1 e 2: {sim_1_2:.2f}%")
    print(f"Similaridade entre texto 1 e 3: {sim_1_3:.2f}%")
    print(f"Similaridade entre texto 2 e 3: {sim_2_3:.2f}%")
    
    # Demonstra detecção de documentos duplicados
    print("\n=== Detecção de Duplicados ===")
    threshold = 85  # 85% de similaridade
    
    if sim_1_2 >= threshold:
        print(f"✓ Textos 1 e 2 são considerados duplicados ({sim_1_2:.2f}%)")
    else:
        print(f"✗ Textos 1 e 2 não são duplicados ({sim_1_2:.2f}%)")
    
    if sim_1_3 >= threshold:
        print(f"✓ Textos 1 e 3 são considerados duplicados ({sim_1_3:.2f}%)")
    else:
        print(f"✗ Textos 1 e 3 não são duplicados ({sim_1_3:.2f}%)")
