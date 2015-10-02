import unittest
from classes import ArgParser


class TestArgParser(unittest.TestCase):
    def setUp(self):
        self.mockedArgParser = ArgParser.ArgParser()

    def testGetCommand(self):
        command = self.mockedArgParser.getCommand(['ohcfs', 'student'])
        self.assertEqual(command, 'student')

    def testDoesntReturnInvalidCommand(self):
        command = self.mockedArgParser.getCommand(['ohcfs', 'BAD_COMMAND'])
        self.assertEqual(command, None)

    def testRecognizesCapitalizedCommand(self):
        command = self.mockedArgParser.getCommand(['ohcfs', 'Student'])
        self.assertEqual(command, 'student')

    def testGetSubCommand(self):
        subCommand = self.mockedArgParser.getSubCommand(['ohcfs', 'student', 'add'])
        self.assertEqual(subCommand, 'add')

    def testGetSimpleFilter(self):
        filters = self.mockedArgParser.getFilters(['ohcfs', 'student', 'add', 'John'])
        self.assertEqual(filters, ['John'])

    def testGetFullNameFilter(self):
        filters = self.mockedArgParser.getFilters(['ohcfs', 'student', 'add', 'John', 'Doe'])
        self.assertEqual(filters, ['John Doe'])

    def testGetTwoNames(self):
        filters = self.mockedArgParser.getFilters(['ohcfs', 'student', 'add', 'John,', 'Jo'])
        self.assertEqual(filters, ['John', 'Jo'])

    def testIgnoresCapitalization(self):
        filters = self.mockedArgParser.getFilters(['ohcfs', 'student', 'add', 'john'])
        self.assertEqual(filters, ['john'])

    def testGetFiltersReturnsEmptyListWhenNoneProvided(self):
        filters = self.mockedArgParser.getFilters(['ohcfs', 'student', 'list'])
        self.assertEqual(filters, [])

    def testGetListSubCommand(self):
        subCommand = self.mockedArgParser.getSubCommand(['ohcfs', 'student', 'list'])
        self.assertEqual(subCommand, 'list')

    def testGetConvertSubCommand(self):
        subCommand = self.mockedArgParser.getSubCommand(['ohcfs', 'student', 'convert'])
        self.assertEqual(subCommand, 'convert')

    def testGetLeaderCommand(self):
        command = self.mockedArgParser.getCommand(['ohcfs', 'leader'])
        self.assertEqual(command, 'leader')
