package linkedlist.otimizado;

/**
 * Classe que armazena estatísticas de performance da LinkedList
 */
public class EstatisticasPerformance {
    private int totalOperacoes;
    private double tempoTotalOperacoes; // em nanosegundos
    private int operacoesPorTipo[];
    private final String[] nomesOperacoes = {
        "adicionarInicio", "adicionarFinal", "adicionarPosicao", 
        "removerInicio", "removerFinal", "removerPosicao", 
        "remover", "contem", "indiceDe", "obter"
    };
    
    public EstatisticasPerformance() {
        this.totalOperacoes = 0;
        this.tempoTotalOperacoes = 0;
        this.operacoesPorTipo = new int[nomesOperacoes.length];
    }
    
    public void registrarOperacao(String tipoOperacao, long tempoNanos) {
        totalOperacoes++;
        tempoTotalOperacoes += tempoNanos;
        
        // Registra por tipo de operação
        for (int i = 0; i < nomesOperacoes.length; i++) {
            if (nomesOperacoes[i].equals(tipoOperacao)) {
                operacoesPorTipo[i]++;
                break;
            }
        }
    }
    
    public void incrementarOperacoes() {
        totalOperacoes++;
    }
    
    public void adicionarTempo(long tempoNanos) {
        tempoTotalOperacoes += tempoNanos;
    }
    
    // Getters
    public int getTotalOperacoes() { return totalOperacoes; }
    public double getTempoTotalOperacoes() { return tempoTotalOperacoes; }
    
    public double getTempoMedioOperacao() {
        return totalOperacoes > 0 ? tempoTotalOperacoes / totalOperacoes : 0;
    }
    
    public int getOperacoesPorTipo(String tipo) {
        for (int i = 0; i < nomesOperacoes.length; i++) {
            if (nomesOperacoes[i].equals(tipo)) {
                return operacoesPorTipo[i];
            }
        }
        return 0;
    }
    
    public void reset() {
        totalOperacoes = 0;
        tempoTotalOperacoes = 0;
        operacoesPorTipo = new int[nomesOperacoes.length];
    }
    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Estatísticas de Performance:\n");
        sb.append(String.format("- Total de operações: %d\n", totalOperacoes));
        sb.append(String.format("- Tempo total: %.2f ms\n", tempoTotalOperacoes / 1_000_000));
        sb.append(String.format("- Tempo médio por operação: %.4f ms\n", getTempoMedioOperacao() / 1_000_000));
        sb.append("- Operações por tipo:\n");
        
        for (int i = 0; i < nomesOperacoes.length; i++) {
            if (operacoesPorTipo[i] > 0) {
                sb.append(String.format("  • %s: %d\n", nomesOperacoes[i], operacoesPorTipo[i]));
            }
        }
        
        return sb.toString();
    }
}