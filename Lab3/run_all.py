import subprocess
import sys
import os
import glob
from utils.consts import *


def run_task(task_path: str, description: str, cwd: str):
    """
    Запуск задачи и вывод описания.

    :param task_path: Путь к скрипту задачи.
    :param description: Описание задачи.
    :param cwd: Рабочая директория для запуска задачи.
    """
    print(f"Запуск задачи: {description}")
    try:
        subprocess.run([sys.executable, task_path], check=True, cwd=cwd)
        print(f"Задача '{description}' выполнена успешно.\n")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении задачи '{description}'.")
        print(f"Статус: {e.returncode}\n")


def run_tests(test_files, description: str, tests_dir: str):
    """
    Запуск тестов и вывод описания.

    :param test_files: Список путей к тестовым скриптам.
    :param description: Описание тестов.
    :param tests_dir: Рабочая директория для запуска тестов.
    """
    print(f"Запуск тестов: {description}")
    for test_file in test_files:
        if '__init__.py' in test_file: continue
        test_filename = os.path.basename(test_file)
        print(f"Запуск теста: {test_filename}")
        try:
            subprocess.run([sys.executable, '-m', 'unittest', test_filename], check=True, cwd=tests_dir)
            print(f"Тест '{test_filename}' пройден успешно.\n")
        except subprocess.CalledProcessError as e:
            print(f"Тест '{test_filename}' не пройден.")
            print(f"Статус: {e.returncode}\n")


def display_file_contents(file_paths):
    """
    Вывод названий и содержимого указанных txt файлов.

    :param file_paths: Список путей к txt файлам.
    """
    for file_path in file_paths:
        print(f"Содержимое файла '{file_path}':")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                contents = file.read()
                print(contents)
                print("-" * 40)  # Разделитель между файлами
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.\n")
        except Exception as e:
            print(f"Ошибка при чтении файла '{file_path}': {e}\n")


def main():
    """
    Основная функция для запуска всех задач и тестов.
    """
    # Определение текущей директории
    current_dir = os.path.dirname(os.path.abspath(__file__))

    for i in range(1, NUM_TASKS + 1):
        task_dir = os.path.join(current_dir, f'{TASK_DIR_PREFIX}{i}')

        if not os.path.isdir(task_dir):
            continue

        print(f"\n{'=' * 60}\nОбработка {TASK_DIR_PREFIX}{i}\n{'=' * 60}\n")

        # Пути к директориям
        input_dir = os.path.join(task_dir, TXT_DIR, INPUT_FILES_DIR)
        output_dir = os.path.join(task_dir, TXT_DIR, OUTPUT_FILES_DIR)
        tests_dir = os.path.join(task_dir, TESTS_DIR)
        main_script = os.path.join(task_dir, MAIN_SCRIPT)

        # Получение списка файлов
        input_files = glob.glob(os.path.join(input_dir, '*.txt'))
        output_files = glob.glob(os.path.join(output_dir, '*.txt'))
        test_files = glob.glob(os.path.join(tests_dir, '*.py'))

        # Отображение содержимого input_files
        if input_files:
            print("Содержимое файлов input_files:")
            display_file_contents(input_files)
        else:
            print(f"Нет файлов в директории '{input_dir}'.\n")

        # Запуск main.py
        if os.path.isfile(main_script):
            run_task(main_script, f"Задача {i}", cwd=task_dir)
        else:
            print(f"Файл '{main_script}' не найден.\n")

        # Отображение содержимого output_files
        if output_files:
            print("Содержимое файлов output_files:")
            display_file_contents(output_files)
        else:
            print(f"Нет файлов в директории '{output_dir}'.\n")

        # Запуск тестов
        if test_files:
            run_tests(test_files, f"Тесты {i}", tests_dir)
        else:
            print(f"Нет тестовых файлов в директории '{tests_dir}'.\n")


if __name__ == '__main__':
    main()
