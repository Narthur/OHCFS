class StudentManager:
    def __init__(self, db):
        self.db = db

    def getStudentsFromFilters(self, filters):
        matches = []
        for filter in filters:
            filterMatches = self._getStudentsFromFilter(filter)
            matches += filterMatches
        return matches

    def _getStudentsFromFilter(self, filter):
        students = self.db.getAllStudents()
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

    def convertStudentToLeader(self, firstName, lastName):
        self.db.convertStudentToLeader(firstName,lastName)

    def addStudent(self, firstName, lastName):
        self.db.addStudent(firstName,lastName)