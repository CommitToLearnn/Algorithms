"""
SHA (Secure Hash Algorithm) - Implementação básica do SHA-256
Algoritmo criptográfico de hash seguro
"""

import struct


class SHA256:
    def __init__(self):
        """Inicializa o SHA-256 com constantes"""
        # Constantes iniciais de hash (primeiros 32 bits das raízes quadradas dos primeiros 8 primos)
        self.h = [
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
        ]
        
        # Constantes de rodada (primeiros 32 bits das raízes cúbicas dos primeiros 64 primos)
        self.k = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]
    
    def _rotr(self, n, b):
        """Rotação à direita"""
        return ((n >> b) | (n << (32 - b))) & 0xffffffff
    
    def _ch(self, x, y, z):
        """Função Choose"""
        return (x & y) ^ (~x & z)
    
    def _maj(self, x, y, z):
        """Função Majority"""
        return (x & y) ^ (x & z) ^ (y & z)
    
    def _sigma0(self, x):
        """Função Sigma0"""
        return self._rotr(x, 2) ^ self._rotr(x, 13) ^ self._rotr(x, 22)
    
    def _sigma1(self, x):
        """Função Sigma1"""
        return self._rotr(x, 6) ^ self._rotr(x, 11) ^ self._rotr(x, 25)
    
    def _gamma0(self, x):
        """Função Gamma0"""
        return self._rotr(x, 7) ^ self._rotr(x, 18) ^ (x >> 3)
    
    def _gamma1(self, x):
        """Função Gamma1"""
        return self._rotr(x, 17) ^ self._rotr(x, 19) ^ (x >> 10)
    
    def _preprocess(self, message):
        """Pré-processamento da mensagem"""
        # Converte string para bytes se necessário
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        # Tamanho original em bits
        msg_len = len(message) * 8
        
        # Adiciona padding: bit 1 seguido de bits 0
        message += b'\x80'
        
        # Adiciona zeros até que o comprimento seja congruente a 448 mod 512
        while (len(message) % 64) != 56:
            message += b'\x00'
        
        # Adiciona o tamanho original como big-endian de 64 bits
        message += struct.pack('>Q', msg_len)
        
        return message
    
    def hash(self, message):
        """Calcula o hash SHA-256 da mensagem"""
        # Pré-processamento
        message = self._preprocess(message)
        
        # Processa em blocos de 512 bits (64 bytes)
        for chunk_start in range(0, len(message), 64):
            chunk = message[chunk_start:chunk_start + 64]
            
            # Quebra o bloco em 16 palavras de 32 bits
            w = list(struct.unpack('>16I', chunk))
            
            # Estende para 64 palavras
            for i in range(16, 64):
                s0 = self._gamma0(w[i-15])
                s1 = self._gamma1(w[i-2])
                w.append((w[i-16] + s0 + w[i-7] + s1) & 0xffffffff)
            
            # Inicializa variáveis de trabalho
            a, b, c, d, e, f, g, h = self.h
            
            # Compressão principal
            for i in range(64):
                s1 = self._sigma1(e)
                ch = self._ch(e, f, g)
                temp1 = (h + s1 + ch + self.k[i] + w[i]) & 0xffffffff
                s0 = self._sigma0(a)
                maj = self._maj(a, b, c)
                temp2 = (s0 + maj) & 0xffffffff
                
                h = g
                g = f
                f = e
                e = (d + temp1) & 0xffffffff
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xffffffff
            
            # Adiciona aos valores de hash
            self.h[0] = (self.h[0] + a) & 0xffffffff
            self.h[1] = (self.h[1] + b) & 0xffffffff
            self.h[2] = (self.h[2] + c) & 0xffffffff
            self.h[3] = (self.h[3] + d) & 0xffffffff
            self.h[4] = (self.h[4] + e) & 0xffffffff
            self.h[5] = (self.h[5] + f) & 0xffffffff
            self.h[6] = (self.h[6] + g) & 0xffffffff
            self.h[7] = (self.h[7] + h) & 0xffffffff
        
        # Produz o hash final
        return ''.join(f'{h:08x}' for h in self.h)


def sha256(message):
    """Função auxiliar para calcular SHA-256"""
    hasher = SHA256()
    return hasher.hash(message)


# Exemplo de uso
if __name__ == "__main__":
    # Testes com diferentes mensagens
    test_messages = [
        "",
        "abc",
        "Hello, World!",
        "The quick brown fox jumps over the lazy dog",
        "SHA-256 é um algoritmo de hash criptográfico seguro"
    ]
    
    print("=== SHA-256 - Secure Hash Algorithm ===")
    
    for message in test_messages:
        hash_result = sha256(message)
        print(f"Mensagem: '{message}'")
        print(f"SHA-256:  {hash_result}")
        print(f"Tamanho:  {len(hash_result)} caracteres hex ({len(hash_result)*4} bits)")
        print()
    
    # Demonstra propriedades do hash
    print("=== Propriedades do SHA-256 ===")
    
    # Efeito avalanche - pequena mudança causa grande diferença
    msg1 = "Hello"
    msg2 = "hello"  # Apenas mudança de maiúscula
    
    hash1 = sha256(msg1)
    hash2 = sha256(msg2)
    
    print(f"Mensagem 1: '{msg1}'")
    print(f"Hash 1:     {hash1}")
    print(f"Mensagem 2: '{msg2}'")
    print(f"Hash 2:     {hash2}")
    
    # Calcula diferenças
    diff_bits = sum(c1 != c2 for c1, c2 in zip(hash1, hash2))
    print(f"Diferenças: {diff_bits} caracteres hex de {len(hash1)} ({diff_bits/len(hash1)*100:.1f}%)")
    
    # Teste de determinismo
    print("\n=== Teste de Determinismo ===")
    test_msg = "Teste de consistência"
    hash_a = sha256(test_msg)
    hash_b = sha256(test_msg)
    
    print(f"Mensagem: '{test_msg}'")
    print(f"Hash A:   {hash_a}")
    print(f"Hash B:   {hash_b}")
    print(f"Iguais:   {hash_a == hash_b}")
