from classes import Gui, TkinterInterface

class Factory:
    def makeTkinterInterface(self):
        return TkinterInterface.TkinterInterface()

    def makeGui(self):
        tk = self.makeTkinterInterface()
        return Gui.Gui(tk)