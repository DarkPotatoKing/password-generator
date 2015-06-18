import string

class CLI():
    """The command line interface class for the password generator."""
    
    @classmethod
    def start(cls):
        print 'Password Generator'
        print '------------------'
        print ''

        cls.get_input()

    @classmethod
    def get_input(cls):
        while True:
            line_input = string.strip(raw_input('> '))

            if line_input == 'exit':
                return