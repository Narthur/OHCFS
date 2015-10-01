class WebApp:
    def __init__(self, htmlGenerator):
        self.htmlGenerator = htmlGenerator

    def getOutput(self, fieldStorage):
        self.fieldStorage = fieldStorage
        header = '''Content-Type: text/html
                '''
        html = self._makeHtml()
        return header + html

    def _makeHtml(self):
        html = '<link rel="stylesheet" type="text/css" href="../style.css">'
        html += self.htmlGenerator.h1('OHCFS')
        html += self._navigation()
        return html

    def _navigation(self):
        isCurrent = self.fieldStorage.getvalue('function') == 'canvassers'
        if isCurrent:
            link = self.htmlGenerator.link('app.py?function=canvassers', 'Manage Canvassers', 'current')
        else:
            link = self.htmlGenerator.link('app.py?function=canvassers', 'Manage Canvassers')
        return self.htmlGenerator.list([link])