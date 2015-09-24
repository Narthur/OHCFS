class ArgParser:
    def getCommand(self, args):
        firstArg = self._getPreparedArg(args,1)
        return firstArg if (firstArg == 'student') else None

    def getSubcommand(self, args):
        secondArg = self._getPreparedArg(args,2)
        return secondArg if (secondArg == 'add') else None

    def _getPreparedArg(self, args, index):
        return args[index].lower()

    def getFilters(self, args):
        filterArgs = self._getFilterArgs(args)
        filterString = ' '.join(filterArgs)
        filters = filterString.split(', ')
        isPracticallyEmptyList = len(filters) == 1 and filters[0] == ''
        return [] if isPracticallyEmptyList else filters

    def _getFilterArgs(self, args):
        return args[3:]
