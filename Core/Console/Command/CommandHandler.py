

class Command_Handler:
    def __init__(self):
        self.commands = []
    
    def register(self, command):
        if command in self.commands:
            raise AssertionError("Command already registered")
        else:
            self.commands.append(command)
        
    def command_registry(self):
        self.register_command(Echo)


class Command:
    def __init__(self, name, description, usage, args, aliases) -> object:
        self.name = name
        self.description = description
        self.usage = usage
        self.args = args
        self.aliases = aliases
        
    def check_args(self, given_args):
        if len(given_args) == len(self.args):
            return True
        else:
            return False
        
    def execute():
        pass