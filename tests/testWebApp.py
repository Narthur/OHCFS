import unittest
from classes import WebApp
from mock import Mock, ReturnValues


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.mockFieldStorage = Mock()
        self.mockHtmlGenerator = Mock({'h1':'heading','link':'link','list':'list'})
        self.webApp = WebApp.WebApp(self.mockHtmlGenerator)

    def testOutputsHeading(self):
        output = self.webApp.getOutput(self.mockFieldStorage)
        self.assertIsNot(output.count('heading'),0)

    def testMakesCanvassersLink(self):
        self.webApp.getOutput(self.mockFieldStorage)
        self.mockHtmlGenerator.mockCheckCall(1,'link','app.py?function=canvassers', 'Manage Canvassers')

    def testMakesList(self):
        self.webApp.getOutput(self.mockFieldStorage)
        self.mockHtmlGenerator.mockCheckCall(2,'list',['link'])

    def testReturnsList(self):
        output = self.webApp.getOutput(self.mockFieldStorage)
        self.assertIsNot(output.count('list'),0)

    def testMarksNavLinkAsCurrent(self):
        fieldStorage = Mock({'getvalue':'canvassers'})
        self.webApp.getOutput(fieldStorage)
        self.mockHtmlGenerator.mockCheckCall(1,'link','app.py?function=canvassers','Manage Canvassers','current')