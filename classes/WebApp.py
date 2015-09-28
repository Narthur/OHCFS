class WebApp:
    def __init__(self, htmlGenerator):
        self.htmlGenerator = htmlGenerator

    def getOutput(self):
        self.htmlGenerator.h1('OHCFS')