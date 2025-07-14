<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=00B894&height=120&section=header&text=Fourier%20Transform&fontSize=35&fontColor=fff&animation=twinkling&fontAlignY=40&desc=Análise%20Espectral%20e%20Processamento%20de%20Sinais&descAlignY=65&descSize=16">

</div>

# Transformada de Fourier

## Descrição

A Transformada de Fourier é uma operação matemática fundamental que decompõe um sinal em suas componentes de frequência. É amplamente usada em processamento digital de sinais, análise de imagens, compressão de dados e muitas outras aplicações científicas e de engenharia.

## Como Funciona

A transformada converte um sinal do domínio do tempo (ou espaço) para o domínio da frequência, revelando quais frequências estão presentes no sinal e suas respectivas amplitudes e fases.

### Fórmula Matemática

**DFT (Discrete Fourier Transform):**
```
X[k] = Σ(n=0 to N-1) x[n] * e^(-j*2π*k*n/N)
```

**IDFT (Inverse DFT):**
```
x[n] = (1/N) * Σ(k=0 to N-1) X[k] * e^(j*2π*k*n/N)
```

## Algoritmos Implementados

### 1. DFT - Discrete Fourier Transform
- **Complexidade**: O(N²)
- **Uso**: Implementação direta, educacional
- **Ideal para**: Sinais pequenos (N < 100)

### 2. FFT - Fast Fourier Transform
- **Complexidade**: O(N log N)
- **Uso**: Implementação otimizada (Cooley-Tukey)
- **Ideal para**: Sinais grandes, aplicações práticas

## Implementação Disponível

### Python (`fourier_basico.py`)
```python
# Exemplo de uso
from fourier_basico import FourierTransform

ft = FourierTransform()

# Gera sinal de teste
signal = generate_test_signal(freq=10, duration=1.0, sample_rate=100)

# Aplica FFT
X = ft.fft(signal)

# Calcula espectro de magnitude
magnitude = ft.magnitude_spectrum(X)

# Encontra frequências dominantes
frequencies = ft.frequency_bins(len(X), sample_rate=100)
```

## Complexidade Computacional

| Algoritmo | Complexidade | Comparação |
|-----------|--------------|------------|
| **DFT** | O(N²) | N=1024: ~1M operações |
| **FFT** | O(N log N) | N=1024: ~10K operações |
| **Speedup** | N/log₂(N) | ~100x mais rápido |

## Componentes Principais

### 1. Espectros Derivados
```python
# Espectro de magnitude
magnitude = [abs(x) for x in X]

# Espectro de fase  
phase = [cmath.phase(x) for x in X]

# Espectro de potência
power = [abs(x)**2 for x in X]
```

### 2. Janelas (Windows)
```python
# Reduz vazamento espectral
windowed_signal = ft.apply_window(signal, 'hann')
```

Tipos de janela disponíveis:
- **Hann**: Boa para análise geral
- **Hamming**: Melhor rejeição de lóbulos laterais  
- **Blackman**: Máxima rejeição, menor resolução

### 3. Bins de Frequência
```python
# Calcula frequências correspondentes aos bins
frequencies = ft.frequency_bins(N, sample_rate)
```

## Casos de Uso

### 1. Análise de Sinais
- **Áudio**: Análise espectral, equalização
- **Biomédicos**: EEG, ECG, EMG
- **Vibração**: Análise modal, diagnóstico

### 2. Processamento de Imagens
- **Filtros**: Passa-baixa, passa-alta, passa-banda
- **Compressão**: JPEG, MPEG
- **Reconhecimento**: Características espectrais

### 3. Comunicações
- **Modulação**: OFDM, QAM
- **Análise de Canal**: Resposta em frequência
- **Equalização**: Correção de distorção

### 4. Ciências
- **Astronomia**: Análise de sinais de radiotelescópios
- **Física**: Análise de oscilações quânticas
- **Química**: Espectroscopia NMR, IR

## Propriedades Importantes

### Linearidade
```
F{a*x₁(t) + b*x₂(t)} = a*X₁(f) + b*X₂(f)
```

### Dualidade Tempo-Frequência
- Sinal curto no tempo → Largo em frequência
- Sinal longo no tempo → Estreito em frequência

### Teorema de Parseval
```
Σ|x[n]|² = (1/N) * Σ|X[k]|²
```
A energia se conserva entre domínios.

### Frequência de Nyquist
```
f_nyquist = sample_rate / 2
```
Máxima frequência detectável.

## Exemplo Prático

