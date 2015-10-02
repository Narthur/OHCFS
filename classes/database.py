class Database:
    def __init__(self, sqliteInterface):
        self.sqlite = sqliteInterface

    def getAllCanvassers(self):
        result = self.sqlite.executeQuery('SELECT * FROM student')
        return result

    def addCanvasser(self, firstName, lastName):
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()
        formatString = "INSERT INTO student (firstName, lastName, isLeader) VALUES ('{0}', '{1}', 0)"
        query = formatString.format(firstName, lastName)
        self.sqlite.executeQuery(query)

    def markCanvasserAsLeader(self, firstName, lastName):
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()
        formatString = "UPDATE student SET isLeader=1 WHERE firstName='{0}' AND lastName='{1}'"
        query = formatString.format(firstName, lastName)
        self.sqlite.executeQuery(query)

    def getColumnNames(self, table):
        formatString = "PRAGMA table_info({})"
        query = formatString.format(table)
        result = self.sqlite.executeQuery(query)
        column = [row[1] for row in result]
        return column
