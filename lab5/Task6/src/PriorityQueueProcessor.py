# Lab5/Task6/src/PriorityQueueProcessor.py

"""Модуль для обработки операций с приоритетной очередью."""

import heapq

class PriorityQueueProcessor:
    """
    Класс для обработки операций с приоритетной очередью:
    - A x: Добавить элемент x.
    - X: Извлечь минимальный элемент.
    - D x y: Уменьшить значение элемента, добавленного в строке x+1, до y.
    """

    def __init__(self):
        self.heap = []        # Мини-куча
        self.element_map = {} # id → значение
        self.id_map = {}      # строка → id элемента
        self.removed = set()  # множество удаленных элементов
        self.current_id = 0   # уникальный id для каждого добавленного элемента

    def process_operations(self, operations):
        """
        Обрабатывает список операций над приоритетной очередью.

        :param operations: Список строк, каждая строка - операция.
        :return: Список результатов для операций X.
        """
        results = []
        for i, operation in enumerate(operations):
            parts = operation.split()
            cmd = parts[0]
            if cmd == "A":
                # Добавляем элемент
                x = int(parts[1])
                heapq.heappush(self.heap, (x, self.current_id))
                self.element_map[self.current_id] = x
                self.id_map[i+1] = self.current_id
                self.current_id += 1

            elif cmd == "X":
                # Извлекаем минимальный
                self._clean_heap()
                if self.heap:
                    _, elem_id = heapq.heappop(self.heap)
                    results.append(str(self.element_map[elem_id]))
                    self.removed.add(elem_id)
                else:
                    results.append("*")

            elif cmd == "D":
                # Уменьшаем значение элемента
                x = int(parts[1]) + 1
                y = int(parts[2])
                elem_id = self.id_map[x]
                self.element_map[elem_id] = y
                heapq.heappush(self.heap, (y, elem_id))

        return results

    def _clean_heap(self):
        """Удаляет из кучи элементы, которые уже были удалены."""
        while self.heap and self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
