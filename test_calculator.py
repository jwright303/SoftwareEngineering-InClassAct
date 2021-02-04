import unittest
import calculator

class TestCase(unittest.TestCase):
	def test_addition(self):
		result = calculator.addNums(3, 4)
		self.assertEqual(result, 7)

		result = calculator.addNums(-4, 2)
		self.assertEqual(result, -2)
		
		result = calculator.addNums(3.2, 2.9)
		self.assertEqual(result, 6.1)
		return

	def test_multiplication(self):
		result = calculator.multiplyNums(3, 4)
		self.assertEqual(result, 12)
		
		result = calculator.multiplyNums(3, 0)
		self.assertEqual(result, 0)
		
		result = calculator.multiplyNums(-2, 7)
		self.assertEqual(result, -14)
		
		result = calculator.multiplyNums(1.5, 4)
		self.assertEqual(result, 6)
		return

	def test_division(self):
		result = calculator.divideNums(4, 2)
		self.assertEqual(result, 2)
		
		with self.assertRaises(ZeroDivisionError):
			calculator.divideNums(4, 0)
		
		result = calculator.divideNums(2, 0.5)
		self.assertEqual(result, 4)
		return

	def test_subtraction(self):
		result = calculator.subtractNums(3, 4)
		self.assertEqual(result, -1)
		
		result = calculator.subtractNums(2.5, 0.5)
		self.assertEqual(result, 2)
		
		result = calculator.subtractNums(3, -1)
		self.assertEqual(result, 4)
		return


