import time
import logging
from functools import wraps
from datetime import timedelta


def timed(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start = time.time()
        result = f(*args, **kwds)
        elapsed = time.time() - start
        print('{} finished. time: {}'.format(f.__name__, str(timedelta(seconds=elapsed))))
        return result

    return wrapper


class CustomFormatter(logging.Formatter):
    """
    custom colors for logging
    """
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    green = "\x1b[1;32m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def eye_candy(title: str):
    log = logging.getLogger(title)
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    log.addHandler(ch)
    return log