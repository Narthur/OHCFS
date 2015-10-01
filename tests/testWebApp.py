import unittest
from classes import WebApp
from mock import Mock, ReturnValues


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.mockFieldStorage = Mock()
        self.mockHtmlGenerator = Mock({'h1':'heading','link':'link','list':'list'})
        self.webApp = WebApp.WebApp(self.mockHtmlGenerator)

    def _assertContains(self, needle, haystack):
        contains = haystack.count(needle) > 0
        self.assertTrue(contains)

    def testOutputsHeading(self):
        output = self.webApp.getOutput(self.mockFieldStorage)
        self._assertContains('heading',output)

    def testMakesCanvassersLink(self):
        self.webApp.getOutput(self.mockFieldStorage)
        self.mockHtmlGenerator.mockCheckCall(1,'link','app.py?function=canvassers', 'Manage Canvassers')

    def testMakesList(self):
        self.webApp.getOutput(self.mockFieldStorage)
        self.mockHtmlGenerator.mockCheckCall(2,'list',['link'])

    def testReturnsList(self):
        output = self.webApp.getOutput(self.mockFieldStorage)
        self._assertContains('list',output)

    def testMarksNavLinkAsCurrent(self):
        fieldStorage = Mock({'getvalue':'canvassers'})
        self.webApp.getOutput(fieldStorage)
        self.mockHtmlGenerator.mockCheckCall(1,'link','app.py?function=canvassers','Manage Canvassers','current')

    def testIncludesHeader(self):
        header = '''Content-Type: text/html
                '''
        output = self.webApp.getOutput(self.mockFieldStorage)
        self._assertContains(header,output)

    def testIncludesCss(self):
        css = '<link rel="stylesheet" type="text/css" href="../style.css">'
        output = self.webApp.getOutput(self.mockFieldStorage)
        self._assertContains(css,output)