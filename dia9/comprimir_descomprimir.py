#modulos integrados, zipfile o shutil

import shutil
import zipfile

mi_zip =zipfile.ZipFile('archivo_comprimido.zip','w')
mi_zip.write('texto.txt')
mi_zip.extract()
mi_zip.close()

'''zip_descomprimir = zipfile.ZipFile('archivo_comprimido.zip','r')
zip_descomprimir.extractall()'''

'''carpeta_origen = "D:\\Miguel\\informatica\\Cursos\\programaciónm\\Python-Curso-git\\Python-Curso"

archivo_destino = "Todo_Comprimido"

shutil.make_archive(archivo_destino,'zip',carpeta_origen) #Para comprimir archivo'''

shutil.unpack_archive('Todo_Comprimido.zip','Extraccion Terminada')

