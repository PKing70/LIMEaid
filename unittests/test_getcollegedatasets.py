import unittest
from model import getcollegedatasets


class TestDataModel(unittest.TestCase):
	def test_basic_pass(self):
		"""
		This is a basic pass test case scenario to make sure coverage banner works
		"""
		self.assertEqual(1,1)
		
	def test_getmostrecentcohorts(self):
		"""
		This is a placeholder to test get most recent cohorts dataset
		"""
		self.assertEqual(1,1)

SUITE = unittest.TestLoader().loadTestsFromTestCase(TestDataModel)
_ = unittest.TextTestRunner().run(SUITE)
