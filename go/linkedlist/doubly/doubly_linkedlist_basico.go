package main

import "fmt"

// DoublyListNode representa um nó da lista duplamente ligada
type DoublyListNode struct {
	data int               // Usando int para simplificar o exemplo básico
	next *DoublyListNode
	prev *DoublyListNode
}

// DoublyLinkedList representa uma lista duplamente ligada
type DoublyLinkedList struct {
	head *DoublyListNode
	tail *DoublyListNode
	size int
}

// NewDoublyLinkedList cria uma nova lista duplamente ligada
func NewDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{
		head: nil,
		tail: nil,
		size: 0,
	}
}

// IsEmpty verifica se a lista está vazia
func (dll *DoublyLinkedList) IsEmpty() bool {
	return dll.head == nil
}

// Size retorna o tamanho da lista
func (dll *DoublyLinkedList) Size() int {
	return dll.size
}

// Prepend adiciona um elemento no início
// Complexidade: O(1) - operação constante
func (dll *DoublyLinkedList) Prepend(data int) {
	newNode := &DoublyListNode{data: data, next: dll.head, prev: nil}

	if dll.head != nil {
		dll.head.prev = newNode
	} else {
		// Lista estava vazia, então tail também aponta para o novo nó
		dll.tail = newNode
	}

	dll.head = newNode
	dll.size++
}

// Append adiciona um elemento no final
// Complexidade: O(1) - operação constante
func (dll *DoublyLinkedList) Append(data int) {
	newNode := &DoublyListNode{data: data, next: nil, prev: dll.tail}

	if dll.tail != nil {
		dll.tail.next = newNode
	} else {
		// Lista estava vazia, então head também aponta para o novo nó
		dll.head = newNode
	}

	dll.tail = newNode
	dll.size++
}

// Delete remove um elemento
// Complexidade: O(n) no pior caso (precisa encontrar o elemento)
func (dll *DoublyLinkedList) Delete(data int) bool {
	current := dll.head

	for current != nil {
		if current.data == data {
			// Atualiza os ponteiros
			if current.prev != nil {
				current.prev.next = current.next
			} else {
				// Era o primeiro elemento
				dll.head = current.next
			}

			if current.next != nil {
				current.next.prev = current.prev
			} else {
				// Era o último elemento
				dll.tail = current.prev
			}

			dll.size--
			return true
		}
		current = current.next
	}

	return false
}

// Search procura um elemento na lista
// Complexidade: O(n) no pior caso
func (dll *DoublyLinkedList) Search(data int) bool {
	current := dll.head
	for current != nil {
		if current.data == data {
			return true
		}
		current = current.next
	}
	return false
}

// DisplayForward exibe a lista da frente para trás
func (dll *DoublyLinkedList) DisplayForward() {
	if dll.head == nil {
		fmt.Println("Lista vazia")
		return
	}

	fmt.Print("Lista (frente para trás): ")
	current := dll.head
	for current != nil {
		fmt.Print(current.data)
		if current.next != nil {
			fmt.Print(" <-> ")
		}
		current = current.next
	}
	fmt.Printf(" (tamanho: %d)\n", dll.size)
}

// DisplayBackward exibe a lista de trás para frente
func (dll *DoublyLinkedList) DisplayBackward() {
	if dll.tail == nil {
		fmt.Println("Lista vazia")
		return
	}

	fmt.Print("Lista (trás para frente): ")
	current := dll.tail
	for current != nil {
		fmt.Print(current.data)
		if current.prev != nil {
			fmt.Print(" <-> ")
		}
		current = current.prev
	}
	fmt.Printf(" (tamanho: %d)\n", dll.size)
}

// Exemplo de uso
func main() {
	fmt.Println("=== Lista Duplamente Ligada - Versão Básica ===")
	
	// Cria uma nova lista
	lista := NewDoublyLinkedList()
	
	// Adiciona elementos
	fmt.Println("\n1. Adicionando elementos no final:")
	lista.Append(1)
	lista.Append(2)
	lista.Append(3)
	lista.DisplayForward()
	
	// Adiciona elemento no início
	fmt.Println("\n2. Adicionando elemento no início:")
	lista.Prepend(0)
	lista.DisplayForward()
	
	// Mostra vantagem da lista dupla: navegação reversa
	fmt.Println("\n3. Navegação reversa:")
	lista.DisplayBackward()
	
	// Busca elementos
	fmt.Println("\n4. Buscando elementos:")
	fmt.Printf("Elemento 2 encontrado: %t\n", lista.Search(2))
	fmt.Printf("Elemento 5 encontrado: %t\n", lista.Search(5))
	
	// Remove elementos
	fmt.Println("\n5. Removendo elementos:")
	fmt.Printf("Removido 2: %t\n", lista.Delete(2))
	lista.DisplayForward()
	lista.DisplayBackward()
	
	// Verifica propriedades
	fmt.Printf("\nTamanho da lista: %d\n", lista.Size())
	fmt.Printf("Lista vazia: %t\n", lista.IsEmpty())
}
