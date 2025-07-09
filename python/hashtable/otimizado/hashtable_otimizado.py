"""
Implementação Otimizada de Hash Table
====================================

Esta implementação incluí várias otimizações como:
- Redimensionamento dinâmico (rehashing)
- Múltiplas estratégias de resolução de colisões
- Estatísticas de performance
- Funções de hash otimizadas

Características desta versão:
- Redimensionamento automático para manter fator de carga baixo
- Múltiplas funções de hash disponíveis
- Suporte a diferentes estratégias de resolução de colisões
- Estatísticas detalhadas de performance

Autor: Algorithms Repository
Data: Julho 2025
"""

from typing import Any, Optional, Tuple, Dict
from enum import Enum

class TipoHash(Enum):
    """Diferentes tipos de função hash disponíveis."""
    DIVISAO = "divisao"
    MULTIPLICACAO = "multiplicacao"
    DJIB2 = "djib2"
    FNV1A = "fnv1a"

class TipoColisao(Enum):
    """Estratégias para resolução de colisões."""
    LINEAR = "linear"
    QUADRATIC = "quadratic"
    DOUBLE_HASH = "double_hash"
    CHAINING = "chaining"

class HashTableOtimizada:
    """
    Hash Table otimizada com múltiplas estratégias e redimensionamento dinâmico.
    """
    
    def __init__(self, capacidade_inicial: int = 16, fator_carga_max: float = 0.75,
                 tipo_hash: TipoHash = TipoHash.DJIB2, 
                 tipo_colisao: TipoColisao = TipoColisao.LINEAR):
        """
        Inicializa a hash table otimizada.
        
        Args:
            capacidade_inicial: Tamanho inicial da tabela
            fator_carga_max: Fator de carga máximo antes do redimensionamento
            tipo_hash: Tipo de função hash a usar
            tipo_colisao: Estratégia de resolução de colisões
        """
        self.capacidade = capacidade_inicial
        self.tamanho = 0
        self.fator_carga_max = fator_carga_max
        self.tipo_hash = tipo_hash
        self.tipo_colisao = tipo_colisao
        
        # Inicializa a estrutura baseada no tipo de colisão
        if tipo_colisao == TipoColisao.CHAINING:
            self.tabela = [[] for _ in range(self.capacidade)]
        else:
            self.tabela = [None] * self.capacidade
            self.deletados = [False] * self.capacidade  # Para lazy deletion
            
        # Estatísticas
        self.colisoes = 0
        self.redimensionamentos = 0
        self.operacoes_busca = 0
        self.total_probes = 0
        
    def _hash_divisao(self, chave: str) -> int:
        """Função hash por divisão (método clássico)."""
        return hash(chave) % self.capacidade
        
    def _hash_multiplicacao(self, chave: str) -> int:
        """Função hash por multiplicação (Knuth)."""
        A = 0.6180339887  # (√5 - 1) / 2
        h = hash(chave)
        return int(self.capacidade * ((h * A) % 1))
        
    def _hash_djib2(self, chave: str) -> int:
        """Função hash djb2 (Daniel J. Bernstein)."""
        hash_value = 5381
        for char in chave:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.capacidade
        
    def _hash_fnv1a(self, chave: str) -> int:
        """Função hash FNV-1a (Fowler-Noll-Vo)."""
        FNV_OFFSET_BASIS = 2166136261
        FNV_PRIME = 16777619
        
        hash_value = FNV_OFFSET_BASIS
        for char in chave:
            hash_value ^= ord(char)
            hash_value *= FNV_PRIME
            hash_value &= 0xFFFFFFFF  # Mantém 32 bits
            
        return hash_value % self.capacidade
        
    def _calcular_hash(self, chave: str) -> int:
        """Calcula o hash baseado no tipo selecionado."""
        if self.tipo_hash == TipoHash.DIVISAO:
            return self._hash_divisao(chave)
        elif self.tipo_hash == TipoHash.MULTIPLICACAO:
            return self._hash_multiplicacao(chave)
        elif self.tipo_hash == TipoHash.DJIB2:
            return self._hash_djib2(chave)
        elif self.tipo_hash == TipoHash.FNV1A:
            return self._hash_fnv1a(chave)
        else:
            return self._hash_divisao(chave)
            
    def _hash_secundario(self, chave: str) -> int:
        """Função hash secundária para double hashing."""
        return 7 - (hash(chave) % 7)  # Número primo menor que capacidade
        
    def _probe_linear(self, indice: int, i: int) -> int:
        """Sondagem linear."""
        return (indice + i) % self.capacidade
        
    def _probe_quadratic(self, indice: int, i: int) -> int:
        """Sondagem quadrática."""
        return (indice + i * i) % self.capacidade
        
    def _probe_double_hash(self, chave: str, indice: int, i: int) -> int:
        """Double hashing."""
        return (indice + i * self._hash_secundario(chave)) % self.capacidade
        
    def _encontrar_posicao(self, chave: str) -> Tuple[int, bool]:
        """
        Encontra a posição de uma chave na tabela.
        
        Returns:
            Tupla (indice, encontrado)
        """
        if self.tipo_colisao == TipoColisao.CHAINING:
            indice = self._calcular_hash(chave)
            return indice, any(item[0] == chave for item in self.tabela[indice])
            
        indice_inicial = self._calcular_hash(chave)
        probes = 0
        
        for i in range(self.capacidade):
            if self.tipo_colisao == TipoColisao.LINEAR:
                indice = self._probe_linear(indice_inicial, i)
            elif self.tipo_colisao == TipoColisao.QUADRATIC:
                indice = self._probe_quadratic(indice_inicial, i)
            else:  # DOUBLE_HASH
                indice = self._probe_double_hash(chave, indice_inicial, i)
                
            probes += 1
            
            # Posição vazia ou deletada
            if self.tabela[indice] is None or self.deletados[indice]:
                self.total_probes += probes
                return indice, False
                
            # Chave encontrada
            if self.tabela[indice][0] == chave:
                self.total_probes += probes
                return indice, True
                
        # Tabela cheia
        self.total_probes += probes
        return -1, False
        
    def _redimensionar(self) -> None:
        """Redimensiona a tabela quando o fator de carga é muito alto."""
        print(f"Redimensionando de {self.capacidade} para {self.capacidade * 2}")
        
        # Salva os dados atuais
        dados_antigos = []
        
        if self.tipo_colisao == TipoColisao.CHAINING:
            for bucket in self.tabela:
                dados_antigos.extend(bucket)
        else:
            for i, item in enumerate(self.tabela):
                if item is not None and not self.deletados[i]:
                    dados_antigos.append(item)
                    
        # Reinicializa com capacidade dobrada
        self.capacidade *= 2
        self.tamanho = 0
        self.redimensionamentos += 1
        
        if self.tipo_colisao == TipoColisao.CHAINING:
            self.tabela = [[] for _ in range(self.capacidade)]
        else:
            self.tabela = [None] * self.capacidade
            self.deletados = [False] * self.capacidade
            
        # Reinsere todos os dados
        for chave, valor in dados_antigos:
            self._inserir_sem_redimensionar(chave, valor)
            
        print(f"Redimensionamento concluído. {len(dados_antigos)} itens reinseridos.")
        
    def _inserir_sem_redimensionar(self, chave: str, valor: Any) -> bool:
        """Insere sem verificar redimensionamento (usado internamente)."""
        if self.tipo_colisao == TipoColisao.CHAINING:
            indice = self._calcular_hash(chave)
            bucket = self.tabela[indice]
            
            # Verifica se já existe
            for i, (k, _) in enumerate(bucket):
                if k == chave:
                    bucket[i] = (chave, valor)
                    return True
                    
            # Adiciona novo item
            bucket.append((chave, valor))
            if len(bucket) > 1:
                self.colisoes += 1
            self.tamanho += 1
            return True
            
        else:  # Open addressing
            indice, encontrado = self._encontrar_posicao(chave)
            
            if indice == -1:
                return False  # Tabela cheia
                
            if encontrado and not self.deletados[indice]:
                # Atualiza valor existente
                self.tabela[indice] = (chave, valor)
                return True
            else:
                # Insere novo valor
                if self.tabela[indice] is not None:
                    self.colisoes += 1
                    
                self.tabela[indice] = (chave, valor)
                self.deletados[indice] = False
                self.tamanho += 1
                return True
                
    def inserir(self, chave: str, valor: Any) -> bool:
        """
        Insere um par chave-valor na hash table.
        
        Args:
            chave: Chave a ser inserida
            valor: Valor associado à chave
            
        Returns:
            True se a inserção foi bem-sucedida
        """
        # Verifica se precisa redimensionar
        fator_carga = self.tamanho / self.capacidade
        if fator_carga >= self.fator_carga_max:
            self._redimensionar()
            
        return self._inserir_sem_redimensionar(chave, valor)
        
    def buscar(self, chave: str) -> Optional[Any]:
        """
        Busca um valor pela chave.
        
        Args:
            chave: Chave a ser buscada
            
        Returns:
            Valor associado à chave ou None se não encontrado
        """
        self.operacoes_busca += 1
        
        if self.tipo_colisao == TipoColisao.CHAINING:
            indice = self._calcular_hash(chave)
            bucket = self.tabela[indice]
            
            for k, v in bucket:
                if k == chave:
                    return v
            return None
            
        else:  # Open addressing
            indice, encontrado = self._encontrar_posicao(chave)
            
            if encontrado and not self.deletados[indice]:
                return self.tabela[indice][1]
            return None
            
    def remover(self, chave: str) -> bool:
        """
        Remove uma chave da hash table.
        
        Args:
            chave: Chave a ser removida
            
        Returns:
            True se a remoção foi bem-sucedida
        """
        if self.tipo_colisao == TipoColisao.CHAINING:
            indice = self._calcular_hash(chave)
            bucket = self.tabela[indice]
            
            for i, (k, _) in enumerate(bucket):
                if k == chave:
                    bucket.pop(i)
                    self.tamanho -= 1
                    return True
            return False
            
        else:  # Open addressing
            indice, encontrado = self._encontrar_posicao(chave)
            
            if encontrado and not self.deletados[indice]:
                self.deletados[indice] = True  # Lazy deletion
                self.tamanho -= 1
                return True
            return False
            
    def obter_estatisticas(self) -> Dict[str, Any]:
        """
        Retorna estatísticas detalhadas da hash table.
        
        Returns:
            Dicionário com estatísticas de performance
        """
        fator_carga = self.tamanho / self.capacidade
        media_probes = self.total_probes / max(self.operacoes_busca, 1)
        
        stats = {
            "capacidade": self.capacidade,
            "tamanho": self.tamanho,
            "fator_carga": round(fator_carga, 3),
            "colisoes_total": self.colisoes,
            "redimensionamentos": self.redimensionamentos,
            "operacoes_busca": self.operacoes_busca,
            "media_probes_por_busca": round(media_probes, 2),
            "tipo_hash": self.tipo_hash.value,
            "tipo_colisao": self.tipo_colisao.value
        }
        
        if self.tipo_colisao == TipoColisao.CHAINING:
            # Estatísticas específicas do chaining
            comprimentos = [len(bucket) for bucket in self.tabela]
            stats.update({
                "buckets_vazios": comprimentos.count(0),
                "maior_bucket": max(comprimentos),
                "comprimento_medio_bucket": round(sum(comprimentos) / len(comprimentos), 2)
            })
        else:
            # Estatísticas específicas do open addressing
            ocupados = sum(1 for i, item in enumerate(self.tabela) 
                          if item is not None and not self.deletados[i])
            deletados = sum(self.deletados)
            stats.update({
                "posicoes_ocupadas": ocupados,
                "posicoes_deletadas": deletados,
                "posicoes_vazias": self.capacidade - ocupados - deletados
            })
            
        return stats
        
    def imprimir_tabela(self, limite: int = 20) -> None:
        """
        Imprime o estado atual da tabela (limitado para não poluir).
        
        Args:
            limite: Número máximo de entradas a mostrar
        """
        print(f"\nEstado da Hash Table ({self.tipo_colisao.value}):")
        print(f"Capacidade: {self.capacidade}, Tamanho: {self.tamanho}")
        print("-" * 50)
        
        contador = 0
        
        if self.tipo_colisao == TipoColisao.CHAINING:
            for i, bucket in enumerate(self.tabela):
                if bucket and contador < limite:
                    print(f"Bucket {i}: {bucket}")
                    contador += 1
        else:
            for i, item in enumerate(self.tabela):
                if item is not None and not self.deletados[i] and contador < limite:
                    print(f"Posição {i}: {item}")
                    contador += 1
                    
        if contador >= limite:
            print("... (mostrando apenas os primeiros entries)")


