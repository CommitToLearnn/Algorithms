/**
 * Lista Ligada Básica - Implementação Educacional em Go
 * =====================================================
 *
 * Esta implementação demonstra uma estrutura de dados linear dinâmica
 * com operações básicas bem documentadas e explicadas.
 *
 * Características:
 * - Implementação simples e didática
 * - Comentários explicativos detalhados
 * - Análise de complexidade para cada operação
 * - Exemplos práticos de uso
 * - Demonstração visual das operações
 *
 * @author matheussricardoo
 * @version 1.0
 * @since Julho 2025
 */

package main

import "fmt"

// ListNode representa um nó da lista ligada simples
type ListNode struct {
	data int       // Dados armazenados no nó
	next *ListNode // Ponteiro para o próximo nó
}

// LinkedList representa uma lista ligada simples
type LinkedList struct {
	head *ListNode // Ponteiro para o primeiro nó
	size int       // Número de elementos na lista
}

// NewLinkedList cria uma nova lista ligada vazia
// Complexidade: O(1)
func NewLinkedList() *LinkedList {
	return &LinkedList{
		head: nil,
		size: 0,
	}
}

// Append adiciona um elemento no final da lista
// Complexidade: O(n) - precisa percorrer toda a lista
func (ll *LinkedList) Append(data int) {
	fmt.Printf("➕ Adicionando %d no final...\n", data)

	newNode := &ListNode{data: data, next: nil}

	// Se a lista estiver vazia, o novo nó se torna o head
	if ll.head == nil {
		ll.head = newNode
		fmt.Println("   Lista estava vazia, novo nó se tornou o primeiro")
	} else {
		// Percorre até o final da lista
		current := ll.head
		position := 0
		for current.next != nil {
			current = current.next
			position++
		}
		// Adiciona o novo nó no final
		current.next = newNode
		fmt.Printf("   Adicionado após percorrer %d nós\n", position+1)
	}

	ll.size++
	fmt.Printf("   ✅ Tamanho atual: %d\n", ll.size)
}

// Prepend adiciona um elemento no início da lista
// Complexidade: O(1) - operação constante
func (ll *LinkedList) Prepend(data int) {
	fmt.Printf("⬆️  Adicionando %d no início...\n", data)

	newNode := &ListNode{data: data, next: ll.head}
	ll.head = newNode
	ll.size++

	fmt.Printf("   ✅ Tamanho atual: %d\n", ll.size)
}

// Delete remove o primeiro elemento com o valor especificado
// Complexidade: O(n) - pode precisar percorrer toda a lista
func (ll *LinkedList) Delete(data int) bool {
	fmt.Printf("🗑️  Removendo elemento %d...\n", data)

	// Lista vazia
	if ll.head == nil {
		fmt.Println("   ❌ Lista vazia")
		return false
	}

	// Se o elemento a ser removido é o primeiro
	if ll.head.data == data {
		ll.head = ll.head.next
		ll.size--
		fmt.Printf("   ✅ Removido do início. Tamanho atual: %d\n", ll.size)
		return true
	}

	// Procura o elemento na lista
	current := ll.head
	position := 0
	for current.next != nil {
		if current.next.data == data {
			// Remove o nó apontando para o próximo do próximo
			current.next = current.next.next
			ll.size--
			fmt.Printf("   ✅ Removido da posição %d. Tamanho atual: %d\n", position+1, ll.size)
			return true
		}
		current = current.next
		position++
	}

	fmt.Println("   ❌ Elemento não encontrado")
	return false
}

// Search procura um elemento na lista
// Complexidade: O(n) - pode precisar percorrer toda a lista
func (ll *LinkedList) Search(data int) bool {
	fmt.Printf("🔍 Procurando elemento %d...\n", data)

	current := ll.head
	position := 0
	for current != nil {
		if current.data == data {
			fmt.Printf("   ✅ Encontrado na posição %d\n", position)
			return true
		}
		current = current.next
		position++
	}

	fmt.Println("   ❌ Elemento não encontrado")
	return false
}

// Size retorna o tamanho da lista
// Complexidade: O(1)
func (ll *LinkedList) Size() int {
	return ll.size
}

// IsEmpty verifica se a lista está vazia
// Complexidade: O(1)
func (ll *LinkedList) IsEmpty() bool {
	return ll.head == nil
}

// Display exibe todos os elementos da lista de forma visual
func (ll *LinkedList) Display() {
	fmt.Print("📋 Lista: ")

	if ll.head == nil {
		fmt.Println("vazia")
		return
	}

	current := ll.head
	for current != nil {
		fmt.Printf("[%d]", current.data)
		if current.next != nil {
			fmt.Print(" → ")
		}
		current = current.next
	}
	fmt.Printf(" (tamanho: %d)\n", ll.size)
}

// Exemplo de uso e demonstração
func main() {
	fmt.Println("╔════════════════════════════════════════╗")
	fmt.Println("║        Lista Ligada Básica - Go       ║")
	fmt.Println("║      Implementação Educacional         ║")
	fmt.Println("╚════════════════════════════════════════╝")
	fmt.Println()

	// Cria uma nova lista
	lista := NewLinkedList()

	fmt.Println("🚀 Demonstração de Operações:")
	fmt.Println()

	// Adiciona elementos no final
	fmt.Println("1️⃣  Adicionando elementos no final:")
	lista.Append(10)
	lista.Append(20)
	lista.Append(30)
	lista.Display()
	fmt.Println()

	// Adiciona elementos no início
	fmt.Println("2️⃣  Adicionando elementos no início:")
	lista.Prepend(5)
	lista.Prepend(1)
	lista.Display()
	fmt.Println()

	// Busca elementos
	fmt.Println("3️⃣  Buscando elementos:")
	lista.Search(20)
	lista.Search(100)
	fmt.Println()

	// Remove elementos
	fmt.Println("4️⃣  Removendo elementos:")
	lista.Delete(20)
	lista.Display()
	lista.Delete(1)
	lista.Display()
	lista.Delete(999)
	fmt.Println()

	// Verifica propriedades
	fmt.Println("5️⃣  Verificando propriedades:")
	fmt.Printf("   📏 Tamanho da lista: %d\n", lista.Size())
	fmt.Printf("   📭 Lista vazia? %t\n", lista.IsEmpty())

	fmt.Println()
	fmt.Println("📊 Análise de Complexidade:")
	fmt.Println("   • Inserção no início: O(1)")
	fmt.Println("   • Inserção no final: O(n)")
	fmt.Println("   • Busca: O(n)")
	fmt.Println("   • Remoção: O(n)")
	fmt.Println("   • Acesso por índice: O(n)")

	fmt.Println()
	fmt.Println("💡 Vantagens:")
	fmt.Println("   • Tamanho dinâmico")
	fmt.Println("   • Inserção/remoção eficiente no início")
	fmt.Println("   • Uso eficiente de memória")

	fmt.Println()
	fmt.Println("⚠️  Desvantagens:")
	fmt.Println("   • Acesso sequencial apenas")
	fmt.Println("   • Overhead de ponteiros")
	fmt.Println("   • Cache locality ruim")
}