```python
import math
from fourier_basico import FourierTransform, generate_test_signal

# Criar sinal composto (10Hz + 25Hz)
ft = FourierTransform()
signal1 = generate_test_signal(10, 1.0, 100, 1.0)
signal2 = generate_test_signal(25, 1.0, 100, 0.5)
combined = [s1 + s2 for s1, s2 in zip(signal1, signal2)]

# Aplicar janela e FFT
windowed = ft.apply_window(combined, 'hann')
X = ft.fft(windowed)

# Analisar resultado
magnitude = ft.magnitude_spectrum(X)
frequencies = ft.frequency_bins(len(X), 100)

# Encontrar picos
for i, mag in enumerate(magnitude[:len(magnitude)//2]):
    if mag > 0.1:  # Threshold
        print(f"Frequência: {frequencies[i]:.1f} Hz, Magnitude: {mag:.2f}")
```

## Aplicações Avançadas

### 1. Análise Tempo-Frequência
```python
# STFT - Short-Time Fourier Transform
def stft(signal, window_size, hop_size):
    spectrograms = []
    for i in range(0, len(signal)-window_size, hop_size):
        window = signal[i:i+window_size]
        X = ft.fft(window)
        spectrograms.append(ft.magnitude_spectrum(X))
    return spectrograms
```

### 2. Filtragem Digital
```python
def low_pass_filter(signal, cutoff_freq, sample_rate):
    X = ft.fft(signal)
    frequencies = ft.frequency_bins(len(X), sample_rate)
    
    # Zera frequências acima do cutoff
    for i, freq in enumerate(frequencies):
        if abs(freq) > cutoff_freq:
            X[i] = 0
    
    return ft.ifft(X)
```

### 3. Detecção de Periodicidade
```python
def detect_periodicity(signal):
    X = ft.fft(signal)
    power_spectrum = ft.power_spectrum(X)
    
    # Encontra pico dominante
    max_power_idx = power_spectrum.index(max(power_spectrum[1:]))
    dominant_freq = frequencies[max_power_idx]
    
    return 1.0 / dominant_freq  # Período
```

## Otimizações de Performance

### 1. Zero-Padding
```python
# Aumenta resolução em frequência
padded_signal = signal + [0] * (next_power_of_2 - len(signal))
```

### 2. In-place FFT
```python
# Economiza memória modificando array original
def fft_inplace(x):
    # Implementação que modifica x diretamente
    pass
```

### 3. Paralelização
```python
# FFT pode ser paralelizada para sinais grandes
import multiprocessing
```

## Métricas de Qualidade

| Métrica | Fórmula | Uso |
|---------|---------|-----|
| SNR | 10*log₁₀(P_signal/P_noise) | Qualidade do sinal |
| THD | √(Σharmonics²)/fundamental | Distorção harmônica |
| SFDR | max_spur - fundamental | Faixa dinâmica |

## Limitações e Considerações

### Vazamento Espectral
- **Causa**: Sinal não periódico na janela
- **Solução**: Usar janelas apropriadas

### Resolução vs Tempo
- **Trade-off**: Melhor resolução em frequência = pior localização temporal
- **Solução**: Análise tempo-frequência (wavelets, STFT)

### Efeito Picket-Fence
- **Causa**: Frequência não coincide com bin
- **Solução**: Zero-padding, interpolação

## Benchmarks

| Operação | N=1024 | N=4096 | N=16384 |
|----------|--------|--------|---------|
| DFT | 1ms | 16ms | 256ms |
| FFT | 0.01ms | 0.06ms | 0.25ms |
| Speedup | 100x | 267x | 1024x |

*Tempos aproximados em hardware moderno*

## Executar Exemplo

```bash
cd python/fourier
python fourier_basico.py
```

## Extensões Avançadas

### 1. FFT 2D (Imagens)
```python
def fft_2d(image):
    # FFT em cada linha
    rows_fft = [ft.fft(row) for row in image]
    # FFT em cada coluna
    return [[ft.fft(col) for col in zip(*rows_fft)]]
```

### 2. Convolução via FFT
```python
def convolution_fft(x, h):
    X = ft.fft(x + [0]*len(h))  # Zero-pad
    H = ft.fft(h + [0]*len(x))
    Y = [X[i] * H[i] for i in range(len(X))]
    return ft.ifft(Y)[:len(x)+len(h)-1]
```

### 3. Chirp Z-Transform
```python
# Para análise de faixas específicas de frequência
def czt(x, start_freq, end_freq, num_points):
    # Implementação do CZT
    pass
```

## Referências

- [The Fast Fourier Transform - Brigham](https://www.amazon.com/Fast-Fourier-Transform-Applications/dp/0133075052)
- [Digital Signal Processing - Proakis](https://www.pearson.com/store/p/digital-signal-processing/P100000157833)
- [Numerical Recipes - Press et al.](http://numerical.recipes/)
- [FFTW Library Documentation](http://fftw.org/)

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
  <i>🌊 "A análise de Fourier é uma ferramenta matemática para dissecar funções periódicas" - Jean-Baptiste Joseph Fourier</i>
  <br>
  <i>🌊 "Fourier analysis is a mathematical tool for dissecting periodic functions" - Jean-Baptiste Joseph Fourier</i>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=00B894&height=120&section=footer"/>

</div>
