/*
K-Nearest Neighbors (KNN) - Implementação Básica em Go
======================================================

Algoritmo de classificação que determina a classe de um ponto baseado
na classe majoritária dos K vizinhos mais próximos.

Complexidade:
- Tempo: O(n * d) para cada predição
- Espaço: O(n * d) para armazenar dados de treino

Características desta implementação:
- Foco na clareza e entendimento
- Comentários extensos
- Estruturas simples
- Visualização do processo
*/

package main

import (
	"fmt"
	"math"
	"sort"
	"strings"
)

// Ponto representa um ponto no espaço n-dimensional
type Ponto struct {
	Coordenadas []float64 // Características do ponto
	Classe      string    // Classe/label do ponto
}

// String retorna representação textual do ponto
func (p Ponto) String() string {
	return fmt.Sprintf("Ponto{Coord: %v, Classe: %s}", p.Coordenadas, p.Classe)
}

// Vizinho representa um vizinho com sua distância
type Vizinho struct {
	Ponto     Ponto
	Distancia float64
}

// KNNBasico implementa o algoritmo K-Nearest Neighbors básico
type KNNBasico struct {
	K           int     // Número de vizinhos a considerar
	DadosTreino []Ponto // Dados de treinamento
}

// NovoKNNBasico cria uma nova instância do classificador KNN
func NovoKNNBasico(k int) *KNNBasico {
	fmt.Printf("🎯 KNN Básico inicializado com k=%d\n", k)
	return &KNNBasico{
		K:           k,
		DadosTreino: make([]Ponto, 0),
	}
}

// CalcularDistanciaEuclidiana calcula a distância euclidiana entre dois pontos
func (knn *KNNBasico) CalcularDistanciaEuclidiana(p1, p2 []float64) (float64, error) {
	if len(p1) != len(p2) {
		return 0, fmt.Errorf("pontos devem ter a mesma dimensão")
	}

	fmt.Printf("   📏 Calculando distância euclidiana:\n")

	somaQuadrados := 0.0
	for i := 0; i < len(p1); i++ {
		diferenca := p1[i] - p2[i]
		quadrado := diferenca * diferenca
		somaQuadrados += quadrado
		fmt.Printf("      Dimensão %d: (%.3f - %.3f)² = %.3f\n",
			i+1, p1[i], p2[i], quadrado)
	}

	distancia := math.Sqrt(somaQuadrados)
	fmt.Printf("      Distância: √%.3f = %.3f\n", somaQuadrados, distancia)

	return distancia, nil
}

// Treinar armazena os dados de treinamento
func (knn *KNNBasico) Treinar(dados []Ponto) {
	knn.DadosTreino = make([]Ponto, len(dados))
	copy(knn.DadosTreino, dados)

	fmt.Printf("📚 Modelo treinado com %d exemplos\n", len(knn.DadosTreino))

	// Conta distribuição das classes
	contadorClasses := make(map[string]int)
	for _, ponto := range dados {
		contadorClasses[ponto.Classe]++
	}

	fmt.Printf("📊 Distribuição das classes: ")
	for classe, count := range contadorClasses {
		fmt.Printf("%s:%d ", classe, count)
	}
	fmt.Println()
}

// EncontrarKVizinhos encontra os k vizinhos mais próximos de um ponto
func (knn *KNNBasico) EncontrarKVizinhos(pontoConsulta []float64) ([]Vizinho, error) {
	if len(knn.DadosTreino) == 0 {
		return nil, fmt.Errorf("modelo não foi treinado")
	}

	fmt.Printf("\n🔍 Buscando %d vizinhos mais próximos para %v\n",
		knn.K, pontoConsulta)

	// Calcula distâncias para todos os pontos de treino
	var vizinhos []Vizinho

	for i, pontoTreino := range knn.DadosTreino {
		fmt.Printf("\n📏 Calculando distância para ponto %d: %v (classe: %s)\n",
			i+1, pontoTreino.Coordenadas, pontoTreino.Classe)

		distancia, err := knn.CalcularDistanciaEuclidiana(pontoConsulta, pontoTreino.Coordenadas)
		if err != nil {
			return nil, err
		}

		vizinhos = append(vizinhos, Vizinho{
			Ponto:     pontoTreino,
			Distancia: distancia,
		})
	}

	// Ordena vizinhos por distância (crescente)
	sort.Slice(vizinhos, func(i, j int) bool {
		return vizinhos[i].Distancia < vizinhos[j].Distancia
	})

	// Retorna apenas os k primeiros
	kVizinhos := vizinhos
	if len(vizinhos) > knn.K {
		kVizinhos = vizinhos[:knn.K]
	}

	fmt.Printf("\n🎯 %d vizinhos mais próximos:\n", len(kVizinhos))
	for i, vizinho := range kVizinhos {
		fmt.Printf("   %dº vizinho: distância=%.3f, classe=%s\n",
			i+1, vizinho.Distancia, vizinho.Ponto.Classe)
	}

	return kVizinhos, nil
}

// Classificar classifica um ponto baseado nos k vizinhos mais próximos
func (knn *KNNBasico) Classificar(pontoConsulta []float64) (string, error) {
	// Encontra os k vizinhos mais próximos
	kVizinhos, err := knn.EncontrarKVizinhos(pontoConsulta)
	if err != nil {
		return "", err
	}

	// Conta a frequência de cada classe
	contadorClasses := make(map[string]int)
	for _, vizinho := range kVizinhos {
		contadorClasses[vizinho.Ponto.Classe]++
	}

	fmt.Printf("\n📊 Contagem de classes nos vizinhos: ")
	for classe, count := range contadorClasses {
		fmt.Printf("%s:%d ", classe, count)
	}
	fmt.Println()

	// Encontra a classe mais frequente
	classePrevista := ""
	maxCount := 0

	for classe, count := range contadorClasses {
		if count > maxCount {
			maxCount = count
			classePrevista = classe
		}
	}

	confianca := float64(maxCount) / float64(len(kVizinhos))

	fmt.Printf("🎯 Classe prevista: %s\n", classePrevista)
	fmt.Printf("🔢 Confiança: %.1f%% (%d/%d vizinhos)\n",
		confianca*100, maxCount, len(kVizinhos))

	return classePrevista, nil
}

