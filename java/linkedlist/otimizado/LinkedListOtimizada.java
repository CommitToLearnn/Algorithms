package linkedlist.otimizado;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Implementação otimizada de uma Lista Ligada
 * Melhorias incluídas:
 * - Referência para o último nó (tail) para inserções O(1) no final
 * - Implementação de Iterator para iteração eficiente
 * - Métodos otimizados para diferentes tipos de inserção/remoção
 * - Coleta de estatísticas de performance
 * - Implementação de Iterable para uso com for-each
 */
public class LinkedListOtimizada<T> implements Iterable<T> {
    private No<T> head;
    private No<T> tail;
    private int tamanho;
    private EstatisticasPerformance estatisticas;
    
    public LinkedListOtimizada() {
        this.head = null;
        this.tail = null;
        this.tamanho = 0;
        this.estatisticas = new EstatisticasPerformance();
    }
    
    /**
     * Adiciona um elemento no início da lista - O(1)
     */
    public void adicionarInicio(T elemento) {
        long inicio = System.nanoTime();
        
        No<T> novoNo = new No<>(elemento);
        
        if (head == null) {
            head = tail = novoNo;
        } else {
            novoNo.proximo = head;
            head = novoNo;
        }
        
        tamanho++;
        estatisticas.registrarOperacao("adicionarInicio", System.nanoTime() - inicio);
    }
    
    /**
     * Adiciona um elemento no final da lista - O(1)
     */
    public void adicionarFinal(T elemento) {
        long inicio = System.nanoTime();
        
        No<T> novoNo = new No<>(elemento);
        
        if (tail == null) {
            head = tail = novoNo;
        } else {
            tail.proximo = novoNo;
            tail = novoNo;
        }
        
        tamanho++;
        estatisticas.registrarOperacao("adicionarFinal", System.nanoTime() - inicio);
    }
    
    /**
     * Adiciona um elemento em uma posição específica - O(n)
     */
    public void adicionarPosicao(int indice, T elemento) {
        if (indice < 0 || indice > tamanho) {
            throw new IndexOutOfBoundsException("Índice inválido: " + indice);
        }
        
        if (indice == 0) {
            adicionarInicio(elemento);
            return;
        }
        
        if (indice == tamanho) {
            adicionarFinal(elemento);
            return;
        }
        
        long inicio = System.nanoTime();
        
        No<T> novoNo = new No<>(elemento);
        No<T> atual = head;
        
        for (int i = 0; i < indice - 1; i++) {
            atual = atual.proximo;
        }
        
        novoNo.proximo = atual.proximo;
        atual.proximo = novoNo;
        tamanho++;
        
        estatisticas.registrarOperacao("adicionarPosicao", System.nanoTime() - inicio);
    }
    
    /**
     * Remove o primeiro elemento da lista - O(1)
     */
    public T removerInicio() {
        if (head == null) {
            throw new NoSuchElementException("Lista vazia");
        }
        
        long inicio = System.nanoTime();
        
        T elemento = head.elemento;
        head = head.proximo;
        
        if (head == null) {
            tail = null;
        }
        
        tamanho--;
        estatisticas.registrarOperacao("removerInicio", System.nanoTime() - inicio);
        return elemento;
    }
    
    /**
     * Remove o último elemento da lista - O(n)
     */
    public T removerFinal() {
        if (tail == null) {
            throw new NoSuchElementException("Lista vazia");
        }
        
        long inicio = System.nanoTime();
        
        if (head == tail) {
            T elemento = head.elemento;
            head = tail = null;
            tamanho--;
            estatisticas.registrarOperacao("removerFinal", System.nanoTime() - inicio);
            return elemento;
        }
        
        No<T> atual = head;
        while (atual.proximo != tail) {
            atual = atual.proximo;
        }
        
        T elemento = tail.elemento;
        atual.proximo = null;
        tail = atual;
        tamanho--;
        
        estatisticas.registrarOperacao("removerFinal", System.nanoTime() - inicio);
        return elemento;
    }
    
    /**
     * Remove elemento em uma posição específica - O(n)
     */
    public T removerPosicao(int indice) {
        if (indice < 0 || indice >= tamanho) {
            throw new IndexOutOfBoundsException("Índice inválido: " + indice);
        }
        
        if (indice == 0) {
            return removerInicio();
        }
        
        if (indice == tamanho - 1) {
            return removerFinal();
        }
        
        long inicio = System.nanoTime();
        
        No<T> atual = head;
        for (int i = 0; i < indice - 1; i++) {
            atual = atual.proximo;
        }
        
        T elemento = atual.proximo.elemento;
        atual.proximo = atual.proximo.proximo;
        tamanho--;
        
        estatisticas.registrarOperacao("removerPosicao", System.nanoTime() - inicio);
        return elemento;
    }
    
