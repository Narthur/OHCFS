import unittest
from classes import StudentManager


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.mockedStudentManager = StudentManager.StudentManager()

    def testHasGetFilteredStudentsMethod(self):
        self.mockedStudentManager.getFilteredStudents(['John Doe'])