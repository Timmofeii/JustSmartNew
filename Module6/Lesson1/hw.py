import os


def sort_files_by_size(directory):
    files = []

    # Проходимся по всем файлам в указанной директории
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Проверяем, является ли объект файлом
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)  # Получаем размер файла в байтах
            files.append((file_name, file_size))

    # Сортируем файлы по размеру в порядке убывания
    sorted_files = sorted(files, key=lambda x: x[1], reverse=True)

    # Выводим результаты
    for file_name, file_size in sorted_files:
        print(f"{file_name}: {file_size} bytes")


# Текущий каталог
current_directory = os.getcwd()
sort_files_by_size(current_directory)