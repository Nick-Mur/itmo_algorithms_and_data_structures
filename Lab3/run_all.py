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


def main():
    """
    Основная функция для запуска всех задач и тестов.
    """
    # Определение путей
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for i in range(6):
        task = os.path.join(current_dir, f'Task{i + 1}', 'main.py')
        tests = os.path.join(current_dir, f'Task{i + 1}', 'tests', 'tests.py')
        run_task(task, f"Задача {i + 1}")
        run_tests(tests, f"Тесты {i + 1}")


if __name__ == '__main__':
    main()
