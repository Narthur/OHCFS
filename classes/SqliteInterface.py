import os.path


class SqliteInterface:
    def _doesDatabaseExist(self):
        PATH = './ohcfs.db'
        return os.path.isfile(PATH)