// demonstracaoKNNBasico executa uma demonstração completa do algoritmo
func demonstracaoKNNBasico() {
	fmt.Println("=" + strings.Repeat("=", 59))
	fmt.Println("🤖 DEMONSTRAÇÃO: K-Nearest Neighbors (KNN) - Versão Básica")
	fmt.Println("=" + strings.Repeat("=", 59))

	// Cria dados de exemplo: classificação de frutas
	// [doçura, acidez] -> tipo_fruta
	dadosFrutas := []Ponto{
		{Coordenadas: []float64{8.0, 2.0}, Classe: "maçã"},
		{Coordenadas: []float64{7.5, 2.5}, Classe: "maçã"},
		{Coordenadas: []float64{8.2, 1.8}, Classe: "maçã"},
		{Coordenadas: []float64{3.0, 8.0}, Classe: "limão"},
		{Coordenadas: []float64{3.5, 7.5}, Classe: "limão"},
		{Coordenadas: []float64{2.8, 8.2}, Classe: "limão"},
		{Coordenadas: []float64{9.0, 3.0}, Classe: "banana"},
		{Coordenadas: []float64{8.8, 3.5}, Classe: "banana"},
		{Coordenadas: []float64{9.2, 2.8}, Classe: "banana"},
	}

	fmt.Printf("🍎 Dataset: Classificação de frutas com %d exemplos\n", len(dadosFrutas))
	fmt.Println("📊 Características: [doçura, acidez]")

	// Inicializa o classificador
	knn := NovoKNNBasico(3)

	// Treina o modelo
	knn.Treinar(dadosFrutas)

	// Testa com diferentes pontos
	pontosTeste := [][]float64{
		{7.8, 2.2}, // Deve ser maçã
		{3.2, 7.8}, // Deve ser limão
		{9.1, 3.2}, // Deve ser banana
		{6.0, 5.0}, // Caso ambíguo
	}

	fmt.Println("\n" + strings.Repeat("=", 40))
	fmt.Println("🧪 TESTANDO CLASSIFICAÇÕES")
	fmt.Println(strings.Repeat("=", 40))

	for i, ponto := range pontosTeste {
		fmt.Printf("\n🔍 TESTE %d: Classificando ponto %v\n", i+1, ponto)
		fmt.Println(strings.Repeat("-", 40))

		classePrevista, err := knn.Classificar(ponto)
		if err != nil {
			fmt.Printf("❌ Erro: %v\n", err)
			continue
		}

		fmt.Printf("✅ Resultado final: %v → %s\n", ponto, classePrevista)
	}
}

// exemploComparacaoK demonstra como diferentes valores de k afetam o resultado
func exemploComparacaoK() {
	fmt.Println("\n" + strings.Repeat("=", 60))
	fmt.Println("📈 COMPARAÇÃO: Efeito de diferentes valores de K")
	fmt.Println(strings.Repeat("=", 60))

	// Dados simples para demonstração
	dados := []Ponto{
		{Coordenadas: []float64{1, 1}, Classe: "A"},
		{Coordenadas: []float64{1, 2}, Classe: "A"},
		{Coordenadas: []float64{2, 1}, Classe: "A"},
		{Coordenadas: []float64{5, 5}, Classe: "B"},
		{Coordenadas: []float64{5, 6}, Classe: "B"},
		{Coordenadas: []float64{6, 5}, Classe: "B"},
		{Coordenadas: []float64{3, 3}, Classe: "A"}, // Ponto intermediário
	}

	pontoTeste := []float64{3, 4}

	valoresK := []int{1, 3, 5}

	for _, k := range valoresK {
		fmt.Printf("\n🎯 Testando com k=%d\n", k)
		fmt.Println(strings.Repeat("-", 30))

		knn := NovoKNNBasico(k)
		knn.Treinar(dados)

		resultado, err := knn.Classificar(pontoTeste)
		if err != nil {
			fmt.Printf("❌ Erro: %v\n", err)
			continue
		}

		fmt.Printf("📊 Com k=%d: %v → %s\n", k, pontoTeste, resultado)
	}
}

// exerciciosPraticos sugere exercícios para prática
func exerciciosPraticos() {
	fmt.Println("\n" + strings.Repeat("=", 60))
	fmt.Println("🎓 EXERCÍCIOS SUGERIDOS:")
	fmt.Println(strings.Repeat("=", 60))
	fmt.Println("1. Implemente outras métricas de distância (Manhattan, Minkowski)")
	fmt.Println("2. Adicione validação dos dados de entrada")
	fmt.Println("3. Implemente KNN para regressão (predizer valores numéricos)")
	fmt.Println("4. Adicione função para encontrar o melhor k automaticamente")
	fmt.Println("5. Crie visualização dos resultados (se usar biblioteca gráfica)")
	fmt.Println("6. Implemente normalização automática dos dados")
	fmt.Println("7. Adicione suporte para pesos baseados na distância")
}

func main() {
	// Executa as demonstrações
	demonstracaoKNNBasico()
	exemploComparacaoK()
	exerciciosPraticos()
}
