# Лабораторная работа №4: Стек, очередь, связанный список.
### Студент ИТМО, Мурашов Никита Александрович

## Описание

Лабораторная работа посвящена разбору элементарных структур данных, таких как стек, очередь и связанный список.

### Задача 1: Стек
Реализован алгоритм обработки операций добавления и удаления элементов из стека. Входные данные представляют последовательность команд, таких как добавление числа в стек или удаление верхнего элемента. Результатом является список удаленных элементов в порядке выполнения команд.

### Задача 2: Очередь
Реализован алгоритм обработки операций добавления и удаления элементов из очереди. Входные данные — последовательность команд, включающих добавление числа в конец очереди и удаление элемента из начала. Результат — список удаленных элементов в порядке выполнения команд.

### Задача 3: Скобочная последовательность Версия 1
Реализована проверка правильности скобочной последовательности. Алгоритм определяет, является ли данная последовательность корректной, учитывая вложенность и порядок скобок (), []. Результатом является список ответов YES или NO для каждой последовательности.

### Задача 4: Скобочная последовательность Версия 2 
Реализована проверка строк на корректность расстановки скобок трех типов: (), {}, []. Алгоритм возвращает Success для правильной строки или индекс первой ошибки в случае некорректности.

### Задача 5: Очередь с минимумом
Реализован стек с поддержкой получения максимального элемента за константное время. Алгоритм обрабатывает команды добавления, удаления элементов и запроса максимума, возвращая результаты запросов max.

### Задача 8: Постфиксная запись
Реализовано вычисление арифметических выражений в постфиксной записи. Алгоритм выполняет операции сложения, вычитания, умножения, проверяя корректность выражения и ограничения на значения операндов и промежуточных результатов.

---

## Инструкция по запуску

1. Клонируйте репозиторий:
      git clone https://github.com/Nick-Mur/itmo_algorithms_and_data_structures
   
2. Перейдите в папку с лабораторной работой:
      cd "itmo_algorithms_and_data_structures/lab4"
   
3. Запустите все задачи и тесты:
      python run_all.py