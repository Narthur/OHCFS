from classes import Gui,TkinterInterface,StudentCli,ArgParser,Database,SqliteInterface,TerminalInterface
from classes import Tabulate,CanvasserManager,WebApp,HtmlGenerator
import sys


class Factory:
    def makeTkinterInterface(self):
        return TkinterInterface.TkinterInterface()

    def makeGui(self):
        tk = self.makeTkinterInterface()
        return Gui.Gui(tk)

    def makeSqliteInterface(self):
        return SqliteInterface.SqliteInterface()

    def makeDatabase(self):
        sqlite = self.makeSqliteInterface()
        return Database.Database(sqlite)

    def makeTerminalInterface(self):
        return TerminalInterface.TerminalInterface()

    def makeTabulate(self):
        return Tabulate.Tabulate()

    def makeCanvasserManager(self):
        db = self.makeDatabase()
        return CanvasserManager.CanvasserManager(db)

    def makeArgHandler(self):
        canvasserManager = self.makeCanvasserManager()
        terminal = self.makeTerminalInterface()
        tabulate = self.makeTabulate()
        args = sys.argv
        argParser = self.makeArgParser()
        command = argParser.getCommand(args)
        subCommand = argParser.getSubcommand(args)
        filters = argParser.getFilters(args)
        return StudentCli.StudentCli(
            canvasserManager,
            terminal,
            tabulate,
            command,
            subCommand,
            filters
        )

    def makeArgParser(self):
        return ArgParser.ArgParser()

    def makeHtmlGenerator(self):
        return HtmlGenerator.HtmlGenerator()

    def makeWebApp(self, fieldStorage):
        htmlGenerator = self.makeHtmlGenerator()
        canvasserManager = self.makeCanvasserManager()
        return WebApp.WebApp(fieldStorage, htmlGenerator, canvasserManager)