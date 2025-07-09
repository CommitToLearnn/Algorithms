"""
Implementação Básica de Lista Duplamente Ligada em Python
=========================================================

Esta implementação demonstra os conceitos fundamentais de uma lista duplamente ligada,
onde cada nó possui ponteiros para o próximo E para o anterior elemento.

Características desta versão:
- Implementação didática e comentada
- Operações fundamentais claramente explicadas
- Navegação bidirecional (frente e trás)
- Inserções e remoções eficientes em ambas as extremidades
- Código otimizado para aprendizado

Vantagens da Lista Duplamente Ligada:
- Navegação em ambas as direções
- Remoção eficiente O(1) quando se tem a referência do nó
- Inserção eficiente em qualquer posição conhecida
- Implementação mais fácil de operações como reversão

@author matheussricardoo
@version 1.0
@since Julho 2025
"""

from typing import Any, Optional, Iterator


class NoDuplo:
    """
    Classe que representa um nó de uma lista duplamente ligada.
    
    Cada nó contém:
    - dados: o valor armazenado
    - proximo: referência para o próximo nó
    - anterior: referência para o nó anterior
    """
    
    def __init__(self, dados: Any, proximo: Optional['NoDuplo'] = None, 
                 anterior: Optional['NoDuplo'] = None):
        """
        Inicializa um nó da lista duplamente ligada.
        
        Args:
            dados: Valor a ser armazenado no nó
            proximo: Referência para o próximo nó (opcional)
            anterior: Referência para o nó anterior (opcional)
        """
        self.dados = dados
        self.proximo = proximo
        self.anterior = anterior
    
    def __str__(self) -> str:
        """Representação em string do nó."""
        return f"NoDuplo({self.dados})"
    
    def __repr__(self) -> str:
        """Representação detalhada do nó."""
        return f"NoDuplo(dados={self.dados}, anterior={self.anterior.dados if self.anterior else None}, proximo={self.proximo.dados if self.proximo else None})"


