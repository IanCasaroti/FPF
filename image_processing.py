import cv2

def process_image(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)

    # Converter a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar um desfoque gaussiano
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    return blurred_image