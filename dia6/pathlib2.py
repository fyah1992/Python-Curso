from pathlib import Path, PureWindowsPath

carpeta = Path("/home/miguel/Escritorio/alternativ/archivo.txt")
ruta_windows = PureWindowsPath(carpeta)
print(carpeta.name)
print(ruta_windows)