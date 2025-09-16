import random
import os

def random_name():
#берем имена файлов в папке и приобразуем в список
    folder = './test_random_akzamov/test_dir'
    names = os.listdir(folder)

#Выдергиваем и печатаем случайное имя файла
    name = random.choice(names)
    return name