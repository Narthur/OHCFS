import unittest
from classes import StudentCli
from mock import Mock, ReturnValues


class TestStudentCli(unittest.TestCase):
    def setUp(self):
        self.mockedDatabase = Mock()
        self.studentCli = StudentCli.StudentCli(self.mockedDatabase,'add',['john doe'])

    def testAddsStudent(self):
        self.mockedDatabase.mockCheckCall(0,'addStudent','john','doe')