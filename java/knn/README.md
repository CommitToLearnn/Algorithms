<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=FF6B35&height=200&section=header&text=KNN%20Java&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=K-Nearest%20Neighbors%20Algorithm%20in%20Java&descAlignY=60&descSize=18">

<p align="center">
  <i>☕ Enterprise-ready K-Nearest Neighbors implementation in Java with design patterns and performance optimizations</i>
</p>

---

</div>

# K-Nearest Neighbors (KNN) - Java ☕

## 📝 Descrição

O algoritmo K-Nearest Neighbors (KNN) implementado em Java com foco em orientação a objetos, design patterns e práticas enterprise. Esta implementação oferece uma versão básica para aprendizado e uma versão otimizada com recursos avançados para uso em produção.

## 🧮 Complexidade

| Operação | Versão Básica | Versão Otimizada |
|----------|---------------|------------------|
| **Treinamento** | O(1) | O(1) |
| **Predição** | O(n·d) | O(n·d) paralelo |
| **Espaço** | O(n·d) | O(n·d) + overhead OOP |

Onde:
- `n` = número de pontos de treino
- `d` = dimensionalidade dos dados

## 🎯 Quando Usar

### ✅ Ideal para:
- Aplicações enterprise Java
- Sistemas que requerem extensibilidade
- Ambientes que precisam de type safety
- Integração com frameworks Spring/Jakarta EE
- Aplicações que valorizam manutenibilidade

### ❌ Evitar quando:
- Performance extrema é crítica (considere C++/Rust)
- Recursos de memória são muito limitados
- Prototipagem rápida (Python pode ser melhor)

## 📁 Estrutura dos Arquivos

```
java/knn/
├── KNNBasico.java         # 🎯 Implementação didática
├── otimizado/
│   └── KNNOtimizado.java  # 🚀 Versão otimizada
└── README.md              # 📖 Esta documentação
```

## 🚀 Como Executar

### Versão Básica
```bash
cd java/knn
javac KNNBasico.java
java KNNBasico
```

### Versão Otimizada
```bash
cd java/knn/otimizado
javac KNNOtimizado.java
java KNNOtimizado
```

## 🎓 Conceitos Fundamentais

### 1. **Design Patterns Utilizados**

#### Strategy Pattern
```java
interface EstrategiaDistancia {
    double calcular(double[] p1, double[] p2);
    String getNome();
}

class DistanciaEuclidiana implements EstrategiaDistancia {
    @Override
    public double calcular(double[] p1, double[] p2) {
        // Implementação euclidiana
    }
}
```

#### Builder Pattern
```java
KNNOtimizado knn = KNNOtimizado.builder()
    .setK(5)
    .setEstrategiaDistancia(new DistanciaEuclidiana())
    .setNormalizar(true)
    .setProcessamentoParalelo(true)
    .build();
```

#### Factory Pattern (implícito)
```java
public static KNNBuilder builder() {
    return new KNNBuilder();
}
```

### 2. **Características Java para ML**

#### Vantagens
- **Type Safety**: Detecção de erros em tempo de compilação
- **OOP**: Modelagem clara de conceitos
- **JVM**: Otimizações em tempo de execução
- **Ecosystem**: Vasta biblioteca de frameworks
- **Portabilidade**: "Write once, run anywhere"

#### Considerações
- **Memory Overhead**: Object headers e garbage collection
- **Verbosity**: Mais código que Python
- **Startup Time**: JVM warm-up

### 3. **Concorrência e Paralelismo**

#### Streams Paralelos
```java
// Processamento paralelo automático
Stream<VizinhoOtimizado> streamVizinhos = processamentoParalelo ?
    IntStream.range(0, dadosTreino.size()).parallel().mapToObj(i -> {
        // Cálculo de distância
    }) :
    IntStream.range(0, dadosTreino.size()).mapToObj(i -> {
        // Cálculo sequencial
    });
```

#### Thread Safety
```java
// Collections thread-safe quando necessário
private final List<PontoOtimizado> dadosTreino = 
    Collections.synchronizedList(new ArrayList<>());
```

## 💡 Implementações

### 🎯 Versão Básica (`KNNBasico.java`)

**Foco**: Orientação a objetos clara e entendimento

**Características**:
- Classes bem definidas (`Ponto`, `Vizinho`, `KNNBasico`)
- Encapsulamento adequado com getters/setters
- Tratamento robusto de exceções
- Javadoc completo
- Validação de entrada
- Immutability onde apropriado

