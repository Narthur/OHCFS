class ArgParser:
    def __init__(self):
        pass

    def getCommand(self, args):
        commands = ['student', 'leader']
        firstArg = self._getPreparedArg(args, 1)
        return firstArg if (firstArg in commands) else None

    def getSubCommand(self, args):
        subCommands = ['add', 'list', 'convert']
        secondArg = self._getPreparedArg(args, 2)
        return secondArg if (secondArg in subCommands) else None

    @staticmethod
    def _getPreparedArg(args, index):
        return args[index].lower()

    def getFilters(self, args):
        filterArgs = self._getFilterArgs(args)
        filterString = ' '.join(filterArgs)
        filters = filterString.split(', ')
        isPracticallyEmptyList = len(filters) == 1 and filters[0] == ''
        return [] if isPracticallyEmptyList else filters

    @staticmethod
    def _getFilterArgs(args):
        return args[3:]
