# Lab5/Task3/src/NetworkPacketsProcessor.py

"""Модуль для обработки сетевых пакетов с ограничением буфера."""

class NetworkPacketsProcessor:
    """
    Класс для вычисления времени обработки пакетов в сети.
    """

    @staticmethod
    def network_packets(buffer_size, packets):
        """
        Рассчитывает стартовое время обработки для каждого пакета.

        :param buffer_size: Размер буфера.
        :param packets: Список пакетов в формате (arrival_time, processing_time).
        :return: Список времен начала обработки, либо -1 если пакет отброшен.
        """
        buffer = []
        start_times = []

        for arrival_time, processing_time in packets:
            while buffer and buffer[0] <= arrival_time:
                buffer.pop(0)

            if len(buffer) >= buffer_size:
                start_times.append('-1')
            else:
                if not buffer:
                    start_time = arrival_time
                else:
                    start_time = buffer[-1]
                start_times.append(str(start_time))
                buffer.append(start_time + processing_time)
        return start_times
