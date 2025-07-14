"""
OCR Básico - Optical Character Recognition
Implementação simples para reconhecimento de caracteres em imagens
Usando técnicas básicas de processamento de imagem
"""

import numpy as np
from collections import defaultdict
import json


class SimpleOCR:
    def __init__(self):
        """Inicializa o OCR com templates de caracteres"""
        self.char_templates = {}
        self._create_basic_templates()
    
    def _create_basic_templates(self):
        """Cria templates básicos para dígitos 0-9"""
        # Templates simplificados 7x5 para dígitos
        # 1 = pixel preto, 0 = pixel branco
        self.char_templates = {
            '0': [
                [0,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0]
            ],
            '1': [
                [0,0,1,0,0],
                [0,1,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,1,1,1,0]
            ],
            '2': [
                [0,1,1,1,0],
                [1,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,1,0],
                [0,0,1,0,0],
                [0,1,0,0,0],
                [1,1,1,1,1]
            ],
            '3': [
                [0,1,1,1,0],
                [1,0,0,0,1],
                [0,0,0,0,1],
                [0,0,1,1,0],
                [0,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0]
            ],
            '4': [
                [0,0,0,1,0],
                [0,0,1,1,0],
                [0,1,0,1,0],
                [1,0,0,1,0],
                [1,1,1,1,1],
                [0,0,0,1,0],
                [0,0,0,1,0]
            ],
            '5': [
                [1,1,1,1,1],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,1,1,1,0],
                [0,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0]
            ],
            '6': [
                [0,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,0],
                [1,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0]
            ],
            '7': [
                [1,1,1,1,1],
                [0,0,0,0,1],
                [0,0,0,1,0],
                [0,0,1,0,0],
                [0,1,0,0,0],
                [0,1,0,0,0],
                [0,1,0,0,0]
            ],
            '8': [
                [0,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0]
            ],
            '9': [
                [0,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,1],
                [0,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0]
            ]
        }
        
        # Converte para arrays numpy
        for char, template in self.char_templates.items():
            self.char_templates[char] = np.array(template)
    
    def preprocess_image(self, image):
        """
        Pré-processa a imagem para OCR
        
        Args:
            image (numpy.ndarray): Imagem em escala de cinza (0-255)
        
        Returns:
            numpy.ndarray: Imagem binária (0 ou 1)
        """
        # Binarização usando limiar simples
        threshold = 127
        binary_image = (image > threshold).astype(int)
        
        # Inversão se necessário (texto preto em fundo branco)
        if np.mean(binary_image) > 0.5:
            binary_image = 1 - binary_image
        
        return binary_image
    
    def segment_characters(self, binary_image):
        """
        Segmenta caracteres individuais da imagem
        
        Args:
            binary_image (numpy.ndarray): Imagem binária
        
        Returns:
            list: Lista de arrays representando caracteres individuais
        """
        height, width = binary_image.shape
        characters = []
        
        # Projeção horizontal para encontrar separações entre caracteres
        horizontal_projection = np.sum(binary_image, axis=0)
        
        # Encontra início e fim de cada caractere
        in_char = False
        start_col = 0
        
        for col in range(width):
            if horizontal_projection[col] > 0 and not in_char:
                # Início de um caractere
                start_col = col
                in_char = True
            elif horizontal_projection[col] == 0 and in_char:
                # Fim de um caractere
                char_image = binary_image[:, start_col:col]
                if char_image.shape[1] > 0:
                    characters.append(char_image)
                in_char = False
        
        # Adiciona último caractere se necessário
        if in_char:
            char_image = binary_image[:, start_col:]
            if char_image.shape[1] > 0:
                characters.append(char_image)
        
        return characters
    
    def resize_character(self, char_image, target_size=(7, 5)):
        """
        Redimensiona caractere para tamanho padrão
        
        Args:
            char_image (numpy.ndarray): Imagem do caractere
            target_size (tuple): Tamanho alvo (altura, largura)
        
        Returns:
            numpy.ndarray: Caractere redimensionado
        """
        height, width = char_image.shape
        target_height, target_width = target_size
        
        # Redimensionamento simples usando interpolação nearest neighbor
        resized = np.zeros(target_size)
        
        for i in range(target_height):
            for j in range(target_width):
                orig_i = int(i * height / target_height)
                orig_j = int(j * width / target_width)
                resized[i, j] = char_image[orig_i, orig_j]
        
        return resized
    
    def match_character(self, char_image):
        """
        Reconhece um caractere comparando com templates
        
        Args:
            char_image (numpy.ndarray): Imagem do caractere
        
        Returns:
            tuple: (caractere_reconhecido, confiança)
        """
        # Redimensiona para tamanho padrão
        resized_char = self.resize_character(char_image)
        
        best_match = None
        best_score = -1
        
        # Compara com cada template
        for char, template in self.char_templates.items():
            # Calcula similaridade (correlação cruzada normalizada)
            score = self._calculate_similarity(resized_char, template)
            
            if score > best_score:
                best_score = score
                best_match = char
        
        # Calcula confiança (0-100%)
        confidence = best_score * 100
        
        return best_match, confidence
    
    def _calculate_similarity(self, image1, image2):
        """Calcula similaridade entre duas imagens binárias"""
        # Correlation coefficient
        flat1 = image1.flatten()
        flat2 = image2.flatten()
        
        # Evita divisão por zero
        if np.std(flat1) == 0 or np.std(flat2) == 0:
            return 0.0
        
        correlation = np.corrcoef(flat1, flat2)[0, 1]
        
        # Converte NaN para 0
        if np.isnan(correlation):
            correlation = 0.0
        
        return max(0.0, correlation)  # Apenas valores positivos
    
    def recognize_text(self, image):
        """
        Reconhece texto completo em uma imagem
        
        Args:
            image (numpy.ndarray): Imagem em escala de cinza
        
        Returns:
            dict: Resultado com texto reconhecido e estatísticas
        """
        # Pré-processamento
        binary_image = self.preprocess_image(image)
        
        # Segmentação de caracteres
        characters = self.segment_characters(binary_image)
        
        # Reconhecimento de cada caractere
        recognized_text = ""
        character_confidences = []
        
        for char_image in characters:
            char, confidence = self.match_character(char_image)
            recognized_text += char if char else "?"
            character_confidences.append(confidence)
        
        # Calcula confiança média
        avg_confidence = np.mean(character_confidences) if character_confidences else 0
        
        return {
            'text': recognized_text,
            'confidence': avg_confidence,
            'num_characters': len(characters),
            'character_confidences': character_confidences
        }
    
    def add_template(self, char, template):
        """Adiciona novo template de caractere"""
        self.char_templates[char] = np.array(template)
    
    def save_templates(self, filename):
        """Salva templates em arquivo JSON"""
        templates_dict = {}
        for char, template in self.char_templates.items():
            templates_dict[char] = template.tolist()
        
        with open(filename, 'w') as f:
            json.dump(templates_dict, f, indent=2)
    
    def load_templates(self, filename):
        """Carrega templates de arquivo JSON"""
        with open(filename, 'r') as f:
            templates_dict = json.load(f)
        
        for char, template in templates_dict.items():
            self.char_templates[char] = np.array(template)


