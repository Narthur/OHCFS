class WebApp:
    def __init__(self, htmlGenerator):
        self.htmlGenerator = htmlGenerator

    def getOutput(self, fieldStorage):
        html = self.htmlGenerator.h1('OHCFS')
        html += self._navigation()
        return html

    def _navigation(self):
        link = self.htmlGenerator.link('app.py?function=canvassers', 'Manage Canvassers')
        return self.htmlGenerator.list([link])