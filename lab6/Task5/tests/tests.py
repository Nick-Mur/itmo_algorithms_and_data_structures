import unittest
from lab6.Task5.src.ElectionsProcessor import ElectionsProcessor

class TestElectionsProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = ElectionsProcessor()

    def test_process_elections(self):
        data = [
            ("ivanov", "900"),
            ("petr", "70"),
            ("tourist", "3")
        ]
        result = self.processor.process_elections(data)
        self.assertEqual(result, ["ivanov 900\n", "petr 70\n", "tourist 3\n"])


if __name__ == '__main__':
    unittest.main()
