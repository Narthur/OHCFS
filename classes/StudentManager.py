class StudentManager:
    def __init__(self, db):
        self.db = db

    def getStudentsFromFilters(self, filters):
        return self.db.getAllStudents() if filters == [] else self._matchingStudents(filters)

    def _matchingStudents(self, filters):
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
        firstName = names[0].lower()
        lastName = names[1].lower()
        for student in students:
            matchesFirstName = student[1].lower().count(firstName) > 0
            matchesLastName = student[2].lower().count(lastName) > 0
            if matchesFirstName and matchesLastName:
                matches.append(student)
        return matches

    def _findStudentsMatchingSingleName(self, names, students):
        matches = []
        singleName = names[0].lower()
        for student in students:
            matchesFirstName = student[1].lower().count(singleName) > 0
            matchesLastName = student[2].lower().count(singleName) > 0
            if matchesFirstName or matchesLastName:
                matches.append(student)
        return matches

    def convertStudentToLeader(self, firstName, lastName):
        self.db.convertStudentToLeader(firstName,lastName)

    def addStudent(self, firstName, lastName):
        self.db.addStudent(firstName,lastName)