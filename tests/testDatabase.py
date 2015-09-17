import unittest
from classes import Database

class testDatabase(unittest.TestCase):
	def setUp(self):
		testDatabase = Database()

# ToDo:
#
# test getStudent
# test every table exists
#
# tableList = ['inventoryRecord', 'student', 'vehicle',
#			 'mileageRecord', 'fuelRecord', 'expense',
#			 'cashOnHandRecord', 'bankTransaction',
#			 'advance', 'dailyStudentRecord', 'book',
#			 'bookSaleRecord']