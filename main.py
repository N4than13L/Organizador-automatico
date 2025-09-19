import os 
import shutil
from pathlib import Path

def organizar_archivos(ruta_origen):
    # definir extenciones por categoria.
    extenciones = {
        'imagenes': ['.jpg','.jpeg', '.png', '.bmp', '.webp', '.gif'],
        'documentos': ['.pdf', '.doc', '.docx', '.txt', '.pptx'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'audio': ['.mp3', '.wav', '.flac'],
        'codigo': ['.py', 'js', '.html', '.css', '.ipynb'],
        'datos': ['.csv', '.xlsx', '.sav']
    }

    # crear categorias si no existen
    for categoria in extenciones.keys():
        carpeta = Path(ruta_origen) / categoria 
        carpeta.mkdir(exist_ok=True)
    
    for archivo in extenciones.keys():
        if os.path.isfile(os.path.join(ruta_origen, archivo)):
            extencion = Path(archivo).suffix.lower()

            # encontrar la categoria correspondiente
            for categoria, exts in extenciones.items():
                if extencion in exts:
                    origen = Path(ruta_origen) / archivo
                    destino = Path(ruta_origen) / categoria / archivo
                    shutil.move(str(origen), str(destino))
                    print(f'Movido: {archivo} -> {categoria}/')
                    break
# Ejecutar
organizar_archivos("C:\\wamp64\\www\\Organizar_automaticamente\\Prueba")
