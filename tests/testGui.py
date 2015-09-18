import unittest
from classes import Gui
from mock import Mock, ReturnValues


class TestGui(unittest.TestCase):
    def setUp(self):
        self.mockTk = Mock({'getRoot':[]})
        self.mockedGui = Gui.Gui(self.mockTk)

    def testGetsRoot(self):
        self.mockTk.mockCheckCall(0,'getRoot')
