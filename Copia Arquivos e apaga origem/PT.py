import glob, os, shutil
import time, sys
from pathlib import Path

# Mostra todos os arquivos antes da copia
data_criacao = lambda f: f.stat().st_ctime
data_modificacao = lambda f: f.stat().st_mtime
directory = Path('C:/TOMS')
files = directory.glob('*.txt')
sorted_files = sorted(files, key=data_modificacao, reverse=True)
print('Files Copy')
for f in sorted_files:
    print(f)

# Copia arquivos
#source_dir = 'C:/TOMS'
#dst = 'C:/TOMS_PYTHON/temp_log'
#files = glob.iglob(os.path.join(source_dir, "*.txt"))
#for file in files:
#    if os.path.isfile(file):
#        shutil.copy2(file, dst)
#print('Copy files...')

# Apaga os arquivos da pasta de origem
folder = 'C:/TOMS'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path) #Substitui o remove()
    except Exception as e:
        print(e)
print('Move files to send...')

input('')