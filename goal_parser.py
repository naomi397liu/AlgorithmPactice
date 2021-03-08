def interpret(self, command):
    """
    :type command: str
    :rtype: str
    """
    command = command.replace("()", "o")
    command = command.replace(")", "")
    command = command.replace("(", "")
    return command