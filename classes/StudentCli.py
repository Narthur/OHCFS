class StudentCli:
    def __init__(self, studentManager, terminal, tabulate, command, subCommand, filters):
        self.studentManager = studentManager
        self.terminal = terminal
        self.tabulate = tabulate
        self.command = command
        self.subCommand = subCommand
        self.filters = filters
        self._processCommands()

    def _processCommands(self):
        if self.command == 'student':
            self._processStudentCommands()
        if self.command == 'leader':
            self._processLeaderCommands()

    def _processLeaderCommands(self):
        self._convertStudentsToLeaders()

    def _convertStudentsToLeaders(self):
        students = self.studentManager.getEveryoneFromFilters(self.filters)
        confirmed = self._confirmSelection(students)
        if confirmed:
            for student in students:
                self.studentManager.markCanvasserAsLeader(student[1], student[2])

    def _confirmSelection(self, students):
        self._displaySelection(students)
        response = self.terminal.requestResponse('Confirm? Y/N ')
        return 'yes'.count(response.lower()) > 0

    def _displaySelection(self, students):
        self.terminal.output('Selection:')
        table = self.tabulate.tabulate(students)
        self.terminal.output(table)

    def _processStudentCommands(self):
        if self.subCommand == 'add':
            self._addCanvasser()
        if self.subCommand == 'list':
            students = self.studentManager.getEveryoneFromFilters(self.filters)
            self._displaySelection(students)

    def _addCanvasser(self):
        for filter in self.filters:
            names = filter.split(' ')
            self.studentManager.addCanvasser(names[0], names[1])
