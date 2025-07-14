"""
Índice Invertido com Hash - Estrutura de dados para busca eficiente em textos
Permite busca rápida de documentos que contêm termos específicos
"""

import re
import hashlib
from collections import defaultdict, Counter
import math


class InvertedIndex:
    def __init__(self):
        """Inicializa o índice invertido"""
        self.index = defaultdict(set)  # termo -> conjunto de document_ids
        self.documents = {}  # document_id -> conteúdo original
        self.term_freq = defaultdict(lambda: defaultdict(int))  # doc_id -> {termo: freq}
        self.doc_lengths = {}  # document_id -> número de termos
        self.total_docs = 0
    
    def _hash_document_id(self, content):
        """Gera um ID único para o documento baseado em hash"""
        hash_obj = hashlib.md5(content.encode('utf-8'))
        return hash_obj.hexdigest()[:12]  # Usa primeiros 12 caracteres
    
    def _tokenize(self, text):
        """Tokeniza o texto em termos"""
        # Remove pontuação e converte para minúsculas
        text = re.sub(r'[^\w\s]', '', text.lower())
        terms = text.split()
        return [term for term in terms if len(term) > 2]  # Remove termos muito curtos
    
    def add_document(self, content, doc_id=None):
        """
        Adiciona um documento ao índice
        
        Args:
            content (str): Conteúdo do documento
            doc_id (str, optional): ID personalizado para o documento
        
        Returns:
            str: ID do documento adicionado
        """
        if doc_id is None:
            doc_id = self._hash_document_id(content)
        
        # Armazena o documento
        self.documents[doc_id] = content
        
        # Tokeniza e processa termos
        terms = self._tokenize(content)
        self.doc_lengths[doc_id] = len(terms)
        
        # Calcula frequência dos termos
        term_counts = Counter(terms)
        
        for term, freq in term_counts.items():
            # Adiciona ao índice invertido
            self.index[term].add(doc_id)
            
            # Armazena frequência do termo no documento
            self.term_freq[doc_id][term] = freq
        
        self.total_docs += 1
        return doc_id
    
    def search(self, query):
        """
        Busca documentos que contêm os termos da query
        
        Args:
            query (str): Termos de busca
        
        Returns:
            list: Lista de document_ids ordenados por relevância
        """
        query_terms = self._tokenize(query)
        
        if not query_terms:
            return []
        
        # Encontra documentos que contêm pelo menos um termo
        candidate_docs = set()
        for term in query_terms:
            if term in self.index:
                candidate_docs.update(self.index[term])
        
        if not candidate_docs:
            return []
        
        # Calcula pontuação TF-IDF para cada documento candidato
        scores = {}
        for doc_id in candidate_docs:
            score = self._calculate_tfidf_score(doc_id, query_terms)
            scores[doc_id] = score
        
        # Ordena por pontuação (maior primeiro)
        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [doc_id for doc_id, score in sorted_docs]
    
    def _calculate_tfidf_score(self, doc_id, query_terms):
        """Calcula pontuação TF-IDF para um documento"""
        score = 0.0
        
        for term in query_terms:
            if term in self.term_freq[doc_id]:
                # Term Frequency (TF)
                tf = self.term_freq[doc_id][term] / self.doc_lengths[doc_id]
                
                # Inverse Document Frequency (IDF)
                docs_with_term = len(self.index[term])
                idf = math.log(self.total_docs / docs_with_term)
                
                # TF-IDF Score
                score += tf * idf
        
        return score
    
    def search_boolean_and(self, query):
        """Busca booleana AND - documentos que contêm TODOS os termos"""
        query_terms = self._tokenize(query)
        
        if not query_terms:
            return []
        
        # Interseção de todos os conjuntos de documentos
        result_docs = self.index[query_terms[0]].copy()
        for term in query_terms[1:]:
            if term in self.index:
                result_docs &= self.index[term]
            else:
                return []  # Se algum termo não existe, não há resultado
        
        return list(result_docs)
    
    def search_boolean_or(self, query):
        """Busca booleana OR - documentos que contêm QUALQUER termo"""
        query_terms = self._tokenize(query)
        
        if not query_terms:
            return []
        
        # União de todos os conjuntos de documentos
        result_docs = set()
        for term in query_terms:
            if term in self.index:
                result_docs |= self.index[term]
        
        return list(result_docs)
    
    def get_document(self, doc_id):
        """Retorna o conteúdo de um documento pelo ID"""
        return self.documents.get(doc_id, None)
    
    def get_stats(self):
        """Retorna estatísticas do índice"""
        total_terms = len(self.index)
        avg_docs_per_term = sum(len(docs) for docs in self.index.values()) / total_terms if total_terms > 0 else 0
        
        return {
            'total_documents': self.total_docs,
            'total_unique_terms': total_terms,
            'average_docs_per_term': avg_docs_per_term,
            'index_size_bytes': self._estimate_memory_usage()
        }
    
    def _estimate_memory_usage(self):
        """Estima uso de memória do índice"""
        # Estimativa simples baseada no número de entradas
        memory = 0
        for term, docs in self.index.items():
            memory += len(term.encode('utf-8'))  # Tamanho do termo
            memory += len(docs) * 12  # Tamanho aproximado dos IDs
        return memory


