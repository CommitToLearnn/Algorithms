package main

import "fmt"

// ListNode representa um nó da lista ligada
type ListNode struct {
	data interface{} // Aceita qualquer tipo de dado
	next *ListNode
}

// LinkedList representa uma lista ligada otimizada
type LinkedList struct {
	head *ListNode
	tail *ListNode // Ponteiro para o último elemento (otimização)
	size int
}

// NewLinkedList cria uma nova lista ligada
func NewLinkedList() *LinkedList {
	return &LinkedList{
		head: nil,
		tail: nil,
		size: 0,
	}
}

// IsEmpty verifica se a lista está vazia
func (ll *LinkedList) IsEmpty() bool {
	return ll.head == nil
}

// Size retorna o tamanho da lista
func (ll *LinkedList) Size() int {
	return ll.size
}

// Prepend adiciona um elemento no início da lista
// Complexidade: O(1) - operação constante
func (ll *LinkedList) Prepend(data interface{}) {
	newNode := &ListNode{data: data, next: ll.head}
	ll.head = newNode

	// Se era a primeira inserção, tail também aponta para o novo nó
	if ll.tail == nil {
		ll.tail = newNode
	}

	ll.size++
}

// Append adiciona um elemento no final da lista
// Complexidade: O(1) - operação constante (otimização com tail pointer)
func (ll *LinkedList) Append(data interface{}) {
	newNode := &ListNode{data: data, next: nil}

	if ll.tail == nil {
		// Lista vazia
		ll.head = newNode
		ll.tail = newNode
	} else {
		// Adiciona no final usando o ponteiro tail
		ll.tail.next = newNode
		ll.tail = newNode
	}

	ll.size++
}

// Insert insere um elemento em uma posição específica
// Complexidade: O(n) no pior caso
func (ll *LinkedList) Insert(index int, data interface{}) error {
	if index < 0 || index > ll.size {
		return fmt.Errorf("índice %d fora dos limites (0-%d)", index, ll.size)
	}

	if index == 0 {
		ll.Prepend(data)
		return nil
	}

	if index == ll.size {
		ll.Append(data)
		return nil
	}

	// Navega até a posição anterior ao índice
	current := ll.head
	for i := 0; i < index-1; i++ {
		current = current.next
	}

	newNode := &ListNode{data: data, next: current.next}
	current.next = newNode
	ll.size++

	return nil
}

// Delete remove o primeiro elemento com o valor especificado
// Complexidade: O(n) no pior caso
func (ll *LinkedList) Delete(data interface{}) bool {
	if ll.head == nil {
		return false
	}

	// Se o elemento a ser removido é o primeiro
	if ll.head.data == data {
		ll.head = ll.head.next
		ll.size--

		// Se a lista ficou vazia, tail também deve ser nil
		if ll.head == nil {
			ll.tail = nil
		}

		return true
	}

	// Procura o elemento na lista
	current := ll.head
	for current.next != nil {
		if current.next.data == data {
			nodeToDelete := current.next
			current.next = nodeToDelete.next

			// Se removemos o último elemento, atualiza tail
			if nodeToDelete == ll.tail {
				ll.tail = current
			}

			ll.size--
			return true
		}
		current = current.next
	}

	return false
}

// DeleteAt remove o elemento em uma posição específica
// Complexidade: O(n) no pior caso
func (ll *LinkedList) DeleteAt(index int) (interface{}, error) {
	if index < 0 || index >= ll.size {
		return nil, fmt.Errorf("índice %d fora dos limites (0-%d)", index, ll.size-1)
	}

	// Se remover o primeiro elemento
	if index == 0 {
		data := ll.head.data
		ll.head = ll.head.next
		ll.size--

		if ll.head == nil {
			ll.tail = nil
		}

		return data, nil
	}

	// Navega até a posição anterior ao índice
	current := ll.head
	for i := 0; i < index-1; i++ {
		current = current.next
	}

	nodeToDelete := current.next
	data := nodeToDelete.data
	current.next = nodeToDelete.next

	// Se removemos o último elemento, atualiza tail
	if nodeToDelete == ll.tail {
		ll.tail = current
	}

	ll.size--
	return data, nil
}

