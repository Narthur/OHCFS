import unittest
from classes import StudentManager


class TestStudentManager(unittest.TestCase):
    def testExists(self):
        StudentManager.StudentManager()