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
        students = self.getAllStudents()
        matches = []
        names = filter.split(' ')
        if len(names) == 1:
            matches += self._findStudentsMatchingSingleName(names, students)
        else:
            matches += self._findStudentsMatchingTwoNames(names, students)
        return matches

    def _findStudentsMatchingTwoNames(self, names, students):
        matches = []
        firstName = names[0]
        lastName = names[1]
        for student in students:
            if student[1].count(firstName) > 0 and student[2].count(lastName) > 0:
                matches.append(student)
        return matches

    def _findStudentsMatchingSingleName(self, names, students):
        matches = []
        singleName = names[0]
        for student in students:
            if student[1].count(singleName) > 0 or student[2].count(singleName) > 0:
                matches.append(student)
        return matches