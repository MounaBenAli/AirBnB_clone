#!/usr/bin/python3
"""unittests for user.py.

Unittest classes:
    Test_User_Docs
    Test_User_All
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

    def test_email(self):
        """Test User email"""
        pass

    def test_password(self):
        """Test User password"""
        pass

    def test_first_name(self):
        """Test User first name"""
        pass

    def test_last_name(self):
        """Test User last name"""
        pass


if __name__ == '__main__':
    unittest.main()
