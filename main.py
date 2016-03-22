from bla import isInList, isEven, plusOne
import unittest, sys
import nltk # 3.1

# +--------------------------------------------------------+
# |assertEqual(a, b)          | a == b                     |
# |assertNotEqual(a, b)       | a != b                     |
# |assertTrue(x)              | bool(x) is True            |
# |assertFalse(x)             | bool(x) is False           |
# |assertIs(a, b)             | a is b                     |
# |assertIsNot(a, b)          | a is not b                 |
# |assertIsNone(x)            | x is None                  |
# |assertIsNotNone(x)         | x is not None              |
# |assertIn(a, b)             | a in b                     |
# |assertNotIn(a, b)          | a not in b                 |
# |assertIsInstance(a, b)     | isinstance(a, b)           |
# |assertNotIsInstance(a, b)  | not isinstance(a, b)       |
# +--------------------------------------------------------+

# unutar moje klase imam dvije metode i svaka metoda reprezentira jedan test
# metode moraju pocinjati s "test_" 

class MyTest(unittest.TestCase):

  def test_in_list(self):
    self.assertTrue(isInList(1, [1,2,3]))
    self.assertTrue(isInList(3, [1,2,3]))

  def test_even_numbers(self):
    self.assertTrue(isEven(4))
    self.assertTrue(isEven(6))
    self.assertTrue(isEven(8))

    self.assertFalse(isEven(7))

  def test_plus_one(self):
    self.assertEqual(plusOne(2), 3) # kada pozovem plusOne(2), vratit ce mi 3
    self.assertEqual(plusOne(3), 5)
    self.assertEqual(plusOne(4), 5)
    self.assertEqual(plusOne(5), 6)


'''
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # @unittest.skipIf(float(nltk.__version__) < 3.2,    
    #                  "not supported in this library version")
    # def test_format(self):
    #     # Tests that work for only a certain version of the library.
    #     pass
   

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
'''

if __name__ == '__main__':
    unittest.main(exit=False)

# - programeri znaju da funkcije rade dobro, a i drugi da su funkcije dobro testirane
# - nakon pokretannja, svaka tockica predstavlja jedan test koji je zavrsio uspjesno. F znaci fail
# - napraviti da je jedan test neuspjesan
# - napraviti kao da smo krivo napisali funkciju a dobro testove - znaci da nesto ne valja s testom ili s kodom
# - dobijemo jasan output
# - napraviti jedan error test - isEven bez argumenata

'''
Literatura:
1. https://docs.python.org/2/library/unittest.html
2. http://pythontips.com/2013/11/15/introduction-to-unittest/
'''