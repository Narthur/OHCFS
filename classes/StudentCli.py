class StudentCli:
    def __init__(self, db, command, subCommand, filters):
        self.db = db
        self.processCommands(command, filters)

    def processCommands(self, command, filters):
        if command == 'student':
            self.processStudentCommands(filters)
        else:
            students = self.db.getAllStudents()
            matches = []
            for filter in filters:
                firstName = filter[0]
                lastName = filter[1]


    def processStudentCommands(self, filters):
        for filter in filters:
            names = filter.split(' ')
            self.db.addStudent(names[0], names[1])