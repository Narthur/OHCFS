import unittest
from classes import Factory


class TestFactory(unittest.TestCase):
    def testExists(self):
        factory = Factory.Factory()
        self.assertIsInstance(factory, Factory.Factory)