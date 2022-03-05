#!/usr/bin/python3
"""unittests for review.py.

Unittest classes:
    Test_Review_Docs
    Test_Review_All
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

    def test_place_id(self):
        """Test Review  place_id"""
        pass

    def test_user_id(self):
        """Test Review  user_id"""
        pass

    def test_text(self):
        """Test Review text"""
        pass


if __name__ == '__main__':
    unittest.main()
