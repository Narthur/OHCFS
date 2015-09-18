import unittest
from classes import Factory, Gui

class TestFactory(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.Factory()

    def testExists(self):
        self.assertIsInstance(self.factory, Factory.Factory)

    def testMakeGui(self):
        gui = self.factory.makeGui()
        self.assertIsInstance(gui, Gui.Gui)