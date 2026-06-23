import shutil
import time
from pathlib import Path

# Пути к папкам
folder_to_watch = Path('Derectory')
music_folder = Path('Derectory/Music')
image_folder = Path('Derectory/Image')
document_folder = Path('Derectory/Document')
video_folder = Path('Derectory/Video')

# Форматы нужных файлов
music_extension = '.wav'
image_extension = '.png'
document_extension = '.docx'
video_extension = '.mkv'

print("Ожидание новых файлов...")
while True:

    # Поиск музыки
    for file_path in folder_to_watch.glob(f'*{music_extension}'):
        if file_path.is_file():
            print(f'Обнаружен новый файл: {file_path.name}')

        for file_path in folder_to_watch.iterdir():
            if file_path.is_file() and music_extension.lower():
                new_path = music_folder / file_path.name

                shutil.move(str(file_path), str(new_path))
                print(f"Файл {file_path.name} успешно перемещен в Music")

    # Поиск изображений
    for file_path in folder_to_watch.glob(f'*{image_extension}'):
        if file_path.is_file():
            print(f'Обнаружен новый файл: {file_path.name}')

        for file_path in folder_to_watch.iterdir():
            if file_path.is_file() and image_extension.lower():
                new_path = image_folder / file_path.name

                shutil.move(str(file_path), str(new_path))
                print(f"Файл {file_path.name} успешно перемещен в Image")

     # Поиск документов
    for file_path in folder_to_watch.glob(f'*{document_extension}'):
        if file_path.is_file():
            print(f'Обнаружен новый файл: {file_path.name}')
        for file_path in folder_to_watch.iterdir():
            if file_path.is_file() and document_extension.lower():
                new_path = document_folder / file_path.name

                shutil.move(str(file_path), str(new_path))
                print(f"Файл {file_path.name} успешно перемещен в Document")

    # Поиск видео
    for file_path in folder_to_watch.glob(f'*{video_extension}'):
        if file_path.is_file():
            print(f'Обнаружен новый файл: {file_path.name}')
        for file_path in folder_to_watch.iterdir():
            if file_path.is_file() and video_extension.lower():
                new_path = video_folder / file_path.name

                shutil.move(str(file_path), str(new_path))
                print(f"Файл {file_path.name} успешно перемещен в Video")

    time.sleep(1)
