#!/usr/bin/python3
"""unittests for city.py.

Unittest classes:
    Test_City_Docs
    Test_City_All
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

    def test_state_id(self):
        """Test City  state_id"""
        pass

    def test_name(self):
        """Test City  name"""
        pass


if __name__ == '__main__':
    unittest.main()
