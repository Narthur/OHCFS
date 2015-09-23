class StudentCli:
    def __init__(self, db, terminal, tabulate, command, subCommand, filters):
        self.db = db
        self.terminal = terminal
        self.tabulate = tabulate
        self.processCommands(command, filters)

    def processCommands(self, command, filters):
        if command == 'student':
            self.processStudentCommands(filters)
        else:
            self.processLeaderCommands(filters)

    def processLeaderCommands(self, filters):
        self.convertStudentsToLeaders(filters)

    def convertStudentsToLeaders(self, filters):
        students = self.db.getStudentsFromFilters(filters)
        confirmed = self._confirmSelection(students)
        if confirmed:
            for student in students:
                self.db.convertStudentToLeader(student[1], student[2])

    def _confirmSelection(self, students):
        self.terminal.output('Selection:')
        self.tabulate.tabulate(students)
        response = self.terminal.requestResponse('Confirm? Y/N ')
        return 'yes'.count(response.lower()) > 0

    def processStudentCommands(self, filters):
        self.addStudents(filters)

    def addStudents(self, filters):
        for filter in filters:
            names = filter.split(' ')
            self.db.addStudent(names[0], names[1])