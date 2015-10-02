import unittest, sys
from classes import Factory, TkGui, StudentCli


class TestFactory(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.Factory()

    def testExists(self):
        self.assertIsInstance(self.factory, Factory.Factory)

    def PASStestMakeGui(self):
        gui = self.factory.makeGui()
        self.assertIsInstance(gui, TkGui.TkGui)

    def PASStestMakeArgParserMakesStudentCli(self):
        sys.argv = ['ohcfs','student','add','john','doe']
        argHandler = self.factory.makeArgHandler()
        self.assertIsInstance(argHandler, StudentCli.StudentCli)

    def testHasMakeWebAppMethod(self):
        self.assertTrue(hasattr(self.factory,'makeWebApp'))
        