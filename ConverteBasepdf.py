import os
import cv2
from pdf2image import convert_from_path
import numpy as np

def convert_pdf_to_image(pdf_path):
    # Converte o PDF em uma lista de imagens PIL
    pil_images = convert_from_path(pdf_path)

    # Converte as imagens PIL em arrays numpy
    numpy_images = [np.array(pil_image) for pil_image in pil_images]

    return numpy_images

def process_image(image):
    # Converte a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecta bordas na imagem
    edges = cv2.Canny(gray_image, threshold1=30, threshold2=100)

    return edges

def save_image(image, output_path):
    # Salva a imagem no caminho de saída
    cv2.imwrite(output_path, image)

def process_pdfs(pdf_directory, output_directory):
    # Obtém uma lista de todos os arquivos PDF no diretório
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        # Converte o PDF em imagens
        images = convert_pdf_to_image(os.path.join(pdf_directory, pdf_file))

        for i, image in enumerate(images):
            # Processa a imagem
            processed_image = process_image(image)

            # Salva a imagem processada
            output_path = os.path.join(output_directory, f'{pdf_file}_{i}.png')
            save_image(processed_image, output_path)


pdf_directory = r'C:\Users\ianca\Desktop\ProjMarmPythonDjango\PDF'
output_directory = r'C:\Users\ianca\Desktop\ProjMarmPythonDjango\Convertidos'

process_pdfs(pdf_directory, output_directory)