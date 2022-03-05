#!/usr/bin/python3
"""unittests for amenity.py.

Unittest classes:
    Test_Amenity_Docs
    Test_Amenity_All
"""
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

    def test_name(self):
        """Test Amenity  name"""
        pass


if __name__ == '__main__':
    unittest.main()
    
