from classes import Gui, TkinterInterface, StudentCli, ArgParser, Database, SqliteInterface
from classes import TerminalInterface, Tabulate, CanvasserManager, WebApp, HtmlGenerator
import sys


class Factory:
    def __init__(self):
        pass

    @staticmethod
    def makeTkinterInterface():
        return TkinterInterface.TkinterInterface()

    def makeGui(self):
        tk = self.makeTkinterInterface()
        return Gui.Gui(tk)

    @staticmethod
    def makeSqliteInterface():
        return SqliteInterface.SqliteInterface()

    def makeDatabase(self):
        sqlite = self.makeSqliteInterface()
        return Database.Database(sqlite)

    @staticmethod
    def makeTerminalInterface():
        return TerminalInterface.TerminalInterface()

    @staticmethod
    def makeTabulate():
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
        subCommand = argParser.getSubCommand(args)
        filters = argParser.getFilters(args)
        return StudentCli.StudentCli(
            canvasserManager,
            terminal,
            tabulate,
            command,
            subCommand,
            filters
        )

    @staticmethod
    def makeArgParser():
        return ArgParser.ArgParser()

    @staticmethod
    def makeHtmlGenerator():
        return HtmlGenerator.HtmlGenerator()

    def makeWebApp(self, fieldStorage):
        htmlGenerator = self.makeHtmlGenerator()
        canvasserManager = self.makeCanvasserManager()
        return WebApp.WebApp(fieldStorage, htmlGenerator, canvasserManager)