def create_sample_digit_image():
    """Cria uma imagem de exemplo com dígitos"""
    # Cria imagem 7x25 com os dígitos "123"
    image = np.ones((7, 25)) * 255  # Fundo branco
    
    # Digit "1" (colunas 0-4)
    template_1 = np.array([
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,1,0]
    ])
    
    # Digit "2" (colunas 7-11)
    template_2 = np.array([
        [0,1,1,1,0],
        [1,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,1,0,0,0],
        [1,1,1,1,1]
    ])
    
    # Digit "3" (colunas 14-18)
    template_3 = np.array([
        [0,1,1,1,0],
        [1,0,0,0,1],
        [0,0,0,0,1],
        [0,0,1,1,0],
        [0,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]
    ])
    
    # Coloca os dígitos na imagem (0 = preto, 255 = branco)
    for i in range(7):
        for j in range(5):
            if template_1[i, j] == 1:
                image[i, j+1] = 0
            if template_2[i, j] == 1:
                image[i, j+8] = 0
            if template_3[i, j] == 1:
                image[i, j+15] = 0
    
    return image.astype(np.uint8)


# Exemplo de uso
if __name__ == "__main__":
    print("=== OCR Básico - Reconhecimento de Caracteres ===")
    
    # Cria instância do OCR
    ocr = SimpleOCR()
    
    # Cria imagem de exemplo
    sample_image = create_sample_digit_image()
    
    print("Imagem de exemplo criada (7x25 pixels):")
    print("Representação ASCII (0=preto, 1=branco):")
    binary_sample = ocr.preprocess_image(sample_image)
    for row in binary_sample:
        print(''.join(['█' if pixel == 1 else ' ' for pixel in row]))
    
    print(f"\nDimensões da imagem: {sample_image.shape}")
    print(f"Valores únicos: {np.unique(sample_image)}")
    
    # Executa OCR
    result = ocr.recognize_text(sample_image)
    
    print(f"\n=== Resultado do OCR ===")
    print(f"Texto reconhecido: '{result['text']}'")
    print(f"Confiança média: {result['confidence']:.1f}%")
    print(f"Número de caracteres: {result['num_characters']}")
    
    if result['character_confidences']:
        print("\nConfiança por caractere:")
        for i, conf in enumerate(result['character_confidences']):
            char = result['text'][i] if i < len(result['text']) else '?'
            print(f"  Caractere '{char}': {conf:.1f}%")
    
    # Demonstra segmentação
    print(f"\n=== Demonstração de Segmentação ===")
    binary_image = ocr.preprocess_image(sample_image)
    characters = ocr.segment_characters(binary_image)
    
    print(f"Número de caracteres segmentados: {len(characters)}")
    for i, char_img in enumerate(characters):
        print(f"\nCaractere {i+1} (tamanho {char_img.shape}):")
        for row in char_img:
            print(''.join(['█' if pixel == 1 else ' ' for pixel in row]))
    
    # Testa templates individuais
    print(f"\n=== Templates de Caracteres ===")
    print("Templates disponíveis:", list(ocr.char_templates.keys()))
    
    # Mostra template do dígito "5"
    print("\nTemplate do dígito '5':")
    template_5 = ocr.char_templates['5']
    for row in template_5:
        print(''.join(['█' if pixel == 1 else ' ' for pixel in row]))
    
    # Demonstra adição de novo template
    print(f"\n=== Adição de Novo Template ===")
    # Template simples para letra "A"
    template_a = [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1]
    ]
    
    ocr.add_template('A', template_a)
    print("Template 'A' adicionado com sucesso!")
    print("Templates disponíveis:", list(ocr.char_templates.keys()))
