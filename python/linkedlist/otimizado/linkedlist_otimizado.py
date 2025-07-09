"""
Implementação Otimizada de Lista Ligada
======================================

Esta implementação inclui várias otimizações e funcionalidades avançadas:
- Cache do último nó acessado para buscas sequenciais
- Tail pointer para inserções no final em O(1)
- Suporte a iteradores Python
- Métodos otimizados para operações comuns
- Lista duplamente ligada opcional

Características desta versão:
- Performance otimizada para casos comuns
- Interface Pythônica com suporte a operadores
- Métodos de conveniência adicionais
- Estatísticas de performance opcionais

@author matheussricardoo
@version 2.0
@since Julho 2025
"""

from typing import Any, Optional, Iterator, List as ListType

class No:
    """
    Classe que representa um nó da lista ligada.
    """
    
    def __init__(self, dados: Any, proximo: Optional['No'] = None):
        """
        Inicializa um nó.
        
        Args:
            dados: Dados a serem armazenados no nó
            proximo: Referência para o próximo nó
        """
        self.dados = dados
        self.proximo = proximo
        
    def __repr__(self) -> str:
        return f"No({self.dados})"

class NoDuplo:
    """
    Classe que representa um nó de lista duplamente ligada.
    """
    
    def __init__(self, dados: Any, proximo: Optional['NoDuplo'] = None, 
                 anterior: Optional['NoDuplo'] = None):
        """
        Inicializa um nó duplo.
        
        Args:
            dados: Dados a serem armazenados no nó
            proximo: Referência para o próximo nó
            anterior: Referência para o nó anterior
        """
        self.dados = dados
        self.proximo = proximo
        self.anterior = anterior
        
    def __repr__(self) -> str:
        return f"NoDuplo({self.dados})"

