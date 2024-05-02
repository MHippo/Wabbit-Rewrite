from Command.CommandHandler import Command_Handler

class Console:
    def __init__(self):
        self.user = None
        self.prompt = None
        self.commands = []
        self.command_handler = Command_Handler()
        pass
    
    def prompt_user(prompt):
        user_input = input("{}", prompt)
        
    def break_input(command):
        command_broken = command.split(" ")
        Main_Command = command[0]
        args = command_broken.pop(0)
        return (Main_Command, args)        
        
    def output(content):
        print("{}", content)