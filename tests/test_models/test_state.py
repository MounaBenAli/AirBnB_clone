#!/usr/bin/python3
"""unittests for state.py.

Unittest classes:
    Test_State_Docs
    Test_State_All
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
from models.state import State


class Test_State_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc(self):
        self.assertIsNotNone(State.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class Test_State_All(unittest.TestCase):
    """Tests for State"""

    def test_name(self):
        """Test State  name"""
        pass


if __name__ == '__main__':
    unittest.main()
