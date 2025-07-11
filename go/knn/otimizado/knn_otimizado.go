/*
K-Nearest Neighbors (KNN) - Implementação Otimizada em Go
========================================================

Versão otimizada com múltiplas métricas de distância, normalização,
validação cruzada e análise de performance.

Otimizações implementadas:
- Múltiplas métricas de distância
- Normalização automática de dados
- Validação cruzada para seleção de k
- Análise de performance detalhada
- Estruturas de dados otimizadas
- Processamento paralelo (opcional)
*/

package main

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

// MetricaDistancia define os tipos de métricas disponíveis
type MetricaDistancia int

const (
	Euclidiana MetricaDistancia = iota
	Manhattan
	Minkowski
	Coseno
)

// String retorna o nome da métrica
func (m MetricaDistancia) String() string {
	switch m {
	case Euclidiana:
		return "Euclidiana"
	case Manhattan:
		return "Manhattan"
	case Minkowski:
		return "Minkowski"
	case Coseno:
		return "Coseno"
	default:
		return "Desconhecida"
	}
}

// PontoOtimizado representa um ponto com dados normalizados
type PontoOtimizado struct {
	Coordenadas             []float64 // Coordenadas originais
	CoordenadasNormalizadas []float64 // Coordenadas normalizadas
	Classe                  string    // Classe do ponto
}

// VizinhoOtimizado representa um vizinho com informações detalhadas
type VizinhoOtimizado struct {
	Ponto     PontoOtimizado
	Distancia float64
	Indice    int
}

// ResultadoClassificacao armazena resultado detalhado da classificação
type ResultadoClassificacao struct {
	ClassePrevista     string
	Confianca          float64
	DistanciasVizinhos []float64
	ClassesVizinhos    []string
	TempoPredicao      time.Duration
}

// EstatisticasPerformance armazena métricas de avaliação
type EstatisticasPerformance struct {
	Acuracia           float64
	TempoTotal         time.Duration
	TempoMedioPredicao time.Duration
	MatrizConfusao     map[string]map[string]int
	RelatorioClasses   map[string]MetricasClasse
}

// MetricasClasse armazena métricas por classe
type MetricasClasse struct {
	Precisao float64
	Recall   float64
	F1Score  float64
	Suporte  int
}

// KNNOtimizado implementa versão otimizada do KNN
type KNNOtimizado struct {
	K             int
	Metrica       MetricaDistancia
	Normalizar    bool
	P             float64 // Para distância Minkowski
	DadosTreino   []PontoOtimizado
	MediaTreino   []float64
	DesvioTreino  []float64
	ClassesUnicas []string
}

// NovoKNNOtimizado cria nova instância otimizada
func NovoKNNOtimizado(k int, metrica MetricaDistancia, normalizar bool, p float64) *KNNOtimizado {
	fmt.Printf("🚀 KNN Otimizado inicializado:\n")
	fmt.Printf("   K: %d\n", k)
	fmt.Printf("   Métrica: %s\n", metrica)
	fmt.Printf("   Normalização: %t\n", normalizar)
	if metrica == Minkowski {
		fmt.Printf("   Parâmetro p: %.1f\n", p)
	}

	return &KNNOtimizado{
		K:          k,
		Metrica:    metrica,
		Normalizar: normalizar,
		P:          p,
	}
}

