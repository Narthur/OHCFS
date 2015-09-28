import unittest
from classes import TerminalInterface


class TestTerminalInterface(unittest.TestCase):
    def setUp(self):
        self.view = TerminalInterface.TerminalInterface()

    def testViewClassExists(self):
        self.assertIsInstance(self.view, TerminalInterface.TerminalInterface)

    def testOutputHeadExists(self):
        self.assertTrue(hasattr(self.view,'outputMainHead'))