    /**
     * Remove a primeira ocorrência de um elemento - O(n)
     */
    public boolean remover(T elemento) {
        if (head == null) {
            return false;
        }
        
        long inicio = System.nanoTime();
        
        // Se é o primeiro elemento
        if (head.elemento.equals(elemento)) {
            removerInicio();
            return true;
        }
        
        No<T> atual = head;
        while (atual.proximo != null) {
            if (atual.proximo.elemento.equals(elemento)) {
                No<T> noRemover = atual.proximo;
                atual.proximo = noRemover.proximo;
                
                if (noRemover == tail) {
                    tail = atual;
                }
                
                tamanho--;
                estatisticas.registrarOperacao("remover", System.nanoTime() - inicio);
                return true;
            }
            atual = atual.proximo;
        }
        
        estatisticas.registrarOperacao("remover", System.nanoTime() - inicio);
        return false;
    }
    
    /**
     * Busca um elemento na lista - O(n)
     */
    public boolean contem(T elemento) {
        long inicio = System.nanoTime();
        
        No<T> atual = head;
        while (atual != null) {
            if (atual.elemento.equals(elemento)) {
                estatisticas.registrarOperacao("contem", System.nanoTime() - inicio);
                return true;
            }
            atual = atual.proximo;
        }
        
        estatisticas.registrarOperacao("contem", System.nanoTime() - inicio);
        return false;
    }
    
    /**
     * Busca o índice de um elemento - O(n)
     */
    public int indiceDe(T elemento) {
        long inicio = System.nanoTime();
        
        No<T> atual = head;
        int indice = 0;
        
        while (atual != null) {
            if (atual.elemento.equals(elemento)) {
                estatisticas.registrarOperacao("indiceDe", System.nanoTime() - inicio);
                return indice;
            }
            atual = atual.proximo;
            indice++;
        }
        
        estatisticas.registrarOperacao("indiceDe", System.nanoTime() - inicio);
        return -1;
    }
    
    /**
     * Obtém elemento em uma posição específica - O(n)
     */
    public T obter(int indice) {
        if (indice < 0 || indice >= tamanho) {
            throw new IndexOutOfBoundsException("Índice inválido: " + indice);
        }
        
        long inicio = System.nanoTime();
        
        No<T> atual = head;
        for (int i = 0; i < indice; i++) {
            atual = atual.proximo;
        }
        
        estatisticas.registrarOperacao("obter", System.nanoTime() - inicio);
        return atual.elemento;
    }
    
    /**
     * Obtém o primeiro elemento - O(1)
     */
    public T obterPrimeiro() {
        if (head == null) {
            throw new NoSuchElementException("Lista vazia");
        }
        return head.elemento;
    }
    
    /**
     * Obtém o último elemento - O(1)
     */
    public T obterUltimo() {
        if (tail == null) {
            throw new NoSuchElementException("Lista vazia");
        }
        return tail.elemento;
    }
    
    /**
     * Limpa a lista - O(1)
     */
    public void limpar() {
        head = null;
        tail = null;
        tamanho = 0;
        estatisticas = new EstatisticasPerformance();
    }
    
    /**
     * Verifica se a lista está vazia - O(1)
     */
    public boolean estaVazia() {
        return tamanho == 0;
    }
    
    /**
     * Retorna o tamanho da lista - O(1)
     */
    public int tamanho() {
        return tamanho;
    }
    
    /**
     * Converte a lista para array - O(n)
     */
    public Object[] paraArray() {
        Object[] array = new Object[tamanho];
        No<T> atual = head;
        
        for (int i = 0; i < tamanho; i++) {
            array[i] = atual.elemento;
            atual = atual.proximo;
        }
        
        return array;
    }
    
    /**
     * Retorna estatísticas de performance
     */
    public EstatisticasPerformance getEstatisticas() {
        return estatisticas;
    }
    
    /**
     * Implementação do Iterator para permitir for-each
     */
    @Override
    public Iterator<T> iterator() {
        return new LinkedListIterator();
    }
    
    /**
     * Classe interna para representar um nó
     */
    private static class No<T> {
        T elemento;
        No<T> proximo;
        
        No(T elemento) {
            this.elemento = elemento;
            this.proximo = null;
        }
    }
    
    /**
     * Implementação do Iterator
     */
    private class LinkedListIterator implements Iterator<T> {
        private No<T> atual = head;
        
        @Override
        public boolean hasNext() {
            return atual != null;
        }
        
        @Override
        public T next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            
            T elemento = atual.elemento;
            atual = atual.proximo;
            return elemento;
        }
    }
    
    /**
     * Representação textual da lista
     */
    @Override
    public String toString() {
        if (estaVazia()) {
            return "[]";
        }
        
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        
        No<T> atual = head;
        while (atual != null) {
            sb.append(atual.elemento);
            if (atual.proximo != null) {
                sb.append(", ");
            }
            atual = atual.proximo;
        }
        
        sb.append("]");
        return sb.toString();
    }
}
