from classes import Gui, TkinterInterface, StudentCli, ArgParser, Database, SqliteInterface
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

    def makeArgHandler(self):
        db = self.makeDatabase()
        args = sys.argv
        argParser = self.makeArgParser()
        command = argParser.getCommand(args)
        subCommand = argParser.getSubcommand(args)
        filters = argParser.getFilters(args)
        return StudentCli.StudentCli(db, command, subCommand, filters)

    def makeArgParser(self):
        return ArgParser.ArgParser()