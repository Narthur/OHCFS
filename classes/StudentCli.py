class StudentCli:
    def __init__(self, db, terminal, command, subCommand, filters):
        self.db = db
        self.terminal = terminal
        self.processCommands(command, filters)

    def processCommands(self, command, filters):
        if command == 'student':
            self.processStudentCommands(filters)
        else:
            students = self.db.getStudentsFromFilters(filters)
            self.terminal.output('Selection:')
            for student in students:
                self.db.convertStudentToLeader(student[1],student[2])


    def processStudentCommands(self, filters):
        for filter in filters:
            names = filter.split(' ')
            self.db.addStudent(names[0], names[1])