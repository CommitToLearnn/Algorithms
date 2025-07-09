package main

import (
	"fmt"
	"hash/fnv"
)

// OptimizedHashTable implementa uma tabela hash otimizada
type OptimizedHashTable struct {
	buckets   []*Node
	size      int
	count     int     // Contador de elementos para eficiência
	threshold float64 // Fator de carga limite para redimensionamento
}

// Node representa um nó na lista ligada para tratamento de colisões
type Node struct {
	key   string
	value interface{} // Aceita qualquer tipo
	next  *Node
}

// NewOptimizedHashTable cria uma nova tabela hash otimizada
func NewOptimizedHashTable(initialSize int) *OptimizedHashTable {
	return &OptimizedHashTable{
		buckets:   make([]*Node, initialSize),
		size:      initialSize,
		count:     0,
		threshold: 0.75, // Redimensiona quando > 75% de ocupação
	}
}

// hash implementa função hash FNV-1a (muito eficiente)
func (ht *OptimizedHashTable) hash(key string) int {
	hasher := fnv.New32a()
	hasher.Write([]byte(key))
	return int(hasher.Sum32()) % ht.size
}

// Put insere ou atualiza um par chave-valor com redimensionamento automático
func (ht *OptimizedHashTable) Put(key string, value interface{}) {
	// Verifica se precisa redimensionar ANTES da inserção
	if ht.LoadFactor() > ht.threshold {
		ht.resize()
	}

	index := ht.hash(key)

	// Se o bucket está vazio, cria um novo nó
	if ht.buckets[index] == nil {
		ht.buckets[index] = &Node{key: key, value: value}
		ht.count++
		return
	}

	// Percorre a lista ligada procurando a chave
	current := ht.buckets[index]
	for current != nil {
		if current.key == key {
			// Atualiza o valor existente (não aumenta count)
			current.value = value
			return
		}
		if current.next == nil {
			break
		}
		current = current.next
	}

	// Adiciona novo nó no final da lista
	current.next = &Node{key: key, value: value}
	ht.count++
}

// Get recupera um valor pela chave
func (ht *OptimizedHashTable) Get(key string) (interface{}, bool) {
	index := ht.hash(key)
	current := ht.buckets[index]

	for current != nil {
		if current.key == key {
			return current.value, true
		}
		current = current.next
	}

	return nil, false
}

// Delete remove um par chave-valor
func (ht *OptimizedHashTable) Delete(key string) bool {
	index := ht.hash(key)
	current := ht.buckets[index]

	// Se o bucket está vazio
	if current == nil {
		return false
	}

	// Se o primeiro nó tem a chave
	if current.key == key {
		ht.buckets[index] = current.next
		ht.count--
		return true
	}

	// Procura na lista ligada
	for current.next != nil {
		if current.next.key == key {
			current.next = current.next.next
			ht.count--
			return true
		}
		current = current.next
	}

	return false
}

// Contains verifica se uma chave existe
func (ht *OptimizedHashTable) Contains(key string) bool {
	_, exists := ht.Get(key)
	return exists
}

// Size retorna o número de elementos (O(1) otimizado)
func (ht *OptimizedHashTable) Size() int {
	return ht.count
}

// LoadFactor calcula o fator de carga
func (ht *OptimizedHashTable) LoadFactor() float64 {
	return float64(ht.count) / float64(ht.size)
}

// resize redimensiona a tabela quando o fator de carga é muito alto
func (ht *OptimizedHashTable) resize() {
	fmt.Printf("🔄 Redimensionando tabela: %d -> %d buckets\n", ht.size, ht.size*2)

	oldBuckets := ht.buckets
	oldSize := ht.size

	// Cria nova tabela com o dobro do tamanho
	ht.size = ht.size * 2
	ht.buckets = make([]*Node, ht.size)
	ht.count = 0 // Será recalculado durante a reinserção

	// Reinsere todos os elementos na nova tabela
	for _, head := range oldBuckets {
		current := head
		for current != nil {
			next := current.next

			// Calcula novo índice
			newIndex := ht.hash(current.key)

			// Reinsere o nó na nova posição
			current.next = ht.buckets[newIndex]
			ht.buckets[newIndex] = current
			ht.count++

			current = next
		}
	}

	fmt.Printf("✅ Redimensionamento concluído. Fator de carga: %.2f -> %.2f\n",
		float64(ht.count)/float64(oldSize), ht.LoadFactor())
}

// Keys retorna todas as chaves
func (ht *OptimizedHashTable) Keys() []string {
	keys := make([]string, 0, ht.count)

	for _, head := range ht.buckets {
		current := head
		for current != nil {
			keys = append(keys, current.key)
			current = current.next
		}
	}

	return keys
}

// Values retorna todos os valores
func (ht *OptimizedHashTable) Values() []interface{} {
	values := make([]interface{}, 0, ht.count)

	for _, head := range ht.buckets {
		current := head
		for current != nil {
			values = append(values, current.value)
			current = current.next
		}
	}

	return values
}

