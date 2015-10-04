class Database:
    def __init__(self, sqliteInterface):
        self.sqlite = sqliteInterface

    def getAllCanvassers(self):
        return self.sqlite.executeQuery('SELECT * FROM student')

    def addCanvasser(self, firstName, lastName):
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()
        formatString = "INSERT INTO student (firstName, lastName, isLeader) VALUES ('{0}', '{1}', 0)"

        self._executeFormattedQuery(formatString, firstName, lastName)

    def markCanvasserAsLeader(self, firstName, lastName):
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()
        formatString = "UPDATE student SET isLeader=1 WHERE firstName='{0}' AND lastName='{1}'"

        self._executeFormattedQuery(formatString, firstName, lastName)

    def getColumnNames(self, table):
        formatString = "PRAGMA table_info({})"
        result = self._executeFormattedQuery(formatString, table)
        fieldNames = [row[1] for row in result]
        return fieldNames

    def _executeFormattedQuery(self, formatString, *args, **kwargs):
        query = formatString.format(*args, **kwargs)
        return self.sqlite.executeQuery(query)