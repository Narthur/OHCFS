class TerminalInterface:
    def __init__(self):
        pass

    @staticmethod
    def output(text):
        print text

    @staticmethod
    def requestResponse(text):
        return raw_input(text + ' ')

    def outputMainHead(self, text):
        head = self._makeMainHead(text)
        for row in head:
            self.output(row)

    @staticmethod
    def _makeMainHead(text):
        length = 30
        bar = length * '='
        centeredName = text.center(length)
        return ['', bar, centeredName, bar]
