import os.path
import sqlite3

class Database:
    def __init__(self):
        self.connectToDb()

    def connectToDb(self):
        PATH = './ohcfs.db'
        if os.path.isfile(PATH) != True:
            self.dbConnection = sqlite3.connect(PATH)
            self.c = self.dbConnection.cursor()
            self.initializeDatabase()
        else:
            self.dbConnection = sqlite3.connect(PATH)
            self.c = self.dbConnection.cursor()

    def initializeDatabase(self):
        self.createVehicleTable()
        self.createMileageRecordTable()
        self.createFuelRecordTable()
        self.createExpenseTable()
        self.createCashOnHandRecordTable()
        self.createBankTransactionTable()
        self.createStudentTable()
        self.createAdvanceTable()
        self.createDailyStudentRecordTable()
        self.createBookTable()
        self.createBookSaleRecordTable()
        self.createInventoryRecordTable()
        self.dbConnection.commit()

    def createVehicleTable(self):
        self.c.execute('''
                CREATE TABLE vehicle(
                vehicleId INTEGER PRIMARY KEY,
                make TEXT,
                model TEXT NOT NULL,
                year INTEGER,
                color TEXT,
                vin TEXT
		)
                ''')

    def createMileageRecordTable(self):
        self.c.execute('''
		CREATE TABLE mileageRecord(
                mileageRecordId INTEGER PRIMARY KEY,
                vehicleId INTEGER NOT NULL,
                mileage REAL NOT NULL,
                date INTEGER NOT NULL,
                FOREIGN KEY(vehicleId) REFERENCES vehicle(vehicleId)
		)
		''')

    def createFuelRecordTable(self):
        self.c.execute('''
		CREATE TABLE fuelRecord(
                fuelRecordId INTEGER PRIMARY KEY,
                vehicleId INTEGER NOT NULL,
                fuelUsed REAL NOT NULL,
                date INTEGER NOT NULL,
                FOREIGN KEY(vehicleId) REFERENCES vehicle(vehicleId)
		)
		''')

    def createExpenseTable(self):
        self.c.execute('''
		CREATE TABLE expense(
                expenseId INTEGER PRIMARY KEY,
                paymentType TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                paidTo TEXT NOT NULL,
                date INTEGER NOT NULL,
                notes TEXT,
                purchaser TEXT NOT NULL
		)
		''')

    def createCashOnHandRecordTable(self):
        self.c.execute('''
		CREATE TABLE cashOnHandRecord(
                cashOnHandRecordId INTEGER PRIMARY KEY,
                onesTotal INTEGER,
                fivesTotal INTEGER,
                tensTotal INTEGER,
                twentiesTotal INTEGER,
                otherBillsTotal INTEGER,
                coinsTotal REAL,
                checksTotal REAL,
                pdChecksTotal REAL,
                creditCardTotal REAL,
                date INTEGER NOT NULL,
                accountant TEXT NOT NULL
		)
		''')

    def createBankTransactionTable(self):
        self.c.execute('''
		CREATE TABLE bankTransaction(
                transactionId INTEGER PRIMARY KEY,
                transactionType TEXT NOT NULL,
                date INTEGER NOT NULL,
                amount REAL NOT NULL,
                accountNumber INTEGER,
                courier TEXT NOT NULL
		)
		''')

    def createStudentTable(self):
        self.c.execute('''
		CREATE TABLE student(
                studentId INTEGER PRIMARY KEY,
                firstName TEXT NOT NULL,
                lastName TEXT
		)
		''')

    def createAdvanceTable(self):
        self.c.execute('''
		CREATE TABLE advance(
                advanceId INTEGER PRIMARY KEY,
                amount REAL NOT NULL,
                studentId INTEGER NOT NULL,
                date INTEGER NOT NULL,
                FOREIGN KEY(studentId) REFERENCES student(studentId)
		)
		''')

    def createDailyStudentRecordTable(self):
        self.c.execute('''
		CREATE TABLE dailyStudentRecord(
                dailyStudentRecordId INTEGER PRIMARY KEY,
                studentId INTEGER NOT NULL,
                checksTotal REAL,
                pdChecksTotal REAL,
                creditCardTotal REAL,
                cashTotal INTEGER,
                coinsTotal REAL,
                leader TEXT,
                location TEXT,
                date INTEGER NOT NULL,
                FOREIGN KEY(studentId) REFERENCES student(studentId)
		)
		''')

    def createBookTable(self):
        self.c.execute('''
		CREATE TABLE book(
                bookId INTEGER PRIMARY KEY,
                bookTitle TEXT NOT NULL
		)
		''')

    def createBookSaleRecordTable(self):
        self.c.execute('''
		CREATE TABLE bookSaleRecord(
                dailyStudentRecordId INTEGER NOT NULL,
                bookId INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY(dailyStudentRecordId) REFERENCES dailyStudentRecord(dailyStudentRecordId),
                FOREIGN KEY(bookId) REFERENCES book(bookId),
                PRIMARY KEY(dailyStudentRecordId, bookId)
		)
		''')

    def createInventoryRecordTable(self):
        self.c.execute('''
		CREATE TABLE inventoryRecord(
                inventoryRecordId INTEGER PRIMARY KEY,
                date INTEGER NOT NULL,
                bookId INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY(bookId) REFERENCES book(bookId)
		)
		''')

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

    def testTablePresent(self, tableName):
        self.c.execute('SELECT count(*) FROM sqlite_master WHERE type=\'table\' AND name=\''
                       + tableName + '\';')
        retval = self.c.fetchone()
        return retval[0]

    def testAllTables(self):
        tableList = ['inventoryRecord', 'student', 'vehicle',
                     'mileageRecord', 'fuelRecord', 'expense',
                     'cashOnHandRecord', 'bankTransaction',
                     'advance', 'dailyStudentRecord', 'book',
                     'bookSaleRecord']
        for table in tableList:
            if self.testTablePresent(table) != 1:
                print 'testAllTables: Failure! ' + table + ' is not a table.'


test = Database()
test.testAllTables()