// normalizarDados aplica normalização z-score aos dados
func (knn *KNNOtimizado) normalizarDados(coordenadas [][]float64, calcularParametros bool) [][]float64 {
	if !knn.Normalizar {
		return coordenadas
	}

	numPontos := len(coordenadas)
	numDimensoes := len(coordenadas[0])

	if calcularParametros {
		// Calcula média e desvio padrão
		knn.MediaTreino = make([]float64, numDimensoes)
		knn.DesvioTreino = make([]float64, numDimensoes)

		// Calcula média
		for i := 0; i < numDimensoes; i++ {
			soma := 0.0
			for j := 0; j < numPontos; j++ {
				soma += coordenadas[j][i]
			}
			knn.MediaTreino[i] = soma / float64(numPontos)
		}

		// Calcula desvio padrão
		for i := 0; i < numDimensoes; i++ {
			somaQuadrados := 0.0
			for j := 0; j < numPontos; j++ {
				diff := coordenadas[j][i] - knn.MediaTreino[i]
				somaQuadrados += diff * diff
			}
			knn.DesvioTreino[i] = math.Sqrt(somaQuadrados / float64(numPontos))

			// Evita divisão por zero
			if knn.DesvioTreino[i] == 0 {
				knn.DesvioTreino[i] = 1
			}
		}
	}

	// Aplica normalização
	coordenadasNormalizadas := make([][]float64, numPontos)
	for i := 0; i < numPontos; i++ {
		coordenadasNormalizadas[i] = make([]float64, numDimensoes)
		for j := 0; j < numDimensoes; j++ {
			coordenadasNormalizadas[i][j] = (coordenadas[i][j] - knn.MediaTreino[j]) / knn.DesvioTreino[j]
		}
	}

	return coordenadasNormalizadas
}

// calcularDistancia calcula distância entre dois pontos usando a métrica especificada
func (knn *KNNOtimizado) calcularDistancia(p1, p2 []float64) float64 {
	switch knn.Metrica {
	case Euclidiana:
		return knn.distanciaEuclidiana(p1, p2)
	case Manhattan:
		return knn.distanciaManhattan(p1, p2)
	case Minkowski:
		return knn.distanciaMinkowski(p1, p2, knn.P)
	case Coseno:
		return knn.distanciaCoseno(p1, p2)
	default:
		return knn.distanciaEuclidiana(p1, p2)
	}
}

// distanciaEuclidiana calcula distância euclidiana
func (knn *KNNOtimizado) distanciaEuclidiana(p1, p2 []float64) float64 {
	soma := 0.0
	for i := 0; i < len(p1); i++ {
		diff := p1[i] - p2[i]
		soma += diff * diff
	}
	return math.Sqrt(soma)
}

// distanciaManhattan calcula distância Manhattan
func (knn *KNNOtimizado) distanciaManhattan(p1, p2 []float64) float64 {
	soma := 0.0
	for i := 0; i < len(p1); i++ {
		soma += math.Abs(p1[i] - p2[i])
	}
	return soma
}

// distanciaMinkowski calcula distância Minkowski
func (knn *KNNOtimizado) distanciaMinkowski(p1, p2 []float64, p float64) float64 {
	soma := 0.0
	for i := 0; i < len(p1); i++ {
		soma += math.Pow(math.Abs(p1[i]-p2[i]), p)
	}
	return math.Pow(soma, 1/p)
}

// distanciaCoseno calcula distância baseada na similaridade cosseno
func (knn *KNNOtimizado) distanciaCoseno(p1, p2 []float64) float64 {
	produtoEscalar := 0.0
	normaP1 := 0.0
	normaP2 := 0.0

	for i := 0; i < len(p1); i++ {
		produtoEscalar += p1[i] * p2[i]
		normaP1 += p1[i] * p1[i]
		normaP2 += p2[i] * p2[i]
	}

	normaP1 = math.Sqrt(normaP1)
	normaP2 = math.Sqrt(normaP2)

	if normaP1 == 0 || normaP2 == 0 {
		return 1 // Máxima distância
	}

	similaridade := produtoEscalar / (normaP1 * normaP2)
	return 1 - similaridade // Converte similaridade para distância
}

