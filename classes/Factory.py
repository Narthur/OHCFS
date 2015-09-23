from classes import Gui,TkinterInterface,StudentCli,ArgParser,Database,SqliteInterface,TerminalInterface
from classes import Tabulate
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

    def makeArgHandler(self):
        db = self.makeDatabase()
        terminal = self.makeTerminalInterface()
        tabulate = self.makeTabulate()
        args = sys.argv
        argParser = self.makeArgParser()
        command = argParser.getCommand(args)
        subCommand = argParser.getSubcommand(args)
        filters = argParser.getFilters(args)
        return StudentCli.StudentCli(db, terminal, tabulate, command, subCommand, filters)

    def makeArgParser(self):
        return ArgParser.ArgParser()