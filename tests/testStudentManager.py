import unittest
from classes import StudentManager
from mock import Mock, ReturnValues


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.mockStudents = [[0,'John','Doe',0],[1,'Jo','Doe',1]]
        self.mockDb = Mock({'getAllStudents':self.mockStudents})
        self.mockedStudentManager = StudentManager.StudentManager(self.mockDb)

    def testHasGetFilteredStudentsMethod(self):
        self.mockedStudentManager.getEveryoneFromFilters(['John Doe'])

    def testGetFilteredStudents(self):
        filters = ['John Doe']
        students = self.mockedStudentManager.getEveryoneFromFilters(filters)
        self.assertEqual(students,[[0,'John','Doe',0]])

    def testGetFilteredStudentsWithOnlyFirstName(self):
        filters = ['John']
        students = self.mockedStudentManager.getEveryoneFromFilters(filters)
        self.assertEqual(students, [[0,'John','Doe',0]])

    def testGetFilteredStudentsWithPartialName(self):
        filters = ['Joh']
        students = self.mockedStudentManager.getEveryoneFromFilters(filters)
        self.assertEqual(students, [[0,'John','Doe',0]])

    def testConvertStudentToLeaderConvertsStudentToLeader(self):
        self.mockedStudentManager.convertStudentToLeader('John','Doe')
        self.mockDb.mockCheckCall(0,'convertStudentToLeader','John','Doe')

    def testAddStudentAddsStudent(self):
        self.mockedStudentManager.addStudent('John','Doe')
        self.mockDb.mockCheckCall(0,'addStudent','John','Doe')

    def testGetFilteredStudentsWithEmptyFiltersListReturnsAllStudents(self):
        students = self.mockedStudentManager.getEveryoneFromFilters([])
        self.assertEqual(students,self.mockStudents)

    def testGetFilteredStudentsWithoutCaps(self):
        filters = ['john']
        students = self.mockedStudentManager.getEveryoneFromFilters(filters)
        self.assertEqual(students, [[0,'John','Doe',0]])