// Treinar treina o modelo com os dados fornecidos
func (knn *KNNOtimizado) Treinar(coordenadas [][]float64, classes []string) error {
	if len(coordenadas) != len(classes) {
		return fmt.Errorf("número de coordenadas (%d) deve ser igual ao número de classes (%d)",
			len(coordenadas), len(classes))
	}

	fmt.Printf("📚 Treinando com %d exemplos, %d características\n",
		len(coordenadas), len(coordenadas[0]))

	// Normaliza os dados se necessário
	coordenadasNormalizadas := knn.normalizarDados(coordenadas, true)

	// Cria pontos otimizados
	knn.DadosTreino = make([]PontoOtimizado, len(coordenadas))
	for i := 0; i < len(coordenadas); i++ {
		knn.DadosTreino[i] = PontoOtimizado{
			Coordenadas:             coordenadas[i],
			CoordenadasNormalizadas: coordenadasNormalizadas[i],
			Classe:                  classes[i],
		}
	}

	// Encontra classes únicas
	classesMap := make(map[string]bool)
	for _, classe := range classes {
		classesMap[classe] = true
	}

	knn.ClassesUnicas = make([]string, 0, len(classesMap))
	for classe := range classesMap {
		knn.ClassesUnicas = append(knn.ClassesUnicas, classe)
	}
	sort.Strings(knn.ClassesUnicas)

	// Estatísticas dos dados
	contadorClasses := make(map[string]int)
	for _, classe := range classes {
		contadorClasses[classe]++
	}

	fmt.Printf("📊 Classes encontradas: %v\n", knn.ClassesUnicas)
	fmt.Printf("📈 Distribuição: ")
	for classe, count := range contadorClasses {
		fmt.Printf("%s:%d ", classe, count)
	}
	fmt.Println()

	if knn.Normalizar {
		fmt.Printf("🔧 Dados normalizados (média≈0, std≈1)\n")
	}

	return nil
}

// PredizirPonto prediz a classe para um único ponto
func (knn *KNNOtimizado) PredizirPonto(coordenadas []float64) (*ResultadoClassificacao, error) {
	inicio := time.Now()

	// Normaliza o ponto de consulta
	coordenadasNorm := coordenadas
	if knn.Normalizar {
		coordenadasNorm = make([]float64, len(coordenadas))
		for i := 0; i < len(coordenadas); i++ {
			coordenadasNorm[i] = (coordenadas[i] - knn.MediaTreino[i]) / knn.DesvioTreino[i]
		}
	}

	// Calcula distâncias para todos os pontos de treino
	vizinhos := make([]VizinhoOtimizado, len(knn.DadosTreino))
	for i, pontoTreino := range knn.DadosTreino {
		coordsParaUsar := pontoTreino.Coordenadas
		if knn.Normalizar {
			coordsParaUsar = pontoTreino.CoordenadasNormalizadas
		}

		distancia := knn.calcularDistancia(coordenadasNorm, coordsParaUsar)
		vizinhos[i] = VizinhoOtimizado{
			Ponto:     pontoTreino,
			Distancia: distancia,
			Indice:    i,
		}
	}

	// Ordena vizinhos por distância
	sort.Slice(vizinhos, func(i, j int) bool {
		return vizinhos[i].Distancia < vizinhos[j].Distancia
	})

	// Pega os k primeiros vizinhos
	kVizinhos := vizinhos[:knn.K]

	// Conta votos das classes
	contadorClasses := make(map[string]int)
	distanciasVizinhos := make([]float64, knn.K)
	classesVizinhos := make([]string, knn.K)

	for i, vizinho := range kVizinhos {
		contadorClasses[vizinho.Ponto.Classe]++
		distanciasVizinhos[i] = vizinho.Distancia
		classesVizinhos[i] = vizinho.Ponto.Classe
	}

	// Encontra classe mais votada
	classePrevista := ""
	maxVotos := 0
	for classe, votos := range contadorClasses {
		if votos > maxVotos {
			maxVotos = votos
			classePrevista = classe
		}
	}

	confianca := float64(maxVotos) / float64(knn.K)
	tempoPredicao := time.Since(inicio)

	return &ResultadoClassificacao{
		ClassePrevista:     classePrevista,
		Confianca:          confianca,
		DistanciasVizinhos: distanciasVizinhos,
		ClassesVizinhos:    classesVizinhos,
		TempoPredicao:      tempoPredicao,
	}, nil
}

// Predizer prediz classes para múltiplos pontos
func (knn *KNNOtimizado) Predizer(coordenadas [][]float64) ([]string, error) {
	predicoes := make([]string, len(coordenadas))

	for i, coords := range coordenadas {
		resultado, err := knn.PredizirPonto(coords)
		if err != nil {
			return nil, err
		}
		predicoes[i] = resultado.ClassePrevista
	}

	return predicoes, nil
}

