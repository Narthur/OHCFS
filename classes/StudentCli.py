class StudentCli:
    def __init__(self, studentManager, terminal, tabulate, command, subCommand, filters):
        self.studentManager = studentManager
        self.terminal = terminal
        self.tabulate = tabulate
        self.subCommand = subCommand
        self._processCommands(command, filters)

    def _processCommands(self, command, filters):
        if command == 'student':
            self._processStudentCommands(filters)
        else:
            self._processLeaderCommands(filters)

    def _processLeaderCommands(self, filters):
        self._convertStudentsToLeaders(filters)

    def _convertStudentsToLeaders(self, filters):
        students = self.studentManager.getStudentsFromFilters(filters)
        confirmed = self._confirmSelection(students)
        if confirmed:
            for student in students:
                self.studentManager.convertStudentToLeader(student[1], student[2])

    def _confirmSelection(self, students):
        self.terminal.output('Selection:')
        table = self.tabulate.tabulate(students)
        self.terminal.output(table)
        response = self.terminal.requestResponse('Confirm? Y/N ')
        return 'yes'.count(response.lower()) > 0

    def _processStudentCommands(self, filters):
        if self.subCommand == 'add':
            self._addStudents(filters)
        if self.subCommand == 'list':
            self.studentManager.getStudentsFromFilters(filters)

    def _addStudents(self, filters):
        for filter in filters:
            names = filter.split(' ')
            self.studentManager.addStudent(names[0], names[1])