# Lab4/Task13/src/Queue.py

"""Модуль с реализацией очереди на основе связного списка."""


class Node:
    """Класс узла для односвязного списка."""

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """Очередь с ограниченным размером на основе связного списка."""

    def __init__(self, max_size):
        """
        Инициализация очереди.

        :param max_size: Максимальный размер очереди.
        """
        self.first = None
        self.last = None
        self.size = 0
        self.max_size = max_size

    def isEmpty(self):
        """Проверяет, пуста ли очередь."""
        return self.size == 0

    def isFull(self):
        """Проверяет, полна ли очередь."""
        return self.size == self.max_size

    def enqueue(self, value):
        """
        Добавляет элемент в конец очереди.

        :param value: Значение для добавления.
        :return: Сообщение, если очередь переполнена.
        """
        if self.isFull():
            return 'Очередь переполнена'
        new_node = Node(value)
        if self.last is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def dequeue(self):
        """
        Удаляет элемент из начала очереди.

        :return: Значение удалённого элемента или сообщение, если очередь пуста.
        """
        if self.isEmpty():
            return 'Очередь пуста'
        dequeued_value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.size -= 1
        return dequeued_value

    def peek(self):
        """
        Возвращает значение первого элемента без удаления.

        :return: Значение или None, если очередь пуста.
        """
        if self.isEmpty():
            return None
        return self.first.value

    def queue_size(self):
        """Возвращает текущий размер очереди."""
        return self.size
