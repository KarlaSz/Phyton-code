import os
cpu_count = os.cpu_count()
print(f"Masz {cpu_count} watkow")

import os
files = os.listdir('.')
current_dir = os.getcwd()
print(f"Pliki z katalogu {current_dir}: {files}")
os.mkdir("nowy_katalog")
os.rmdir("nowy katalog")

