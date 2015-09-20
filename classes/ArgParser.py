class ArgParser:
    def getCommand(self, args):
        firstArg = args[0].lower()
        if firstArg == 'student':
            return firstArg
        else:
            return None