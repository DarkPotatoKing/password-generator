from Crypto.Random import random
import string

class Generator():
    """A class for generating passwords"""

    #possible sets to generate password from

    UPPERCASE_LETTERS = string.ascii_uppercase #'ABC...Z'
    LOWERCASE_LETTERS = string.ascii_lowercase #'abc...z'
    DIGITS = string.digits # '0..9'
    PUNCTUATION = string.punctuation #punctuation marks

    #generate a random password
    @classmethod
    def generate_random_password(self, length = 8):
        #concatination of all chosen sets (uppercase, lowercase, etc.)
        password_set = self.UPPERCASE_LETTERS + self.LOWERCASE_LETTERS + self.DIGITS + self.PUNCTUATION
        password = ''
        for i in xrange(length):
            password += random.choice(password_set)
        return password

