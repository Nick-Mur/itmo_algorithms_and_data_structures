# Lab4/Task13/tests/test_queue.py

import unittest
from lab4.Task13.src.Queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(5)

    def test_empty_queue(self):
        self.assertTrue(self.queue.isEmpty())
        self.assertEqual(self.queue.peek(), None)
        self.assertEqual(self.queue.queue_size(), 0)

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.isEmpty())
        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(self.queue.queue_size(), 1)

    def test_dequeue(self):
        self.queue.dequeue()
        self.assertTrue(self.queue.isEmpty())
        self.assertEqual(self.queue.peek(), None)
        self.assertEqual(self.queue.queue_size(), 0)
        self.assertEqual(self.queue.dequeue(), 'Очередь пуста')

    def test_full(self):
        self.queue.enqueue(20)
        self.queue.enqueue(10)
        self.queue.enqueue(30)
        self.queue.enqueue(40)
        self.queue.enqueue(50)
        self.assertTrue(self.queue.isFull())
        self.assertEqual(self.queue.enqueue(60), 'Очередь переполнена')


if __name__ == '__main__':
    unittest.main()
