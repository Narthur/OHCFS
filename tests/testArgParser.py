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