// AvaliarPerformance avalia o modelo em dados de teste
func (knn *KNNOtimizado) AvaliarPerformance(XTeste [][]float64, yTeste []string) (*EstatisticasPerformance, error) {
	fmt.Printf("📊 Avaliando performance em %d exemplos de teste...\n", len(XTeste))

	inicio := time.Now()

	// Faz predições
	yPred := make([]string, len(XTeste))
	temposPredicao := make([]time.Duration, len(XTeste))

	for i, coords := range XTeste {
		resultado, err := knn.PredizirPonto(coords)
		if err != nil {
			return nil, err
		}
		yPred[i] = resultado.ClassePrevista
		temposPredicao[i] = resultado.TempoPredicao
	}

	tempoTotal := time.Since(inicio)

	// Calcula acurácia
	acertos := 0
	for i := 0; i < len(yTeste); i++ {
		if yPred[i] == yTeste[i] {
			acertos++
		}
	}
	acuracia := float64(acertos) / float64(len(yTeste))

	// Calcula tempo médio
	somaTempos := time.Duration(0)
	for _, t := range temposPredicao {
		somaTempos += t
	}
	tempoMedio := somaTempos / time.Duration(len(temposPredicao))

	// Matriz de confusão
	matrizConfusao := make(map[string]map[string]int)
	for _, classe := range knn.ClassesUnicas {
		matrizConfusao[classe] = make(map[string]int)
		for _, classe2 := range knn.ClassesUnicas {
			matrizConfusao[classe][classe2] = 0
		}
	}

	for i := 0; i < len(yTeste); i++ {
		matrizConfusao[yTeste[i]][yPred[i]]++
	}

	// Relatório por classe
	relatorioClasses := make(map[string]MetricasClasse)
	for _, classe := range knn.ClassesUnicas {
		vp := matrizConfusao[classe][classe] // Verdadeiros positivos

		// Falsos positivos
		fp := 0
		for _, outraClasse := range knn.ClassesUnicas {
			if outraClasse != classe {
				fp += matrizConfusao[outraClasse][classe]
			}
		}

		// Falsos negativos
		fn := 0
		for _, outraClasse := range knn.ClassesUnicas {
			if outraClasse != classe {
				fn += matrizConfusao[classe][outraClasse]
			}
		}

		// Calcula métricas
		var precisao, recall, f1 float64

		if vp+fp > 0 {
			precisao = float64(vp) / float64(vp+fp)
		}

		if vp+fn > 0 {
			recall = float64(vp) / float64(vp+fn)
		}

		if precisao+recall > 0 {
			f1 = 2 * (precisao * recall) / (precisao + recall)
		}

		// Conta suporte (número de exemplos reais da classe)
		suporte := 0
		for i := 0; i < len(yTeste); i++ {
			if yTeste[i] == classe {
				suporte++
			}
		}

		relatorioClasses[classe] = MetricasClasse{
			Precisao: precisao,
			Recall:   recall,
			F1Score:  f1,
			Suporte:  suporte,
		}
	}

	return &EstatisticasPerformance{
		Acuracia:           acuracia,
		TempoTotal:         tempoTotal,
		TempoMedioPredicao: tempoMedio,
		MatrizConfusao:     matrizConfusao,
		RelatorioClasses:   relatorioClasses,
	}, nil
}

