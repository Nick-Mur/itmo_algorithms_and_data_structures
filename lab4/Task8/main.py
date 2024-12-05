# Task8/main.py

"""Основной скрипт для вычисления выражений в постфиксной записи."""

import os
from lab4.Task8.src.PostfixEvaluator import PostfixEvaluator
from lab4.utils.consts import *
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Основная функция для запуска вычисления постфиксных выражений."""
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    # Создание экземпляра вычислителя
    evaluator = PostfixEvaluator()

    # Чтение и валидация входных данных
    try:
        n, expr = evaluator.read_expression(input_path)
    except (ValueError, IndexError) as e:
        print(f"Ошибка при чтении входных данных: {e}")
        return

    if not evaluator.validate_input(n, expr):
        print("Введите корректные данные")
        return

    # Вычисление выражения
    try:
        result = evaluator.evaluate_postfix(expr)
    except (ValueError, IndexError) as e:
        print(f"Ошибка при вычислении выражения: {e}")
        return

    # Запись результата
    evaluator.write_result(output_path, result)
    print(f"Результат вычисления: {result}")
    print("Обработка завершена. Результат записан в output.txt")


if __name__ == '__main__':
    main()
