# composition.py
# ------------------------
# Object Oriented Design
#------------------------
from abc import ABC, abstractmethod

# this class enforces all its children to implement `log` interface
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(message)

class TextFileLogger(Logger):
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message)
        self.file_object.write("\n")
        self.file_object.flush()


class CSVLogger(Logger):
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        from csv import writer
        words = message.split()
        w = writer(self.file_object)
        w.writerow(words)
        self.file_object.flush()

class HTMLLogger(Logger):
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        contents = f"<h5>{message}</h5>"
        self.file_object.write(contents)
        self.file_object.write("\n")
        self.file_object.flush()
 
class HTTPLogger(Logger):
    def log(self, message):
        ...


class Spam(Logger):
    def greet(self):
        return "hello world"

    def log(self, message):
        return "hello world"

# Composite class
class FilteredLogger:
    # it takes an object instance of the calss that has implemented `log` method
    def __init__(self, pattern, logger_object):
        self.pattern = pattern
        self.logger_object = logger_object      # dependancy injection

    def log(self, message):
        if self.pattern in message:
            self.logger_object.log(message)