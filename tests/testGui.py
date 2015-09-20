import unittest
from classes import Gui
from mock import Mock, ReturnValues


class TestGui(unittest.TestCase):
    def PASSsetUp(self):
        self.mockTk = Mock()
        self.mockedGui = Gui.Gui(self.mockTk)

    def PASStestAddsTitle(self):
        self.mockTk.mockCheckCall(0,'addLabel','OHCFS')
