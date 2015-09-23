class TerminalInterface():
    def output(self, text):
        print text

    def requestResponse(self, text):
        return raw_input(text + ' ')

    def outputMainHead(self, text):
        head = self._makeMainHead(text)
        for row in head:
            self.output(row)

    def _makeMainHead(self, text):
        length = 30
        bar = length * '='
        centeredName = text.center(length)
        return ['',bar,centeredName,bar]