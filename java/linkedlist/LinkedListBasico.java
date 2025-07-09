/**
 * Lista Ligada Básica - Implementação Educacional em Java
 * =======================================================
 * 
 * Esta implementação demonstra uma estrutura de dados linear dinâmica
 * com operações básicas bem documentadas e explicadas.
 * 
 * Características:
 * - Implementação simples e didática
 * - Operações básicas com visualização
 * - Análise de complexidade detalhada
 * - Comentários explicativos extensivos
 * - Demonstração prática de uso
 * 
 * @author matheussricardoo
 * @version 1.0
 * @since Julho 2025
 */

package linkedlist;

public class LinkedListBasico {
    
    // Classe para representar um nó da lista ligada
    static class No {
        int dado;        // Dados armazenados no nó
        No proximo;      // Referência para o próximo nó
        
        public No(int dado) {
            this.dado = dado;
            this.proximo = null;
        }
        
        @Override
        public String toString() {
            return "[" + dado + "]";
        }
    }
    
    private No cabeca; // Primeiro nó da lista
    private int tamanho;
    
    // Construtor - cria lista vazia
    public LinkedListBasico() {
        this.cabeca = null;
        this.tamanho = 0;
    }
    
    // Verifica se a lista está vazia
    public boolean isEmpty() {
        return cabeca == null;
    }
    
    // Retorna o tamanho da lista
    public int size() {
        return tamanho;
    }
    
    // Adiciona elemento no início da lista
    // Complexidade: O(1)
    public void addFirst(int dado) {
        System.out.println("Adicionando " + dado + " no início");
        
        No novoNo = new No(dado);
        novoNo.proximo = cabeca;
        cabeca = novoNo;
        tamanho++;
        
        System.out.println("  → Elemento adicionado. Tamanho atual: " + tamanho);
    }
    
    // Adiciona elemento no final da lista
    // Complexidade: O(n)
    public void addLast(int dado) {
        System.out.println("Adicionando " + dado + " no final");
        
        No novoNo = new No(dado);
        
        if (cabeca == null) {
            cabeca = novoNo;
        } else {
            No atual = cabeca;
            while (atual.proximo != null) {
                atual = atual.proximo;
            }
            atual.proximo = novoNo;
        }
        tamanho++;
        
        System.out.println("  → Elemento adicionado. Tamanho atual: " + tamanho);
    }
    
    // Adiciona elemento em uma posição específica
    // Complexidade: O(n)
    public void add(int indice, int dado) {
        if (indice < 0 || indice > tamanho) {
            System.out.println("Erro: Índice " + indice + " inválido (tamanho: " + tamanho + ")");
            return;
        }
        
        if (indice == 0) {
            addFirst(dado);
            return;
        }
        
        System.out.println("Adicionando " + dado + " na posição " + indice);
        
        No novoNo = new No(dado);
        No atual = cabeca;
        
        // Navega até a posição anterior ao índice
        for (int i = 0; i < indice - 1; i++) {
            atual = atual.proximo;
        }
        
        novoNo.proximo = atual.proximo;
        atual.proximo = novoNo;
        tamanho++;
        
        System.out.println("  → Elemento adicionado. Tamanho atual: " + tamanho);
    }
    
    // Remove o primeiro elemento
    // Complexidade: O(1)
    public boolean removeFirst() {
        System.out.println("Removendo primeiro elemento");
        
        if (cabeca == null) {
            System.out.println("  → Lista vazia, nada para remover");
            return false;
        }
        
        int dadoRemovido = cabeca.dado;
        cabeca = cabeca.proximo;
        tamanho--;
        
        System.out.println("  → Removido: " + dadoRemovido + ". Tamanho atual: " + tamanho);
        return true;
    }
    
    // Remove elemento por valor
    // Complexidade: O(n)
    public boolean remove(int dado) {
        System.out.println("Removendo elemento: " + dado);
        
        if (cabeca == null) {
            System.out.println("  → Lista vazia");
            return false;
        }
        
        // Se o elemento a ser removido é o primeiro
        if (cabeca.dado == dado) {
            cabeca = cabeca.proximo;
            tamanho--;
            System.out.println("  → Elemento removido do início. Tamanho atual: " + tamanho);
            return true;
        }
        
        // Procura o elemento na lista
        No atual = cabeca;
        while (atual.proximo != null && atual.proximo.dado != dado) {
            atual = atual.proximo;
        }
        
        if (atual.proximo != null) {
            atual.proximo = atual.proximo.proximo;
            tamanho--;
            System.out.println("  → Elemento removido. Tamanho atual: " + tamanho);
            return true;
        }
        
        System.out.println("  → Elemento não encontrado");
        return false;
    }
    
    // Remove elemento por índice
    // Complexidade: O(n)
    public boolean removeAt(int indice) {
        if (indice < 0 || indice >= tamanho) {
            System.out.println("Erro: Índice " + indice + " inválido (tamanho: " + tamanho + ")");
            return false;
        }
        
        if (indice == 0) {
            return removeFirst();
        }
        
        System.out.println("Removendo elemento na posição " + indice);
        
        No atual = cabeca;
        for (int i = 0; i < indice - 1; i++) {
            atual = atual.proximo;
        }
        
        int dadoRemovido = atual.proximo.dado;
        atual.proximo = atual.proximo.proximo;
        tamanho--;
        
        System.out.println("  → Removido: " + dadoRemovido + ". Tamanho atual: " + tamanho);
        return true;
    }
    
    // Busca um elemento
    // Complexidade: O(n)
    public boolean contains(int dado) {
        No atual = cabeca;
        int posicao = 0;
        
        while (atual != null) {
            if (atual.dado == dado) {
                System.out.println("Elemento " + dado + " encontrado na posição " + posicao);
                return true;
            }
            atual = atual.proximo;
            posicao++;
        }
        
        System.out.println("Elemento " + dado + " não encontrado");
        return false;
    }
    
