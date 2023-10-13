#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Exit the program using EOF (Ctrl+D)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
