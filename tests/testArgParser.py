import unittest
from classes import ArgParser


class TestArgParser(unittest.TestCase):
    def testExists(self):
        ArgParser.ArgParser()