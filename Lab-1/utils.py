# utils.py

def read_input():
    """
    Функция для чтения входных данных из файла 'input.txt'.

    Возвращает список строк без символов перевода строки.
    """
    with open('input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def write_output(*args):
    """
    Функция для записи выходных данных в файл 'output.txt'.

    Принимает переменное количество аргументов и записывает каждый на новой строке.
    """
    with open('output.txt', 'w') as f:
        for arg in args:
            print(arg, file=f)
