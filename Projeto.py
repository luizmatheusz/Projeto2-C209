# bibliotecas
import cv2 # OpenCV para tratar das imagens
import numpy as np # numpy para tratar dos arrays

# carrega a imagem de fundo (background) e a imagem com objeto em movimento (image)
background = cv2.imread('background.jpg')
foreground = cv2.imread('image.jpg')

# redimensiona as imagens para ter as mesmas dimensões
background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))

# converte as imagens para escala de cinza
background_grayscale = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
foreground_grayscale = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)

# calcula a diferença absoluta entre as imagens (background subtraction)
diff = cv2.absdiff(background_grayscale, foreground_grayscale)

# aplica um limiar (threshold) para destacar as regiões de diferença
_, thresholded = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

# inverte a imagem binária
img_binary = cv2.bitwise_not(thresholded)

# exibe a imagem com o movimento identificado (preto - objeto novo)
cv2.imshow('Detecção do movimento', img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
