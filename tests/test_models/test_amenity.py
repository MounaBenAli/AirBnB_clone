#!/usr/bin/python3
"""unittests for amenity.py.

Unittest classes:
    Test_Amenity_Docs
    Test_Amenity_All
"""
import unittest
import os
import pep8
from models.__init__ import storage
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class Test_Amenity_All(unittest.TestCase):
    """Tests for Amenity"""

    @classmethod
    def setUp(cls):
        """Standard setUp()"""
        cls.Amenity = Amenity()
        cls.Amenity.name = "travel pack"

    @classmethod
    def tearDown(cls):
        """Standard tearDown()"""
        del cls.Amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Test for inheritance from BaseModel"""
        self.assertTrue(issubclass(self.Amenity.__class__, BaseModel), True)

    def test_no_args_instantiates(self):
        """Test no args"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_args_unused(self):
        """Test unused args"""
        my_Amenity = Amenity(None)
        self.assertNotIn(None, my_Amenity.__dict__.values())

    def test_attr(self):
        """Test updated_at and created_at"""
        self.assertTrue('id' in self.Amenity.__dict__)
        self.assertTrue('created_at' in self.Amenity.__dict__)
        self.assertTrue('updated_at' in self.Amenity.__dict__)
        self.assertTrue('name' in self.Amenity.__dict__)

    def test_unique_id(self):
        """Test for uuid"""
        us_id1 = Amenity()
        us_id2 = Amenity()
        self.assertNotEqual(us_id1.id, us_id2.id)

    def test_save(self):
        """Test save()"""
        self.Amenity.save()
        self.assertNotEqual(self.Amenity.created_at, self.Amenity.updated_at)

    def test_to_dict(self):
        """Test to_dict()"""
        self.assertEqual('to_dict' in dir(self.Amenity), True)

    def test_to_dict_type(self):
        """Test to_dict() type"""
        self.assertTrue(dict, type(Amenity().to_dict()))


if __name__ == '__main__':
    unittest.main()
