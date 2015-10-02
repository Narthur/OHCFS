import unittest
from classes import Database
from mock import Mock  # ReturnValues


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.mockStudents = [[0, 'John', 'Doe', 0], [1, 'Jo', 'Doe', 0]]
        self.mockSqliteInterface = Mock({'executeQuery': self.mockStudents})
        self.mockedDatabase = Database.Database(self.mockSqliteInterface)

    def testGetAllStudentsGetsAllStudents(self):
        self.mockedDatabase.getAllCanvassers()
        self.mockSqliteInterface.mockCheckCall(0, 'executeQuery', 'SELECT * FROM student')

    def testGetAllStudentsReturnsAllStudents(self):
        students = self.mockedDatabase.getAllCanvassers()
        self.assertEqual(students, self.mockStudents)

    def testAddsStudent(self):
        self.mockedDatabase.addCanvasser('John', 'Doe')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "INSERT INTO student (firstName, lastName, isLeader) VALUES ('John', 'Doe', 0)"
        )

    def testCapitalizesNames(self):
        self.mockedDatabase.addCanvasser('john', 'doe')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "INSERT INTO student (firstName, lastName, isLeader) VALUES ('John', 'Doe', 0)"
        )

    def testConvertStudentToLeaderConvertsStudent(self):
        self.mockedDatabase.markCanvasserAsLeader('John', 'Doe')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "UPDATE student SET isLeader=1 WHERE firstName='John' AND lastName='Doe'"
        )

    def testConvertStudentToLeaderCapitalizesNames(self):
        self.mockedDatabase.markCanvasserAsLeader('john', 'doe')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "UPDATE student SET isLeader=1 WHERE firstName='John' AND lastName='Doe'"
        )

    def testGetColumnNamesMethodGetsTableColumnData(self):
        self.mockedDatabase.getColumnNames('table')
        self.mockSqliteInterface.mockCheckCall(
            0,
            'executeQuery',
            "PRAGMA table_info(table)"
        )

    def testGetColumnNamesMethodReturnsColumnNames(self):
        mockResult = [
            [0, 'vehicleId', 'INTEGER', 0, None, 1],
            [1, 'make', 'TEXT', 0, None, 0],
            [2, 'model', 'TEXT', 1, None, 0],
            [3, 'year', 'INTEGER', 0, None, 0],
            [4, 'color', 'TEXT', 0, None, 0],
            [5, 'vin', 'TEXT', 0, None, 0]
        ]

        sqlite = Mock({'executeQuery': mockResult})
        expected = ['vehicleId', 'make', 'model', 'year', 'color', 'vin']
        db = Database.Database(sqlite)
        actual = db.getColumnNames('table')
        self.assertEqual(expected, actual)
