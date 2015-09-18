import unittest
from classes import Gui
from mock import Mock, ReturnValues


class TestGui(unittest.TestCase):
    def setUp(self):
        self.mockTk = Mock()
        self.mockedGui = Gui.Gui(self.mockTk)

    def testAddsTitle(self):
        self.mockTk.mockCheckCall(0,'addLabel','OHCFS')
