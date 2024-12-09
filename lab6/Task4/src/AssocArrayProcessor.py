"""Модуль для обработки операций над ассоциативным массивом."""

from collections import OrderedDict


class AssocArrayProcessor:
    """
    Класс для обработки команд над ассоциативным массивом.

    Поддерживаемые команды:
    - put x y: добавить или обновить значение по ключу x
    - get x: получить значение по ключу x или <none>
    - prev x: получить значение по предыдущему ключу относительно x
    - next x: получить значение по следующему ключу относительно x
    - delete x: удалить ключ x
    """

    @staticmethod
    def process_commands(commands):
        """
        Обрабатывает список команд.

        :param commands: Список строк команд.
        :return: Список результатов для команд get, prev, next.
        """
        assoc_array = OrderedDict()
        results = []

        for line in commands:
            parts = line.strip().split()
            command = parts[0]

            if command == "put":
                x, y = parts[1], parts[2]
                assoc_array[x] = y

            elif command == "get":
                x = parts[1]
                results.append(assoc_array.get(x, "<none>"))

            elif command == "prev":
                x = parts[1]
                if x in assoc_array:
                    keys = list(assoc_array.keys())
                    idx = keys.index(x)
                    if idx > 0:
                        results.append(assoc_array[keys[idx - 1]])
                    else:
                        results.append("<none>")
                else:
                    results.append("<none>")

            elif command == "next":
                x = parts[1]
                if x in assoc_array:
                    keys = list(assoc_array.keys())
                    idx = keys.index(x)
                    if idx < len(keys) - 1:
                        results.append(assoc_array[keys[idx + 1]])
                    else:
                        results.append("<none>")
                else:
                    results.append("<none>")

            elif command == "delete":
                x = parts[1]
                assoc_array.pop(x, None)

        return results
