#!/usr/bin/python3
"""This is command line interpreter entry."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Define command line interpreter class."""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Quit the cli on EOF signal."""
        return True

    def emptyline(self):
        """Do not excute anything."""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
