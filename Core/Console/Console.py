from Command.CommandHandler import Command_Handler
import json

class Console:
    def __init__(self):
        self.user = None
        self.prompt = None
        self.commands = []
        self.command_handler = Command_Handler()
        pass
    
    def prompt_user(prompt):
        user_input = input("{}", prompt)

    def output(content):
        print("{}", content)
        
    def get_config(file):
        with open("../Settings/json") as settings:
            config = json.dump(data, settings)
        pass