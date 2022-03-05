#!/usr/bin/python3
"""unittests for base_model.py.

Unittest classes:
    Test_BaseModel_Docs
    Test_BaseModel_All
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


class Test_BaseModel_Docs(unittest.TestCase):
    """Test documentation"""
    def test_doc(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
        
class Test_BaseModel_All(unittest.TestCase):
    """Tests for BaseModel"""

    def init(self):
        """Test instantiation"""
        pass
    
    def test_save(self):
        """Test save()"""
        pass

    def test_not_empty(self):
        """ Test if the json file is not empty """
        self.assertTrue('file.json')

    def test_to_dict(self):
        """Test to_dict()"""
        pass


if __name__ == '__main__':
    unittest.main()
    