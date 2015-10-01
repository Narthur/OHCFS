class WebApp:
    def __init__(self, htmlGenerator):
        self.htmlGenerator = htmlGenerator

    def getOutput(self, fieldStorage):
        self.fieldStorage = fieldStorage
        return self._makeHtml()

    def _makeHtml(self):
        html = '<link rel="stylesheet" type="text/css" href="../style.css">'
        html += self.htmlGenerator.h1('OHCFS')
        html += self._navigation()
        return html

    def _navigation(self):
        isCurrent = self.fieldStorage.getvalue('function') == 'canvassers'
        classes = 'current' if isCurrent else None
        link = self.htmlGenerator.link('app.py?function=canvassers', 'Manage Canvassers', classes)
        return self.htmlGenerator.list([link])