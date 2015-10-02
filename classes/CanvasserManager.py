class CanvasserManager:
    def __init__(self, db):
        self.db = db

    def getEveryoneFromFilters(self, filters):
        return self.db.getAllCanvassers() if filters == [] else self._matchingCanvassers(filters)

    def _matchingCanvassers(self, filters):
        matches = []
        for filter in filters:
            filterMatches = self._getCanvassersFromFilter(filter)
            matches += filterMatches
        return matches

    def _getCanvassersFromFilter(self, filter):
        students = self.db.getAllCanvassers()
        matches = []
        names = filter.split(' ')
        if len(names) == 1:
            matches += self._findPeopleMatchingSingleName(names, students)
        else:
            matches += self._findPeopleMatchingTwoNames(names, students)
        return matches

    @staticmethod
    def _findPeopleMatchingTwoNames(names, students):
        matches = []
        firstName = names[0].lower()
        lastName = names[1].lower()
        for student in students:
            matchesFirstName = student[1].lower().count(firstName) > 0
            matchesLastName = student[2].lower().count(lastName) > 0
            if matchesFirstName and matchesLastName:
                matches.append(student)
        return matches

    @staticmethod
    def _findPeopleMatchingSingleName(names, students):
        matches = []
        singleName = names[0].lower()
        for student in students:
            matchesFirstName = student[1].lower().count(singleName) > 0
            matchesLastName = student[2].lower().count(singleName) > 0
            if matchesFirstName or matchesLastName:
                matches.append(student)
        return matches

    def markCanvasserAsLeader(self, firstName, lastName):
        self.db.markCanvasserAsLeader(firstName, lastName)

    def addStudent(self, firstName, lastName):
        self.db.addStudent(firstName, lastName)

    def getCanvasserAttributeNames(self):
        return self.db.getColumnNames('student')
