import unittest
import time

from fibonacci import fibonacciGenerator


class FibonacciTest(unittest.TestCase):
    # Example assertion with message
    # def test_max_length_is_50(self):
    #     with self.assertRaisesRegexp(Exception, 'The maximum length is 50'):
    #         fibonacciGenerator.generateFibonacciSequence(51)

    def test_should_return_zero_for_fibonacci_zero(self):
        result: int = fibonacciGenerator.generateFibonacciSequence(0)
        self.assertEqual(0, result)

    def test_should_return_one_for_fibonacci_1(self):
        result: int = fibonacciGenerator.generateFibonacciSequence(1)
        self.assertEqual(1, result)

    def test_should_return_one_for_fibonacci_2(self):
        result: int = fibonacciGenerator.generateFibonacciSequence(2)
        self.assertEqual(1, result)

    def test_should_return_two_for_fibonacci_3(self):
        result: int = fibonacciGenerator.generateFibonacciSequence(3)
        self.assertEqual(2, result)

    def test_should_return_21_for_fibonacci_8(self):
        result: int = fibonacciGenerator.generateFibonacciSequence(8)
        self.assertEqual(21, result)

    # bonus
    def test_should_test_memoized_is_faster_than_normal(self):
        initialMemo = time.time()
        fibonacciGenerator.generateFibonacciSequence(21)
        endMemo = time.time()
        fibonacciGenerator.generateFibonacciSequence = fibonacciGenerator.Memoize(fibonacciGenerator.generateFibonacciSequence)
        fibonacciGenerator.generateFibonacciSequence(150)
        endSequence = time.time()

        deltaRecursive = endMemo - initialMemo
        deltaMemoized = endSequence - endMemo
        self.assertGreater(0.5, deltaMemoized)
        self.assertGreater(deltaRecursive, deltaMemoized)


if __name__ == '__main__':
    unittest.main()
