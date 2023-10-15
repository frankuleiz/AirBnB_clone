#!/usr/bin/python3
"""
This is a module for the console module
Defines the class HBNBCommand
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
from shlex import split
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
            }

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Terminates the console incase of the input is CTRL + D"""
        return True

    def emptyline(self):
        """Does not execute anything"""
        pass

    def help_quit(self):
        """Documentation for the help command"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """Documentation for the EOF command"""
        print("Exit the program using EOF (Ctrl+D)")

    def do_create(self, arg):
        """creates a new instance of and save it as a JSON file"""
        if not arg:
            print("** class name missing **")
            return
        if arg in HBNBCommand.classes:
            instance = HBNBCommand.classes[arg]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints the string representation of an instance"""
        args = split(arg)
        if not args:
            print("** class name mising ***")
            return
        if args[0] in HBNBCommand.classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                print(objects.get(key, "** no instance found **"))
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return
        args = split(arg)

        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name
        <classname>.all()
        """

        args = split(arg)
        if len(args) > 0 and args[1] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(args) == 0:
                    obj1.append(obj.__str__())
                print(obj1)

    def do_update(self, arg):
        """updates an instance based on the class name and id"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key not in objects:
                print("** no instance fount **")
                return
            else:
                instance = objects[key]
                setattr(instance, args[2], args[3])
                instance.updated_at = datetime.now()
                storage.save()

    def do_count(self, arg):
        """ counts the number of instances of a class"""

        args = split(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
