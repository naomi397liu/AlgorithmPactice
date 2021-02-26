def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
    # take in a string and within that string replace every '.' with '[.]' and return the new str
    return "[.]".join(address.split('.'))