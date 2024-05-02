from CommandHandler import Command
import Console

class Echo(Command):
    def __init__(self):
        self.name = "echo"
        self.args = ["content"]
        self.description = "Repeats what you say"
    
    def execute(content):
        Console.output(content)