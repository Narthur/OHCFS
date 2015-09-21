import unittest
from classes import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.mockedDatabase = Database.Database()

    def testHasGetAllStudentsMethod(self):
        self.mockedDatabase.getAllStudents()

# ToDo:
#
# - move Sqlite commands into SqliteInterface
# - finish testing getAllStudents method