#!/usr/bin/python3
""" unittest for Review class """
import unittest
from models import storage
from models.review import Review
import os
from datetime import datetime, date, time
import time
import uuid
import pep8


class TestReview(unittest.TestCase):
    """ Review class """

    def setUp(self):
        """ Move json file if it exists """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """ Delete test json file and put original file back """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_pep8(self):
        """ pep8 test """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_default_attributes(self):
        """ default attributes """
        brba = Review()
        self.assertTrue(hasattr(brba, "updated_at"))
        self.assertTrue(hasattr(brba, "created_at"))
        self.assertTrue(hasattr(brba, "id"))
        self.assertEqual(type(brba.updated_at), datetime)
        self.assertEqual(type(brba.created_at), datetime)
        self.assertEqual(type(brba.id), str)
        self.assertFalse(hasattr(brba, "brent"))
        self.assertTrue(hasattr(brba, "place_id"))
        self.assertTrue(hasattr(brba, "user_id"))
        self.assertTrue(hasattr(brba, "text"))
        self.assertEqual(type(brba.text), str)

    def test_assigned_attributes(self):
        """ test assigned attributes """
        brba = Review()
        brba.place_id = "49"
        brba.text = "text"
        self.assertEqual(type(brba.place_id), str)
        self.assertEqual(type(brba.text), str)

    def test_save(self):
        """ save method from BaseModel """
        brba = Review()
        br = brba.updated_at
        time.sleep(0.1)
        brba.save()
        ba = brba.updated_at
        self.assertNotEqual(br, ba)

    def test_dict(self):
        """ dic_to method from BaseModel """
        brba = Review()
        brba.name = "Paradise"
        brba.appartment = 4
        dicti = brba.to_dict()
        self.assertTrue("name" in dicti)
        self.assertEqual(type(dicti["name"]), str)
        self.assertTrue("appartment" in dicti)
        self.assertEqual(type(dicti["appartment"]), int)
        self.assertTrue("created_at" in dicti)
        self.assertTrue("updated_at" in dicti)
        self.assertTrue("id" in dicti)

    def test_recreate_from_kwargs(self):
        """ recreate the dictionary from saved one """
        brba = Review()
        brba.name = "Paradise"
        brba.appartment = 9
        dicti = brba.to_dict()
        new_dicti = Review(**dicti)
        self.assertEqual(brba.name, new_dicti.name)
        self.assertEqual(brba.appartment, new_dicti.appartment)
        self.assertEqual(brba.id, new_dicti.id)
        self.assertEqual(brba.created_at, new_dicti.created_at)
        self.assertEqual(brba.updated_at, new_dicti.updated_at)
        self.assertEqual(type(new_dicti.id), str)
        self.assertFalse(new_dicti is dicti)

    def test_time_format(self):
        """ time format """
        brba = Review()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dicti = brba.to_dict()
        self.assertEqual(dicti["created_at"],
                         brba.created_at.strftime(time_format))
        self.assertEqual(dicti["updated_at"],
                         brba.updated_at.strftime(time_format))

if __name__ == '__main__':
    unittest.main()