// Get retorna o elemento em uma posição específica
// Complexidade: O(n) no pior caso
func (ll *LinkedList) Get(index int) (interface{}, error) {
	if index < 0 || index >= ll.size {
		return nil, fmt.Errorf("índice %d fora dos limites (0-%d)", index, ll.size-1)
	}

	current := ll.head
	for i := 0; i < index; i++ {
		current = current.next
	}

	return current.data, nil
}

// Contains verifica se a lista contém um elemento
// Complexidade: O(n) no pior caso
func (ll *LinkedList) Contains(data interface{}) bool {
	current := ll.head
	for current != nil {
		if current.data == data {
			return true
		}
		current = current.next
	}
	return false
}

// IndexOf retorna o índice da primeira ocorrência de um elemento
// Complexidade: O(n) no pior caso
func (ll *LinkedList) IndexOf(data interface{}) int {
	current := ll.head
	index := 0

	for current != nil {
		if current.data == data {
			return index
		}
		current = current.next
		index++
	}

	return -1 // Não encontrado
}

// ToSlice converte a lista para slice
// Complexidade: O(n)
func (ll *LinkedList) ToSlice() []interface{} {
	result := make([]interface{}, 0, ll.size)
	current := ll.head

	for current != nil {
		result = append(result, current.data)
		current = current.next
	}

	return result
}

// Reverse inverte a lista
// Complexidade: O(n)
func (ll *LinkedList) Reverse() {
	if ll.head == nil || ll.head.next == nil {
		return
	}

	var prev *ListNode
	current := ll.head
	ll.tail = ll.head // O antigo head se torna o novo tail

	for current != nil {
		next := current.next
		current.next = prev
		prev = current
		current = next
	}

	ll.head = prev
}

// Clear remove todos os elementos da lista
// Complexidade: O(1)
func (ll *LinkedList) Clear() {
	ll.head = nil
	ll.tail = nil
	ll.size = 0
}

// Display exibe todos os elementos da lista
func (ll *LinkedList) Display() {
	if ll.head == nil {
		fmt.Println("Lista vazia")
		return
	}

	fmt.Print("Lista: ")
	current := ll.head
	for current != nil {
		fmt.Print(current.data)
		if current.next != nil {
			fmt.Print(" -> ")
		}
		current = current.next
	}
	fmt.Printf(" (tamanho: %d)\n", ll.size)
}

// Exemplo de uso
func main() {
	fmt.Println("=== Lista Ligada Simples - Versão Otimizada ===")

	// Cria uma nova lista
	lista := NewLinkedList()

	// Demonstra as otimizações
	fmt.Println("\n1. Append otimizado (O(1) com tail pointer):")
	lista.Append("primeiro")
	lista.Append("segundo")
	lista.Append("terceiro")
	lista.Display()

	fmt.Println("\n2. Operações com tipos mistos:")
	lista.Append(42)
	lista.Append(3.14)
	lista.Display()

	fmt.Println("\n3. Insert em posições específicas:")
	lista.Insert(0, "início")
	lista.Insert(2, "meio")
	lista.Display()

	fmt.Println("\n4. Busca por índice:")
	if val, err := lista.Get(3); err == nil {
		fmt.Printf("Elemento no índice 3: %v\n", val)
	}

	fmt.Println("\n5. Conversão para slice:")
	slice := lista.ToSlice()
	fmt.Printf("Como slice: %v\n", slice)

	fmt.Println("\n6. Reverter lista:")
	lista.Reverse()
	lista.Display()

	fmt.Printf("\nTamanho final: %d\n", lista.Size())
}
