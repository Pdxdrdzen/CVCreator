import os
import unittest
from utils import validate_email, recursive_count_skills
from models import User, CV
from data_handler import load_data, save_data
import time
from memory_profiler import profile


class TestCVCreator(unittest.TestCase):
    def setUp(self):
        self.user = User("Jan Kowalski", "jan@example.com", "Mgr", "Programista", ["Python", "Java"])

    def test_validate_email(self):
        self.assertTrue(validate_email("jan@example.com"))
        self.assertFalse(validate_email("invalid_email"))

    def test_recursive_count_skills(self):
        self.assertEqual(recursive_count_skills(["Python", "Java"]), 2)

    def test_save_load_data(self):
        data = {"users": [self.user.__dict__]}
        save_data(data)
        loaded = load_data()
        self.assertEqual(loaded["users"][0]["name"], "Jan Kowalski")

    def test_generate_cv(self):
        cv = CV(self.user)
        cv.generate_cv()
        self.assertTrue(os.path.exists("output/cv_jan@example.com.txt"))

    def test_boundary_email(self):
        with self.assertRaises(AssertionError):
            User("Jan", "", "Mgr", "Programista", ["Python"])

    @profile
    def test_memory_usage(self):
        cv = CV(self.user)
        cv.generate_cv()

    def test_performance(self):
        start = time.time()
        cv = CV(self.user)
        cv.generate_cv()
        self.assertLess(time.time() - start, 1)


if __name__ == "__main__":
    unittest.main()