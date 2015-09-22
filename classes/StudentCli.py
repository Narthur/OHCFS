class StudentCli:
    def __init__(self, db, command, subCommand, filters):
        self.db = db
        for filter in filters:
            names = filter.split(' ')
            self.db.addStudent(names[0],names[1])