import os
from typing import List, Tuple


class IOHandler:
    """
    Класс для чтения и записи данных из/в файлы.
    """

    @staticmethod
    def get_path(*args: str) -> str:
        """
        Генерирует абсолютный путь, объединяя несколько сегментов.

        :param args: Части пути.
        :return: Полный путь.
        """
        return os.path.abspath(os.path.join(*args))

    @staticmethod
    def read_integer(file_path: str) -> int:
        """
        Читает одно целое число из файла.

        :param file_path: Путь к файлу.
        :return: Целое число.
        """
        with open(IOHandler.get_path(file_path), 'r') as file:
            return int(file.readline())

    @staticmethod
    def read_list(file_path: str) -> List[int]:
        """
        Читает список целых чисел из файла.

        :param file_path: Путь к файлу.
        :return: Список целых чисел.
        """
        with open(IOHandler.get_path(file_path), 'r') as file:
            file.readline()  # Пропустить первую строку, если необходимо
            return list(map(int, file.readline().split()))

    @staticmethod
    def write_list(file_path: str, data: List[int]) -> None:
        """
        Записывает список целых чисел в файл.

        :param file_path: Путь к файлу.
        :param data: Список целых чисел для записи.
        """
        with open(IOHandler.get_path(file_path), 'w') as file:
            file.write(' '.join(map(str, data)))

    @staticmethod
    def read_input_scarecrow_sort(file_path: str) -> Tuple[int, int, List[int]]:
        """
        Читает входные данные для задачи "Сортировка пугалом".

        :param file_path: Путь к входному файлу.
        :return: Кортеж из n, k и списка размеров матрёшек.
        """
        with open(IOHandler.get_path(file_path), 'r') as file:
            first_line = file.readline().strip()
            if not first_line:
                raise ValueError("Входной файл пуст.")
            n, k = map(int, first_line.split())
            second_line = file.readline().strip()
            if not second_line:
                raise ValueError("Входной файл содержит только одну строку.")
            arr = list(map(int, second_line.split()))
            if len(arr) != n:
                raise ValueError(f"Ожидалось {n} элементов, получено {len(arr)}.")
            return n, k, arr

    @staticmethod
    def write_result(file_path: str, result: str) -> None:
        """
        Записывает результат в выходной файл.

        :param file_path: Путь к выходному файлу.
        :param result: Строка результата ("ДА" или "НЕТ").
        """
        with open(IOHandler.get_path(file_path), 'w', encoding='UTF-8') as file:
            file.write(result)

    @staticmethod
    def read_input_point_segments(file_path: str) -> Tuple[int, int, List[Tuple[int, int]], List[int]]:
        """
        Читает входные данные для задачи "Точки и отрезки".

        :param file_path: Путь к входному файлу.
        :return: Кортеж из s, p, списка отрезков и списка точек.
        :raises ValueError: Если данные некорректны.
        """
        with open(IOHandler.get_path(file_path), 'r') as file:
            first_line = file.readline().strip()
            if not first_line:
                raise ValueError("Входной файл пуст.")
            parts = first_line.split()
            if len(parts) != 2:
                raise ValueError("Первая строка должна содержать ровно два числа.")
            try:
                s, p = map(int, parts)
            except ValueError:
                raise ValueError("s и p должны быть целыми числами.")

            segments = []
            for _ in range(s):
                line = file.readline().strip()
                if not line:
                    raise ValueError("Недостаточно строк с отрезками.")
                try:
                    a, b = map(int, line.split())
                except ValueError:
                    raise ValueError("Отрезки должны содержать два целых числа.")
                if a > b:
                    raise ValueError(f"Начало отрезка {a} должно быть меньше или равно его концу {b}.")
                segments.append((a, b))

            last_line = file.readline().strip()
            if not last_line:
                raise ValueError("Входной файл не содержит строку с точками.")
            try:
                points = list(map(int, last_line.split()))
            except ValueError:
                raise ValueError("Координаты точек должны быть целыми числами.")

            if len(points) != p:
                raise ValueError(f"Ожидалось {p} точек, но получено {len(points)}.")

            return s, p, segments, points

    @staticmethod
    def write_output_point_segments(file_path: str, counts: List[int]) -> None:
        """
        Записывает результаты в выходной файл для задачи "Точки и отрезки".

        :param file_path: Путь к выходному файлу.
        :param counts: Список количеств отрезков для каждой точки.
        """
        with open(IOHandler.get_path(file_path), 'w') as file:
            file.write(' '.join(map(str, counts)))

    @staticmethod
    def read_input_h_index(file_path: str) -> List[int]:
        """
        Читает входные данные для задачи "Вычисление H-индекса".

        :param file_path: Путь к входному файлу.
        :return: Список чисел, представляющих количество цитирований каждой публикации.
        :raises ValueError: Если данные некорректны.
        """
        with open(IOHandler.get_path(file_path), 'r') as file:
            line = file.readline().strip()
            if not line:
                raise ValueError("Входной файл пуст.")
            # Заменяем запятые на пробелы и разбиваем строку на числа
            try:
                citations = list(map(int, line.replace(',', ' ').split()))
            except ValueError:
                raise ValueError("Цитирования должны быть целыми числами.")
            return citations

    @staticmethod
    def write_output_h_index(file_path: str, h_index: int) -> None:
        """
        Записывает результат в выходной файл для задачи "Вычисление H-индекса".

        :param file_path: Путь к выходному файлу.
        :param h_index: Вычисленный H-индекс.
        """
        with open(IOHandler.get_path(file_path), 'w') as file:
            file.write(str(h_index) + '\n')

    @staticmethod
    def read_input_product_sum(file_path: str) -> Tuple[int, int, List[int], List[int]]:
        """
        Читает входные данные для задачи "Сумма выбранных произведений".

        :param file_path: Путь к входному файлу.
        :return: Кортеж из n, m, списка A и списка B.
        :raises ValueError: Если данные некорректны.
        """
        with open(IOHandler.get_path(file_path), 'r') as file:
            # Чтение первой строки для n и m
            first_line = file.readline().strip()
            if not first_line:
                raise ValueError("Входной файл пуст.")
            parts = first_line.split()
            if len(parts) != 2:
                raise ValueError("Первая строка должна содержать ровно два числа.")
            try:
                n, m = map(int, parts)
            except ValueError:
                raise ValueError("n и m должны быть целыми числами.")

            # Чтение второй строки для списка A
            second_line = file.readline().strip()
            if not second_line:
                raise ValueError("Входной файл должен содержать строку с элементами A.")
            try:
                A = list(map(int, second_line.split()))
            except ValueError:
                raise ValueError("Элементы списка A должны быть целыми числами.")
            if len(A) != n:
                raise ValueError(f"Ожидалось {n} элементов в списке A, но получено {len(A)}.")

            # Чтение третьей строки для списка B
            third_line = file.readline().strip()
            if not third_line:
                raise ValueError("Входной файл должен содержать строку с элементами B.")
            try:
                B = list(map(int, third_line.split()))
            except ValueError:
                raise ValueError("Элементы списка B должны быть целыми числами.")
            if len(B) != m:
                raise ValueError(f"Ожидалось {m} элементов в списке B, но получено {len(B)}.")

            return n, m, A, B

    @staticmethod
    def write_output_product_sum(file_path: str, total_sum: int) -> None:
        """
        Записывает результат в выходной файл для задачи "Сумма выбранных произведений".

        :param file_path: Путь к выходному файлу.
        :param total_sum: Вычисленная сумма.
        """
        with open(IOHandler.get_path(file_path), 'w') as file:
            file.write(str(total_sum) + '\n')
