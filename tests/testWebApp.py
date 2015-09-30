import unittest
from classes import WebApp
from mock import Mock, ReturnValues


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.mockFieldStorage = Mock()
        self.mockHtmlGenerator = Mock({'h1':'heading'})
        self.webApp = WebApp.WebApp(self.mockHtmlGenerator)

    def testOutputsHeading(self):
        output = self.webApp.getOutput(self.mockFieldStorage)
        self.assertIsNot(output.count('heading'),0)

    def testAcceptsFieldStorage(self):
        self.webApp.getOutput(self.mockFieldStorage)