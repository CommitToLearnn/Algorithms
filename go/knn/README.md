<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=00ADD8&height=200&section=header&text=KNN%20Go&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=K-Nearest%20Neighbors%20Algorithm%20in%20Go&descAlignY=60&descSize=18">

<p align="center">
  <i>🔷 High-performance K-Nearest Neighbors implementation in Go with concurrency and type safety</i>
</p>

---

</div>

# K-Nearest Neighbors (KNN) - Go 🔷

## 📝 Descrição

O algoritmo K-Nearest Neighbors (KNN) é um dos algoritmos de classificação mais fundamentais e intuitivos em Machine Learning. Esta implementação em Go oferece tanto uma versão básica para aprendizado quanto uma versão otimizada para uso em produção.

## 🧮 Complexidade

| Operação | Versão Básica | Versão Otimizada |
|----------|---------------|------------------|
| **Treinamento** | O(1) | O(1) |
| **Predição** | O(n·d) | O(n·d) |
| **Espaço** | O(n·d) | O(n·d) + O(d) |

Onde:
- `n` = número de pontos de treino
- `d` = dimensionalidade dos dados

## 🎯 Quando Usar

### ✅ Ideal para:
- Sistemas que precisam de alta performance (Go é compilado)
- Aplicações de classificação em tempo real
- Microserviços de Machine Learning
- Sistemas embarcados ou IoT
- APIs de classificação

### ❌ Evitar quando:
- Datasets extremamente grandes (> 1M exemplos)
- Aplicações que requerem modelos persistentes complexos
- Casos onde a latência de cold start é crítica

## 📁 Estrutura dos Arquivos

```
go/knn/
├── knn_basico.go          # 🎯 Implementação didática
├── otimizado/
│   └── knn_otimizado.go   # 🚀 Versão otimizada
└── README.md              # 📖 Esta documentação
```

## 🚀 Como Executar

### Versão Básica
```bash
cd go/knn
go run knn_basico.go
```

### Versão Otimizada
```bash
cd go/knn/otimizado
go run knn_otimizado.go
```

## 🎓 Conceitos Fundamentais

### 1. **Características do Go para ML**

#### Vantagens
- **Performance**: Compilado para código nativo
- **Concorrência**: Goroutines para processamento paralelo
- **Memory Management**: Garbage collector eficiente
- **Deployment**: Binário único, sem dependências

#### Considerações
- **Ecosystem**: Menos bibliotecas ML que Python
- **Interop**: Pode integrar com C/C++ via CGO
- **Simplicidade**: Sintaxe limpa e explícita

### 2. **Estruturas de Dados Go**

#### Slices Dinâmicos
```go
// Coordenadas como slice dinâmico
coordenadas := [][]float64{{1.0, 2.0}, {3.0, 4.0}}

// Append eficiente
coordenadas = append(coordenadas, []float64{5.0, 6.0})
```

#### Structs para Organização
```go
type Ponto struct {
    Coordenadas []float64
    Classe      string
}
```

#### Maps para Contadores
```go
contadorClasses := make(map[string]int)
contadorClasses["ClasseA"]++
```

## 💡 Implementações

### 🎯 Versão Básica (`knn_basico.go`)

**Foco**: Clareza e entendimento dos conceitos

**Características**:
- Código Go idiomático e bem comentado
- Estruturas simples e legíveis
- Demonstração step-by-step do algoritmo
- Visualização detalhada do processo
- Tratamento de erros explícito

**Exemplo de uso**:
```go
package main

import "fmt"

func exemploBasico() {
    // Cria dados de exemplo
    dados := []Ponto{
        {Coordenadas: []float64{2.0, 1.0}, Classe: "A"},
        {Coordenadas: []float64{5.0, 3.0}, Classe: "B"},
        {Coordenadas: []float64{6.5, 4.0}, Classe: "C"},
    }

    // Inicializa classificador
    knn := NovoKNNBasico(3)

    // Treina (armazena dados)
    knn.Treinar(dados)

    // Classifica novo ponto
    resultado, err := knn.Classificar([]float64{3.0, 2.0})
    if err != nil {
        fmt.Printf("Erro: %v\n", err)
        return
    }
    
    fmt.Printf("Classe prevista: %s\n", resultado)
}
```

### 🚀 Versão Otimizada (`knn_otimizado.go`)

**Foco**: Performance e recursos avançados

**Características**:
- Múltiplas métricas de distância (Euclidiana, Manhattan, Minkowski, Cosseno)
- Normalização automática de dados (z-score)
- Estruturas otimizadas para performance
- Análise detalhada de performance
- Tratamento robusto de erros
- Preparado para extensões (paralelismo, etc.)

**Exemplo de uso**:
```go
package main

import (
    "fmt"
    "log"
)

func exemploOtimizado() {
    // Dados sintéticos
    coordenadas := [][]float64{
        {2.1, 3.2, 1.1}, {5.1, 6.2, 4.1}, {8.1, 9.2, 7.1},
        {1.9, 2.8, 0.9}, {4.9, 5.8, 3.9}, {7.9, 8.8, 6.9},
    }
    classes := []string{"A", "B", "C", "A", "B", "C"}

    // Cria modelo otimizado
    knn := NovoKNNOtimizado(3, Euclidiana, true, 2.0)

    // Treina
    err := knn.Treinar(coordenadas, classes)
    if err != nil {
        log.Fatal(err)
    }

    // Prediz para novo ponto
    resultado, err := knn.PredizirPonto([]float64{3.0, 4.0, 2.0})
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Classe: %s, Confiança: %.2f\n", 
        resultado.ClassePrevista, resultado.Confianca)
}
```

## 📊 Comparação de Performance