class ListaLigadaOtimizada:
    """
    Lista ligada simples com otimizações de performance.
    """
    
    def __init__(self):
        """
        Inicializa uma lista ligada vazia.
        """
        self.cabeca = None
        self.cauda = None  # Otimização: ponteiro para o final
        self.tamanho = 0
        
        # Cache para otimizar buscas sequenciais
        self._cache_no = None
        self._cache_indice = -1
        
        # Estatísticas opcionais
        self.estatisticas_ativas = False
        self.total_acessos = 0
        self.cache_hits = 0
        
    def _invalidar_cache(self) -> None:
        """Invalida o cache quando a lista é modificada."""
        self._cache_no = None
        self._cache_indice = -1
        
    def _atualizar_cache(self, no: No, indice: int) -> None:
        """Atualiza o cache com o nó acessado."""
        self._cache_no = no
        self._cache_indice = indice
        
    def _buscar_no_otimizado(self, indice: int) -> No:
        """
        Busca um nó por índice com otimizações de cache.
        
        Args:
            indice: Índice do nó a ser buscado
            
        Returns:
            Nó encontrado
            
        Raises:
            IndexError: Se o índice estiver fora dos limites
        """
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora dos limites da lista")
            
        self.total_acessos += 1
        
        # Verifica se pode usar o cache
        if (self._cache_no is not None and 
            self._cache_indice != -1 and 
            self._cache_indice <= indice):
            
            # Continua a partir do cache
            no_atual = self._cache_no
            i = self._cache_indice
            self.cache_hits += 1
            
        else:
            # Busca a partir do início
            no_atual = self.cabeca
            i = 0
            
        # Avança até o índice desejado
        while i < indice:
            no_atual = no_atual.proximo
            i += 1
            
        # Atualiza o cache
        self._atualizar_cache(no_atual, indice)
        
        return no_atual
        
    def inserir_inicio(self, dados: Any) -> None:
        """
        Insere um elemento no início da lista. O(1)
        
        Args:
            dados: Dados a serem inseridos
        """
        novo_no = No(dados, self.cabeca)
        self.cabeca = novo_no
        
        # Se a lista estava vazia, atualiza a cauda
        if self.cauda is None:
            self.cauda = novo_no
            
        self.tamanho += 1
        self._invalidar_cache()
        
    def inserir_fim(self, dados: Any) -> None:
        """
        Insere um elemento no final da lista. O(1) com ponteiro de cauda.
        
        Args:
            dados: Dados a serem inseridos
        """
        novo_no = No(dados)
        
        if self.cauda is None:
            # Lista vazia
            self.cabeca = self.cauda = novo_no
        else:
            # Lista não-vazia
            self.cauda.proximo = novo_no
            self.cauda = novo_no
            
        self.tamanho += 1
        
    def inserir_posicao(self, indice: int, dados: Any) -> None:
        """
        Insere um elemento em uma posição específica.
        
        Args:
            indice: Posição onde inserir (0-based)
            dados: Dados a serem inseridos
            
        Raises:
            IndexError: Se o índice estiver fora dos limites
        """
        if indice < 0 or indice > self.tamanho:
            raise IndexError("Índice fora dos limites para inserção")
            
        if indice == 0:
            self.inserir_inicio(dados)
        elif indice == self.tamanho:
            self.inserir_fim(dados)
        else:
            # Busca o nó anterior à posição
            no_anterior = self._buscar_no_otimizado(indice - 1)
            novo_no = No(dados, no_anterior.proximo)
            no_anterior.proximo = novo_no
            self.tamanho += 1
            self._invalidar_cache()
            
    def remover_inicio(self) -> Any:
        """
        Remove e retorna o primeiro elemento da lista. O(1)
        
        Returns:
            Dados do elemento removido
            
        Raises:
            IndexError: Se a lista estiver vazia
        """
        if self.cabeca is None:
            raise IndexError("Não é possível remover de uma lista vazia")
            
        dados = self.cabeca.dados
        self.cabeca = self.cabeca.proximo
        
        # Se a lista ficou vazia, atualiza a cauda
        if self.cabeca is None:
            self.cauda = None
            
        self.tamanho -= 1
        self._invalidar_cache()
        
        return dados
        
    def remover_fim(self) -> Any:
        """
        Remove e retorna o último elemento da lista. O(n)
        
        Returns:
            Dados do elemento removido
            
        Raises:
            IndexError: Se a lista estiver vazia
        """
        if self.cabeca is None:
            raise IndexError("Não é possível remover de uma lista vazia")
            
        if self.cabeca == self.cauda:
            # Apenas um elemento
            dados = self.cabeca.dados
            self.cabeca = self.cauda = None
            self.tamanho = 0
            self._invalidar_cache()
            return dados
            
        # Busca o penúltimo nó
        no_atual = self.cabeca
        while no_atual.proximo != self.cauda:
            no_atual = no_atual.proximo
            
        dados = self.cauda.dados
        self.cauda = no_atual
        self.cauda.proximo = None
        self.tamanho -= 1
        self._invalidar_cache()
        
        return dados
        
    def remover_posicao(self, indice: int) -> Any:
        """
        Remove e retorna o elemento de uma posição específica.
        
        Args:
            indice: Posição do elemento a ser removido
            
        Returns:
            Dados do elemento removido
            
        Raises:
            IndexError: Se o índice estiver fora dos limites
        """
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora dos limites da lista")
            
        if indice == 0:
            return self.remover_inicio()
        elif indice == self.tamanho - 1:
            return self.remover_fim()
        else:
            # Busca o nó anterior ao que será removido
            no_anterior = self._buscar_no_otimizado(indice - 1)
            no_a_remover = no_anterior.proximo
            no_anterior.proximo = no_a_remover.proximo
            self.tamanho -= 1
            self._invalidar_cache()
            
            return no_a_remover.dados
            
    def buscar(self, dados: Any) -> Optional[int]:
        """
        Busca um elemento na lista e retorna seu índice.
        
        Args:
            dados: Dados a serem buscados
            
        Returns:
            Índice do elemento ou None se não encontrado
        """
        no_atual = self.cabeca
        indice = 0
        
        while no_atual is not None:
            if no_atual.dados == dados:
                # Atualiza o cache com o nó encontrado
                self._atualizar_cache(no_atual, indice)
                return indice
            no_atual = no_atual.proximo
            indice += 1
            
        return None
        
    def obter(self, indice: int) -> Any:
        """
        Obtém o elemento de uma posição específica.
        
        Args:
            indice: Posição do elemento
            
        Returns:
            Dados do elemento
            
        Raises:
            IndexError: Se o índice estiver fora dos limites
        """
        no = self._buscar_no_otimizado(indice)
        return no.dados
        
    def definir(self, indice: int, dados: Any) -> None:
        """
        Define o valor de um elemento em uma posição específica.
        
        Args:
            indice: Posição do elemento
            dados: Novos dados
            
        Raises:
            IndexError: Se o índice estiver fora dos limites
        """
        no = self._buscar_no_otimizado(indice)
        no.dados = dados
        
    def esta_vazia(self) -> bool:
        """
        Verifica se a lista está vazia.
        
        Returns:
            True se a lista estiver vazia
        """
        return self.cabeca is None
        
    def obter_tamanho(self) -> int:
        """
        Retorna o tamanho da lista.
        
        Returns:
            Número de elementos na lista
        """
        return self.tamanho
        
    def reverter(self) -> None:
        """
        Reverte a ordem dos elementos na lista. O(n)
        """
        if self.cabeca is None or self.cabeca.proximo is None:
            return  # Lista vazia ou com um elemento
            
        # Troca cabeca e cauda
        self.cauda = self.cabeca
        
        anterior = None
        atual = self.cabeca
        
        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
            
        self.cabeca = anterior
        self._invalidar_cache()
        
    def concatenar(self, outra_lista: 'ListaLigadaOtimizada') -> None:
        """
        Concatena outra lista ao final desta lista.
        
        Args:
            outra_lista: Lista a ser concatenada
        """
        if outra_lista.esta_vazia():
            return
            
        if self.esta_vazia():
            self.cabeca = outra_lista.cabeca
            self.cauda = outra_lista.cauda
        else:
            self.cauda.proximo = outra_lista.cabeca
            self.cauda = outra_lista.cauda
            
        self.tamanho += outra_lista.tamanho
        self._invalidar_cache()
        
    def para_lista(self) -> ListType[Any]:
        """
        Converte para uma lista Python padrão.
        
        Returns:
            Lista Python com os elementos
        """
        resultado = []
        no_atual = self.cabeca
        
        while no_atual is not None:
            resultado.append(no_atual.dados)
            no_atual = no_atual.proximo
            
        return resultado
        
    def obter_estatisticas(self) -> dict:
        """
        Retorna estatísticas de performance da lista.
        
        Returns:
            Dicionário com estatísticas
        """
        cache_rate = 0
        if self.total_acessos > 0:
            cache_rate = (self.cache_hits / self.total_acessos) * 100
            
        return {
            "tamanho": self.tamanho,
            "total_acessos": self.total_acessos,
            "cache_hits": self.cache_hits,
            "cache_hit_rate": round(cache_rate, 2)
        }
        
    def limpar_estatisticas(self) -> None:
        """Limpa as estatísticas de performance."""
        self.total_acessos = 0
        self.cache_hits = 0
        
    def __len__(self) -> int:
        """Suporte ao operador len()."""
        return self.tamanho
        
    def __getitem__(self, indice: int) -> Any:
        """Suporte ao operador []."""
        return self.obter(indice)
        
    def __setitem__(self, indice: int, dados: Any) -> None:
        """Suporte ao operador [] para atribuição."""
        self.definir(indice, dados)
        
    def __iter__(self) -> Iterator[Any]:
        """Suporte à iteração Python."""
        no_atual = self.cabeca
        while no_atual is not None:
            yield no_atual.dados
            no_atual = no_atual.proximo
            
    def __str__(self) -> str:
        """Representação string da lista."""
        elementos = " -> ".join(str(dado) for dado in self)
        return f"[{elementos}]" if elementos else "[]"
        
    def __repr__(self) -> str:
        """Representação detalhada da lista."""
        return f"ListaLigadaOtimizada({self.para_lista()})"