class ListaDuplamenteLigada:
    """
    Implementação básica de uma Lista Duplamente Ligada.
    
    Esta estrutura permite navegação eficiente em ambas as direções
    e operações O(1) nas extremidades.
    """
    
    def __init__(self):
        """
        Inicializa uma lista duplamente ligada vazia.
        
        A lista mantém referências para:
        - cabeca: primeiro nó da lista
        - cauda: último nó da lista
        - tamanho: número de elementos
        """
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
    
    def esta_vazia(self) -> bool:
        """
        Verifica se a lista está vazia.
        
        Returns:
            bool: True se a lista estiver vazia, False caso contrário
        """
        return self.cabeca is None
    
    def obter_tamanho(self) -> int:
        """
        Retorna o número de elementos na lista.
        
        Returns:
            int: Tamanho da lista
        """
        return self.tamanho
    
    def inserir_inicio(self, dados: Any) -> None:
        """
        Insere um elemento no início da lista. Complexidade: O(1)
        
        Args:
            dados: Valor a ser inserido
        """
        print(f"🔹 Inserindo '{dados}' no início da lista")
        
        # Cria o novo nó
        novo_no = NoDuplo(dados)
        
        if self.esta_vazia():
            # Lista vazia: novo nó é tanto cabeca quanto cauda
            self.cabeca = self.cauda = novo_no
            print(f"  ✅ Lista estava vazia. '{dados}' é agora cabeca e cauda")
        else:
            # Lista não-vazia: ajusta os ponteiros
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no
            print(f"  ✅ '{dados}' inserido no início. Nova cabeca definida")
        
        self.tamanho += 1
        print(f"  📊 Tamanho atual: {self.tamanho}")
    
    def inserir_fim(self, dados: Any) -> None:
        """
        Insere um elemento no final da lista. Complexidade: O(1)
        
        Args:
            dados: Valor a ser inserido
        """
        print(f"🔸 Inserindo '{dados}' no final da lista")
        
        # Cria o novo nó
        novo_no = NoDuplo(dados)
        
        if self.esta_vazia():
            # Lista vazia: novo nó é tanto cabeca quanto cauda
            self.cabeca = self.cauda = novo_no
            print(f"  ✅ Lista estava vazia. '{dados}' é agora cabeca e cauda")
        else:
            # Lista não-vazia: ajusta os ponteiros
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no
            print(f"  ✅ '{dados}' inserido no final. Nova cauda definida")
        
        self.tamanho += 1
        print(f"  📊 Tamanho atual: {self.tamanho}")
    
    def inserir_posicao(self, indice: int, dados: Any) -> None:
        """
        Insere um elemento em uma posição específica.
        
        Args:
            indice: Posição onde inserir (0-based)
            dados: Valor a ser inserido
            
        Raises:
            IndexError: Se o índice estiver fora dos limites
        """
        if indice < 0 or indice > self.tamanho:
            raise IndexError(f"Índice {indice} fora dos limites [0, {self.tamanho}]")
        
        print(f"🔷 Inserindo '{dados}' na posição {indice}")
        
        # Casos especiais
        if indice == 0:
            self.inserir_inicio(dados)
            return
        elif indice == self.tamanho:
            self.inserir_fim(dados)
            return
        
        # Inserção no meio: busca otimizada
        if indice <= self.tamanho // 2:
            # Busca a partir do início
            print("  🔍 Buscando a partir do início (mais próximo)")
            no_atual = self.cabeca
            for _ in range(indice):
                no_atual = no_atual.proximo
        else:
            # Busca a partir do final
            print("  🔍 Buscando a partir do final (mais próximo)")
            no_atual = self.cauda
            for _ in range(self.tamanho - 1, indice, -1):
                no_atual = no_atual.anterior
        
        # Cria e insere o novo nó
        novo_no = NoDuplo(dados, no_atual, no_atual.anterior)
        no_atual.anterior.proximo = novo_no
        no_atual.anterior = novo_no
        
        self.tamanho += 1
        print(f"  ✅ '{dados}' inserido na posição {indice}")
        print(f"  📊 Tamanho atual: {self.tamanho}")
    
    def remover_inicio(self) -> Any:
        """
        Remove e retorna o primeiro elemento da lista. Complexidade: O(1)
        
        Returns:
            Any: Dados do elemento removido
            
        Raises:
            IndexError: Se a lista estiver vazia
        """
        if self.esta_vazia():
            raise IndexError("Não é possível remover de uma lista vazia")
        
        dados = self.cabeca.dados
        print(f"🗑️  Removendo '{dados}' do início da lista")
        
        if self.tamanho == 1:
            # Único elemento: lista fica vazia
            self.cabeca = self.cauda = None
            print("  ✅ Lista ficou vazia após remoção")
        else:
            # Múltiplos elementos: ajusta ponteiros
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
            print(f"  ✅ Nova cabeca: '{self.cabeca.dados}'")
        
        self.tamanho -= 1
        print(f"  📊 Tamanho atual: {self.tamanho}")
        
        return dados
    
    def remover_fim(self) -> Any:
        """
        Remove e retorna o último elemento da lista. Complexidade: O(1)
        
        Returns:
            Any: Dados do elemento removido
            
        Raises:
            IndexError: Se a lista estiver vazia
        """
        if self.esta_vazia():
            raise IndexError("Não é possível remover de uma lista vazia")
        
        dados = self.cauda.dados
        print(f"🗑️  Removendo '{dados}' do final da lista")
        
        if self.tamanho == 1:
            # Único elemento: lista fica vazia
            self.cabeca = self.cauda = None
            print("  ✅ Lista ficou vazia após remoção")
        else:
            # Múltiplos elementos: ajusta ponteiros
            self.cauda = self.cauda.anterior
            self.cauda.proximo = None
            print(f"  ✅ Nova cauda: '{self.cauda.dados}'")
        
        self.tamanho -= 1
        print(f"  📊 Tamanho atual: {self.tamanho}")
        
        return dados
    
    def remover_valor(self, dados: Any) -> bool:
        """
        Remove a primeira ocorrência de um valor específico.
        
        Args:
            dados: Valor a ser removido
            
        Returns:
            bool: True se o elemento foi removido, False se não encontrado
        """
        print(f"🔍 Procurando '{dados}' para remoção")
        
        no_atual = self.cabeca
        
        while no_atual is not None:
            if no_atual.dados == dados:
                print(f"  ✅ Elemento '{dados}' encontrado")
                
                # Ajusta ponteiros do nó anterior
                if no_atual.anterior is not None:
                    no_atual.anterior.proximo = no_atual.proximo
                else:
                    # É o primeiro nó
                    self.cabeca = no_atual.proximo
                
                # Ajusta ponteiros do nó posterior
                if no_atual.proximo is not None:
                    no_atual.proximo.anterior = no_atual.anterior
                else:
                    # É o último nó
                    self.cauda = no_atual.anterior
                
                self.tamanho -= 1
                print(f"  🗑️  '{dados}' removido com sucesso")
                print(f"  📊 Tamanho atual: {self.tamanho}")
                return True
            
            no_atual = no_atual.proximo
        
        print(f"  ❌ Elemento '{dados}' não encontrado")
        return False
    
    def buscar(self, dados: Any) -> Optional[int]:
        """
        Busca um elemento na lista e retorna seu índice.
        
        Args:
            dados: Valor a ser buscado
            
        Returns:
            Optional[int]: Índice do elemento ou None se não encontrado
        """
        print(f"🔍 Buscando '{dados}' na lista")
        
        no_atual = self.cabeca
        indice = 0
        
        while no_atual is not None:
            if no_atual.dados == dados:
                print(f"  ✅ '{dados}' encontrado na posição {indice}")
                return indice
            
            no_atual = no_atual.proximo
            indice += 1
        
        print(f"  ❌ '{dados}' não encontrado na lista")
        return None
    
    def obter(self, indice: int) -> Any:
        """
        Obtém o elemento de uma posição específica.
        
        Args:
            indice: Posição do elemento (0-based)
            
        Returns:
            Any: Dados do elemento
            
        Raises:
            IndexError: Se o índice estiver fora dos limites
        """
        if indice < 0 or indice >= self.tamanho:
            raise IndexError(f"Índice {indice} fora dos limites [0, {self.tamanho-1}]")
        
        print(f"🔍 Obtendo elemento da posição {indice}")
        
        # Busca otimizada: escolhe a direção mais próxima
        if indice <= self.tamanho // 2:
            # Busca a partir do início
            print("  ➡️  Buscando a partir do início")
            no_atual = self.cabeca
            for _ in range(indice):
                no_atual = no_atual.proximo
        else:
            # Busca a partir do final
            print("  ⬅️  Buscando a partir do final")
            no_atual = self.cauda
            for _ in range(self.tamanho - 1, indice, -1):
                no_atual = no_atual.anterior
        
        print(f"  ✅ Elemento encontrado: '{no_atual.dados}'")
        return no_atual.dados
    
    def reverter(self) -> None:
        """
        Reverte a ordem dos elementos na lista. Complexidade: O(n)
        """
        if self.tamanho <= 1:
            print("📋 Lista vazia ou com um elemento - não há o que reverter")
            return
        
        print("🔄 Revertendo a lista...")
        
        no_atual = self.cabeca
        
        # Troca as referências anterior/proximo de cada nó
        while no_atual is not None:
            # Troca anterior e proximo
            no_atual.anterior, no_atual.proximo = no_atual.proximo, no_atual.anterior
            # Move para o "próximo" (que era o anterior)
            no_atual = no_atual.anterior
        
        # Troca cabeca e cauda
        self.cabeca, self.cauda = self.cauda, self.cabeca
        
        print("  ✅ Lista revertida com sucesso")
    
    def para_lista_frente(self) -> list:
        """
        Converte a lista duplamente ligada para uma lista Python (do início ao fim).
        
        Returns:
            list: Lista Python com os elementos
        """
        resultado = []
        no_atual = self.cabeca
        
        while no_atual is not None:
            resultado.append(no_atual.dados)
            no_atual = no_atual.proximo
        
        return resultado
    
    def para_lista_tras(self) -> list:
        """
        Converte a lista duplamente ligada para uma lista Python (do fim ao início).
        
        Returns:
            list: Lista Python com os elementos em ordem reversa
        """
        resultado = []
        no_atual = self.cauda
        
        while no_atual is not None:
            resultado.append(no_atual.dados)
            no_atual = no_atual.anterior
        
        return resultado
    
    def limpar(self) -> None:
        """
        Remove todos os elementos da lista.
        """
        print("🧹 Limpando a lista...")
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        print("  ✅ Lista limpa com sucesso")
    
    def __len__(self) -> int:
        """Suporte ao operador len()."""
        return self.tamanho
    
    def __iter__(self) -> Iterator[Any]:
        """Suporte à iteração Python (do início ao fim)."""
        no_atual = self.cabeca
        while no_atual is not None:
            yield no_atual.dados
            no_atual = no_atual.proximo
    
    def iter_reverso(self) -> Iterator[Any]:
        """Iterador que percorre a lista do fim ao início."""
        no_atual = self.cauda
        while no_atual is not None:
            yield no_atual.dados
            no_atual = no_atual.anterior
    
    def __str__(self) -> str:
        """Representação em string da lista."""
        if self.esta_vazia():
            return "Lista Duplamente Ligada: vazia"
        
        elementos = " <-> ".join(str(dados) for dados in self)
        return f"Lista Duplamente Ligada: {elementos}"
    
    def __repr__(self) -> str:
        """Representação detalhada da lista."""
        return f"ListaDuplamenteLigada({self.para_lista_frente()})"
    
    def imprimir_detalhado(self) -> None:
        """
        Imprime uma representação detalhada da lista mostrando as conexões.
        """
        print("\n" + "="*60)
        print("📋 ESTRUTURA DETALHADA DA LISTA DUPLAMENTE LIGADA")
        print("="*60)
        
        if self.esta_vazia():
            print("Lista vazia")
            return
        
        print(f"📊 Tamanho: {self.tamanho}")
        print(f"🟢 Cabeça: {self.cabeca.dados}")
        print(f"🔴 Cauda: {self.cauda.dados}")
        print()
        
        no_atual = self.cabeca
        posicao = 0
        
        while no_atual is not None:
            anterior = no_atual.anterior.dados if no_atual.anterior else "None"
            proximo = no_atual.proximo.dados if no_atual.proximo else "None"
            
            print(f"Posição {posicao}: [{anterior}] ← [{no_atual.dados}] → [{proximo}]")
            
            no_atual = no_atual.proximo
            posicao += 1
        
        print("="*60)