# Exemplo de uso
if __name__ == "__main__":
    # Criar índice invertido
    idx = InvertedIndex()
    
    # Documentos de exemplo
    documents = [
        "Python é uma linguagem de programação versátil e poderosa",
        "Machine learning com Python é muito popular entre cientistas de dados", 
        "Algoritmos de busca são fundamentais na ciência da computação",
        "Estruturas de dados como hash tables são eficientes para busca",
        "Índices invertidos permitem busca rápida em grandes coleções de texto",
        "Python oferece muitas bibliotecas para processamento de linguagem natural"
    ]
    
    print("=== Índice Invertido com Hash ===")
    print("Adicionando documentos ao índice...")
    
    # Adiciona documentos ao índice
    doc_ids = []
    for i, doc in enumerate(documents):
        doc_id = idx.add_document(doc, f"doc_{i+1}")
        doc_ids.append(doc_id)
        print(f"  [{doc_id}] {doc[:50]}...")
    
    # Estatísticas do índice
    stats = idx.get_stats()
    print(f"\n=== Estatísticas do Índice ===")
    print(f"Total de documentos: {stats['total_documents']}")
    print(f"Termos únicos: {stats['total_unique_terms']}")
    print(f"Média de docs por termo: {stats['average_docs_per_term']:.2f}")
    print(f"Uso estimado de memória: {stats['index_size_bytes']} bytes")
    
    # Testes de busca
    queries = [
        "Python",
        "busca algoritmos",
        "machine learning",
        "linguagem programação"
    ]
    
    print(f"\n=== Testes de Busca ===")
    
    for query in queries:
        print(f"\nQuery: '{query}'")
        
        # Busca TF-IDF (ranqueada)
        results_tfidf = idx.search(query)
        print(f"  Busca TF-IDF ({len(results_tfidf)} resultados):")
        for doc_id in results_tfidf[:3]:  # Top 3
            content = idx.get_document(doc_id)
            print(f"    [{doc_id}] {content[:60]}...")
        
        # Busca booleana AND
        results_and = idx.search_boolean_and(query)
        print(f"  Busca AND ({len(results_and)} resultados): {results_and}")
        
        # Busca booleana OR
        results_or = idx.search_boolean_or(query)
        print(f"  Busca OR ({len(results_or)} resultados): {results_or}")
    
    # Demonstra eficiência do hash
    print(f"\n=== Demonstração de Hash ===")
    doc_content = "Documento de teste para demonstrar hash"
    hash_id = idx._hash_document_id(doc_content)
    print(f"Conteúdo: '{doc_content}'")
    print(f"Hash ID: {hash_id}")
    
    # Testa consistência do hash
    hash_id2 = idx._hash_document_id(doc_content)
    print(f"Hash ID (segunda vez): {hash_id2}")
    print(f"Hashes são iguais: {hash_id == hash_id2}")
