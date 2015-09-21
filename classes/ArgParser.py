class ArgParser:
    def getCommand(self, args):
        firstArg = self._getPreparedArg(args,0)
        return firstArg if (firstArg == 'student') else None

    def getSubcommand(self, args):
        secondArg = self._getPreparedArg(args,1)
        return secondArg if (secondArg == 'add') else None

    def _getPreparedArg(self, args, index):
        return args[index].lower()

    def getFilters(self, args):
        filterArgs = self._getFilterArgs(args)
        filterString = ' '.join(filterArgs)
        return filterString.split(', ')

    def _getFilterArgs(self, args):
        filterArgs = args[2:]
        preparedArgs = []
        for arg in filterArgs:
            preparedArgs.append(arg.capitalize())
        return preparedArgs
