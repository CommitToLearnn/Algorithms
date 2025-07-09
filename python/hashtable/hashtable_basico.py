#!/usr/bin/env python3
"""
Tabela Hash Básica - Implementação didática em Python
Demonstra conceitos de função hash e tratamento de colisões
"""

class HashTable:
    """Tabela hash simples com tratamento de colisões por encadeamento"""
    
    def __init__(self, size=5):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0
    
    def _hash(self, key):
        """Função hash simples - soma códigos ASCII"""
        hash_value = sum(ord(char) for char in str(key))
        index = hash_value % self.size
        print(f"   Hash de '{key}': {hash_value} % {self.size} = {index}")
        return index
    
    def put(self, key, value):
        """Insere par chave-valor"""
        print(f"\n📝 Inserindo ('{key}', '{value}')")
        index = self._hash(key)
        
        # Verifica se chave já existe
        for i, (k, _) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                print(f"   Valor atualizado no bucket {index}")
                return
        
        # Adiciona novo par
        self.buckets[index].append((key, value))
        self.count += 1
        print(f"   Adicionado no bucket {index}")
        
        if len(self.buckets[index]) > 1:
            print(f"   ⚠️  COLISÃO! Bucket {index} tem {len(self.buckets[index])} elementos")
    
    def get(self, key):
        """Recupera valor pela chave"""
        print(f"\n🔍 Buscando '{key}'")
        index = self._hash(key)
        
        for k, v in self.buckets[index]:
            if k == key:
                print(f"   ✅ Encontrado: {v}")
                return v
        
        print("   ❌ Não encontrado")
        return None
    
    def delete(self, key):
        """Remove par chave-valor"""
        print(f"\n🗑️  Removendo '{key}'")
        index = self._hash(key)
        
        for i, (k, _) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                self.count -= 1
                print(f"   ✅ Removido do bucket {index}")
                return True
        
        print("   ❌ Chave não encontrada")
        return False
    
    def display(self):
        """Exibe estado da tabela"""
        print("\n📊 Estado da Tabela Hash:")
        print(f"   Tamanho: {self.size} buckets")
        print(f"   Elementos: {self.count}")
        print(f"   Fator de carga: {self.count/self.size:.2f}")
        
        for i, bucket in enumerate(self.buckets):
            if bucket:
                items = [f"('{k}':'{v}')" for k, v in bucket]
                print(f"   Bucket {i}: {' -> '.join(items)}")
            else:
                print(f"   Bucket {i}: vazio")

def main():
    print("=" * 50)
    print("    TABELA HASH BÁSICA EM PYTHON")
    print("=" * 50)
    
    ht = HashTable(5)
    
    print("\n1️⃣  Inserindo elementos:")
    ht.put("nome", "Ana")
    ht.put("idade", "25")
    ht.put("cidade", "SP")
    ht.display()
    
    print("\n2️⃣  Buscando elementos:")
    ht.get("nome")
    ht.get("profissao")
    
    print("\n3️⃣  Removendo elemento:")
    ht.delete("idade")
    ht.display()

if __name__ == "__main__":
    main()
