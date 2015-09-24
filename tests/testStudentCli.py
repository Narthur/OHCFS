import unittest
from classes import StudentCli
from mock import Mock, ReturnValues


class TestStudentCli(unittest.TestCase):
    def setUp(self):
        self.studentRows = [[0, 'John', 'Doe', 0], [1, 'Joe', 'Doe', 0]]
        self.mockStudentManager = Mock({'getEveryoneFromFilters': self.studentRows})
        self.mockTerminalInterface = Mock({'requestResponse':'Y'})
        self.mockTabulateInterface = Mock({'tabulate':'table'})

    def _initWithAddSubCommand(self):
        self.studentCli = StudentCli.StudentCli(
            self.mockStudentManager,
            self.mockTerminalInterface,
            self.mockTabulateInterface,
            'student',
            'add',
            ['john doe']
        )

    def _initWithConvertSubCommand(self):
        self.studentCli = StudentCli.StudentCli(
            self.mockStudentManager,
            self.mockTerminalInterface,
            self.mockTabulateInterface,
            'leader',
            'convert',
            ['joh doe']
        )

    def _initWithListSubCommand(self):
        self.studentCli = StudentCli.StudentCli(
            self.mockStudentManager,
            self.mockTerminalInterface,
            self.mockTabulateInterface,
            'student',
            'list',
            ['john doe']
        )

    def testAddsStudent(self):
        self._initWithAddSubCommand()
        self.mockStudentManager.mockCheckCall(0,'addStudent','john','doe')

    def testGetsAllStudentsWhenConverting(self):
        self._initWithConvertSubCommand()
        self.mockStudentManager.mockCheckCall(0,'getEveryoneFromFilters',['joh doe'])

    def testConvertsStudent(self):
        self._initWithConvertSubCommand()
        self.mockStudentManager.mockCheckCall(1,'convertStudentToLeader','John','Doe')

    def testOutputsSelectionHead(self):
        self._initWithConvertSubCommand()
        self.mockTerminalInterface.mockCheckCall(0,'output','Selection:')

    def testTabulatesSelection(self):
        self._initWithConvertSubCommand()
        self.mockTabulateInterface.mockCheckCall(0,'tabulate',self.studentRows)

    def testConfirmsSelection(self):
        self._initWithConvertSubCommand()
        self.mockTerminalInterface.mockCheckCall(2,'requestResponse','Confirm? Y/N ')

    def testOutputsTable(self):
        self._initWithConvertSubCommand()
        self.mockTerminalInterface.mockCheckCall(1,'output','table')

    def testListArgGetsStudentsFromFilters(self):
        self._initWithListSubCommand()
        self.mockStudentManager.mockCheckCall(0,'getEveryoneFromFilters',['john doe'])

    def testListArgTabulatesStudents(self):
        self._initWithListSubCommand()
        self.mockTabulateInterface.mockCheckCall(0,'tabulate',self.studentRows)