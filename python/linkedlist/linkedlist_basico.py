"""
Lista Ligada Básica - Implementação Educacional em Python
=========================================================

Esta implementação demonstra os conceitos fundamentais de uma lista ligada,
uma estrutura de dados linear dinâmica onde elementos são conectados por ponteiros.

Características desta versão:
- Implementação simples e didática
- Operações fundamentais claramente explicadas  
- Código comentado para facilitar entendimento
- Ideal para estudantes iniciantes

@author matheussricardoo
@version 1.0
@since Julho 2025
"""

class Node:
    """Nó da lista ligada"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Lista ligada simples"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Adiciona elemento no final - O(n)"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
        print(f"   Adicionado {data} no final")
    
    def prepend(self, data):
        """Adiciona elemento no início - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print(f"   Adicionado {data} no início")
    
    def delete(self, data):
        """Remove primeira ocorrência do elemento"""
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            print(f"   Removido {data}")
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                print(f"   Removido {data}")
                return True
            current = current.next
        
        print(f"   {data} não encontrado")
        return False
    
    def search(self, data):
        """Busca elemento na lista"""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def display(self):
        """Exibe a lista"""
        if not self.head:
            print("Lista vazia")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(f"Lista: {' -> '.join(elements)} (tamanho: {self.size})")

def main():
    print("=" * 50)
    print("    LISTA LIGADA BÁSICA EM PYTHON")
    print("=" * 50)
    
    ll = LinkedList()
    
    print("\n1️⃣  Adicionando elementos:")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()
    
    print("\n2️⃣  Adicionando no início:")
    ll.prepend(0)
    ll.display()
    
    print("\n3️⃣  Buscando elementos:")
    pos = ll.search(2)
    print(f"   Elemento 2 na posição: {pos}")
    
    print("\n4️⃣  Removendo elementos:")
    ll.delete(2)
    ll.display()

if __name__ == "__main__":
    main()
