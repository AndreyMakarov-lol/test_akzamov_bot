import random
import os


def random_name(name_dir):
#берем имена файлов в папке и приобразуем в список
    folder = f'./test_random_akzamov/{name_dir}'
    names = os.listdir(folder)

#Выдергиваем и печатаем случайное имя файла
    name = random.choice(names)
    file_path = f'./test_random_akzamov/test_dir/{name}'
    return file_path



