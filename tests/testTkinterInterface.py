import unittest
from classes import TkinterInterface

class testTkinterInterface(unittest.TestCase):
    def setUp(self):
        self.tk = TkinterInterface.TkinterInterface()

    def testHasGetRootMethod(self):
        self.assertTrue(hasattr(self.tk, 'getRoot'))