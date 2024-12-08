# Lab4/Task13/src/Stack.py

"""Модуль с реализацией стека на основе связного списка."""


class Node:
    """Класс узла для односвязного списка."""

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Стек на основе связного списка."""

    def __init__(self):
        """Инициализация стека."""
        self.top = None

    def isEmpty(self):
        """Проверяет, пуст ли стек."""
        return self.top is None

    def push(self, data):
        """Добавляет элемент на вершину стека."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Удаляет элемент с вершины стека.

        :return: Значение удалённого элемента или None, если стек пуст.
        """
        if self.isEmpty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def display(self):
        """Отображает элементы стека."""
        if self.isEmpty():
            return
        current = self.top
        while current:
            print(current.data, end=", ")
            current = current.next
        print("None")
