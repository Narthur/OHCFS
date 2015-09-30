class WebApp:
    def __init__(self, htmlGenerator):
        self.htmlGenerator = htmlGenerator

    def getOutput(self, fieldStorage):
        return self.htmlGenerator.h1('OHCFS')