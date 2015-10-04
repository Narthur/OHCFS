import unittest
from classes import SqliteInterface


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mockedSqliteInterface = SqliteInterface.SqliteInterface()

    def testHasExecuteQueryMethod(self):
        self.mockedSqliteInterface.executeQuery('SELECT * FROM vehicle;')