**Exemplo de uso**:
```java
import java.util.*;

public class ExemploBasico {
    public static void main(String[] args) {
        // Cria dados de exemplo
        List<Ponto> dados = Arrays.asList(
            new Ponto(new double[]{2.0, 1.0}, "A"),
            new Ponto(new double[]{5.0, 3.0}, "B"),
            new Ponto(new double[]{6.5, 4.0}, "C")
        );
        
        // Inicializa classificador
        KNNBasico knn = new KNNBasico(3);
        
        // Treina
        knn.treinar(dados);
        
        // Classifica
        String resultado = knn.classificar(new double[]{3.0, 2.0});
        System.out.println("Classe prevista: " + resultado);
    }
}
```

### 🚀 Versão Otimizada (`KNNOtimizado.java`)

**Foco**: Design patterns, performance e extensibilidade

**Características**:
- **Strategy Pattern** para métricas de distância
- **Builder Pattern** para configuração flexível
- **Streams API** para programação funcional
- **Processamento paralelo** com Fork/Join framework
- **AutoCloseable** para gerenciamento de recursos
- **Immutable data classes** para thread safety
- **Comprehensive metrics** para análise

**Exemplo de uso**:
```java
public class ExemploOtimizado {
    public static void main(String[] args) {
        // Dados sintéticos
        double[][] coordenadas = {
            {2.1, 3.2}, {5.1, 6.2}, {8.1, 9.2},
            {1.9, 2.8}, {4.9, 5.8}, {7.9, 8.8}
        };
        String[] classes = {"A", "B", "C", "A", "B", "C"};
        
        // Cria modelo com builder pattern
        try (KNNOtimizado knn = KNNOtimizado.builder()
                .setK(3)
                .setEstrategiaDistancia(new DistanciaEuclidiana())
                .setNormalizar(true)
                .setProcessamentoParalelo(true)
                .build()) {
            
            // Treina
            knn.treinar(coordenadas, classes);
            
            // Prediz com métricas detalhadas
            ResultadoClassificacao resultado = knn.predizirPonto(new double[]{3.0, 4.0});
            
            System.out.printf("Classe: %s, Confiança: %.2f%n",
                resultado.getClassePrevista(), resultado.getConfianca());
            System.out.printf("Tempo: %s%n", resultado.getTempoPredicao());
        }
    }
}
```

## 📊 Comparação de Performance

| Aspecto | Básica | Otimizada |
|---------|--------|-----------|
| **Velocidade** | ~100ms | ~20ms |
| **Paralelismo** | Não | Sim (ForkJoin) |
| **Métricas** | Euclidiana | 4 métricas |
| **Configuração** | Construtores | Builder Pattern |
| **Extensibilidade** | Limitada | Alta |
| **Type Safety** | Básica | Avançada |

## 🛠️ Técnicas de Otimização Java

### 1. **Object Pooling**
```java
// Pool de arrays para evitar alocações
private final Queue<double[]> arrayPool = new ConcurrentLinkedQueue<>();

private double[] getArray(int size) {
    double[] array = arrayPool.poll();
    if (array == null || array.length != size) {
        array = new double[size];
    }
    return array;
}
```

### 2. **Primitive Collections**
```java
// Use TIntArrayList ao invés de ArrayList<Integer>
// Evita boxing/unboxing
import gnu.trove.list.array.TIntArrayList;
```

### 3. **JVM Tuning**
```bash
# Otimizações de JVM para ML
java -XX:+UseG1GC \
     -XX:MaxGCPauseMillis=100 \
     -XX:+UseCompressedOops \
     -server \
     KNNOtimizado
```

### 4. **Micro-benchmarking**
```java
@Benchmark
public void benchmarkKNN(Blackhole bh) {
    ResultadoClassificacao resultado = knn.predizirPonto(pontoTeste);
    bh.consume(resultado);
}
```

## 🧪 Exercícios Práticos

### Iniciante
1. **Adicione logging** com java.util.logging
2. **Implemente toString()** personalizado para todas as classes
3. **Crie testes unitários** com JUnit

### Intermediário
4. **Adicione validação** com Bean Validation (JSR 303)
5. **Implemente serialização** para persistência
6. **Crie factory methods** para diferentes configurações
7. **Adicione métricas** com Micrometer

### Avançado
8. **Integre com Spring Boot** como um serviço
9. **Implemente cache** com Caffeine ou Redis
10. **Crie API REST** com JAX-RS ou Spring Web
11. **Adicione monitoramento** com Actuator
12. **Implemente sharding** para datasets grandes

