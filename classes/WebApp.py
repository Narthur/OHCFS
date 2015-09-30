class WebApp:
    def __init__(self, htmlGenerator):
        self.htmlGenerator = htmlGenerator

    def getOutput(self, fieldStorage):
        html = self.htmlGenerator.h1('OHCFS')
        link = self.htmlGenerator.link('app.py?function=canvassers','Manage Canvassers')
        html += self.htmlGenerator.list([link])
        return html