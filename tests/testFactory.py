import unittest, sys
from classes import Factory, Gui, StudentCli

class TestFactory(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.Factory()

    def testExists(self):
        self.assertIsInstance(self.factory, Factory.Factory)

    def PASStestMakeGui(self):
        gui = self.factory.makeGui()
        self.assertIsInstance(gui, Gui.Gui)

    def testMakeArgParserMakesStudentCli(self):
        sys.argv = ['student']
        argHandler = self.factory.makeArgHandler()
        self.assertIsInstance(argHandler, StudentCli.StudentCli)