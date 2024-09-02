# user.py
from lib import FilteredTextFileLogger, FilteredCSVLogger
from lib import FilteredConsoleLogger, FilteredHTMLLogger

f = open("trace.html", "w")
logger = FilteredHTMLLogger(f, "TRACE")

with open("/Users/sandeep/Desktop/training/_python/data_files/sample.log") as _f:
    for line in _f:
        clean_line = line.strip()
        if clean_line:
            logger.log(clean_line)