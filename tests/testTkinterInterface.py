import unittest
from classes import TkinterInterface


class TestTkinterInterface(unittest.TestCase):
    def setUp(self):
        self.tk = TkinterInterface.TkinterInterface()

    def testHasAddTitleMethod(self):
        self.assertTrue(hasattr(self.tk, 'addLabel'))