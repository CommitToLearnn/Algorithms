"""
Transformada de Fourier - Implementação básica
Algoritmo para análise de frequência de sinais
Inclui DFT (Discrete Fourier Transform) e FFT (Fast Fourier Transform)
"""

import math
import cmath


class FourierTransform:
    def __init__(self):
        """Inicializa a classe de Transformada de Fourier"""
        pass
    
    def dft(self, signal):
        """
        Discrete Fourier Transform (DFT) - Implementação básica
        Complexidade: O(N²)
        
        Args:
            signal (list): Sinal de entrada (números reais ou complexos)
        
        Returns:
            list: Coeficientes de Fourier (números complexos)
        """
        N = len(signal)
        X = []
        
        for k in range(N):
            sum_term = 0
            for n in range(N):
                # e^(-j*2*pi*k*n/N)
                angle = -2j * math.pi * k * n / N
                sum_term += signal[n] * cmath.exp(angle)
            X.append(sum_term)
        
        return X
    
    def idft(self, X):
        """
        Inverse Discrete Fourier Transform (IDFT)
        
        Args:
            X (list): Coeficientes de Fourier
        
        Returns:
            list: Sinal reconstruído
        """
        N = len(X)
        signal = []
        
        for n in range(N):
            sum_term = 0
            for k in range(N):
                # e^(j*2*pi*k*n/N)
                angle = 2j * math.pi * k * n / N
                sum_term += X[k] * cmath.exp(angle)
            signal.append(sum_term / N)
        
        return signal
    
    def fft(self, signal):
        """
        Fast Fourier Transform (FFT) - Algoritmo de Cooley-Tukey
        Complexidade: O(N log N)
        
        Args:
            signal (list): Sinal de entrada (deve ter tamanho potência de 2)
        
        Returns:
            list: Coeficientes de Fourier
        """
        N = len(signal)
        
        # Caso base
        if N <= 1:
            return signal
        
        # Verifica se N é potência de 2
        if N & (N - 1) != 0:
            # Preenche com zeros até a próxima potência de 2
            next_power = 1 << (N - 1).bit_length()
            signal = signal + [0] * (next_power - N)
            N = next_power
        
        # Divide em partes par e ímpar
        even = [signal[i] for i in range(0, N, 2)]
        odd = [signal[i] for i in range(1, N, 2)]
        
        # Recursão
        even_fft = self.fft(even)
        odd_fft = self.fft(odd)
        
        # Combina os resultados
        X = [0] * N
        for k in range(N // 2):
            # Fator de torção (twiddle factor)
            twiddle = cmath.exp(-2j * math.pi * k / N) * odd_fft[k]
            
            X[k] = even_fft[k] + twiddle
            X[k + N // 2] = even_fft[k] - twiddle
        
        return X
    
    def ifft(self, X):
        """
        Inverse Fast Fourier Transform (IFFT)
        
        Args:
            X (list): Coeficientes de Fourier
        
        Returns:
            list: Sinal reconstruído
        """
        N = len(X)
        
        # Conjuga os coeficientes
        X_conj = [x.conjugate() for x in X]
        
        # Aplica FFT
        signal_conj = self.fft(X_conj)
        
        # Conjuga novamente e normaliza
        signal = [x.conjugate() / N for x in signal_conj]
        
        return signal
    
    def magnitude_spectrum(self, X):
        """Calcula o espectro de magnitude"""
        return [abs(x) for x in X]
    
    def phase_spectrum(self, X):
        """Calcula o espectro de fase"""
        return [cmath.phase(x) for x in X]
    
    def power_spectrum(self, X):
        """Calcula o espectro de potência"""
        return [abs(x)**2 for x in X]
    
    def frequency_bins(self, N, sample_rate=1.0):
        """
        Calcula as frequências correspondentes aos bins da FFT
        
        Args:
            N (int): Número de amostras
            sample_rate (float): Taxa de amostragem
        
        Returns:
            list: Frequências em Hz
        """
        return [k * sample_rate / N for k in range(N)]
    
    def apply_window(self, signal, window_type='hann'):
        """
        Aplica janela ao sinal para reduzir vazamento espectral
        
        Args:
            signal (list): Sinal de entrada
            window_type (str): Tipo de janela ('hann', 'hamming', 'blackman')
        
        Returns:
            list: Sinal com janela aplicada
        """
        N = len(signal)
        windowed_signal = []
        
        for n in range(N):
            if window_type == 'hann':
                window_value = 0.5 * (1 - math.cos(2 * math.pi * n / (N - 1)))
            elif window_type == 'hamming':
                window_value = 0.54 - 0.46 * math.cos(2 * math.pi * n / (N - 1))
            elif window_type == 'blackman':
                window_value = 0.42 - 0.5 * math.cos(2 * math.pi * n / (N - 1)) + 0.08 * math.cos(4 * math.pi * n / (N - 1))
            else:
                window_value = 1.0  # Janela retangular
            
            windowed_signal.append(signal[n] * window_value)
        
        return windowed_signal


def generate_test_signal(freq, duration, sample_rate, amplitude=1.0, noise_level=0.0):
    """Gera sinal de teste senoidal com ruído opcional"""
    num_samples = int(duration * sample_rate)
    signal = []
    
    for n in range(num_samples):
        t = n / sample_rate
        # Sinal senoidal
        sample = amplitude * math.sin(2 * math.pi * freq * t)
        
        # Adiciona ruído se especificado
        if noise_level > 0:
            import random
            noise = random.gauss(0, noise_level)
            sample += noise
        
        signal.append(sample)
    
    return signal


def find_dominant_frequencies(magnitude_spectrum, frequencies, num_peaks=3):
    """Encontra as frequências dominantes no espectro"""
    # Cria lista de (magnitude, frequência)
    freq_mag_pairs = list(zip(magnitude_spectrum, frequencies))
    
    # Ordena por magnitude (maior primeiro)
    freq_mag_pairs.sort(key=lambda x: x[0], reverse=True)
    
    # Retorna as primeiras num_peaks frequências
    dominant_freqs = []
    for i in range(min(num_peaks, len(freq_mag_pairs))):
        magnitude, freq = freq_mag_pairs[i]
        if magnitude > 0.1:  # Filtra componentes muito pequenas
            dominant_freqs.append((freq, magnitude))
    
    return dominant_freqs


# Exemplo de uso
if __name__ == "__main__":
    print("=== Transformada de Fourier ===")
    
    # Cria instância da transformada
    ft = FourierTransform()
    
    # Parâmetros do sinal
    sample_rate = 100  # Hz
    duration = 1.0     # segundos
    
    # Gera sinal composto (soma de senoides)
    freq1, freq2 = 10, 25  # Hz
    signal1 = generate_test_signal(freq1, duration, sample_rate, amplitude=1.0)
    signal2 = generate_test_signal(freq2, duration, sample_rate, amplitude=0.5)
    
    # Combina os sinais
    combined_signal = [s1 + s2 for s1, s2 in zip(signal1, signal2)]
    
    print(f"Sinal gerado:")
    print(f"  Frequência 1: {freq1} Hz (amplitude 1.0)")
    print(f"  Frequência 2: {freq2} Hz (amplitude 0.5)")
    print(f"  Taxa de amostragem: {sample_rate} Hz")
    print(f"  Duração: {duration} s")
    print(f"  Número de amostras: {len(combined_signal)}")
    
    # Aplicação de janela
    windowed_signal = ft.apply_window(combined_signal, 'hann')
    
    print(f"\n=== Comparação DFT vs FFT ===")
    
    # Aplica DFT (para sinal menor devido à complexidade O(N²))
    small_signal = combined_signal[:16]  # Apenas 16 amostras
    
    import time
    
    # Mede tempo DFT
    start_time = time.time()
    dft_result = ft.dft(small_signal)
    dft_time = time.time() - start_time
    
    # Mede tempo FFT
    start_time = time.time()
    fft_result = ft.fft(small_signal)
    fft_time = time.time() - start_time
    
    print(f"DFT (16 amostras): {dft_time:.6f} segundos")
    print(f"FFT (16 amostras): {fft_time:.6f} segundos")
    print(f"Speedup: {dft_time/fft_time:.2f}x")
    
    # Verifica se os resultados são similares
    max_diff = max(abs(d - f) for d, f in zip(dft_result, fft_result))
    print(f"Diferença máxima DFT vs FFT: {max_diff:.2e}")
    
    # Análise espectral completa com FFT
    print(f"\n=== Análise Espectral ===")
    
    # Aplica FFT ao sinal com janela
    X = ft.fft(windowed_signal)
    
    # Calcula espectros
    magnitude = ft.magnitude_spectrum(X)
    phase = ft.phase_spectrum(X)
    power = ft.power_spectrum(X)
    
    # Calcula frequências correspondentes
    frequencies = ft.frequency_bins(len(X), sample_rate)
    
    # Encontra frequências dominantes
    dominant = find_dominant_frequencies(magnitude, frequencies)
    
    print(f"Frequências dominantes detectadas:")
    for freq, mag in dominant:
        print(f"  {freq:.1f} Hz (magnitude: {mag:.2f})")
    
    # Testa reconstrução do sinal
    print(f"\n=== Teste de Reconstrução ===")
    
    # Reconstrói sinal usando IFFT
    reconstructed = ft.ifft(X)
    
    # Calcula erro de reconstrução (apenas parte real)
    original_real = [x.real if isinstance(x, complex) else x for x in windowed_signal]
    reconstructed_real = [x.real for x in reconstructed]
    
    # Ajusta tamanhos se necessário
    min_len = min(len(original_real), len(reconstructed_real))
    original_real = original_real[:min_len]
    reconstructed_real = reconstructed_real[:min_len]
    
    mse = sum((o - r)**2 for o, r in zip(original_real, reconstructed_real)) / len(original_real)
    
    print(f"Erro quadrático médio de reconstrução: {mse:.2e}")
    print(f"Sinal reconstruído com sucesso: {mse < 1e-10}")
    
    # Demonstração de diferentes janelas
    print(f"\n=== Comparação de Janelas ===")
    
    windows = ['hann', 'hamming', 'blackman']
    
    for window_type in windows:
        windowed = ft.apply_window(combined_signal[:32], window_type)
        X_windowed = ft.fft(windowed)
        magnitude_windowed = ft.magnitude_spectrum(X_windowed)
        
        # Calcula vazamento espectral (energia fora dos picos principais)
        total_energy = sum(magnitude_windowed)
        peak_energy = max(magnitude_windowed)
        leakage = (total_energy - peak_energy) / total_energy * 100
        
        print(f"  Janela {window_type}: vazamento espectral = {leakage:.1f}%")
    
    # Análise de sinal com ruído
    print(f"\n=== Análise com Ruído ===")
    
    # Gera sinal com ruído
    noisy_signal = generate_test_signal(15, 0.5, sample_rate, amplitude=1.0, noise_level=0.3)
    
    # Aplica FFT
    X_noisy = ft.fft(noisy_signal)
    magnitude_noisy = ft.magnitude_spectrum(X_noisy)
    frequencies_noisy = ft.frequency_bins(len(X_noisy), sample_rate)
    
    # Encontra frequências dominantes no sinal ruidoso
    dominant_noisy = find_dominant_frequencies(magnitude_noisy, frequencies_noisy)
    
    print(f"Frequências detectadas em sinal ruidoso:")
    for freq, mag in dominant_noisy[:3]:
        print(f"  {freq:.1f} Hz (magnitude: {mag:.2f})")
    
    print(f"\n=== Estatísticas Finais ===")
    print(f"Tamanho da FFT: {len(X)} pontos")
    print(f"Resolução em frequência: {sample_rate/len(X):.2f} Hz")
    print(f"Frequência de Nyquist: {sample_rate/2:.1f} Hz")
    print(f"Componentes de frequência: {len(X)//2} (devido à simetria)")
