#!/usr/bin/python3
"""unittests for console.py.

Unittest classes:
    Test_Console_Docs
    Test_Console_All
"""

import unittest
import pep8
from console import HBNBCommand
from models.base_model import BaseModel
import models
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_Console_Docs(unittest.TestCase):
    """Test documentation"""
    def test_doc(self):
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class Test_Console_All(unittest.TestCase):
    """Tests for Console"""

    def test_empty(self):
        """Test empty line input"""
        pass

    def test_quit(self):
        """test quit command input"""
        pass

    def test_create(self):
        """Test create command inpout"""
        pass

    if __name__ == "__main__":
        unittest.main()
