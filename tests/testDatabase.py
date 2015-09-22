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

    def testAddsStudent(self):
        self.mockedDatabase.addStudent('John','Doe')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "INSERT INTO student (firstName, lastName, isLeader) VALUES ('John', 'Doe', 0)"
        )

    def testCapitalizesNames(self):
        self.mockedDatabase.addStudent('john','doe')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "INSERT INTO student (firstName, lastName, isLeader) VALUES ('John', 'Doe', 0)"
        )

    def testConvertStudentToLeaderConvertsStudent(self):
        self.mockedDatabase.convertStudentToLeader('John','Doe')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "UPDATE student SET isLeader=1 WHERE firstName='John', lastName='Doe'"
        )

    def testConvertStudentToLeaderCapitalizesNames(self):
        self.mockedDatabase.convertStudentToLeader('john','doe')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "UPDATE student SET isLeader=1 WHERE firstName='John', lastName='Doe'"
        )