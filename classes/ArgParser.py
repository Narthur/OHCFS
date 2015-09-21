class ArgParser:
    def getCommand(self, args):
        firstArg = self._getPreparedArg(args,0)
        if firstArg == 'student':
            return firstArg
        else:
            return None

    def getSubcommand(self, args):
        secondArg = self._getPreparedArg(args,1)
        if secondArg == 'add':
            return secondArg
        else:
            return None

    def _getPreparedArg(self, args, index):
        return args[index].lower()

    def getFilters(self, args):
        filterArgs = args[2:]
        filterString = ' '.join(filterArgs)
        filters = filterString.split(', ')
        return filters