def demonstracao_basica():
    """
    Demonstra as funcionalidades básicas da lista duplamente ligada.
    """
    print("╔════════════════════════════════════════╗")
    print("║  Lista Duplamente Ligada - Básica     ║")
    print("║       Implementação Educacional       ║")
    print("╚════════════════════════════════════════╝")
    print()
    
    # Criação da lista
    lista = ListaDuplamenteLigada()
    print(f"📋 Lista criada: {lista}")
    print()
    
    # Inserções
    print("1️⃣  INSERINDO ELEMENTOS:")
    print("=" * 50)
    lista.inserir_inicio("primeiro")
    lista.inserir_fim("último")
    lista.inserir_inicio("novo_primeiro")
    lista.inserir_fim("novo_último")
    lista.inserir_posicao(2, "meio")
    
    print(f"\n📋 Lista atual: {lista}")
    lista.imprimir_detalhado()
    
    # Buscas
    print("\n2️⃣  BUSCANDO ELEMENTOS:")
    print("=" * 50)
    lista.buscar("meio")
    lista.buscar("inexistente")
    
    print(f"Elemento na posição 2: {lista.obter(2)}")
    print(f"Elemento na posição 0: {lista.obter(0)}")
    print(f"Elemento na posição {len(lista)-1}: {lista.obter(len(lista)-1)}")
    
    # Navegação bidirecional
    print("\n3️⃣  NAVEGAÇÃO BIDIRECIONAL:")
    print("=" * 50)
    print("➡️  Do início ao fim:")
    for i, elemento in enumerate(lista):
        print(f"  Posição {i}: {elemento}")
    
    print("\n⬅️  Do fim ao início:")
    for i, elemento in enumerate(lista.iter_reverso()):
        print(f"  Posição {len(lista)-1-i}: {elemento}")
    
    # Conversões
    print("\n4️⃣  CONVERSÕES PARA LISTA PYTHON:")
    print("=" * 50)
    print(f"Frente para trás: {lista.para_lista_frente()}")
    print(f"Trás para frente: {lista.para_lista_tras()}")
    
    # Remoções
    print("\n5️⃣  REMOVENDO ELEMENTOS:")
    print("=" * 50)
    lista.remover_inicio()
    print(f"Lista após remoção: {lista}")
    
    lista.remover_fim()
    print(f"Lista após remoção: {lista}")
    
    lista.remover_valor("meio")
    print(f"Lista após remoção: {lista}")
    
    # Reversão
    print("\n6️⃣  REVERTENDO A LISTA:")
    print("=" * 50)
    print(f"Lista antes da reversão: {lista}")
    lista.reverter()
    print(f"Lista após reversão: {lista}")
    
    # Estatísticas finais
    print("\n7️⃣  ESTATÍSTICAS FINAIS:")
    print("=" * 50)
    print(f"📏 Tamanho final: {len(lista)}")
    print(f"📭 Lista vazia? {lista.esta_vazia()}")
    
    lista.imprimir_detalhado()


