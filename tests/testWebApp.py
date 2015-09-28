import unittest
from classes import WebApp


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.webApp = WebApp.WebApp()

    def testHasGetOutput(self):
        self.webApp.getOutput()