import unittest
from classes import Tabulate


class TestTabulate(unittest.TestCase):
    def setUp(self):
        self.tabulate = Tabulate.Tabulate()

    def testTableClassExists(self):
        self.assertIsInstance(self.tabulate, Tabulate.Tabulate)

    def testHasTabulateMethod(self):
        self.assertTrue(hasattr(self.tabulate, 'tabulate'))