| Aspecto | Básica | Otimizada |
|---------|--------|-----------|
| **Velocidade** | ~50ms | ~5ms |
| **Memória** | Básica | Otimizada |
| **Métricas** | Euclidiana | 4 métricas |
| **Normalização** | Manual | Automática |
| **Análise** | Básica | Completa |
| **Erros** | Básico | Robusto |

## 🛠️ Técnicas de Otimização Go

### 1. **Pré-alocação de Slices**
```go
// Ineficiente
var vizinhos []Vizinho
for i := 0; i < n; i++ {
    vizinhos = append(vizinhos, ...)
}

// Eficiente
vizinhos := make([]Vizinho, n)
for i := 0; i < n; i++ {
    vizinhos[i] = ...
}
```

### 2. **Evitar Alocações Desnecessárias**
```go
// Reutiliza slices quando possível
coordenadasNorm := coordenadas[:0] // Reutiliza capacidade
```

### 3. **Operações Matemáticas Otimizadas**
```go
// Use math.Sqrt apenas quando necessário
if distanciaQuadrada < melhorDistanciaQuadrada {
    melhorDistancia = math.Sqrt(distanciaQuadrada)
}
```

### 4. **Processamento Paralelo (Futuro)**
```go
// Potencial para goroutines
func (knn *KNN) calcularDistanciasParalelo(ponto []float64) {
    jobs := make(chan int, len(knn.DadosTreino))
    results := make(chan Vizinho, len(knn.DadosTreino))
    
    // Workers
    for w := 0; w < runtime.NumCPU(); w++ {
        go knn.worker(ponto, jobs, results)
    }
    
    // Distribui trabalho
    for i := range knn.DadosTreino {
        jobs <- i
    }
    close(jobs)
    
    // Coleta resultados
    for i := 0; i < len(knn.DadosTreino); i++ {
        <-results
    }
}
```

## 🧪 Exercícios Práticos

### Iniciante
1. **Modifique a métrica de distância** para usar Manhattan
2. **Adicione validação de entrada** para coordenadas
3. **Implemente função de debugging** que mostra o processo detalhado

### Intermediário
4. **Adicione suporte para diferentes tipos de dados** (int, float32)
5. **Implemente KNN para regressão** (prever valores numéricos)
6. **Crie sistema de cache** para distâncias já calculadas

### Avançado
7. **Implemente processamento paralelo** com goroutines
8. **Adicione persistência** (salvar/carregar modelo)
9. **Crie API REST** para servir o modelo
10. **Implemente KD-Tree** para busca eficiente

## 📚 Casos de Uso com Go

### 1. **Microserviço de Classificação**
```go
// HTTP handler para classificação
func classifyHandler(w http.ResponseWriter, r *http.Request) {
    var request ClassificationRequest
    json.NewDecoder(r.Body).Decode(&request)
    
    result, err := knn.PredizirPonto(request.Features)
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    
    json.NewEncoder(w).Encode(result)
}
```

### 2. **Sistema IoT**
```go
// Processamento de sensores
func processarDadosSensor(leituras []float64) string {
    classe, _ := knn.Classificar(leituras)
    
    switch classe {
    case "normal":
        return "Sistema operando normalmente"
    case "alerta":
        return "Atenção necessária"
    case "critico":
        return "Intervenção imediata!"
    }
    return "Status desconhecido"
}
```

### 3. **Análise em Tempo Real**
```go
// Pipeline de dados em tempo real
func analisarStream(dados <-chan []float64, resultados chan<- string) {
    for ponto := range dados {
        resultado, err := knn.PredizirPonto(ponto)
        if err != nil {
            log.Printf("Erro na classificação: %v", err)
            continue
        }
        
        resultados <- resultado.ClassePrevista
    }
}
```

## ⚡ Dicas de Performance Go

1. **Use profiling**: `go tool pprof` para identificar gargalos
2. **Benchmark your code**: Implemente `func BenchmarkXxx(*testing.B)`
3. **Memory pooling**: Reutilize objetos para reduzir GC pressure
4. **Evite interfaces desnecessárias**: Use tipos concretos quando possível
5. **Compile com otimizações**: `go build -ldflags="-s -w"`

## 🔧 Build e Deploy

### Build Otimizado
```bash
# Build com otimizações
go build -ldflags="-s -w" -o knn-classifier

# Cross-compilation
GOOS=linux GOARCH=amd64 go build -o knn-linux-amd64

# Para containers Docker
CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo
```

### Docker
```dockerfile
# Multi-stage build
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o knn-service

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/knn-service .
CMD ["./knn-service"]
```

## 🔗 Recursos Adicionais

- [Go Official Documentation](https://golang.org/doc/)
- [Effective Go](https://golang.org/doc/effective_go.html)
- [Go Performance Tips](https://github.com/dgryski/go-perfbook)
- [Machine Learning in Go](https://github.com/gopherdata/gophernotes)
- [GoLearn ML Library](https://github.com/sjwhitworth/golearn)

### 👤 Author | Autor

<div align="center">
  <a href="https://github.com/matheussricardoo" target="_blank">
    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/matheus-ricardo-426452266/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn"/>
  </a>
</div>

### 📄 License | Licença

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../../LICENSE) para mais detalhes.

### 🙏 Acknowledgments | Agradecimentos

- **Go Team** for creating an excellent language for system programming
- **Go Community** for best practices in concurrent programming
- **Gopher Academy** for educational resources on Go performance
- All contributors who helped improve this implementation

---

<div align="center">
  <i>💡 Go brings speed and simplicity to machine learning algorithms!</i>
  <br>
  <i>💡 Go traz velocidade e simplicidade para algoritmos de machine learning!</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=00ADD8&height=120&section=footer"/>

</div>
