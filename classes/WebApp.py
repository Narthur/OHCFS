class WebApp:
    def __init__(self, htmlGenerator):
        self.htmlGenerator = htmlGenerator

    def getOutput(self):
        return self.htmlGenerator.h1('OHCFS')