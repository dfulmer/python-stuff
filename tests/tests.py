import unittest

class TestStringMethods(unittest.TestCase):
        
    def test_begin(self):
        helloworldmessage = 'Hello world!'
        self.assertTrue(helloworldmessage.startswith('Hello'))

    def test_end(self):
        helloworldmessage = 'Hello world!'
        self.assertTrue(helloworldmessage.endswith('world!'))

if __name__ == '__main__':
      unittest.main()