class ListaDuplamenteLigada:
    """
    Lista duplamente ligada com operações otimizadas.
    """
    
    def __init__(self):
        """Inicializa uma lista duplamente ligada vazia."""
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        
    def inserir_inicio(self, dados: Any) -> None:
        """Insere no início. O(1)"""
        novo_no = NoDuplo(dados, self.cabeca)
        
        if self.cabeca is not None:
            self.cabeca.anterior = novo_no
        else:
            self.cauda = novo_no
            
        self.cabeca = novo_no
        self.tamanho += 1
        
    def inserir_fim(self, dados: Any) -> None:
        """Insere no final. O(1)"""
        novo_no = NoDuplo(dados, None, self.cauda)
        
        if self.cauda is not None:
            self.cauda.proximo = novo_no
        else:
            self.cabeca = novo_no
            
        self.cauda = novo_no
        self.tamanho += 1
        
    def remover_inicio(self) -> Any:
        """Remove do início. O(1)"""
        if self.cabeca is None:
            raise IndexError("Lista vazia")
            
        dados = self.cabeca.dados
        self.cabeca = self.cabeca.proximo
        
        if self.cabeca is not None:
            self.cabeca.anterior = None
        else:
            self.cauda = None
            
        self.tamanho -= 1
        return dados
        
    def remover_fim(self) -> Any:
        """Remove do final. O(1)"""
        if self.cauda is None:
            raise IndexError("Lista vazia")
            
        dados = self.cauda.dados
        self.cauda = self.cauda.anterior
        
        if self.cauda is not None:
            self.cauda.proximo = None
        else:
            self.cabeca = None
            
        self.tamanho -= 1
        return dados
        
    def __len__(self) -> int:
        return self.tamanho
        
    def __iter__(self) -> Iterator[Any]:
        no_atual = self.cabeca
        while no_atual is not None:
            yield no_atual.dados
            no_atual = no_atual.proximo
            
    def __str__(self) -> str:
        elementos = " <-> ".join(str(dado) for dado in self)
        return f"[{elementos}]" if elementos else "[]"