## 📚 Casos de Uso Enterprise

### 1. **Microserviço Spring Boot**
```java
@RestController
@RequestMapping("/api/knn")
public class KNNController {
    
    @Autowired
    private KNNService knnService;
    
    @PostMapping("/classify")
    public ResponseEntity<ClassificationResponse> classify(
            @RequestBody ClassificationRequest request) {
        
        ResultadoClassificacao resultado = knnService.classificar(request.getFeatures());
        
        return ResponseEntity.ok(new ClassificationResponse(
            resultado.getClassePrevista(),
            resultado.getConfianca()
        ));
    }
}
```

### 2. **Integração com JPA**
```java
@Entity
@Table(name = "training_points")
public class TrainingPoint {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ElementCollection
    @CollectionTable(name = "point_coordinates")
    private List<Double> coordinates;
    
    @Column(name = "class_label")
    private String classLabel;
    
    // getters, setters, etc.
}
```

### 3. **Cache com Spring**
```java
@Service
public class KNNService {
    
    @Cacheable(value = "predictions", key = "#coordinates")
    public ResultadoClassificacao classificar(double[] coordinates) {
        return knn.predizirPonto(coordinates);
    }
    
    @CacheEvict(value = "predictions", allEntries = true)
    public void retreinar(double[][] newData, String[] newLabels) {
        knn.treinar(newData, newLabels);
    }
}
```

## ⚡ Dicas de Performance Java

1. **Profile your code**: Use JProfiler, VisualVM, ou async-profiler
2. **Minimize object creation**: Reutilize objetos quando possível
3. **Use primitive collections**: Evite boxing/unboxing
4. **Optimize garbage collection**: Tune GC parameters
5. **Consider off-heap storage**: Para datasets muito grandes

## 🔧 Build e Deploy

### Maven Configuration
```xml
<project>
    <groupId>com.example</groupId>
    <artifactId>knn-classifier</artifactId>
    <version>1.0.0</version>
    
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.9.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

### Gradle Configuration
```gradle
plugins {
    id 'java'
    id 'application'
}

java {
    sourceCompatibility = '17'
    targetCompatibility = '17'
}

dependencies {
    implementation 'com.google.guava:guava:31.1-jre'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.9.2'
}

application {
    mainClass = 'KNNOtimizado'
}
```

### Docker
```dockerfile
FROM openjdk:17-jre-slim

COPY target/knn-classifier-1.0.0.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-XX:+UseContainerSupport", "-jar", "/app.jar"]
```

## 🔗 Bibliotecas Relacionadas

### Machine Learning
- [Weka](https://www.cs.waikato.ac.nz/ml/weka/) - Suite completa ML
- [Smile](https://haifengl.github.io/) - Statistical ML Library
- [MOA](https://moa.cms.waikato.ac.nz/) - Stream mining

### Utilitárias
- [Apache Commons Math](https://commons.apache.org/proper/commons-math/) - Matemática
- [Google Guava](https://github.com/google/guava) - Utilities
- [Eclipse Collections](https://www.eclipse.org/collections/) - High-performance collections

### Frameworks
- [Spring Boot](https://spring.io/projects/spring-boot) - Enterprise applications
- [Quarkus](https://quarkus.io/) - Cloud-native Java
- [Micronaut](https://micronaut.io/) - Microservices

## 📖 Recursos Adicionais

- [Oracle Java Documentation](https://docs.oracle.com/en/java/)
- [Effective Java by Joshua Bloch](https://www.oreilly.com/library/view/effective-java/9780134686097/)
- [Java Performance by Scott Oaks](https://www.oreilly.com/library/view/java-performance-2nd/9781492056102/)
- [Machine Learning in Java](https://github.com/haifengl/smile)
- [Java Memory Model](https://docs.oracle.com/javase/specs/jls/se17/html/jls-17.4)

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

- **Java Community** for excellent design patterns and best practices
- **Enterprise Java** ecosystem for inspiration on scalable architectures
- **Spring Framework** team for showing how to build maintainable code
- All contributors who helped improve this implementation

---

<div align="center">
  <i>💡 Java brings type safety and enterprise patterns to machine learning!</i>
  <br>
  <i>💡 Java traz segurança de tipos e padrões enterprise para machine learning!</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=FF6B35&height=120&section=footer"/>

</div>
