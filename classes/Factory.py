from classes import Gui,TkinterInterface,StudentCli,ArgParser,Database,SqliteInterface,TerminalInterface
from classes import Tabulate,StudentManager,WebApp,HtmlGenerator
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

    def makeStudentManager(self):
        db = self.makeDatabase()
        return StudentManager.StudentManager(db)

    def makeArgHandler(self):
        studentManager = self.makeStudentManager()
        terminal = self.makeTerminalInterface()
        tabulate = self.makeTabulate()
        args = sys.argv
        argParser = self.makeArgParser()
        command = argParser.getCommand(args)
        subCommand = argParser.getSubcommand(args)
        filters = argParser.getFilters(args)
        return StudentCli.StudentCli(studentManager, terminal, tabulate, command, subCommand, filters)

    def makeArgParser(self):
        return ArgParser.ArgParser()

    def makeHtmlGenerator(self):
        return HtmlGenerator.HtmlGenerator()

    def makeWebApp(self):
        htmlGenerator = self.makeHtmlGenerator()
        return WebApp.WebApp(htmlGenerator)