from PIL import Image
import os

# Ruta del directorio con las imágenes JPG y JPEG
directorio = "./img"

# Lee todas las imágenes JPG o JPEG en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".jpg") or archivo.endswith(".jpeg") or archivo.endswith(".png"):
        # Lee la imagen JPG o JPEG
        ruta_original = os.path.join(directorio, archivo)
        imagen_original = Image.open(ruta_original)

        # Crea la ruta de la imagen WebP
        nombre_webp = os.path.splitext(archivo)[0] + ".webp"
        ruta_webp = os.path.join(directorio, nombre_webp)

        # Convierte la imagen a WebP y guárdala
        imagen_original.save(ruta_webp, "WEBP")

        # Borra la imagen JPG o JPEG original
        os.remove(ruta_original)

print("¡Hecho!")
