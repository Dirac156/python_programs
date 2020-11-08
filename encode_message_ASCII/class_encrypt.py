class Encrypt:

    """
    Encrypt Calss
    ==============

    This class create an object that contains an Encrypted
    message in ascii code based o a key
    """

    def __init__(self):
        self.sentence = ""
        self.ascii = []
        self.coded = []
        self.key = []
        self.inversekey = []

    def get_ascii_code(self):

        """
        Get ascii code
        ==============
        This class create an ascii code for our sentence created
        as an object in ou class
        """

        for letter in self.sentence:
            self.ascii.append(ord(letter))

        print(self.ascii)
