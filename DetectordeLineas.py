import cv2
import numpy as np

# Lectura de la imagen
img = cv2.imread('C:/ImgenTP4IA/motor2.jpg')

# Mostrar la imagen original
cv2.imshow('original', img)
cv2.waitKey(0)

# Convertir la imagen a tonos grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar la detección de bordes por Canny
edges = cv2.Canny(gray, 50, 150)  # Utilizar Canny para detectar bordes
cv2.imshow('Bordes', edges)  # Mostrar la imagen de bordes
cv2.waitKey(0)

# Función HoughLines
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

# Verificar si se encontraron líneas
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Mostrar la imagen con las líneas detectadas
cv2.imshow('Lineas detectadas', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

