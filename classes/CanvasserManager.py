class CanvasserManager:
    def __init__(self, db):
        self.db = db

    def getEveryoneFromFilters(self, filters):
        return self.db.getAllCanvassers() if filters == [] else self._matchingCanvassers(filters)

    def _matchingCanvassers(self, filters):
        matches = []
        for f in filters:
            filterMatches = self._getCanvassersFromFilter(f)
            matches += filterMatches
        return matches

    def _getCanvassersFromFilter(self, f):
        names = f.split(' ')
        students = self.db.getAllCanvassers()
        matches = list()
        for student in students:
            if self._doNamesMatchStudent(names, student):
                matches.append(student)
        return matches

    def _doNamesMatchStudent(self, names, student):
        if len(names) == 1:
            return self._doesSingleNameMatchStudent(names, student[1], student[2])
        else:
            return self._doTwoNamesMatchStudent(names, student[1], student[2])

    def _doTwoNamesMatchStudent(self, names, studentFirst, studentLast):
        matchesFirstName = self._doNamesMatch(names[0], studentFirst)
        matchesLastName = self._doNamesMatch(names[1], studentLast)
        return matchesFirstName and matchesLastName

    def _doesSingleNameMatchStudent(self, names, studentFirst, studentLast):
        matchesFirstName = self._doNamesMatch(names[0], studentFirst)
        matchesLastName = self._doNamesMatch(names[0], studentLast)
        return matchesFirstName or matchesLastName

    @staticmethod
    def _doNamesMatch(needleName, haystackName):
        return haystackName.lower().count(needleName.lower()) > 0

    def markCanvasserAsLeader(self, firstName, lastName):
        self.db.markCanvasserAsLeader(firstName, lastName)

    def addStudent(self, firstName, lastName):
        self.db.addStudent(firstName, lastName)

    def getCanvasserAttributeNames(self):
        return self.db.getColumnNames('student')
