/**
 * Hash Table Básica - Implementação Educacional em Java
 * =====================================================
 * 
 * Esta implementação demonstra uma estrutura de dados hash table
 * com tratamento de colisões por encadeamento (chaining).
 * 
 * Características:
 * - Implementação simples e didática
 * - Tratamento de colisões por encadeamento
 * - Função hash básica (soma dos valores ASCII)
 * - Visualização das operações
 * - Análise de complexidade incluída
 * 
 * @author matheussricardoo
 * @version 1.0
 * @since Julho 2025
 */

package hashtable;

import java.util.ArrayList;
import java.util.List;

public class HashTableBasico {
    
    // Classe para representar uma entrada da hash table
    static class Entrada {
        String chave;
        String valor;
        Entrada proxima; // Para tratamento de colisões por encadeamento
        
        public Entrada(String chave, String valor) {
            this.chave = chave;
            this.valor = valor;
            this.proxima = null;
        }
        
        @Override
        public String toString() {
            return chave + ":" + valor;
        }
    }
    
    private Entrada[] tabela;
    private int tamanho;
    private int numeroElementos;
    
    // Construtor - cria hash table com tamanho padrão
    public HashTableBasico() {
        this.tamanho = 10; // Tamanho inicial
        this.tabela = new Entrada[tamanho];
        this.numeroElementos = 0;
    }
    
    // Construtor com tamanho customizado
    public HashTableBasico(int tamanho) {
        this.tamanho = tamanho;
        this.tabela = new Entrada[tamanho];
        this.numeroElementos = 0;
    }
    
    // Função hash simples - soma dos valores ASCII
    private int hash(String chave) {
        int soma = 0;
        for (char c : chave.toCharArray()) {
            soma += (int) c;
        }
        return soma % tamanho;
    }
    
    // Adiciona ou atualiza um elemento
    public void put(String chave, String valor) {
        int indice = hash(chave);
        System.out.println("Inserindo: " + chave + " = " + valor + " (índice: " + indice + ")");
        
        // Se a posição estiver vazia
        if (tabela[indice] == null) {
            tabela[indice] = new Entrada(chave, valor);
            numeroElementos++;
            System.out.println("  → Inserido diretamente na posição " + indice);
        } else {
            // Trata colisão por encadeamento
            Entrada atual = tabela[indice];
            
            // Verifica se a chave já existe
            while (atual != null) {
                if (atual.chave.equals(chave)) {
                    atual.valor = valor; // Atualiza valor existente
                    System.out.println("  → Valor atualizado para chave existente");
                    return;
                }
                if (atual.proxima == null) break;
                atual = atual.proxima;
            }
            
            // Adiciona nova entrada no final da cadeia
            atual.proxima = new Entrada(chave, valor);
            numeroElementos++;
            System.out.println("  → Colisão! Adicionado no final da cadeia");
        }
        
        mostrarEstatisticas();
    }
    
    // Busca um elemento
    public String get(String chave) {
        int indice = hash(chave);
        System.out.println("Buscando: " + chave + " (índice: " + indice + ")");
        
        Entrada atual = tabela[indice];
        int passos = 0;
        
        while (atual != null) {
            passos++;
            if (atual.chave.equals(chave)) {
                System.out.println("  → Encontrado em " + passos + " passo(s): " + atual.valor);
                return atual.valor;
            }
            atual = atual.proxima;
        }
        
        System.out.println("  → Não encontrado após " + passos + " passo(s)");
        return null;
    }
    
    // Remove um elemento
    public boolean remove(String chave) {
        int indice = hash(chave);
        System.out.println("Removendo: " + chave + " (índice: " + indice + ")");
        
        Entrada atual = tabela[indice];
        Entrada anterior = null;
        
        while (atual != null) {
            if (atual.chave.equals(chave)) {
                if (anterior == null) {
                    // Remove o primeiro elemento da cadeia
                    tabela[indice] = atual.proxima;
                } else {
                    // Remove elemento do meio/final da cadeia
                    anterior.proxima = atual.proxima;
                }
                numeroElementos--;
                System.out.println("  → Elemento removido com sucesso");
                return true;
            }
            anterior = atual;
            atual = atual.proxima;
        }
        
        System.out.println("  → Elemento não encontrado");
        return false;
    }
    
    // Verifica se uma chave existe
    public boolean containsKey(String chave) {
        return get(chave) != null;
    }
    
    // Retorna todas as chaves
    public List<String> getKeys() {
        List<String> chaves = new ArrayList<>();
        
        for (int i = 0; i < tamanho; i++) {
            Entrada atual = tabela[i];
            while (atual != null) {
                chaves.add(atual.chave);
                atual = atual.proxima;
            }
        }
        
        return chaves;
    }
    
