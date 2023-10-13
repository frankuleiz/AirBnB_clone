#!/usr/bin/python3
"""
This is a module for the console module
Defines the class HBNBCommand
"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
