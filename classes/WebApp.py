class WebApp:
    def __init__(self, htmlGenerator, canvasserManager):
        self.htmlGenerator = htmlGenerator
        self.canvasserManager = canvasserManager

    def getOutput(self, fieldStorage):
        self.fieldStorage = fieldStorage
        return self._pageHead() + self._pageBody()

    def _pageHead(self):
        css = '<link rel="stylesheet" type="text/css" href="../style.css">'
        classes = self._makeLinkClasses(None)
        headLink = self.htmlGenerator.link('app.py', 'OHCFS', classes)
        title = self.htmlGenerator.h1(headLink)
        nav = self._navigation()
        return css + title + nav

    def _pageBody(self):
        if self.fieldStorage.getvalue('function') == 'canvassers':
            canvassers = self.canvasserManager.getEveryoneFromFilters([])
            body = self.htmlGenerator.table(canvassers)
        else:
            body = ''
        return body

    def _navigation(self):
        links = list()
        links.append(self._makeNavLink('canvassers','Manage Canvassers'))
        links.append(self._makeNavLink('daily','Daily'))
        return self.htmlGenerator.list(links)

    def _makeNavLink(self, slug, title):
        classes = self._makeLinkClasses(slug)
        link = self.htmlGenerator.link('app.py?function={}'.format(slug), title, classes)
        return link

    def _makeLinkClasses(self,slug):
        isCurrent = self.fieldStorage.getvalue('function') == slug
        return 'current' if isCurrent else None
