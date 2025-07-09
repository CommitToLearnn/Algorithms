package main

import "fmt"

// SimpleHashTable implementa uma tabela hash básica e didática
type SimpleHashTable struct {
	buckets [][]KeyValue // Array de slices para tratar colisões
	size    int          // Tamanho da tabela
}

// KeyValue representa um par chave-valor
type KeyValue struct {
	key   string
	value string // Usando string para simplificar o exemplo
}

// NewSimpleHashTable cria uma nova tabela hash simples
func NewSimpleHashTable(size int) *SimpleHashTable {
	return &SimpleHashTable{
		buckets: make([][]KeyValue, size),
		size:    size,
	}
}

// simpleHash função de hash básica usando soma dos códigos ASCII
// Não é a melhor função, mas é didática e fácil de entender
func (ht *SimpleHashTable) simpleHash(key string) int {
	fmt.Printf("  Calculando hash para '%s': ", key)

	hash := 0
	for i, char := range key {
		hash += int(char)
		fmt.Printf("%c(%d)", char, int(char))
		if i < len(key)-1 {
			fmt.Print("+")
		}
	}

	index := hash % ht.size
	fmt.Printf(" = %d %% %d = %d\n", hash, ht.size, index)

	return index
}

// Put insere um par chave-valor na tabela
// Complexidade média: O(1), pior caso: O(n) se muitas colisões
func (ht *SimpleHashTable) Put(key, value string) {
	fmt.Printf("\n=== Inserindo ('%s', '%s') ===\n", key, value)

	// Calcula o índice usando a função hash
	index := ht.simpleHash(key)

	// Verifica se já existe a chave no bucket
	for i, kv := range ht.buckets[index] {
		if kv.key == key {
			fmt.Printf("  Chave '%s' já existe no bucket %d, atualizando valor\n", key, index)
			ht.buckets[index][i].value = value
			return
		}
	}

	// Adiciona novo par chave-valor
	ht.buckets[index] = append(ht.buckets[index], KeyValue{key, value})
	fmt.Printf("  Adicionado no bucket %d\n", index)

	// Mostra se houve colisão
	if len(ht.buckets[index]) > 1 {
		fmt.Printf("  ⚠️  COLISÃO detectada no bucket %d! Agora tem %d elementos\n",
			index, len(ht.buckets[index]))
	}
}

// Get recupera um valor pela chave
// Complexidade média: O(1), pior caso: O(n)
func (ht *SimpleHashTable) Get(key string) (string, bool) {
	fmt.Printf("\n=== Buscando chave '%s' ===\n", key)

	// Calcula onde a chave deveria estar
	index := ht.simpleHash(key)

	// Procura no bucket correspondente
	fmt.Printf("  Procurando no bucket %d...\n", index)
	for i, kv := range ht.buckets[index] {
		fmt.Printf("  Comparando com elemento %d: '%s'\n", i, kv.key)
		if kv.key == key {
			fmt.Printf("  ✅ Encontrado! Valor: '%s'\n", kv.value)
			return kv.value, true
		}
	}

	fmt.Printf("  ❌ Chave '%s' não encontrada\n", key)
	return "", false
}

// Delete remove um par chave-valor
// Complexidade média: O(1), pior caso: O(n)
func (ht *SimpleHashTable) Delete(key string) bool {
	fmt.Printf("\n=== Removendo chave '%s' ===\n", key)

	index := ht.simpleHash(key)

	for i, kv := range ht.buckets[index] {
		if kv.key == key {
			// Remove o elemento do slice
			ht.buckets[index] = append(ht.buckets[index][:i], ht.buckets[index][i+1:]...)
			fmt.Printf("  ✅ Chave '%s' removida do bucket %d\n", key, index)
			return true
		}
	}

	fmt.Printf("  ❌ Chave '%s' não encontrada para remoção\n", key)
	return false
}

// Contains verifica se uma chave existe
func (ht *SimpleHashTable) Contains(key string) bool {
	_, found := ht.Get(key)
	return found
}

// Size retorna o número total de elementos
func (ht *SimpleHashTable) Size() int {
	count := 0
	for _, bucket := range ht.buckets {
		count += len(bucket)
	}
	return count
}

// LoadFactor calcula o fator de carga (elementos / buckets)
func (ht *SimpleHashTable) LoadFactor() float64 {
	return float64(ht.Size()) / float64(ht.size)
}

// Display mostra o estado atual da tabela hash
func (ht *SimpleHashTable) Display() {
	fmt.Printf("\n=== Estado da Tabela Hash ===\n")
	fmt.Printf("Tamanho da tabela: %d buckets\n", ht.size)
	fmt.Printf("Total de elementos: %d\n", ht.Size())
	fmt.Printf("Fator de carga: %.2f\n\n", ht.LoadFactor())

	for i, bucket := range ht.buckets {
		if len(bucket) > 0 {
			fmt.Printf("Bucket %d (%d elementos): ", i, len(bucket))
			for j, kv := range bucket {
				fmt.Printf("('%s':'%s')", kv.key, kv.value)
				if j < len(bucket)-1 {
					fmt.Print(" -> ")
				}
			}
			fmt.Println()
		} else {
			fmt.Printf("Bucket %d: vazio\n", i)
		}
	}
	fmt.Println()
}

// Exemplo de uso
func main() {
	fmt.Println("=== Tabela Hash - Versão Básica e Didática ===")

	// Cria uma tabela hash pequena para demonstrar colisões
	ht := NewSimpleHashTable(5)

	fmt.Println("Criada tabela hash com 5 buckets")
	ht.Display()

	// Demonstra inserções
	fmt.Println("📝 INSERINDO ELEMENTOS:")
	ht.Put("nome", "João")
	ht.Put("idade", "25")
	ht.Put("city", "SP")     // Pode colidir dependendo do hash
	ht.Put("país", "Brasil") // Pode colidir dependendo do hash

	ht.Display()

	// Demonstra busca
	fmt.Println("\n🔍 BUSCANDO ELEMENTOS:")
	if value, found := ht.Get("nome"); found {
		fmt.Printf("Resultado: nome = %s\n", value)
	}

	if value, found := ht.Get("profissão"); found {
		fmt.Printf("Resultado: profissão = %s\n", value)
	}

	// Demonstra atualização
	fmt.Println("\n🔄 ATUALIZANDO ELEMENTO:")
	ht.Put("idade", "26") // Atualiza valor existente

	ht.Display()

	// Demonstra remoção
	fmt.Println("\n🗑️  REMOVENDO ELEMENTO:")
	ht.Delete("city")

	ht.Display()

	// Explicação final
	fmt.Println("=== Como Funciona ===")
	fmt.Println("1. HASH: Converte chave em índice do array")
	fmt.Println("   - Soma códigos ASCII dos caracteres")
	fmt.Println("   - Aplica módulo pelo tamanho da tabela")
	fmt.Println("2. COLISÕES: Quando duas chaves geram mesmo índice")
	fmt.Println("   - Resolve usando lista dentro do bucket")
	fmt.Println("3. PERFORMANCE: O(1) média, O(n) pior caso")
	fmt.Println("4. FATOR DE CARGA: Elementos/Buckets - idealmente < 0.75")
}
