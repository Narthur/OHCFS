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
        return self.sqlite.executeQuery('SELECT * FROM student')

    def addStudent(self, firstName, lastName):
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()
        format = "INSERT INTO student (firstName, lastName, isLeader) VALUES ('{0}', '{1}', 0)"
        query = format.format(firstName, lastName)
        self.sqlite.executeQuery(query)

    def convertStudentToLeader(self, firstName, lastName):
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()
        format = "UPDATE student SET isLeader=1 WHERE firstName='{0}', lastName='{1}'"
        query = format.format(firstName,lastName)
        self.sqlite.executeQuery(query)

    def getStudentsFromFilters(self, filters):
        matches = []
        for filter in filters:
            filterMatches = self._getStudentsFromFilter(filter)
            matches += filterMatches
        return matches

    def _getStudentsFromFilter(self, filter):
        firstName = self._getFilterFirstName(filter)
        lastName = self._getFilterLastName(filter)
        students = self.getAllStudents()
        matches = []
        for student in students:
            if student[1] == firstName and student[2] == lastName:
                matches.append(student)
        return matches

    def _getFilterLastName(self, filter):
        names = filter.split(' ')
        lastName = names[1]
        return lastName

    def _getFilterFirstName(self, filter):
        names = filter.split(' ')
        firstName = names[0]
        return firstName