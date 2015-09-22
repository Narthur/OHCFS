import unittest
from classes import Database
from mock import Mock, ReturnValues


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.mockSqliteInterface = Mock({'executeQuery':'result'})
        self.mockedDatabase = Database.Database(self.mockSqliteInterface)

    def testGetAllStudentsGetsAllStudents(self):
        self.mockedDatabase.getAllStudents()
        self.mockSqliteInterface.mockCheckCall(0,'executeQuery','SELECT * FROM student')

    def testGetAllStudentsReturnsAllStudents(self):
        students = self.mockedDatabase.getAllStudents()
        self.assertEqual(students,'result')