def exemplo_lista_otimizada():
    """Demonstra as funcionalidades da lista otimizada."""
    print("=== Lista Ligada Otimizada ===\n")
    
    lista = ListaLigadaOtimizada()
    
    # Inserções
    print("Inserindo elementos...")
    for i in range(5):
        lista.inserir_fim(f"item_{i}")
        
    print(f"Lista: {lista}")
    print(f"Tamanho: {len(lista)}")
    
    # Acessos sequenciais (para demonstrar cache)
    print("\nAcessos sequenciais (demonstra cache):")
    for i in range(5):
        for j in range(i, 5):
            valor = lista[j]
            print(f"  lista[{j}] = {valor}")
            
    stats = lista.obter_estatisticas()
    print("\nEstatísticas de cache:")
    print(f"  Total de acessos: {stats['total_acessos']}")
    print(f"  Cache hits: {stats['cache_hits']}")
    print(f"  Taxa de acerto: {stats['cache_hit_rate']}%")
    
    # Operações avançadas
    print(f"\nRemoção do início: {lista.remover_inicio()}")
    print(f"Lista após remoção: {lista}")
    
    lista.reverter()
    print(f"Lista revertida: {lista}")


def exemplo_lista_dupla():
    """Demonstra a lista duplamente ligada."""
    print("\n" + "="*50)
    print("=== Lista Duplamente Ligada ===")
    print("="*50 + "\n")
    
    lista = ListaDuplamenteLigada()
    
    # Inserções
    for i in range(5):
        lista.inserir_fim(f"elemento_{i}")
        
    print(f"Lista: {lista}")
    
    # Remoções otimizadas
    print(f"Removido do início: {lista.remover_inicio()}")
    print(f"Removido do fim: {lista.remover_fim()}")
    print(f"Lista final: {lista}")


def comparacao_performance():
    """Compara performance entre versões."""
    print("\n" + "="*50)
    print("=== Comparação de Performance ===")
    print("="*50)
    
    import time
    
    # Teste com muitos elementos
    n = 1000
    
    print(f"\nTeste com {n} elementos:")
    
    # Lista otimizada
    lista_otim = ListaLigadaOtimizada()
    
    inicio = time.time()
    for i in range(n):
        lista_otim.inserir_fim(i)
    tempo_insercao = time.time() - inicio
    
    inicio = time.time()
    for i in range(0, n, 10):  # Acessa 10% dos elementos
        _ = lista_otim[i]
    tempo_acesso = time.time() - inicio
    
    print("Lista Otimizada:")
    print(f"  Inserção: {tempo_insercao:.4f}s")
    print(f"  Acesso: {tempo_acesso:.4f}s")
    
    stats = lista_otim.obter_estatisticas()
    print(f"  Cache hit rate: {stats['cache_hit_rate']}%")


if __name__ == "__main__":
    exemplo_lista_otimizada()
    exemplo_lista_dupla()
    comparacao_performance()
