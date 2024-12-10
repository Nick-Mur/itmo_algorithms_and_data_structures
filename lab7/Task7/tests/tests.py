import unittest
from lab7.Task7.src.PatternMatcher import PatternMatcher

class TestMatchesPattern(unittest.TestCase):

    def test_exact_match(self):
        self.assertEqual(PatternMatcher.matches_pattern("kitten", "kitten"), "YES")

    def test_question_mark(self):
        self.assertEqual(PatternMatcher.matches_pattern("k?tten", "kitten"), "YES")

    def test_asterisk(self):
        self.assertEqual(PatternMatcher.matches_pattern("*ten", "kitten"), "YES")

    def test_no_match(self):
        self.assertEqual(PatternMatcher.matches_pattern("dog", "cat"), "NO")

    def test_asterisk_and_question(self):
        self.assertEqual(PatternMatcher.matches_pattern("*a?b", "zaab"), "YES")

    def test_empty_pattern(self):
        self.assertEqual(PatternMatcher.matches_pattern("", "kitten"), "NO")

    def test_empty_string(self):
        self.assertEqual(PatternMatcher.matches_pattern("*", ""), "YES")

    def test_empty_both(self):
        self.assertEqual(PatternMatcher.matches_pattern("", ""), "YES")


if __name__ == "__main__":
    unittest.main()
