#!/usr/bin/python3
"""unittests for user.py.

Unittest classes:
    Test_City_Docs
    Test_City_All
"""
import unittest
import os
import pep8
from models.__init__ import storage
from models.base_model import BaseModel
from models.city import City


class Test_City_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc(self):
        self.assertIsNotNone(City.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class Test_City_All(unittest.TestCase):
    """Tests for City"""

    @classmethod
    def setUp(cls):
        """Standard setUp()"""
        cls.City = City()
        cls.City.name = "San Diego"
        cls.City.state_id = "California"

    @classmethod
    def tearDown(cls):
        """Standard tearDown()"""
        del cls.City
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Test for inheritance from BaseModel"""
        self.assertTrue(issubclass(self.City.__class__, BaseModel), True)

    def test_no_args_instantiates(self):
        """Test no args"""
        self.assertEqual(City, type(City()))

    def test_args_unused(self):
        """Test unused args"""
        my_City = City(None)
        self.assertNotIn(None, my_City.__dict__.values())

    def test_attr(self):
        """Test updated_at and created_at"""
        self.assertTrue('id' in self.City.__dict__)
        self.assertTrue('created_at' in self.City.__dict__)
        self.assertTrue('updated_at' in self.City.__dict__)
        self.assertTrue('name' in self.City.__dict__)
        self.assertTrue('state_id' in self.City.__dict__)

    def test_unique_id(self):
        """Test for uuid"""
        us_id1 = City()
        us_id2 = City()
        self.assertNotEqual(us_id1.id, us_id2.id)

    def test_save(self):
        """Test save()"""
        self.City.save()
        self.assertNotEqual(self.City.created_at, self.City.updated_at)

    def test_to_dict(self):
        """Test to_dict()"""
        self.assertEqual('to_dict' in dir(self.City), True)

    def test_to_dict_type(self):
        """Test to_dict() type"""
        self.assertTrue(dict, type(City().to_dict()))


if __name__ == '__main__':
    unittest.main()
