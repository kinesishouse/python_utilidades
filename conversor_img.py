from PIL import Image
import os
import webp

# Ruta del directorio con las imágenes JPG
directorio = "./img"

# Lee todas las imágenes JPG en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".jpg"):
        # Lee la imagen JPG
        ruta_jpg = os.path.join(directorio, archivo)
        imagen_jpg = Image.open(ruta_jpg)

        # Crea la ruta de la imagen WebP
        nombre_webp = os.path.splitext(archivo)[0] + ".webp"
        ruta_webp = os.path.join(directorio, nombre_webp)

        # Convierte la imagen a WebP y guárdala
        imagen_jpg.save(ruta_webp, "WEBP")

        # Borra la imagen JPG original
        os.remove(ruta_jpg)

print("¡Hecho!")
