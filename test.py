import unittest
import main

class TestGame(unittest.TestCase):
    def test_input(self):
        guess = 5
        answer = 5
        result = main.run_guess(5, 5)
        self.assertTrue(result)
        

if __name__ == '__main__':
  unittest.main()
