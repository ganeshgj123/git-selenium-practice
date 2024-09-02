# lib.py
# ------------------------
# Object Oriented Design
#------------------------
from csv import writer

class ConsoleLogger:
    def log(self, message):
        print(message)

class TextFileLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message)
        self.file_object.write("\n")
        self.file_object.flush()


class CSVLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        words = message.split()
        w = writer(self.file_object)
        w.writerow(words)
        self.file_object.flush()


class HTMLLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        contents = f"<h5>{message}</h5>"
        self.file_object.write(contents)
        self.file_object.write("\n")
        self.file_object.flush()
        

class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message:     # filteration is extra functionality
            super().log(message)


class FilteredTextFileLogger(TextFileLogger):
    def __init__(self, file_object, pattern):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


class FilteredCSVLogger(CSVLogger):
    def __init__(self, file_object, pattern):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


class FilteredHTMLLogger(HTMLLogger):
    def __init__(self, file_object, pattern):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

