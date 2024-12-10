# utils/IOHandler.py

"""Класс для обработки ввода-вывода."""

import os


class IOHandler:
    """Обработчик ввода-вывода."""

    @staticmethod
    def get_path(*args):
        """Возвращает корректный путь, объединяя переданные аргументы."""
        return os.path.join(*args)

    @staticmethod
    def read_file(file_path):
        """Считывает содержимое файла."""
        with open(file_path, 'r') as file:
            return file.readlines()

    @staticmethod
    def write_file(file_path, data):
        """Записывает данные в файл."""
        with open(file_path, 'w') as file:
            file.write(data)
