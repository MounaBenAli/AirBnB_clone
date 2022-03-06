#!/usr/bin/python3
"""unittests for user.py.

Unittest classes:
    Test_User_Docs
    Test_User_All
"""
import unittest
import os
import pep8
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User


class Test_User_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc(self):
        self.assertIsNotNone(User.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class Test_User_All(unittest.TestCase):
    """Tests for User"""

    @classmethod
    def setUp(cls):
        """Standard setUp()"""
        cls.user = User()
        cls.user.first_name = "Mouna"
        cls.user.last_name = "Ben Ali"
        cls.user.email = "mbenali@holberonschool.com"
        cls.user.password = "Hello.World"

    @classmethod
    def tearDown(cls):
        """Standard tearDown()"""
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Test for inheritance from BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_no_args_instantiates(self):
        """Test no args"""
        self.assertEqual(User, type(User()))

    def test_args_unused(self):
        """Test unused args"""
        my_user = User(None)
        self.assertNotIn(None, my_user.__dict__.values())

    def test_attr(self):
        """Test updated_at and created_at"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_unique_id(self):
        """Test for uuid"""
        us_id1 = User()
        us_id2 = User()
        self.assertNotEqual(us_id1.id, us_id2.id)

    def test_save(self):
        """Test save()"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Test to_dict()"""
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_to_dict_type(self):
        """Test to_dict() type"""
        self.assertTrue(dict, type(User().to_dict()))


if __name__ == '__main__':
    unittest.main()