    // Mostra o conteúdo da hash table
    public void display() {
        System.out.println("\n=== CONTEÚDO DA HASH TABLE ===");
        for (int i = 0; i < tamanho; i++) {
            System.out.print("Índice " + i + ": ");
            
            if (tabela[i] == null) {
                System.out.println("vazio");
            } else {
                Entrada atual = tabela[i];
                boolean primeiro = true;
                while (atual != null) {
                    if (!primeiro) System.out.print(" → ");
                    System.out.print("[" + atual.chave + ":" + atual.valor + "]");
                    atual = atual.proxima;
                    primeiro = false;
                }
                System.out.println();
            }
        }
        System.out.println("================================\n");
    }
    
    // Mostra estatísticas
    private void mostrarEstatisticas() {
        double fatorCarga = (double) numeroElementos / tamanho;
        System.out.println("  Elementos: " + numeroElementos + "/" + tamanho + 
                         " (fator de carga: " + String.format("%.2f", fatorCarga) + ")");
    }
    
    // Calcula o comprimento médio das cadeias
    public double comprimentoMedioCadeias() {
        int cadeias = 0;
        int comprimentoTotal = 0;
        
        for (int i = 0; i < tamanho; i++) {
            if (tabela[i] != null) {
                cadeias++;
                Entrada atual = tabela[i];
                int comprimento = 0;
                while (atual != null) {
                    comprimento++;
                    atual = atual.proxima;
                }
                comprimentoTotal += comprimento;
            }
        }
        
        return cadeias > 0 ? (double) comprimentoTotal / cadeias : 0;
    }
    
    // Método principal - exemplo de uso e demonstração
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════╗");
        System.out.println("║       Hash Table Básica - Java        ║");
        System.out.println("║      Implementação Educacional        ║");
        System.out.println("╚════════════════════════════════════════╝");
        System.out.println();
        
        // Tamanho pequeno para demonstrar colisões
        HashTableBasico ht = new HashTableBasico(7);
        
        System.out.println("📊 Hash Table criada com tamanho 7 (pequeno para demonstrar colisões)");
        System.out.println();
        
        // Adiciona elementos
        System.out.println("1️⃣  INSERINDO ELEMENTOS:");
        System.out.println("=" .repeat(40));
        ht.put("nome", "João Silva");
        ht.put("idade", "28");
        ht.put("cidade", "São Paulo");
        ht.put("profissao", "Engenheiro");
        ht.put("email", "joao.silva@email.com");

        ht.display();

        // Busca elementos
        System.out.println("2️⃣  BUSCANDO ELEMENTOS:");
        System.out.println("=" .repeat(40));
        ht.get("nome");
        ht.get("idade");
        ht.get("telefone"); // Não existe

        System.out.println();

        // Atualiza elemento
        System.out.println("3️⃣  ATUALIZANDO ELEMENTO:");
        System.out.println("=" .repeat(40));
        ht.put("idade", "29"); // Atualiza idade existente

        System.out.println();

        // Remove elemento
        System.out.println("4️⃣  REMOVENDO ELEMENTO:");
        System.out.println("=" .repeat(40));
        ht.remove("email");

        ht.display();

        // Estatísticas finais
        System.out.println("5️⃣  ESTATÍSTICAS FINAIS:");
        System.out.println("=" .repeat(40));
        System.out.println("📏 Comprimento médio das cadeias: " + 
                         String.format("%.2f", ht.comprimentoMedioCadeias()));
        System.out.println("🔑 Todas as chaves: " + ht.getKeys());

        System.out.println();
        System.out.println("📊 Análise de Complexidade (Caso Médio):");
        System.out.println("   • Inserção: O(1)");
        System.out.println("   • Busca: O(1)");
        System.out.println("   • Remoção: O(1)");
        
        System.out.println();
        System.out.println("⚠️  Análise de Complexidade (Pior Caso):");
        System.out.println("   • Inserção: O(n) - todas as chaves na mesma posição");
        System.out.println("   • Busca: O(n) - todas as chaves na mesma posição");
        System.out.println("   • Remoção: O(n) - todas as chaves na mesma posição");
        
        System.out.println();
        System.out.println("💡 Fatores que Afetam Performance:");
        System.out.println("   • Qualidade da função hash");
        System.out.println("   • Fator de carga (load factor)");
        System.out.println("   • Tamanho da tabela");
        System.out.println("   • Distribuição dos dados");
        
        System.out.println();
        System.out.println("🚀 Possíveis Melhorias:");
        System.out.println("   • Função hash mais sofisticada");
        System.out.println("   • Redimensionamento dinâmico");
        System.out.println("   • Open addressing (ao invés de chaining)");
        System.out.println("   • Cuckoo hashing para garantir O(1)");
    }
}
