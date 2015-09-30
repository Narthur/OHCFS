import unittest
from classes import HtmlGenerator


class TestHtmlGenerator(unittest.TestCase):
    def setUp(self):
        self.htmlGenerator = HtmlGenerator.HtmlGenerator()

    def testH1MethodMakesHeading(self):
        heading = self.htmlGenerator.h1('head')
        expected = '<h1>head</h1>'
        self.assertEqual(heading, expected)