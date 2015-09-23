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
        self.terminal.output('Selection:')
        self.tabulate.tabulate(students)
        self.terminal.requestResponse('Confirm? Y/N ')
        for student in students:
            self.db.convertStudentToLeader(student[1], student[2])

    def processStudentCommands(self, filters):
        self.addStudents(filters)

    def addStudents(self, filters):
        for filter in filters:
            names = filter.split(' ')
            self.db.addStudent(names[0], names[1])