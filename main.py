import os

# 1. Conocer el path actual
os.getcwd()

# 2. Ver ficheros y directorios
os.listdir() #Actual directorio
os.listdir(path)

# 3. Eliminación de ficheros
os.remove(path_file)

## Incluyendo try except
try:
    os.remove(path_file)
except OSError as e:
    print(f"Error: {path_file} {e.strerror}")