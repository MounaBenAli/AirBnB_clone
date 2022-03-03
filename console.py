#!/usr/bin/python3
""" program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
