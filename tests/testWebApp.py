import unittest
from classes import WebApp


class TestWebApp(unittest.TestCase):
    def setUp(self):
        WebApp.WebApp()

    def testExists(self):
        pass