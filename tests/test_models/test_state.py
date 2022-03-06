#!/usr/bin/python3
"""unittests for state.py.

Unittest classes:
    Test_State_Docs
    Test_State_All
"""
import unittest
import os
import pep8
from models.__init__ import storage
from models.base_model import BaseModel
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

    @classmethod
    def setUp(cls):
        """Standard setUp()"""
        cls.State = State()
        cls.State.name = "California"

    @classmethod
    def tearDown(cls):
        """Standard tearDown()"""
        del cls.State
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Test for inheritance from BaseModel"""
        self.assertTrue(issubclass(self.State.__class__, BaseModel), True)

    def test_no_args_instantiates(self):
        """Test no args"""
        self.assertEqual(State, type(State()))

    def test_args_unused(self):
        """Test unused args"""
        my_State = State(None)
        self.assertNotIn(None, my_State.__dict__.values())

    def test_attr(self):
        """Test attributes of State"""
        self.assertTrue('id' in self.State.__dict__)
        self.assertTrue('created_at' in self.State.__dict__)
        self.assertTrue('updated_at' in self.State.__dict__)
        self.assertTrue('name' in self.State.__dict__)

    def test_strings(self):
        """Test str type of State attributes"""
        self.assertEqual(type(self.State.name), str)

    def test_unique_id(self):
        """Test for uuid"""
        us_id1 = State()
        us_id2 = State()
        self.assertNotEqual(us_id1.id, us_id2.id)

    def test_save(self):
        """Test save()"""
        self.State.save()
        self.assertNotEqual(self.State.created_at, self.State.updated_at)

    def test_to_dict(self):
        """Test to_dict()"""
        self.assertEqual('to_dict' in dir(self.State), True)

    def test_to_dict_type(self):
        """Test to_dict() type"""
        self.assertTrue(dict, type(State().to_dict()))


if __name__ == '__main__':
    unittest.main()
