import unittest
from classes import HtmlGenerator


class TestHtmlGenerator(unittest.TestCase):
    def setUp(self):
        self.htmlGenerator = HtmlGenerator.HtmlGenerator()

    def testH1MethodMakesHeading(self):
        heading = self.htmlGenerator.h1('head')
        expected = '<h1>head</h1>'
        self.assertEqual(heading, expected)

    def testListMethodTakesItems(self):
        self.htmlGenerator.list([1,2,3])

    def testListMethodReturnsList(self):
        list = self.htmlGenerator.list([1,2,3])
        expected = '<ul><li>1</li><li>2</li><li>3</li></ul>'
        self.assertEqual(list,expected)