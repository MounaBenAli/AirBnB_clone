#!/usr/bin/python3
"""unittests for place.py.

Unittest classes:
    Test_Place_Docs
    Test_Place_All
"""
import unittest
import os
import pep8
from models.__init__ import storage
from models.base_model import BaseModel
from models.place import Place


class Test_Place_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc(self):
        self.assertIsNotNone(Place.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class Test_Place_All(unittest.TestCase):
    """Tests for Place"""

    @classmethod
    def setUp(cls):
        """Standard setUp()"""
        cls.Place = Place()
        cls.Place.city_id = "Tunis"
        cls.Place.user_id = "User-1"
        cls.Place.name = "Lac 1"
        cls.Place.description = "Best School"
        cls.Place.number_rooms = 0
        cls.Place.number_bathrooms = 0
        cls.Place.max_guest = 0
        cls.Place.price_by_night = 0
        cls.Place.latitude = 0.0
        cls.Place.longitude = 0.0
        cls.Place.amenity_ids = []

    @classmethod
    def tearDown(cls):
        """Standard tearDown()"""
        del cls.Place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Test for inheritance from BaseModel"""
        self.assertTrue(issubclass(self.Place.__class__, BaseModel), True)

    def test_no_args_instantiates(self):
        """Test no args"""
        self.assertEqual(Place, type(Place()))

    def test_args_unused(self):
        """Test unused args"""
        my_Place = Place(None)
        self.assertNotIn(None, my_Place.__dict__.values())

    def test_attr(self):
        """Test attributes of Place"""
        self.assertTrue('id' in self.Place.__dict__)
        self.assertTrue('created_at' in self.Place.__dict__)
        self.assertTrue('updated_at' in self.Place.__dict__)
        self.assertTrue('city_id' in self.Place.__dict__)
        self.assertTrue('user_id' in self.Place.__dict__)
        self.assertTrue('name' in self.Place.__dict__)
        self.assertTrue('description' in self.Place.__dict__)
        self.assertTrue('number_rooms' in self.Place.__dict__)
        self.assertTrue('number_bathrooms' in self.Place.__dict__)
        self.assertTrue('max_guest' in self.Place.__dict__)
        self.assertTrue('price_by_night' in self.Place.__dict__)
        self.assertTrue('latitude' in self.Place.__dict__)
        self.assertTrue('longitude' in self.Place.__dict__)
        self.assertTrue('amenity_ids' in self.Place.__dict__)

    def test_strings(self):
        """Test str type of Place attributes"""
        self.assertEqual(type(self.Place.city_id), str)
        self.assertEqual(type(self.Place.user_id), str)
        self.assertEqual(type(self.Place.name), str)
        self.assertEqual(type(self.Place.description), str)
        self.assertEqual(type(self.Place.number_rooms), int)
        self.assertEqual(type(self.Place.number_bathrooms), int)
        self.assertEqual(type(self.Place.max_guest), int)
        self.assertEqual(type(self.Place.price_by_night), int)
        self.assertEqual(type(self.Place.latitude), float)
        self.assertEqual(type(self.Place.longitude), float)
        self.assertEqual(type(self.Place.amenity_ids), list)

    def test_unique_id(self):
        """Test for uuid"""
        us_id1 = Place()
        us_id2 = Place()
        self.assertNotEqual(us_id1.id, us_id2.id)

    def test_save(self):
        """Test save()"""
        self.Place.save()
        self.assertNotEqual(self.Place.created_at, self.Place.updated_at)

    def test_to_dict(self):
        """Test to_dict()"""
        self.assertEqual('to_dict' in dir(self.Place), True)

    def test_to_dict_type(self):
        """Test to_dict() type"""
        self.assertTrue(dict, type(Place().to_dict()))


if __name__ == '__main__':
    unittest.main()
