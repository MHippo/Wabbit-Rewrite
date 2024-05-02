from CommandHandler import Command
import Console

class Echo(Command):
    def execute(content):
        Console.output(content)