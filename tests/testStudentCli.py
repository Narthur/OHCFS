import unittest
from classes import StudentCli
from mock import Mock, ReturnValues


class TestStudentCli(unittest.TestCase):
    def setUp(self):
        self.mockedDatabase = Mock()

    def _initWithAddSubCommand(self):
        self.studentCli = StudentCli.StudentCli(self.mockedDatabase,'student','add',['john doe'])

    def testAddsStudent(self):
        self._initWithAddSubCommand()
        self.mockedDatabase.mockCheckCall(0,'addStudent','john','doe')

    def testGetsAllStudentsWhenConverting(self):
        self.studentCli = StudentCli.StudentCli(self.mockedDatabase,'leader','convert',['john doe'])
        self.mockedDatabase.mockCheckCall(0,'getAllStudents')