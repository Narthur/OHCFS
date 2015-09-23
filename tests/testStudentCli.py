import unittest
from classes import StudentCli
from mock import Mock, ReturnValues


class TestStudentCli(unittest.TestCase):
    def setUp(self):
        self.mockDatabase = Mock({'getStudentsFromFilters':[[0,'John','Doe',0],[1,'Joe','Doe',0]]})
        self.mockTerminalInterface = Mock()

    def _initWithAddSubCommand(self):
        self.studentCli = StudentCli.StudentCli(
            self.mockDatabase,
            self.mockTerminalInterface,
            'student',
            'add',
            ['john doe']
        )

    def _initWithConvertSubCommand(self):
        self.studentCli = StudentCli.StudentCli(
            self.mockDatabase,
            self.mockTerminalInterface,
            'leader',
            'convert',
            ['joh doe']
        )

    def testAddsStudent(self):
        self._initWithAddSubCommand()
        self.mockDatabase.mockCheckCall(0,'addStudent','john','doe')

    def testGetsAllStudentsWhenConverting(self):
        self._initWithConvertSubCommand()
        self.mockDatabase.mockCheckCall(0,'getStudentsFromFilters',['joh doe'])

    def testConvertsStudent(self):
        self._initWithConvertSubCommand()
        self.mockDatabase.mockCheckCall(1,'convertStudentToLeader','John','Doe')

    def testConfirmsSelection(self):
        self._initWithConvertSubCommand()
        self.mockTerminalInterface.mockCheckCall(0,'output','Selection:')