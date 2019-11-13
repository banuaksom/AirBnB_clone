#!/usr/bin/python3
""" Test for Console """
import unittest
import os.path
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Test for Console """

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

    def test_create(self):
        """ Test create """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Banu")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

    def test_show(self):
        """ Test show """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Brent")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel " + str(id))
            self.assertTrue(type(f), str)
            self.assertEqual(len(f.getvalue().strip()), 23)

    def test_destroy(self):
        """ Test destroy """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Banu")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel " + str(id))
            self.assertEqual(f.getvalue().strip(), "")

    def test_all(self):
        """ Test all """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertTrue("[User]" in f.getvalue().strip())
            self.assertTrue("[State]" in f.getvalue().strip())
            self.assertTrue("[City]" in f.getvalue().strip())
            self.assertTrue("[Amenity]" in f.getvalue().strip())
            self.assertTrue("[Place]" in f.getvalue().strip())
            self.assertTrue("[Review]" in f.getvalue().strip())
            self.assertTrue("created_at" in f.getvalue().strip())
            self.assertTrue("updated_at" in f.getvalue().strip())
            self.assertTrue("id" in f.getvalue().strip())

    def test_update(self):
        """ Test update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Brent")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User Banu")
            self.assertEqual(f.getvalue().strip(),
                             "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id))
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_newline_spaces(self):
        """ Test newline and spaces input """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(" ")
            self.assertEqual(f.getvalue().strip(), "")

    def test_fake_command(self):
        """ Test commands that do not exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: garbage")

    def test_help(self):
        """ Test help """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue().strip(),
                             "Documented commands (type help <topic>):" +
                             "\n========================================" +
                             "\nEOF  all  count  create  destroy  help  " +
                             "quit  show  update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue().strip(), "EOF to exit the program")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue().strip(), "Print all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue().strip(),
                             "Counts the number of objects.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(),
                             "Create a new instance of BaseModel.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip(),
                             "Delete an instance based on class name and id.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertEqual(f.getvalue().strip(), "List available " +
                             "commands with \"help\" or detailed help " +
                             "with \"help cmd\".")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue().strip(),
                             "Quit to exit the program")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(),
                             "Print an instance based on class name and id.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue().strip(),
                             "Update an instance based on class name and id.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help garbage")
            self.assertEqual(f.getvalue().strip(),
                             "*** No help on garbage")

if __name__ == '__main__':
    unittest.main()
