#!/usr/bin/python3
"""unittests for Place.py.

Unittest classes:
    Test_Place_Docs
    Test_Place_All
"""
from tkinter import Y
import unittest
import os
import uuid
import pep8
from datetime import datetime
from datetime import time
from models.base_model import BaseModel
import models
from models.__init__ import storage
from models.user import User
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

    def test_city_id(self):
        """Test Place city_id"""
        pass

    def user_city_id(self):
        """Test Place user_id"""
        pass


if __name__ == '__main__':
    unittest.main()
