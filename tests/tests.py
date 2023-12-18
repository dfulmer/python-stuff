import unittest
from helloworld import Helloworld

class HelloWorldTests(unittest.TestCase):
  def test_helloworld(self):
    amessage = Helloworld()
    self.assertEqual(amessage.message, "Hello world!")

  def test_helloworld_beginning(self):
    amessage = Helloworld()
    string_message = str(amessage.message)
    self.assertTrue(string_message.startswith('Hello'))

  def test_helloworld_ending(self):
    amessage = Helloworld()
    string_message = str(amessage.message)
    self.assertTrue(string_message.endswith('world!'))

if __name__ == '__main__':
      unittest.main()
