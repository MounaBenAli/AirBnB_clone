#!/usr/bin/python3
"""unittests for file_storage.py.

Unittest classes:
    Test_FileStorage_Docs
    Test_FileStorage_All
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
from models.engine.file_storage import FileStorage


class Test_FileStorage_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc(self):
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class Test_FileStorage_All(unittest.TestCase):
    """Tests for FileStorage"""

    def test_all(self):
        """Test FileStorage  all()"""
        pass

    def test_new(self):
        """Test FileStorage  new()"""
        pass


if __name__ == '__main__':
    unittest.main()
