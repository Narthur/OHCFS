import unittest
from classes import TkGui
from mock import Mock  # ReturnValues


class TestTkGui(unittest.TestCase):
    def PASSsetUp(self):
        self.mockTk = Mock()
        self.mockedGui = TkGui.TkGui(self.mockTk)

    def PASStestAddsTitle(self):
        self.mockTk.mockCheckCall(0, 'addLabel', 'OHCFS')
