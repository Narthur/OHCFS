import unittest
from classes import StudentCli

class TestStudentCli(unittest.TestCase):
    def testExists(self):
        StudentCli.StudentCli()