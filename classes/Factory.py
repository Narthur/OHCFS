from classes import Gui, TkinterInterface, StudentCli

class Factory:
    def makeTkinterInterface(self):
        return TkinterInterface.TkinterInterface()

    def makeGui(self):
        tk = self.makeTkinterInterface()
        return Gui.Gui(tk)

    def makeArgHandler(self):
        return StudentCli.StudentCli()