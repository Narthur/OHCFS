import unittest
from classes import TkinterInterface

class testTkinterInterface(unittest.TestCase):
    def testExists(self):
        TkinterInterface.TkinterInterface()

    def testHasGetRootMethod(self):
        tkinter = TkinterInterface.TkinterInterface()
        self.assertTrue(hasattr(tkinter, 'getRoot'))