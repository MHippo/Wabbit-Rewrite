class Command_Handler:
    def __init__(self):
        self.commands = []

class Command:
    def __init__(self, name, description, usage, args, aliases) -> object:
        self.name = name
        self.description = description
        self.usage = usage
        self.args = args
        self.aliases = aliases
        
    def check_args(given_args):
        if len(given_args) == len(self.args):
            return True
        else:
            return False
        
    def 