def exemplo_comparacao_funcoes_hash():
    """
    Compara diferentes funções de hash.
    """
    print("=== Comparação de Funções de Hash ===\n")
    
    dados = ["apple", "banana", "cherry", "date", "elderberry", 
             "fig", "grape", "honeydew", "kiwi", "lemon"]
    
    tipos_hash = [TipoHash.DIVISAO, TipoHash.MULTIPLICACAO, 
                  TipoHash.DJIB2, TipoHash.FNV1A]
    
    for tipo in tipos_hash:
        print(f"\nTeste com {tipo.value}:")
        ht = HashTableOtimizada(capacidade_inicial=8, tipo_hash=tipo)
        
        for i, item in enumerate(dados):
            ht.inserir(item, i)
            
        stats = ht.obter_estatisticas()
        print(f"Colisões: {stats['colisoes_total']}")
        print(f"Fator de carga: {stats['fator_carga']}")


def exemplo_comparacao_colisoes():
    """
    Compara diferentes estratégias de resolução de colisões.
    """
    print("\n" + "="*60)
    print("=== Comparação de Estratégias de Colisão ===")
    print("="*60 + "\n")
    
    dados = [(f"key{i}", f"value{i}") for i in range(50)]
    
    tipos_colisao = [TipoColisao.LINEAR, TipoColisao.QUADRATIC, 
                     TipoColisao.DOUBLE_HASH, TipoColisao.CHAINING]
    
    for tipo in tipos_colisao:
        print(f"\nTeste com {tipo.value}:")
        ht = HashTableOtimizada(capacidade_inicial=16, tipo_colisao=tipo)
        
        # Insere dados
        for chave, valor in dados:
            ht.inserir(chave, valor)
            
        # Faz algumas buscas
        for i in range(0, 50, 5):
            ht.buscar(f"key{i}")
            
        stats = ht.obter_estatisticas()
        print(f"Colisões: {stats['colisoes_total']}")
        print(f"Redimensionamentos: {stats['redimensionamentos']}")
        print(f"Média de probes por busca: {stats['media_probes_por_busca']}")


