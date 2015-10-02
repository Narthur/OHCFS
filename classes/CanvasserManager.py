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

    @staticmethod
    def _doNamesMatchStudent(names, student):
        names = [name.lower() for name in names]
        studentFirst = student[1].lower()
        studentLast = student[2].lower()
        if len(names) == 1:
            return CanvasserManager._doesSingleNameMatchStudent(names, studentFirst, studentLast)
        else:
            return CanvasserManager._doTwoNamesMatchStudent(names, studentFirst, studentLast)

    @staticmethod
    def _doTwoNamesMatchStudent(names, studentFirst, studentLast):
        matchesFirstName = studentFirst.count(names[0]) > 0
        matchesLastName = studentLast.count(names[1]) > 0
        return matchesFirstName and matchesLastName

    @staticmethod
    def _doesSingleNameMatchStudent(names, studentFirst, studentLast):
        matchesFirstName = studentFirst.count(names[0]) > 0
        matchesLastName = studentLast.count(names[0]) > 0
        return matchesFirstName or matchesLastName

    def markCanvasserAsLeader(self, firstName, lastName):
        self.db.markCanvasserAsLeader(firstName, lastName)

    def addStudent(self, firstName, lastName):
        self.db.addStudent(firstName, lastName)

    def getCanvasserAttributeNames(self):
        return self.db.getColumnNames('student')
