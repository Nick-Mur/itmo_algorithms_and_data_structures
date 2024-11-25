import subprocess
import sys
import os


def run_task(task_path: str, description: str):
    """
    Запуск задачи и вывод описания.

    :param task_path: Путь к скрипту задачи.
    :param description: Описание задачи.
    """
    print(f"Запуск задачи: {description}")
    try:
        subprocess.run([sys.executable, task_path], check=True)
        print(f"Задача '{description}' выполнена успешно.\n")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении задачи '{description}'.\n")
        print(f"Статус: {e.returncode}\n")


def run_tests(test_path: str, description: str):
    """
    Запуск тестов и вывод описания.

    :param test_path: Путь к скрипту тестов.
    :param description: Описание тестов.
    """
    print(f"Запуск тестов: {description}")
    try:
        subprocess.run([sys.executable, '-m', 'unittest', test_path], check=True)
        print(f"Тесты '{description}' пройдены успешно.\n")
    except subprocess.CalledProcessError as e:
        print(f"Тесты '{description}' не пройдены.\n")
        print(f"Статус: {e.returncode}\n")


def display_file_contents(file_paths):
    """
    Вывод названий и содержимого указанных txt файлов.

    :param file_paths: Список путей или сам путь к txt файлам.
    """
    if isinstance(file_paths, str): file_paths = [file_paths]
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
    # Определение путей
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_files = ['output_merge_sort.txt',
            'output_quick.txt',
            'output_randomized_p3_quick.txt',
            'output_randomized_quick.txt']
    for i in range(6):
        input_file = os.path.join(current_dir, f'Task{i + 1}', 'txtf', 'input.txt')
        task = os.path.join(current_dir, f'Task{i + 1}', 'main.py')
        tests = os.path.join(current_dir, f'Task{i + 1}', 'tests', 'tests.py')
        display_file_contents(input_file)
        run_task(task, f"Задача {i + 1}")
        if i == 0:
            for file in output_files:
                output_file = os.path.join(current_dir, f'Task{i + 1}', 'txtf', file)
                display_file_contents(output_file)
        run_tests(tests, f"Тесты {i + 1}")


if __name__ == '__main__':
    main()
