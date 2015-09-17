import unittest
from classes import Factory

class MyTestCase(unittest.TestCase):
    def testExists(self):
        factory = Factory.Factory()
        self.assertIsInstance(factory, Factory.Factory)