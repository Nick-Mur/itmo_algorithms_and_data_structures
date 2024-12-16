# Задача 4: Линейный поиск

## Описание

В данной задаче реализуется алгоритм линейного поиска для нахождения индексов всех вхождений заданного элемента в массив. Если элемент не найден, возвращается `-1`.

### Формат входных данных
- Входные данные находятся в файле `input.txt`.
- Первая строка содержит список целых чисел — массив для поиска.
- Вторая строка содержит целое число `v`, которое нужно найти в массиве.

### Формат выходных данных
- В выходном файле `output.txt` должен содержаться список индексов всех вхождений элемента `v` (индексы начинаются с 1), разделённых запятой и пробелом. Если элемент не найден, выводится `-1`.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта

```
Task-4/
|-- src/
|   |-- input.txt             # Входные данные
|   |-- linear_search.py      # Реализация алгоритма линейного поиска
|   |-- output.txt            # Выходные данные
|-- tests/
|   |-- test_linear_search.py # Тесты для проверки корректности работы алгоритма
```

## Код задачи

```python
def linear_search(arr, v):
    """
    Функция для поиска элемента в массиве с использованием линейного поиска.

    Возвращает индексы всех вхождений элемента v в массив arr или -1, если элемент не найден.

    :param arr: Список целых чисел для поиска.
    :param v: Элемент для поиска.
    :return: Список индексов или -1, если элемент не найден.
    """
    result = list()
    for i, num in enumerate(arr):
        if num == v:
            result.append(str(i + 1))
    return result if result else '-1'

if __name__ == '__main__':
    with open('input.txt') as f:
        massive, v = f.readlines()
    result = linear_search(massive.split(), v)
    result = ', '.join(result) if isinstance(result, list) else '-1'
    with open('output.txt', 'w') as f:
        print(result, file=f)
```

## Запуск проекта

1. Перейдите в директорию `src`.
2. Убедитесь, что файл `input.txt` содержит корректные входные данные в указанном формате.
3. Запустите скрипт:
   ```sh
   python linear_search.py
   ```
4. Результат выполнения будет записан в файл `output.txt`.

## Тестирование

Для проверки корректности работы программы выполните тесты, находящиеся в директории `tests`.

1. Перейдите в директорию `tests`.
2. Выполните команду:
   ```sh
   python -m unittest test_linear_search.py
   ```

### Тесты

```python
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
    """
    Тесты для функции линейного поиска.
    """

    def test_linear_search(self):
        """
        Проверка корректности работы линейного поиска.
        """
        self.assertEqual(linear_search(['10', '20', '30', '40'], '30'), ['3'])
        self.assertEqual(linear_search(['10', '20', '30', '40'], '50'), '-1')
        self.assertEqual(linear_search(['10', '20', '30', '40', '40'], '40'), ['4', '5'])

if __name__ == '__main__':
    unittest.main()
```

## Пример

### Входные данные (input.txt)
```
10 20 30 40
30
```

### Выходные данные (output.txt)
```
3
```
