import unittest
from classes import HtmlGenerator


class TestHtmlGenerator(unittest.TestCase):
    def setUp(self):
        self.htmlGenerator = HtmlGenerator.HtmlGenerator()

    def testH1MethodMakesHeading(self):
        heading = self.htmlGenerator.h1('head')
        expected = '<h1>head</h1>'
        self.assertEqual(heading, expected)

    def testListMethodReturnsList(self):
        list = self.htmlGenerator.list([1,2,3])
        expected = '<ul><li>1</li><li>2</li><li>3</li></ul>'
        self.assertEqual(list,expected)

    def testLinkMethodReturnsLink(self):
        link = self.htmlGenerator.link('google.com','Google')
        expected = '<a href="google.com">Google</a>'
        self.assertEqual(link,expected)

    def testLinkMethodWithClass(self):
        link = self.htmlGenerator.link('google.com','Google','current')
        expected = '<a href="google.com" class="current">Google</a>'
        self.assertEqual(link,expected)

    def testTableMethodReturnsTable(self):
        data = [['cell']]
        expected = '<table><tbody><tr><td>cell</td></tr></tbody></table>'
        table = self.htmlGenerator.table(data)
        self.assertEqual(expected,table)

    def testTableMethodAllowsAdditionOfHeaders(self):
        data = [['cell']]
        heads = ['head']
        expected = '<table><thead><tr><th>head</th></tr></thead><tbody><tr><td>cell</td></tr></tbody></table>'
        table = self.htmlGenerator.table(data, heads)
        self.assertEqual(expected,table)