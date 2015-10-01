import unittest
from classes import WebApp
from mock import Mock, ReturnValues


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.mockFieldStorage = Mock()
        self.mockHtmlGenerator = Mock({'h1':'heading','link':'link','list':'list'})
        self.mockedWebApp = WebApp.WebApp(self.mockHtmlGenerator)

    def _assertContains(self, needle, haystack):
        contains = haystack.count(needle) > 0
        self.assertTrue(contains)

    def _mockedOutput(self):
        return self.mockedWebApp.getOutput(self.mockFieldStorage)

    def testOutputsHeading(self):
        self._assertContains('heading',self._mockedOutput())

    def testMakesCanvassersLink(self):
        self.mockedWebApp.getOutput(self.mockFieldStorage)
        self.mockHtmlGenerator.mockCheckCall(1,'link','app.py?function=canvassers', 'Manage Canvassers', None)

    def testMakesList(self):
        self.mockedWebApp.getOutput(self.mockFieldStorage)
        self.mockHtmlGenerator.mockCheckCall(2,'list',['link'])

    def testReturnsList(self):
        self._assertContains('list',self._mockedOutput())

    def testMarksNavLinkAsCurrent(self):
        fieldStorage = Mock({'getvalue':'canvassers'})
        self.mockedWebApp.getOutput(fieldStorage)
        self.mockHtmlGenerator.mockCheckCall(1,'link','app.py?function=canvassers','Manage Canvassers','current')

    def testIncludesCss(self):
        css = '<link rel="stylesheet" type="text/css" href="../style.css">'
        self._assertContains(css,self._mockedOutput())