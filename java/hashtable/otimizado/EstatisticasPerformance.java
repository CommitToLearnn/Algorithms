package hashtable.otimizado;

/**
 * Classe que armazena estatísticas de performance da Hash Table
 */
public class EstatisticasPerformance {
    private int totalOperacoes;
    private int colisoes;
    private int redimensionamentos;
    private double tempoTotalOperacoes; // em nanosegundos
    private int capacidadeMaxima;
    private int capacidadeMinima;
    
    public EstatisticasPerformance() {
        this.totalOperacoes = 0;
        this.colisoes = 0;
        this.redimensionamentos = 0;
        this.tempoTotalOperacoes = 0;
        this.capacidadeMaxima = 0;
        this.capacidadeMinima = Integer.MAX_VALUE;
    }
    
    public void incrementarOperacoes() {
        totalOperacoes++;
    }
    
    public void registrarOperacao(long tempoNanos, boolean houveColisao) {
        tempoTotalOperacoes += tempoNanos;
        if (houveColisao) {
            colisoes++;
        }
        totalOperacoes++;
    }
    
    public void registrarColisao() {
        colisoes++;
    }
    
    public void registrarRedimensionamento(int capacidadeAntiga, int novaCapacidade) {
        redimensionamentos++;
        if (novaCapacidade > capacidadeMaxima) {
            capacidadeMaxima = novaCapacidade;
        }
        if (novaCapacidade < capacidadeMinima) {
            capacidadeMinima = novaCapacidade;
        }
    }
    
    public void adicionarTempo(long tempoNanos) {
        tempoTotalOperacoes += tempoNanos;
    }
    
    // Getters
    public int getTotalOperacoes() { return totalOperacoes; }
    public int getColisoes() { return colisoes; }
    public int getRedimensionamentos() { return redimensionamentos; }
    public double getTempoTotalOperacoes() { return tempoTotalOperacoes; }
    public int getCapacidadeMaxima() { return capacidadeMaxima; }
    public int getCapacidadeMinima() { return capacidadeMinima; }
    
    public double getTempoMedioOperacao() {
        return totalOperacoes > 0 ? tempoTotalOperacoes / totalOperacoes : 0;
    }
    
    public double getTaxaColisoes() {
        return totalOperacoes > 0 ? (double) colisoes / totalOperacoes : 0;
    }
    
    public void reset() {
        totalOperacoes = 0;
        colisoes = 0;
        redimensionamentos = 0;
        tempoTotalOperacoes = 0;
        capacidadeMaxima = 0;
        capacidadeMinima = Integer.MAX_VALUE;
    }
    
    @Override
    public String toString() {
        return String.format(
            "Estatísticas de Performance:\n" +
            "- Total de operações: %d\n" +
            "- Colisões: %d (%.2f%%)\n" +
            "- Redimensionamentos: %d\n" +
            "- Tempo total: %.2f ms\n" +
            "- Tempo médio por operação: %.4f ms\n" +
            "- Capacidade máxima: %d\n" +
            "- Capacidade mínima: %d",
            totalOperacoes,
            colisoes, getTaxaColisoes() * 100,
            redimensionamentos,
            tempoTotalOperacoes / 1_000_000,
            getTempoMedioOperacao() / 1_000_000,
            capacidadeMaxima,
            capacidadeMinima == Integer.MAX_VALUE ? 0 : capacidadeMinima
        );
    }
}
