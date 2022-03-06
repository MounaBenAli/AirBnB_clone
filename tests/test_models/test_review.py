#!/usr/bin/python3
"""unittests for review.py.

Unittest classes:
    Test_Review_Docs
    Test_Review_All
"""
import unittest
import os
import pep8
from models.__init__ import storage
from models.base_model import BaseModel
from models.review import Review


class Test_Review_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class Test_Review_All(unittest.TestCase):
    """Tests for Review"""

    @classmethod
    def setUp(cls):
        """Standard setUp()"""
        cls.Review = Review()
        cls.Review.place_id = "Tunis"
        cls.Review.user_id = "User-1"
        cls.Review.text = "happy"

    @classmethod
    def tearDown(cls):
        """Standard tearDown()"""
        del cls.Review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Test for inheritance from BaseModel"""
        self.assertTrue(issubclass(self.Review.__class__, BaseModel), True)

    def test_no_args_instantiates(self):
        """Test no args"""
        self.assertEqual(Review, type(Review()))

    def test_args_unused(self):
        """Test unused args"""
        my_Review = Review(None)
        self.assertNotIn(None, my_Review.__dict__.values())

    def test_attr(self):
        """Test attributes of Review"""
        self.assertTrue('id' in self.Review.__dict__)
        self.assertTrue('created_at' in self.Review.__dict__)
        self.assertTrue('updated_at' in self.Review.__dict__)
        self.assertTrue('place_id' in self.Review.__dict__)
        self.assertTrue('user_id' in self.Review.__dict__)
        self.assertTrue('text' in self.Review.__dict__)

    def test_strings(self):
        """Test str type of Review attributes"""
        self.assertEqual(type(self.Review.place_id), str)
        self.assertEqual(type(self.Review.user_id), str)
        self.assertEqual(type(self.Review.text), str)

    def test_unique_id(self):
        """Test for uuid"""
        us_id1 = Review()
        us_id2 = Review()
        self.assertNotEqual(us_id1.id, us_id2.id)

    def test_save(self):
        """Test save()"""
        self.Review.save()
        self.assertNotEqual(self.Review.created_at, self.Review.updated_at)

    def test_to_dict(self):
        """Test to_dict()"""
        self.assertEqual('to_dict' in dir(self.Review), True)

    def test_to_dict_type(self):
        """Test to_dict() type"""
        self.assertTrue(dict, type(Review().to_dict()))


if __name__ == '__main__':
    unittest.main()
