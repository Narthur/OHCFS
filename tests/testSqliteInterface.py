import unittest
from classes import SqliteInterface


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mockedSqliteInterface = SqliteInterface.SqliteInterface()