// GetStats retorna estatísticas da tabela hash
func (ht *OptimizedHashTable) GetStats() map[string]interface{} {
	emptyBuckets := 0
	maxChainLength := 0
	totalChainLength := 0
	chainLengths := make([]int, 0)

	for _, head := range ht.buckets {
		if head == nil {
			emptyBuckets++
			chainLengths = append(chainLengths, 0)
		} else {
			length := 0
			current := head
			for current != nil {
				length++
				current = current.next
			}
			chainLengths = append(chainLengths, length)
			totalChainLength += length
			if length > maxChainLength {
				maxChainLength = length
			}
		}
	}

	avgChainLength := float64(totalChainLength) / float64(ht.size-emptyBuckets)
	if ht.size == emptyBuckets {
		avgChainLength = 0
	}

	return map[string]interface{}{
		"total_buckets":    ht.size,
		"used_buckets":     ht.size - emptyBuckets,
		"empty_buckets":    emptyBuckets,
		"total_elements":   ht.count,
		"load_factor":      ht.LoadFactor(),
		"max_chain_length": maxChainLength,
		"avg_chain_length": avgChainLength,
		"chain_lengths":    chainLengths,
	}
}

// Display exibe o conteúdo e estatísticas da tabela hash
func (ht *OptimizedHashTable) Display() {
	fmt.Println("\n=== Estado da Tabela Hash Otimizada ===")

	stats := ht.GetStats()
	fmt.Printf("📊 Estatísticas:\n")
	fmt.Printf("  Total de buckets: %d\n", stats["total_buckets"])
	fmt.Printf("  Buckets utilizados: %d\n", stats["used_buckets"])
	fmt.Printf("  Buckets vazios: %d\n", stats["empty_buckets"])
	fmt.Printf("  Total de elementos: %d\n", stats["total_elements"])
	fmt.Printf("  Fator de carga: %.3f\n", stats["load_factor"])
	fmt.Printf("  Maior cadeia: %d elementos\n", stats["max_chain_length"])
	fmt.Printf("  Cadeia média: %.2f elementos\n", stats["avg_chain_length"])

	fmt.Printf("\n📦 Conteúdo dos buckets:\n")
	for i, head := range ht.buckets {
		if head != nil {
			fmt.Printf("  Bucket %d: ", i)
			current := head
			for current != nil {
				fmt.Printf("('%s':%v)", current.key, current.value)
				if current.next != nil {
					fmt.Print(" -> ")
				}
				current = current.next
			}
			fmt.Println()
		}
	}
	fmt.Println()
}

// Demonstração de performance
func (ht *OptimizedHashTable) BenchmarkOperations() {
	fmt.Println("🚀 Teste de Performance:")

	// Insere muitos elementos para forçar redimensionamentos
	testData := []struct{ key, value string }{
		{"user1", "Alice"}, {"user2", "Bob"}, {"user3", "Charlie"},
		{"product1", "Laptop"}, {"product2", "Mouse"}, {"product3", "Keyboard"},
		{"order1", "Pending"}, {"order2", "Shipped"}, {"order3", "Delivered"},
		{"session1", "Active"}, {"session2", "Expired"}, {"session3", "New"},
	}

	fmt.Printf("Inserindo %d elementos...\n", len(testData))
	for _, data := range testData {
		ht.Put(data.key, data.value)
	}

	ht.Display()
}

// Exemplo de uso
func main() {
	fmt.Println("=== Tabela Hash - Versão Otimizada ===")

	// Cria tabela hash otimizada com tamanho inicial pequeno
	ht := NewOptimizedHashTable(4)

	fmt.Println("Criada tabela hash otimizada com 4 buckets iniciais")
	ht.Display()

	// Demonstra funcionamento básico
	fmt.Println("📝 Operações básicas:")
	ht.Put("nome", "Maria")
	ht.Put("idade", 30)
	ht.Put("profissao", "Engenheira")
	ht.Put("cidade", "Rio de Janeiro")

	ht.Display()

	// Força redimensionamento adicionando mais elementos
	fmt.Println("➕ Adicionando mais elementos (força redimensionamento):")
	ht.Put("pais", "Brasil")
	ht.Put("empresa", "TechCorp")
	ht.Put("salario", 8500.50)

	ht.Display()

	// Demonstra operações
	fmt.Println("🔍 Testando operações:")
	if value, found := ht.Get("nome"); found {
		fmt.Printf("✅ nome: %v\n", value)
	}

	fmt.Printf("🗑️  Removendo 'idade': %t\n", ht.Delete("idade"))
	fmt.Printf("🔍 'idade' ainda existe: %t\n", ht.Contains("idade"))

	// Mostra todas as chaves
	fmt.Printf("🔑 Todas as chaves: %v\n", ht.Keys())

	// Teste de performance
	fmt.Println("\n==================================================")
	ht.BenchmarkOperations()

	fmt.Println("=== Otimizações Implementadas ===")
	fmt.Println("✅ Função hash FNV-1a (distribuição uniforme)")
	fmt.Println("✅ Redimensionamento automático (evita degradação)")
	fmt.Println("✅ Contador de elementos O(1)")
	fmt.Println("✅ Suporte a qualquer tipo de valor")
	fmt.Println("✅ Estatísticas detalhadas de performance")
	fmt.Println("✅ Gerenciamento de fator de carga")
}
