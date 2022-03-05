#!/usr/bin/python3
import unittest
import os
from models.__init__ import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def setUpModule():
    """ """
    pass


def tearDownModule():
    """ """
    pass


class TestModels(unittest.TestCase):

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        self.my_model.my_number = 80
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set a Class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Del a Class"""
        print("tearDownClass")

    def test_models_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


    def test_models_number(self):
        """ Check if the number is create """
        self.assertEqual(self.my_model.my_number, 80)



if __name__ == '__main__':
    unittest.main()


