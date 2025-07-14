<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=28A745&height=120&section=header&text=SHA-256&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Secure%20Hash%20Algorithm%20Criptográfico&descAlignY=65&descSize=16">

</div>

# SHA-256 - Secure Hash Algorithm

## Descrição

SHA-256 (Secure Hash Algorithm 256-bit) é uma função de hash criptográfica que produz um hash de 256 bits (32 bytes). Faz parte da família SHA-2 e é amplamente usado em criptografia, blockchain, assinaturas digitais e verificação de integridade.

## Como Funciona

1. **Pré-processamento**: Adiciona padding e comprimento da mensagem
2. **Inicialização**: Define constantes iniciais (primeiras 32 bits das raízes quadradas dos primeiros 8 primos)
3. **Processamento**: Processa a mensagem em blocos de 512 bits
4. **Compressão**: Aplica 64 rodadas de operações bit a bit
5. **Finalização**: Produz hash final de 256 bits

## Propriedades Criptográficas

- **Determinístico**: Mesma entrada sempre produz mesma saída
- **Efeito Avalanche**: Pequena mudança na entrada causa grande mudança na saída
- **Unidirecional**: Computacionalmente impossível reverter
- **Resistente a Colisões**: Difícil encontrar duas entradas com mesmo hash
- **Distribuição Uniforme**: Hash aparenta ser aleatório

## Complexidade

- **Tempo**: O(n) onde n é o tamanho da mensagem
- **Espaço**: O(1) - usa quantidade constante de memória
- **Segurança**: 2^256 operações para quebrar por força bruta

## Implementação Disponível

### Python (`sha_basico.py`)
```python
# Exemplo de uso
from sha_basico import SHA256, sha256

# Usando a classe
hasher = SHA256()
result = hasher.hash("Hello, World!")
print(f"SHA-256: {result}")

# Usando a função auxiliar
result = sha256("Hello, World!")
print(f"SHA-256: {result}")
```

## Componentes Principais

### Constantes
- **H**: 8 valores iniciais de 32 bits cada
- **K**: 64 constantes de rodada (raízes cúbicas dos primeiros 64 primos)

### Funções Auxiliares
- **ROTR**: Rotação à direita
- **Ch**: Função Choose
- **Maj**: Função Majority
- **Σ0, Σ1**: Funções Sigma
- **σ0, σ1**: Funções sigma minúsculas

### Operações
- **Padding**: Adiciona bit '1' seguido de zeros e tamanho
- **Parsing**: Divide em blocos de 512 bits
- **Expansion**: Estende 16 palavras para 64
- **Compression**: 64 rodadas de transformação

## Casos de Uso

1. **Verificação de Integridade**: Detectar alterações em arquivos
2. **Armazenamento de Senhas**: Hash de senhas (com salt)
3. **Blockchain**: Proof of work em Bitcoin
4. **Assinaturas Digitais**: Parte de esquemas criptográficos
5. **Certificados Digitais**: Verificação de autenticidade
6. **Checksums**: Verificação de downloads

## Características de Segurança

| Propriedade | Força |
|-------------|-------|
| Resistência a Pré-imagem | 2^256 |
| Resistência a Segunda Pré-imagem | 2^256 |
| Resistência a Colisões | 2^128 |
| Tamanho do Hash | 256 bits |
| Tamanho do Bloco | 512 bits |

## Comparação com Outros Hashes

| Algoritmo | Tamanho Hash | Segurança | Velocidade |
|-----------|--------------|-----------|------------|
| MD5 | 128 bits | ❌ Quebrado | Muito Rápida |
| SHA-1 | 160 bits | ⚠️ Fraca | Rápida |
| **SHA-256** | **256 bits** | **✅ Forte** | **Média** |
| SHA-512 | 512 bits | ✅ Forte | Média |
| SHA-3 | Variável | ✅ Forte | Lenta |

## Exemplo de Saída

```
Entrada: ""
SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Entrada: "abc"
SHA-256: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad

Entrada: "Hello, World!"
SHA-256: dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f
```

## Demonstração do Efeito Avalanche

```
Entrada: "Hello"
SHA-256: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969

Entrada: "hello" (apenas mudança de maiúscula)
SHA-256: 2cf24dba4f21d4288094c43616f93533d2d0d30e229d1a10dc30a2e9b5e3e6df

Diferença: ~50% dos bits mudaram
```

## Performance

| Operação | Tempo Típico |
|----------|--------------|
| Hash de 1KB | ~0.1ms |
| Hash de 1MB | ~100ms |
| Hash de 1GB | ~100s |

*Tempos aproximados em hardware moderno*

## Executar Exemplo

```bash
cd python/sha
python sha_basico.py
```

## Aplicações Práticas

### 1. Verificação de Arquivo
```python
import hashlib

def verify_file(file_path, expected_hash):
    with open(file_path, 'rb') as f:
        content = f.read()
    
    actual_hash = hashlib.sha256(content).hexdigest()
    return actual_hash == expected_hash
```

### 2. Proof of Work (simplificado)
```python
def mine_block(data, difficulty):
    nonce = 0
    target = "0" * difficulty
    
    while True:
        block_content = f"{data}{nonce}"
        hash_result = sha256(block_content)
        
        if hash_result.startswith(target):
            return nonce, hash_result
        
        nonce += 1
```

## Padrões e Standards

- **FIPS 180-4**: Padrão oficial do NIST
- **RFC 6234**: Especificação da Internet Engineering Task Force
- **PKCS #1**: Usado em RSA
- **X.509**: Certificados digitais

## Referências

- [FIPS 180-4: Secure Hash Standard](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)
- [RFC 6234: US Secure Hash Algorithms](https://tools.ietf.org/html/rfc6234)
- [NIST Hash Functions](https://csrc.nist.gov/projects/hash-functions)

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
  <i>🔐 "A segurança não é um produto, mas um processo" - Bruce Schneier</i>
  <br>
  <i>🔐 "Security is not a product, but a process" - Bruce Schneier</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=28A745&height=120&section=footer"/>

</div>
