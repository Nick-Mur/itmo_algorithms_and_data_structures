# Задача 3: Сортировка вставками по убыванию

## Описание

В данной задаче реализуется алгоритм сортировки вставками по убыванию. Алгоритм проходит по элементам массива и вставляет каждый элемент в его правильную позицию среди уже отсортированных элементов, упорядочивая их по убыванию.

### Формат входных данных
- Входные данные находятся в файле `input.txt`.
- Первая строка содержит одно число `n` (1 ≤ n ≤ 1000) — количество элементов в массиве.
- Вторая строка содержит `n` целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле `output.txt` должен содержаться отсортированный массив по убыванию. Все числа должны быть разделены ровно одним пробелом.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта

```
Task-3/
|-- src/
|   |-- input.txt                      # Входные данные
|   |-- insertion_sort_descending.py    # Реализация алгоритма сортировки вставками по убыванию
|   |-- output.txt                     # Выходные данные
|-- tests/
|   |-- test_insertion_sort_descending.py  # Тесты для проверки корректности работы алгоритма
```

## Код задачи

```python
def insertion_sort_descending(arr):
    """
    Функция сортировки массива методом вставки по убыванию.

    :param arr: Список целых чисел для сортировки.
    :return: Отсортированный по убыванию список.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы, которые меньше key, на одну позицию вперед
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == '__main__':
    with open('input.txt') as f:
        n, massive = f.readlines()
    array = insertion_sort_descending(list(map(int, massive.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)
```

## Запуск проекта

1. Перейдите в директорию `src`.
2. Убедитесь, что файл `input.txt` содержит корректные входные данные в указанном формате.
3. Запустите скрипт:
   ```sh
   python insertion_sort_descending.py
   ```
4. Результат выполнения будет записан в файл `output.txt`.

## Тестирование

Для проверки корректности работы программы выполните тесты, находящиеся в директории `tests`.

1. Перейдите в директорию `tests`.
2. Выполните команду:
   ```sh
   python -m unittest test_insertion_sort_descending.py
   ```

### Тесты

```python
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from insertion_sort_descending import insertion_sort_descending

class TestInsertionSortDescending(unittest.TestCase):
    """
    Тесты для сортировки вставками по убыванию.
    """

    def test_insertion_sort_descending(self):
        """
        Проверка корректности работы сортировки вставками по убыванию.
        """
        self.assertEqual(insertion_sort_descending([31, 41, 59, 26, 41, 58]), [59, 58, 41, 41, 31, 26])

if __name__ == '__main__':
    unittest.main()
```

## Пример

### Входные данные (input.txt)
```
6
31 41 59 26 41 58
```

### Выходные данные (output.txt)
```
59 58 41 41 31 26
```
