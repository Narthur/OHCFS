import unittest
from classes import CanvasserManager
from mock import Mock  # ReturnValues


class TestCanvasserManager(unittest.TestCase):
    def setUp(self):
        self.mockStudents = [[0, 'John', 'Doe', 0], [1, 'Jo', 'Doe', 1]]
        self.mockDb = Mock({
            'getAllCanvassers': self.mockStudents,
            'getColumnNames': ['names']
        })
        self.mockedCanvasserManager = CanvasserManager.CanvasserManager(self.mockDb)

    def testHasGetFilteredStudentsMethod(self):
        self.mockedCanvasserManager.getEveryoneFromFilters(['John Doe'])

    def testGetFilteredStudents(self):
        filters = ['John Doe']
        students = self.mockedCanvasserManager.getEveryoneFromFilters(filters)
        self.assertEqual(students, [[0, 'John', 'Doe', 0]])

    def testGetFilteredStudentsWithOnlyFirstName(self):
        filters = ['John']
        students = self.mockedCanvasserManager.getEveryoneFromFilters(filters)
        self.assertEqual(students, [[0, 'John', 'Doe', 0]])

    def testGetFilteredStudentsWithPartialName(self):
        filters = ['Joh']
        students = self.mockedCanvasserManager.getEveryoneFromFilters(filters)
        self.assertEqual(students, [[0, 'John', 'Doe', 0]])

    def testConvertStudentToLeaderConvertsStudentToLeader(self):
        self.mockedCanvasserManager.markCanvasserAsLeader('John', 'Doe')
        self.mockDb.mockCheckCall(0, 'markCanvasserAsLeader', 'John', 'Doe')

    def testAddStudentAddsStudent(self):
        self.mockedCanvasserManager.addStudent('John', 'Doe')
        self.mockDb.mockCheckCall(0, 'addStudent', 'John', 'Doe')

    def testGetFilteredStudentsWithEmptyFiltersListReturnsAllStudents(self):
        students = self.mockedCanvasserManager.getEveryoneFromFilters([])
        self.assertEqual(students, self.mockStudents)

    def testGetFilteredStudentsWithoutCaps(self):
        filters = ['john']
        students = self.mockedCanvasserManager.getEveryoneFromFilters(filters)
        self.assertEqual(students, [[0, 'John', 'Doe', 0]])

    def testHasGetCanvasserAttributeNamesMethod(self):
        self.mockedCanvasserManager.getCanvasserAttributeNames()

    def testGetCanvasserAttributeNamesGetsThem(self):
        self.mockedCanvasserManager.getCanvasserAttributeNames()
        self.mockDb.mockCheckCall(0, 'getColumnNames', 'student')

    def testReturnsCanvasserAttributeNames(self):
        actual = self.mockedCanvasserManager.getCanvasserAttributeNames()
        expected = ['names']
        self.assertEqual(actual, expected)
