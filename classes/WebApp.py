class WebApp:
    def __init__(self, htmlGenerator):
        self.htmlGenerator = htmlGenerator

    def getOutput(self, fieldStorage):
        self.fieldStorage = fieldStorage
        return self._makeHtml()

    def _makeHtml(self):
        html = '<link rel="stylesheet" type="text/css" href="../style.css">'
        classes = self._makeLinkClasses(None)
        headLink = self.htmlGenerator.link('app.py','OHCFS',classes)
        html += self.htmlGenerator.h1(headLink)
        html += self._navigation()
        return html

    def _navigation(self):
        classes = self._makeLinkClasses('canvassers')
        link = self.htmlGenerator.link('app.py?function=canvassers', 'Manage Canvassers', classes)
        return self.htmlGenerator.list([link])

    def _makeLinkClasses(self,slug):
        isCurrent = self.fieldStorage.getvalue('function') == slug
        return 'current' if isCurrent else None
