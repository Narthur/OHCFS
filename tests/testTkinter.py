import unittest
from classes import Tkinter

class testTkinter(unittest.TestCase):
    def testExists(self):
        Tkinter.Tkinter()

    def testHasGetRootMethod(self):
        tkinter = Tkinter.Tkinter()
        self.assertTrue(hasattr(tkinter, 'getRoot'))