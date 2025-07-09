package hashtable.otimizado;

import java.util.ArrayList;
import java.util.List;

/**
 * Implementação otimizada de uma Hash Table
 * Melhorias incluídas:
 * - Função hash mais eficiente
 * - Redimensionamento automático
 * - Resolução de colisões por chaining otimizado
 * - Coleta de estatísticas de performance
 */
public class HashTableOtimizada<K, V> {
    private static final int CAPACIDADE_INICIAL = 16;
    private static final double FATOR_CARGA_MAXIMO = 0.75;
    private static final double FATOR_CARGA_MINIMO = 0.25;
    
    private Entrada<K, V>[] tabela;
    private int tamanho;
    private int capacidade;
    private EstatisticasPerformance estatisticas;
    
    @SuppressWarnings("unchecked")
    public HashTableOtimizada() {
        this.capacidade = CAPACIDADE_INICIAL;
        this.tabela = new Entrada[capacidade];
        this.tamanho = 0;
        this.estatisticas = new EstatisticasPerformance();
    }
    
    @SuppressWarnings("unchecked")
    public HashTableOtimizada(int capacidadeInicial) {
        this.capacidade = Math.max(capacidadeInicial, CAPACIDADE_INICIAL);
        this.tabela = new Entrada[capacidade];
        this.tamanho = 0;
        this.estatisticas = new EstatisticasPerformance();
    }
    
    /**
     * Função hash otimizada usando multiplicação e bit shifting
     */
    private int hash(K chave) {
        if (chave == null) return 0;
        
        int hash = chave.hashCode();
        // Aplica mistura para melhor distribuição
        hash ^= (hash >>> 16);
        return Math.abs(hash % capacidade);
    }
    
    /**
     * Insere ou atualiza um par chave-valor
     */
    public V put(K chave, V valor) {
        long inicio = System.nanoTime();
        
        // Verifica se precisa redimensionar
        if (getFatorCarga() > FATOR_CARGA_MAXIMO) {
            redimensionar(capacidade * 2);
        }
        
        int indice = hash(chave);
        estatisticas.incrementarOperacoes();
        
        Entrada<K, V> entrada = tabela[indice];
        
        // Se não há entrada no índice, cria nova
        if (entrada == null) {
            tabela[indice] = new Entrada<>(chave, valor);
            tamanho++;
            estatisticas.registrarOperacao(System.nanoTime() - inicio, false);
            return null;
        }
        
        // Procura na cadeia
        int colisoes = 0;
        while (entrada != null) {
            if (entrada.chave.equals(chave)) {
                V valorAnterior = entrada.valor;
                entrada.valor = valor;
                estatisticas.registrarOperacao(System.nanoTime() - inicio, colisoes > 0);
                return valorAnterior;
            }
            
            if (entrada.proximo == null) {
                entrada.proximo = new Entrada<>(chave, valor);
                tamanho++;
                estatisticas.registrarOperacao(System.nanoTime() - inicio, true);
                return null;
            }
            
            entrada = entrada.proximo;
            colisoes++;
        }
        
        estatisticas.registrarOperacao(System.nanoTime() - inicio, colisoes > 0);
        return null;
    }
    
    /**
     * Busca um valor pela chave
     */
    public V get(K chave) {
        long inicio = System.nanoTime();
        
        int indice = hash(chave);
        estatisticas.incrementarOperacoes();
        
        Entrada<K, V> entrada = tabela[indice];
        int colisoes = 0;
        
        while (entrada != null) {
            if (entrada.chave.equals(chave)) {
                estatisticas.registrarOperacao(System.nanoTime() - inicio, colisoes > 0);
                return entrada.valor;
            }
            entrada = entrada.proximo;
            colisoes++;
        }
        
        estatisticas.registrarOperacao(System.nanoTime() - inicio, colisoes > 0);
        return null;
    }
    