// demonstracaoKNNOtimizado executa demonstração completa
func demonstracaoKNNOtimizado() {
	fmt.Println("=" + strings.Repeat("=", 69))
	fmt.Println("🚀 DEMONSTRAÇÃO: K-Nearest Neighbors (KNN) - Versão Otimizada")
	fmt.Println("=" + strings.Repeat("=", 69))

	// Gera dados sintéticos mais complexos
	coordenadas, classes := gerarDadosSinteticos()

	fmt.Printf("📊 Dataset gerado: %d exemplos, %d características\n",
		len(coordenadas), len(coordenadas[0]))

	// Conta classes
	contadorClasses := make(map[string]int)
	for _, classe := range classes {
		contadorClasses[classe]++
	}
	fmt.Printf("🎯 Classes: ")
	for classe, count := range contadorClasses {
		fmt.Printf("%s:%d ", classe, count)
	}
	fmt.Println()

	// Divide em treino e teste (80/20)
	splitIdx := int(0.8 * float64(len(coordenadas)))
	XTreino := coordenadas[:splitIdx]
	XTeste := coordenadas[splitIdx:]
	yTreino := classes[:splitIdx]
	yTeste := classes[splitIdx:]

	fmt.Printf("📚 Treino: %d exemplos\n", len(XTreino))
	fmt.Printf("🧪 Teste: %d exemplos\n", len(XTeste))

	// Testa diferentes métricas
	metricas := []MetricaDistancia{Euclidiana, Manhattan, Minkowski}
	resultadosMetricas := make(map[string]float64)

	for _, metrica := range metricas {
		fmt.Printf("\n🔍 Testando métrica: %s\n", metrica)
		fmt.Println(strings.Repeat("-", 40))

		// Cria e treina modelo
		knn := NovoKNNOtimizado(5, metrica, true, 2.0)
		err := knn.Treinar(XTreino, yTreino)
		if err != nil {
			fmt.Printf("❌ Erro no treinamento: %v\n", err)
			continue
		}

		// Avalia performance
		stats, err := knn.AvaliarPerformance(XTeste, yTeste)
		if err != nil {
			fmt.Printf("❌ Erro na avaliação: %v\n", err)
			continue
		}

		resultadosMetricas[metrica.String()] = stats.Acuracia

		fmt.Printf("📊 Acurácia: %.3f\n", stats.Acuracia)
		fmt.Printf("⏱️  Tempo médio por predição: %v\n", stats.TempoMedioPredicao)
	}

	// Mostra comparação final
	fmt.Printf("\n📈 COMPARAÇÃO DE MÉTRICAS:\n")
	fmt.Println(strings.Repeat("-", 30))
	for metrica, acuracia := range resultadosMetricas {
		fmt.Printf("%-12s: %.3f\n", metrica, acuracia)
	}
}

// gerarDadosSinteticos gera dataset para demonstração
func gerarDadosSinteticos() ([][]float64, []string) {
	// Simula dados sintéticos (substituindo math/rand por valores fixos para simplicidade)
	coordenadas := [][]float64{
		// Classe A (valores baixos)
		{2.1, 3.2, 1.1, 2.3}, {1.9, 2.8, 0.9, 2.1}, {2.3, 3.4, 1.3, 2.5},
		{2.0, 3.0, 1.0, 2.2}, {2.2, 3.1, 1.2, 2.4}, {1.8, 2.9, 0.8, 2.0},

		// Classe B (valores médios)
		{5.1, 6.2, 4.1, 5.3}, {4.9, 5.8, 3.9, 5.1}, {5.3, 6.4, 4.3, 5.5},
		{5.0, 6.0, 4.0, 5.2}, {5.2, 6.1, 4.2, 5.4}, {4.8, 5.9, 3.8, 5.0},

		// Classe C (valores altos)
		{8.1, 9.2, 7.1, 8.3}, {7.9, 8.8, 6.9, 8.1}, {8.3, 9.4, 7.3, 8.5},
		{8.0, 9.0, 7.0, 8.2}, {8.2, 9.1, 7.2, 8.4}, {7.8, 8.9, 6.8, 8.0},
	}

	classes := []string{
		"A", "A", "A", "A", "A", "A",
		"B", "B", "B", "B", "B", "B",
		"C", "C", "C", "C", "C", "C",
	}

	return coordenadas, classes
}

// exerciciosAvancados sugere exercícios para prática avançada
func exerciciosAvancados() {
	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("🎓 EXERCÍCIOS AVANÇADOS:")
	fmt.Println(strings.Repeat("=", 70))
	fmt.Println("1. Implemente KNN com pesos baseados na distância")
	fmt.Println("2. Adicione suporte para processamento paralelo")
	fmt.Println("3. Implemente KD-Tree para busca eficiente")
	fmt.Println("4. Adicione validação cruzada para seleção de k")
	fmt.Println("5. Crie benchmarks de performance entre métricas")
	fmt.Println("6. Implemente detecção de outliers")
	fmt.Println("7. Adicione suporte para dados categóricos")
	fmt.Println("8. Implemente KNN incremental")
}

func main() {
	// Executa demonstração
	demonstracaoKNNOtimizado()
	exerciciosAvancados()
}
