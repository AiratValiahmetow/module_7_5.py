import os,time

for (dirpath, dirnames, filenames) in os.walk('.'):

    for dirname in dirnames:
        for filename in filenames:
            print(f'Обнаружен файл: {filename}, Путь: {os.path.join(dirpath, filename)}, Размер: {os.path.getsize(filename)} байт, Время изменения: {time.ctime(os.path.getmtime(filename))}, Родительская директория: {os.path.split(os.getcwd())[0]}')