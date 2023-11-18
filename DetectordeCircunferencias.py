import cv2
import numpy as np

# Lectura de la imagen
img = cv2.imread('C:/ImgenTP4IA/motor2.jpg')

# Mostrar la imagen original
cv2.imshow('original', img)
cv2.waitKey(0)

# Convertir la imagen a tonos grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', gray)
cv2.waitKey(0)

# Aplicar filtro pasabajas 3x3
gray_blurred = cv2.blur(gray, (9, 9))
cv2.imshow('Borrosa', gray_blurred)
cv2.waitKey(0)

# Función HoughCircles para detectar circunferencias
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 40, param1= 100, param2= 30, minRadius= 150, maxRadius=170)

#Revisar que el método haya regresado algún valor
if detected_circles is not None:

    #Convertir los parámetros del círculo en enteros de 16 bits
    detected_circles = np.uint16(np.around(detected_circles))

    #Ahora si se recorren todos los circulos detectados
    for pt in detected_circles [0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        #Dibujar la circunferencia
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        #Mostrar los datos de las circunferencias
        print("Centro ({:}, {:}), radio = {:}".format(a, b, r))

        #Dibujar un circulo chico alrededor del centro
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

        #Mostrar las circunferencias encontradas
        cv2.imshow('Circunferencias detectadas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
