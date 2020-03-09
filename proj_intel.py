#!/usr/bin/python3
'''
Command interpreter for Projects 
'''

import cmd

class PROJCommand(cmd.Cmd):
    '''
    Coomand interpreter class
    '''

    promt = '(intelX) '
    ERR = [
        '** class name missing **'
        '** class doesn\'t exist **'
        '** instance id missing **'
        '** no instance found **'
        '** attribute name missing **'
        '** value missing **'
    ]

    def preloop(self):
        '''
        handles intro to command interpreter
        '''
        print('.---------------------------.')
        print('| Welcome to intelX console |')
        print('|   to quit, input \'quit\' |')
        print('.---------------------------.')

    def postloop(self):
        """
        handles exit to command interpreter
        """
        print('.----------------------------.')
        print('|  Thank you, have a good day |')
        print('.----------------------------.')

    def default(self, line):
        '''
        default response for unknown commands
        '''
        print("This \"{}\" is invalid".format(line))

    def emptyline(self):
        '''
        called when empty line is entered in prompt
        '''
        pass

    def __class_err(self, arg):
        '''
        private: checks for missing class or unkown class
        '''
        error = 0
        if len(arg) == 0:
            print(PROJCommand.ERR[1])
            error = 1
        else:
            if isinstance(arg, list):
                arg = arg[0]
            if arg not in CNC.keys():
                print(PROJCommand.ERR[1])
                error = 1
            return error

    def do_quit(self, line):
        """quit: quit
        USAGE: Command to quit the program
        """
        return True

    def do_EOF(self, line):
        """function to handle EOF"""
        print()
        return True

    

if __name__ == '__main__':
    """
    MAIN Loop
    """
    PROJCommand().cmdloop()
    

    