def exemplo_performance_grande():
    """
    Teste de performance com grande volume de dados.
    """
    print("\n" + "="*60)
    print("=== Teste de Performance - Grande Volume ===")
    print("="*60 + "\n")
    
    import time
    
    # Testa com diferentes tamanhos
    tamanhos = [1000, 5000, 10000]
    
    for tamanho in tamanhos:
        print(f"\nTeste com {tamanho} elementos:")
        
        ht = HashTableOtimizada(
            capacidade_inicial=64,
            tipo_hash=TipoHash.DJIB2,
            tipo_colisao=TipoColisao.CHAINING
        )
        
        # Inserção
        inicio = time.time()
        for i in range(tamanho):
            ht.inserir(f"chave_{i:06d}", f"valor_{i}")
        tempo_insercao = time.time() - inicio
        
        # Busca
        inicio = time.time()
        for i in range(0, tamanho, 10):  # Busca 10% dos elementos
            ht.buscar(f"chave_{i:06d}")
        tempo_busca = time.time() - inicio
        
        stats = ht.obter_estatisticas()
        
        print(f"Tempo de inserção: {tempo_insercao:.3f}s")
        print(f"Tempo de busca: {tempo_busca:.3f}s")
        print(f"Fator de carga final: {stats['fator_carga']}")
        print(f"Redimensionamentos: {stats['redimensionamentos']}")


if __name__ == "__main__":
    exemplo_comparacao_funcoes_hash()
    exemplo_comparacao_colisoes()
    exemplo_performance_grande()
