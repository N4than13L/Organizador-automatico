import os 
import shutil
from pathlib import Path

def organizar_archivos(ruta_origen):
    # definir extenciones por categoria.
    extenciones = {
        # extensiones de imagenes.
        'imagenes': ['.jpg','.jpeg', '.png', '.bmp', '.webp', '.gif'],
        # extensiones de documentos.
        'documentos': ['.pdf', '.doc', '.docx', '.txt', ".dotx", ".dotm", ".rtf", ".odt", ".docm"],
        # extensiones de videos.
        'videos': ['.mp4', '.avi', '.mkv', '.mov', ".avi", "WebM"],
        # extensiones de audio.
        'audio': ['.mp3', '.wav', '.flac'],
        # extensiones de codigo.
        'codigo': ['.py', '.js', '.html', '.css', '.ipynb', ".php", ".c", ".cpp", ".java", ".rb", ".go", ".rs"],
        # extensiones de hojas de calculo y/o datos.
        'datos': ['.csv', '.xlsx', ".xltx", ".xltm", ".xlr", '.sav', '.xlsb', '.xls', '.json', '.xml'],
        # extensiones de aplicaciones e instaladores (imagenes ISO).
        "Instaladores": ['.exe', '.iso', '.bin'],
        # extensiones de fuentes de texto.
        "fuentes": ['.ttf', '.otf', '.fon'],
        # extensiones de presentaciones.
        "presentaciones": ['.ppt', '.pptx', '.key', '.odp'],
        # extensiones de archivos comprimidos.
        'archivos_comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', ".Gzip"],
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
print("================================")
print("  Organizador de Archivos  ")
print("================================")
ruta_archivo = str(input("Agrega la ruta de la carpeta a organizar:\n"))

if ruta_archivo != " ":
    organizar_archivos(ruta_archivo)
else:
    print("Debes de poner la direccion del directorio obligatoriamente.")