def comparacao_com_lista_simples():
    """
    Compara operações entre lista simples e duplamente ligada.
    """
    print("\n" + "="*60)
    print("📊 COMPARAÇÃO: LISTA SIMPLES vs DUPLAMENTE LIGADA")
    print("="*60)
    
    # Análise de complexidade
    operacoes = [
        ("Inserção no início", "O(1)", "O(1)"),
        ("Inserção no final", "O(n)*", "O(1)"),
        ("Remoção do início", "O(1)", "O(1)"),
        ("Remoção do final", "O(n)", "O(1)"),
        ("Busca por valor", "O(n)", "O(n)"),
        ("Acesso por índice", "O(n)", "O(n/2)**"),
        ("Reversão", "O(n)", "O(n)"),
    ]
    
    print(f"{'Operação':<20} {'Lista Simples':<15} {'Lista Dupla':<15}")
    print("-" * 50)
    for op, simples, dupla in operacoes:
        print(f"{op:<20} {simples:<15} {dupla:<15}")
    
    print("\n* Com tail pointer: O(1)")
    print("** Busca otimizada (direção mais próxima)")
    
    print("\n🎯 QUANDO USAR LISTA DUPLAMENTE LIGADA:")
    vantagens = [
        "Remoções frequentes no final da lista",
        "Navegação bidirecional necessária",
        "Implementação de estruturas como deques",
        "Operações de reversão frequentes",
        "Quando você tem referência direta para os nós"
    ]
    
    for vantagem in vantagens:
        print(f"  ✅ {vantagem}")
    
    print("\n⚠️  DESVANTAGENS:")
    desvantagens = [
        "Maior uso de memória (ponteiro extra por nó)",
        "Maior complexidade de implementação",
        "Ligeiramente mais lenta para operações simples"
    ]
    
    for desvantagem in desvantagens:
        print(f"  ❌ {desvantagem}")


