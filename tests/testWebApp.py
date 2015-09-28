import unittest
from classes import WebApp
from mock import Mock, ReturnValues


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.mockHtmlGenerator = Mock()
        self.webApp = WebApp.WebApp(self.mockHtmlGenerator)

    def testHasGetOutput(self):
        self.webApp.getOutput()

    def testGetsHeading(self):
        self.webApp.getOutput()
        self.mockHtmlGenerator.mockCheckCall(0,'h1','OHCFS')