import unittest
from classes import WebApp
from mock import Mock, ReturnValues


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.mockFieldStorage = Mock()
        self.mockHtmlGenerator = Mock({
            'h1':'heading',
            'link':'link',
            'list':ReturnValues('navList','canvasserList')
        })
        self.mockCanvasserManager = Mock({'getEveryoneFromFilters':['everyone']})
        self.mockedWebApp = WebApp.WebApp(self.mockHtmlGenerator, self.mockCanvasserManager)

    def _assertContains(self, needle, haystack):
        contains = haystack.count(needle) > 0
        self.assertTrue(contains)

    def _getMockedOutput(self, pageSlug=None):
        if pageSlug is not None:
            self.mockFieldStorage = Mock({'getvalue':pageSlug})
        return self.mockedWebApp.getOutput(self.mockFieldStorage)

    def testOutputsHeading(self):
        self._assertContains('heading',self._getMockedOutput())

    def testMakesCanvassersLink(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(2,'link','app.py?function=canvassers', 'Manage Canvassers', None)

    def testMakesList(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(4,'list',['link','link'])

    def testReturnsList(self):
        self._assertContains('navList',self._getMockedOutput())

    def testMarksNavLinkAsCurrent(self):
        self._getMockedOutput('canvassers')
        self.mockHtmlGenerator.mockCheckCall(2,'link','app.py?function=canvassers','Manage Canvassers','current')

    def testIncludesCss(self):
        css = '<link rel="stylesheet" type="text/css" href="../style.css">'
        self._assertContains(css,self._getMockedOutput())

    def testMakesHeaderLink(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(0,'link','app.py','OHCFS','current')

    def testUsesLinkToMakeHeading(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(1,'h1','link')

    def testMakesDailyLink(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(3,'link','app.py?function=daily', 'Daily', None)

    def testGetsEveryoneFromFilters(self):
        self._getMockedOutput('canvassers')
        self.mockCanvasserManager.mockCheckCall(0,'getEveryoneFromFilters',[])

    def testMakesListFromEveryone(self):
        self._getMockedOutput('canvassers')
        self.mockHtmlGenerator.mockCheckCall(5,'list',['everyone'])

    def testOutputsCanvasserList(self):
        output = self._getMockedOutput('canvassers')
        self._assertContains('canvasserList',output)
