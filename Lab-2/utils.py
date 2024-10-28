# utils.py
import os

def read_input(task):
    """
    Функция для чтения входных данных из файла 'input.txt'.

    Возвращает список строк без символов перевода строки.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task-{task}', 'txtf', 'input.txt'))
    with open(base_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def write_output(task, *args):
    """
    Функция для записи выходных данных в файл 'output.txt'.

    Принимает переменное количество аргументов и записывает каждый на новой строке.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task-{task}', 'txtf', 'output.txt'))
    with open(base_path, 'w') as f:
        for arg in args:
            print(arg, file=f)
