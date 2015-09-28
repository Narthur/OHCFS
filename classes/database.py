class Database:
    def __init__(self, sqliteInterface):
        self.sqlite = sqliteInterface

    def getStudent(self, studentId=0, firstName='', lastName=''):
        if studentId != 0 and firstName == '' and lastName == '':
            self.c.execute('SELECT * FROM student WHERE studentId=?', studentId)
            return self.c.fetchone()
        elif studentId == 0 and firstName != '' and lastName == '':
            self.c.execute('SELECT * FROM student WHERE firstName=?', firstName)
            return self.c.fetchone()
        elif studentId == 0 and firstName == '' and lastName != '':
            self.c.execute('SELECT * FROM student WHERE lastName=?', lastName)
            return self.c.fetchone()
        elif studentId != 0 and firstName != '' and lastName == '':
            # Check SQL syntax
            self.c.execute('SELECT * FROM student WHERE studentId=? AND firstName=?',
                           studentId, firstName)
            return self.c.fetchone()
        elif studentId != 0 and firstName == '' and lastName != '':
            self.c.execute('SELECT * FROM student WHERE studentId=? AND lastName=?',
                           studentId, lastName)
            return self.c.fetchone()
        elif studentId == 0 and firstName != '' and lastName != '':
            self.c.execute('SELECT * FROM student WHERE firstName=? AND lastName=?',
                           firstName, lastName)
            return self.c.fetchone()
        elif studentId != 0 and firstName != '' and lastName != '':
            self.c.execute('SELECT * FROM student WHERE studentId=? AND firstName=? AND lastName=?',
                           studentId, firstName, lastName)
            return self.c.fetchone()
        elif studentId == 0 and firstName == '' and lastName == '':
            return None

    def getAllStudents(self):
        result = self.sqlite.executeQuery('SELECT * FROM student')
        return result

    def addStudent(self, firstName, lastName):
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()
        format = "INSERT INTO student (firstName, lastName, isLeader) VALUES ('{0}', '{1}', 0)"
        query = format.format(firstName, lastName)
        self.sqlite.executeQuery(query)

    def convertStudentToLeader(self, firstName, lastName):
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()
        format = "UPDATE student SET isLeader=1 WHERE firstName='{0}' AND lastName='{1}'"
        query = format.format(firstName,lastName)
        self.sqlite.executeQuery(query)