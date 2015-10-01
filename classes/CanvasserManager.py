class CanvasserManager:
    def __init__(self, db):
        self.db = db

    def getEveryoneFromFilters(self, filters):
        return self.db.getAllStudents() if filters == [] else self._matchingPeople(filters)

    def _matchingPeople(self, filters):
        matches = []
        for filter in filters:
            filterMatches = self._getEveryoneFromFilter(filter)
            matches += filterMatches
        return matches

    def _getEveryoneFromFilter(self, filter):
        students = self.db.getAllStudents()
        matches = []
        names = filter.split(' ')
        if len(names) == 1:
            matches += self._findPeopleMatchingSingleName(names, students)
        else:
            matches += self._findPeopleMatchingTwoNames(names, students)
        return matches

    def _findPeopleMatchingTwoNames(self, names, students):
        matches = []
        firstName = names[0].lower()
        lastName = names[1].lower()
        for student in students:
            matchesFirstName = student[1].lower().count(firstName) > 0
            matchesLastName = student[2].lower().count(lastName) > 0
            if matchesFirstName and matchesLastName:
                matches.append(student)
        return matches

    def _findPeopleMatchingSingleName(self, names, students):
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