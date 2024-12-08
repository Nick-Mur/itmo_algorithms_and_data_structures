# Lab4/Task13/main.py

"""Основной скрипт для проверки работы очереди и стека."""

from lab4.Task13.src.Queue import Queue
from lab4.Task13.src.Stack import Stack
from lab4.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main():
    # Продемонстрируем работу очереди
    print("Демонстрация очереди:")
    queue = Queue(5)
    queue.enqueue(10)
    print("Размер очереди:", queue.queue_size())
    print("Первый элемент:", queue.peek())
    queue.dequeue()
    print("После удаления размер очереди:", queue.queue_size())
    print("Первый элемент:", queue.peek())
    print()

    # Продемонстрируем работу стека
    print("Демонстрация стека:")
    stack = Stack()
    print("Стек пуст:", stack.isEmpty())
    stack.push(10)
    stack.display()
    popped_value = stack.pop()
    print("Извлечён элемент:", popped_value)
    stack.display()
    print("Стек пуст:", stack.isEmpty())
    print()


if __name__ == '__main__':
    main()
