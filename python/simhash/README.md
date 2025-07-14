<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=FF6B6B&height=120&section=header&text=SimHash&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Detecção%20de%20Similaridade%20de%20Documentos&descAlignY=65&descSize=16">

</div>

# SimHash - Algoritmo para Detecção de Documentos Similares

## Descrição

SimHash é um algoritmo de hash sensível à localidade (locality-sensitive hashing) usado para detectar documentos similares de forma eficiente. Desenvolvido pelo Google, é amplamente utilizado para detecção de conteúdo duplicado e near-duplicado em grandes volumes de dados.

## Como Funciona

1. **Tokenização**: O texto é dividido em tokens (palavras)
2. **Hash de Tokens**: Cada token é transformado em um hash (MD5)
3. **Vetor de Características**: Para cada bit do hash, incrementa ou decrementa um contador
4. **Fingerprint Final**: Bits com contador positivo = 1, negativos = 0

## Características

- **Fingerprint de 64 bits**: Cada documento é representado por um hash de 64 bits
- **Distância de Hamming**: Documentos similares têm baixa distância de Hamming
- **Escalabilidade**: Eficiente para grandes volumes de documentos
- **Resistência a Mudanças**: Pequenas alterações resultam em pequenas mudanças no hash

## Complexidade

- **Geração do Hash**: O(n) onde n é o número de tokens
- **Comparação**: O(1) para calcular distância de Hamming
- **Busca no Índice**: O(m) onde m é o número de documentos

## Implementações Disponíveis

### Python (`simhash_basico.py`)
```python
# Exemplo de uso
from simhash_basico import SimHash

# Gera hashes
hash1 = SimHash("O gato subiu no telhado")
hash2 = SimHash("O gato subiu no telhado para pegar o rato")

# Calcula similaridade
similarity = hash1.similarity(hash2)
print(f"Similaridade: {similarity:.2f}%")
```

### Go (`simhash_basico.go`)
```go
// Exemplo de uso
hash1 := NewSimHash("O gato subiu no telhado", 64)
hash2 := NewSimHash("O gato subiu no telhado para pegar o rato", 64)

similarity := hash1.Similarity(hash2)
fmt.Printf("Similaridade: %.2f%%\n", similarity)
```

### Java (`SimHashBasico.java`)
```java
// Exemplo de uso
SimHash hash1 = new SimHash("O gato subiu no telhado");
SimHash hash2 = new SimHash("O gato subiu no telhado para pegar o rato");

double similarity = hash1.similarity(hash2);
System.out.printf("Similaridade: %.2f%%\n", similarity);
```

## Casos de Uso

1. **Detecção de Plágio**: Identificar documentos copiados ou muito similares
2. **Deduplicação**: Remover conteúdo duplicado em grandes coleções
3. **Clustering**: Agrupar documentos similares
4. **Web Crawling**: Evitar indexar páginas duplicadas
5. **Recomendação**: Encontrar conteúdo similar ao interesse do usuário

## Parâmetros Importantes

- **Hash Bits**: Número de bits do fingerprint (64 é padrão)
- **Threshold**: Limiar de similaridade para considerar duplicados (80-90%)
- **Tokenização**: Como dividir o texto (palavras, n-gramas, etc.)

## Vantagens

- **Rapidez**: Comparação muito rápida entre documentos
- **Memória Eficiente**: Cada documento usa apenas 64 bits
- **Escalável**: Funciona bem com milhões de documentos
- **Robusto**: Resistente a pequenas mudanças no texto

## Limitações

- **Sensível à Ordem**: Mudanças na ordem das palavras afetam o resultado
- **Idioma**: Funciona melhor com textos no mesmo idioma
- **Tamanho Mínimo**: Documentos muito pequenos podem não funcionar bem
- **Falsos Positivos/Negativos**: Como qualquer algoritmo de hash, pode ter erros

## Benchmarks

| Operação | Tempo (ms) | Observações |
|----------|------------|-------------|
| Geração Hash | 0.1-1 | Depende do tamanho do texto |
| Comparação | 0.001 | Muito rápida (XOR + contagem) |
| Busca (1000 docs) | 1-10 | Linear no número de documentos |

## Executar Exemplos

### Python
```bash
cd python/simhash
python simhash_basico.py
```

## Referências

- [Detecting near-duplicates for web crawling](https://www.cs.princeton.edu/courses/archive/spring13/cos598C/broder97resemblance.pdf)
- [Similarity estimation techniques from rounding algorithms](https://dl.acm.org/doi/10.1145/276698.276781)
- [Google's approach to duplicate detection](https://research.google/pubs/pub33026/)

---

<div align="center">

## 👤 Autor | Author

<div align="center">
  <a href="https://github.com/matheussricardoo" target="_blank">
    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/matheus-ricardo-426452266/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn"/>
  </a>
</div>

## 📄 Licença | License

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../../LICENSE) para mais detalhes.

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

---

<div align="center">
  <i>🔍 "A similaridade está nos detalhes, mas a diferença está na essência"</i>
  <br>
  <i>🔍 "Similarity lies in details, but difference lies in essence"</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=FF6B6B&height=120&section=footer"/>

</div>
