import string

class CLI():
    """The command line interface class for the password generator."""

    @classmethod
    def start(cls):
        """Start the command line interface."""
        print 'Password Generator'
        print '------------------'
        print ''

        # wait for user input
        cls.get_input()

    @classmethod
    def get_input(cls):
        """Ask line input(s) from user."""
        while True:
            # strip the line input and store into a variable
            line_input = string.strip(raw_input('> '))

            # exit if user enters 'exit'
            if line_input == 'exit':
                return
            # else pass the line_input to parsing method for evaluation
            else:
                cls.parse_input(line_input)



    @classmethod
    def parse_input(cls, line_input):
        line_input
