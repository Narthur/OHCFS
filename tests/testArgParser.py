import unittest
from classes import ArgParser


class TestArgParser(unittest.TestCase):
    def setUp(self):
        self.mockedArgParser = ArgParser.ArgParser()

    def testGetCommand(self):
        command = self.mockedArgParser.getCommand(['student'])
        self.assertEqual(command, 'student')

    def testDoesntReturnInvalidCommand(self):
        command = self.mockedArgParser.getCommand(['BAD_COMMAND'])
        self.assertEqual(command, None)

    def testRecognizesCapitalizedCommand(self):
        command = self.mockedArgParser.getCommand(['Student'])
        self.assertEqual(command, 'student')

    def testGetSubcommand(self):
        subcommand = self.mockedArgParser.getSubcommand(['student','add'])
        self.assertEqual(subcommand, 'add')

    def testGetSimpleFilter(self):
        filters = self.mockedArgParser.getFilters(['student','add','John'])
        self.assertEqual(filters,['John'])

    def testGetFullNameFilter(self):
        filters = self.mockedArgParser.getFilters(['student','add','John','Doe'])
        self.assertEqual(filters,['John Doe'])

    def testGetTwoNames(self):
        filters = self.mockedArgParser.getFilters(['student','add','John,','Jo'])
        self.assertEqual(filters,['John','Jo'])

    def testIgnoresCapitalization(self):
        filters = self.mockedArgParser.getFilters(['student','add','john'])
        self.assertEqual(filters,['john'])