    /**
     * Remove uma entrada pela chave
     */
    public V remove(K chave) {
        long inicio = System.nanoTime();
        
        int indice = hash(chave);
        estatisticas.incrementarOperacoes();
        
        Entrada<K, V> entrada = tabela[indice];
        Entrada<K, V> anterior = null;
        int colisoes = 0;
        
        while (entrada != null) {
            if (entrada.chave.equals(chave)) {
                V valorRemovido = entrada.valor;
                
                if (anterior == null) {
                    tabela[indice] = entrada.proximo;
                } else {
                    anterior.proximo = entrada.proximo;
                }
                
                tamanho--;
                
                // Verifica se precisa redimensionar para baixo
                if (getFatorCarga() < FATOR_CARGA_MINIMO && capacidade > CAPACIDADE_INICIAL) {
                    redimensionar(capacidade / 2);
                }
                
                estatisticas.registrarOperacao(System.nanoTime() - inicio, colisoes > 0);
                return valorRemovido;
            }
            
            anterior = entrada;
            entrada = entrada.proximo;
            colisoes++;
        }
        
        estatisticas.registrarOperacao(System.nanoTime() - inicio, colisoes > 0);
        return null;
    }
    
    /**
     * Verifica se a tabela contém uma chave
     */
    public boolean containsKey(K chave) {
        return get(chave) != null;
    }
    
    /**
     * Redimensiona a tabela hash
     */
    @SuppressWarnings("unchecked")
    private void redimensionar(int novaCapacidade) {
        Entrada<K, V>[] tabelaAntiga = tabela;
        int capacidadeAntiga = capacidade;
        
        capacidade = novaCapacidade;
        tabela = new Entrada[capacidade];
        tamanho = 0;
        
        // Reinsere todas as entradas
        for (int i = 0; i < capacidadeAntiga; i++) {
            Entrada<K, V> entrada = tabelaAntiga[i];
            while (entrada != null) {
                put(entrada.chave, entrada.valor);
                entrada = entrada.proximo;
            }
        }
        
        estatisticas.registrarRedimensionamento(capacidadeAntiga, capacidade);
    }
    
    /**
     * Retorna o fator de carga atual
     */
    public double getFatorCarga() {
        return (double) tamanho / capacidade;
    }
    
    /**
     * Retorna todas as chaves
     */
    public List<K> getChaves() {
        List<K> chaves = new ArrayList<>();
        for (int i = 0; i < capacidade; i++) {
            Entrada<K, V> entrada = tabela[i];
            while (entrada != null) {
                chaves.add(entrada.chave);
                entrada = entrada.proximo;
            }
        }
        return chaves;
    }
    
    /**
     * Retorna todas as entradas
     */
    public List<EntradaPublica<K, V>> getEntradas() {
        List<EntradaPublica<K, V>> entradas = new ArrayList<>();
        for (int i = 0; i < capacidade; i++) {
            Entrada<K, V> entrada = tabela[i];
            while (entrada != null) {
                entradas.add(new EntradaPublica<>(entrada.chave, entrada.valor));
                entrada = entrada.proximo;
            }
        }
        return entradas;
    }
    
    public int getTamanho() {
        return tamanho;
    }
    
    public int getCapacidade() {
        return capacidade;
    }
    
    public boolean isEmpty() {
        return tamanho == 0;
    }
    
    public EstatisticasPerformance getEstatisticas() {
        return estatisticas;
    }
    
    /**
     * Limpa todas as entradas
     */
    @SuppressWarnings("unchecked")
    public void clear() {
        tabela = new Entrada[CAPACIDADE_INICIAL];
        capacidade = CAPACIDADE_INICIAL;
        tamanho = 0;
        estatisticas = new EstatisticasPerformance();
    }
    
    /**
     * Classe interna para representar uma entrada
     */
    private static class Entrada<K, V> {
        K chave;
        V valor;
        Entrada<K, V> proximo;
        
        Entrada(K chave, V valor) {
            this.chave = chave;
            this.valor = valor;
        }
    }
    
    /**
     * Classe pública para expor entradas
     */
    public static class EntradaPublica<K, V> {
        private final K chave;
        private final V valor;
        
        public EntradaPublica(K chave, V valor) {
            this.chave = chave;
            this.valor = valor;
        }
        
        public K getChave() { return chave; }
        public V getValor() { return valor; }
        
        @Override
        public String toString() {
            return chave + "=" + valor;
        }
    }
}
