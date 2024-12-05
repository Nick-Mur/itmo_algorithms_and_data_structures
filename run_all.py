import subprocess
import sys
import os


def run_lab(task_path: str, description: str, cwd: str):
    """
    Запуск задачи и вывод описания.

    :param task_path: Путь к скрипту задачи.
    :param description: Описание задачи.
    :param cwd: Рабочая директория для запуска задачи.
    """
    print(f"Запуск лабораторной: {description}")
    try:
        subprocess.run([sys.executable, task_path], check=True, cwd=cwd)
        print(f"Лабораторная '{description}' выполнена успешно.\n")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении лабораторной '{description}'.")
        print(f"Статус: {e.returncode}\n")


def main():
    """
    Основная функция для запуска всех задач и тестов.
    """
    # Определение текущей директории
    massive = os.listdir()
    massive = [el for el in massive if 'lab' in el]
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for el in massive:
        task_dir = os.path.join(current_dir, el)
        file_path = os.path.join(task_dir, 'run_all.py')
        if os.path.isfile(file_path):
            run_lab(file_path, el, cwd=task_dir)


if __name__ == '__main__':
    main()