    // Retorna elemento por índice
    // Complexidade: O(n)
    public Integer get(int indice) {
        if (indice < 0 || indice >= tamanho) {
            System.out.println("Erro: Índice " + indice + " inválido (tamanho: " + tamanho + ")");
            return null;
        }
        
        No atual = cabeca;
        for (int i = 0; i < indice; i++) {
            atual = atual.proximo;
        }
        
        System.out.println("Elemento na posição " + indice + ": " + atual.dado);
        return atual.dado;
    }
    
    // Encontra o índice de um elemento
    // Complexidade: O(n)
    public int indexOf(int dado) {
        No atual = cabeca;
        int indice = 0;
        
        while (atual != null) {
            if (atual.dado == dado) {
                return indice;
            }
            atual = atual.proximo;
            indice++;
        }
        
        return -1; // Não encontrado
    }
    
    // Limpa a lista
    public void clear() {
        System.out.println("Limpando a lista");
        cabeca = null;
        tamanho = 0;
        System.out.println("  → Lista limpa");
    }
    
    // Exibe a lista
    public void display() {
        System.out.print("Lista: ");
        
        if (cabeca == null) {
            System.out.println("vazia");
            return;
        }
        
        No atual = cabeca;
        while (atual != null) {
            System.out.print(atual.dado);
            if (atual.proximo != null) {
                System.out.print(" → ");
            }
            atual = atual.proximo;
        }
        System.out.println(" (tamanho: " + tamanho + ")");
    }
    
    // Converte para array
    public int[] toArray() {
        int[] array = new int[tamanho];
        No atual = cabeca;
        int i = 0;
        
        while (atual != null) {
            array[i++] = atual.dado;
            atual = atual.proximo;
        }
        
        return array;
    }
    
    // Método principal - exemplo de uso e demonstração
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════╗");
        System.out.println("║      Lista Ligada Básica - Java       ║");
        System.out.println("║      Implementação Educacional        ║");
        System.out.println("╚════════════════════════════════════════╝");
        System.out.println();

        LinkedListBasico lista = new LinkedListBasico();

        // Teste 1: Adicionar elementos
        System.out.println("1️⃣  ADICIONANDO ELEMENTOS:");
        System.out.println("=" .repeat(50));
        lista.addFirst(10);
        lista.addFirst(20);
        lista.addLast(30);
        lista.addLast(40);
        lista.display();

        System.out.println();

        // Teste 2: Inserir em posição específica
        System.out.println("2️⃣  INSERINDO EM POSIÇÕES ESPECÍFICAS:");
        System.out.println("=" .repeat(50));
        lista.add(2, 25); // Insere 25 na posição 2
        lista.add(0, 5);  // Insere 5 no início
        lista.display();

        System.out.println();

        // Teste 3: Buscar elementos
        System.out.println("3️⃣  BUSCANDO ELEMENTOS:");
        System.out.println("=" .repeat(50));
        lista.contains(25);
        lista.contains(100);
        lista.get(3);

        System.out.println();

        // Teste 4: Remover elementos
        System.out.println("4️⃣  REMOVENDO ELEMENTOS:");
        System.out.println("=" .repeat(50));
        lista.remove(25);
        lista.removeAt(0);
        lista.removeFirst();
        lista.display();

        System.out.println();

        // Teste 5: Operações adicionais
        System.out.println("5️⃣  OPERAÇÕES ADICIONAIS:");
        System.out.println("=" .repeat(50));
        System.out.println("📍 Índice do elemento 30: " + lista.indexOf(30));
        System.out.println("📏 Tamanho da lista: " + lista.size());
        System.out.println("📭 Lista está vazia? " + lista.isEmpty());

        // Demonstrar array conversion
        int[] array = lista.toArray();
        System.out.print("📦 Array convertido: [");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i < array.length - 1) System.out.print(", ");
        }
        System.out.println("]");

        System.out.println();

        // Limpar lista
        System.out.println("6️⃣  LIMPANDO LISTA:");
        System.out.println("=" .repeat(50));
        lista.clear();
        lista.display();

        System.out.println();
        System.out.println("📊 Análise de Complexidade:");
        System.out.println("   • Inserção no início: O(1) - acesso direto ao head");
        System.out.println("   • Inserção no final: O(n) - precisa percorrer toda lista");
        System.out.println("   • Busca por valor: O(n) - busca linear");
        System.out.println("   • Remoção por valor: O(n) - busca + remoção");
        System.out.println("   • Acesso por índice: O(n) - navegação sequencial");
        
        System.out.println();
        System.out.println("💡 Vantagens:");
        System.out.println("   • Tamanho dinâmico (cresce conforme necessário)");
        System.out.println("   • Inserção/remoção eficiente no início");
        System.out.println("   • Uso eficiente de memória (aloca conforme precisa)");
        System.out.println("   • Não precisa declarar tamanho máximo");
        
        System.out.println();
        System.out.println("⚠️  Desvantagens:");
        System.out.println("   • Acesso sequencial (não permite acesso aleatório)");
        System.out.println("   • Overhead de memória para ponteiros");
        System.out.println("   • Cache locality ruim (dados espalhados na memória)");
        System.out.println("   • Não permite busca binária");
        
        System.out.println();
        System.out.println("🚀 Quando Usar:");
        System.out.println("   • Tamanho da coleção varia muito");
        System.out.println("   • Inserções/remoções frequentes no início");
        System.out.println("   • Não precisa de acesso aleatório");
        System.out.println("   • Implementação de pilhas, filas, etc.");
    }
}
