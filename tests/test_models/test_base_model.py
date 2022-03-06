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

    @classmethod
    def setUp(cls):
        """Standard setUp()"""
        cls.model = BaseModel()

    @classmethod
    def tearDown(cls):
        """Standard tearDown()"""
        del cls.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def init(self):
        """Test instantiation"""
        self.assertIsInstance(self.model, BaseModel)

    def test_no_args_instantiates(self):
        """Test no args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_args_unused(self):
        """Test unused args"""
        my_model = BaseModel(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_attr(self):
        """Test updated_at and created_at"""
        self.assertEqual(datetime, type(BaseModel().updated_at))
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_unique_id(self):
        """Test for uuid"""
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

    def test_save(self):
        """Test save()"""
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_not_empty(self):
        """ Test if the json file is not empty """
        self.assertTrue('file.json')

    def test_to_dict(self):
        """Test to_dict()"""
        model_dict = self.model.to_dict()
        self.assertEqual(self.model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
