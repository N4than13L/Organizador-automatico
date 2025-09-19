import os 
import shutil
from pathlib import Path

def organizar_archivos(ruta_origen):
    # definir extenciones por categoria.
    extenciones = {
        'imagenes': ['.jpg','.jpeg', '.png', '.bmp', '.webp', '.gif'],
        'documentos': ['.pdf', '.doc', '.docx', '.txt', '.pptx', '.ppt', '.xls'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'audio': ['.mp3', '.wav', '.flac'],
        'codigo': ['.py', '.js', '.html', '.css', '.ipynb'],
        'datos': ['.csv', '.xlsx', '.sav', '.xlsb'],
        'archivos_comprimidos': ['.zip']
    }

    # crear categorias si no existen
    for categoria in extenciones.keys():
        carpeta = Path(ruta_origen) / categoria 
        carpeta.mkdir(exist_ok=True)

    for archivo in os.listdir(ruta_origen):
        ruta_archivo = Path(ruta_origen) / archivo
        if ruta_archivo.is_file():
            extension = ruta_archivo.suffix.lower()

        # encontrar la categoría correspondiente
        extension = ruta_archivo.suffix.lower()
        for categoria, exts in extenciones.items():
            if extension in exts:
                destino = Path(ruta_origen) / categoria / archivo
                shutil.move(str(ruta_archivo), str(destino))
                print(f'Movido: {archivo} -> {categoria}/')
                break

# Ejecutar
ruta_archivo = str(input("Agrega la ruta de la carpeta a organizar:\n"))

if ruta_archivo != " ":
    organizar_archivos(ruta_archivo)
else:
    print("Debes de poner la direccion del directorio obligatoriamente.")