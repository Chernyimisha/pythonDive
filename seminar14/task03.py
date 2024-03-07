import unittest
from task02 import clear_text


class TestClearText(unittest.TestCase):
    def test_no_changes(self):
        self.assertEqual(clear_text('hello world'),'hell world', msg='строка вернулась с изменениями')

    def test_register(self):
        self.assertEqual(clear_text('Hello world'), 'hello world')

    def test_delete_punctuation(self):
        self.assertEqual(clear_text('Hello world!'), 'hello world')

    def test_delete_foreign_alpha(self):
        self.assertEqual(clear_text('Hello мир'), 'hello ')

    def test_all(self):
        self.assertEqual(clear_text('Hello, world или мир!'), 'hello world ')


if __name__ == '__main__':
    unittest.main(verbosity=2)