def exemplo_casos_uso():
    """
    Demonstra casos de uso práticos da lista duplamente ligada.
    """
    print("\n" + "="*60)
    print("🎯 CASOS DE USO PRÁTICOS")
    print("="*60)
    
    # Caso 1: Histórico de navegação
    print("\n1️⃣  HISTÓRICO DE NAVEGAÇÃO DE UM NAVEGADOR")
    print("-" * 50)
    
    historico = ListaDuplamenteLigada()
    
    paginas = ["google.com", "github.com", "stackoverflow.com", "python.org"]
    
    print("📱 Navegando pelas páginas:")
    for pagina in paginas:
        historico.inserir_fim(pagina)
        print(f"  Visitou: {pagina}")
    
    print(f"\n📋 Histórico atual: {historico.para_lista_frente()}")
    
    print("\n⬅️  Voltando páginas:")
    while not historico.esta_vazia():
        pagina = historico.remover_fim()
        print(f"  Voltou para: {pagina if historico.cauda else 'página inicial'}")
        if historico.cauda:
            print(f"    Páginas restantes: {historico.para_lista_frente()}")
    
    # Caso 2: Editor de texto com undo/redo
    print("\n2️⃣  SISTEMA DE UNDO/REDO DE EDITOR")
    print("-" * 50)
    
    acoes = ListaDuplamenteLigada()
    
    operacoes = ["digitar 'Hello'", "digitar ' World'", "deletar 'World'", "digitar ' Python'"]
    
    print("✏️  Realizando operações:")
    for operacao in operacoes:
        acoes.inserir_fim(operacao)
        print(f"  Ação: {operacao}")
    
    print(f"\n📝 Histórico de ações: {acoes.para_lista_frente()}")
    
    print("\n↶ Desfazendo operações:")
    for _ in range(2):
        if not acoes.esta_vazia():
            acao = acoes.remover_fim()
            print(f"  Undo: {acao}")
            print(f"    Estado atual: {acoes.para_lista_frente()}")
    
    # Caso 3: Player de música
    print("\n3️⃣  PLAYER DE MÚSICA (PLAYLIST)")
    print("-" * 50)
    
    playlist = ListaDuplamenteLigada()
    
    musicas = ["Song A", "Song B", "Song C", "Song D"]
    
    for musica in musicas:
        playlist.inserir_fim(musica)
    
    print(f"🎵 Playlist: {playlist.para_lista_frente()}")
    
    print("\n⏯️  Navegação na playlist:")
    print("  ▶️  Reprodução normal:")
    for musica in playlist:
        print(f"    🎵 Tocando: {musica}")
    
    print("\n  ◀️  Reprodução reversa:")
    for musica in playlist.iter_reverso():
        print(f"    🎵 Tocando: {musica}")


if __name__ == "__main__":
    demonstracao_basica()
    comparacao_com_lista_simples()
    exemplo_casos_uso()
    
    print("\n" + "="*60)
    print("📚 ANÁLISE DE COMPLEXIDADE RESUMIDA")
    print("="*60)
    print("⚡ Inserção/Remoção nas extremidades: O(1)")
    print("🔍 Busca por valor: O(n)")
    print("📍 Acesso por índice: O(n) - otimizado para O(n/2)")
    print("🔄 Reversão: O(n)")
    print("💾 Espaço extra: O(n) - um ponteiro adicional por nó")
    
    print("\n💡 DICAS DE IMPLEMENTAÇÃO:")
    print("  • Sempre mantenha cabeca e cauda atualizadas")
    print("  • Verifique casos especiais (lista vazia, um elemento)")
    print("  • Use busca bidirecional para otimizar acesso por índice")
    print("  • Teste bem as operações de inserção/remoção no meio")
    print("  • Cuidado com vazamentos de memória em linguagens sem GC")
