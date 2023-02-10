#!/usr/bin/python3

"""
  My console file
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command Line Interpreter
    """
    prompt = '(hbnb)'
    def do_quit(self, line):
        """
          quit: quit USAGE: Command to quit the program
        """
        return True

    def do_EOF(self, line):
        """
           function to handle EOF
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
