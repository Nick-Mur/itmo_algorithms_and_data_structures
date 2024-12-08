# Lab5/Task3/tests/tests.py

import unittest
import time
import tracemalloc
from lab5.Task3.src.NetworkPacketsProcessor import NetworkPacketsProcessor

class TestNetworkPacketsProcessor(unittest.TestCase):

    def test_network_packets_simple(self):
        processor = NetworkPacketsProcessor()
        buffer_size = 1
        packets = [(0,3),(3,3),(10,3)]
        tracemalloc.start()
        t_start = time.perf_counter()

        res = processor.network_packets(buffer_size, packets)

        tracemalloc.stop()

        self.assertEqual(res, ['0', '3', '10'])
        self.assertLess(time.perf_counter() - t_start, 2)
        # Проверка памяти опущена тут, можно проверить отдельно


if __name__ == '__main__':
    unittest.main()
