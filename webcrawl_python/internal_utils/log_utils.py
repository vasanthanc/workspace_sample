import sys
sys.path.append("./")
import coloredlogs
import logging
import functools
import logging.config
import copy

__all__ = ['Logger']

class Logger(object):

    RESET = '\033[0m'
    BOLD = '\033[01m'
    DISALE = '\033[02m'
    UNDERLINE = '\033[04m'
    REVERSE = '\033[07m'
    STRIKETHROUGH = '\033[09m'
    INVISIBLE = '\033[08m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CLAYN = '\033[36m'
    LIGHTGREY = '\033[37m'
    DARKGREY = '\033[90m'
    LIGHTRED = '\033[91m'
    LIGHTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHTBLUE = '\033[94m'
    PINK = '\033[95m'
    LIGHTCYAN = '\033[96m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_ORANGE = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_LIGHTGREY = '\033[47m'

    def __new__(cls, *args, **kwargs):
        cls.logger = logging.getLogger(
            cls.__get_name(__name__, cls.__class__.__name__))
        return super(Logger, cls).__new__(cls)

    def __init__(cls,object=None):
        Logger.class_name = object.__class__.__name__
        # print(cls.class_name)
        handler = logging.StreamHandler()
        cls.logger.addHandler(handler)
        FORMAT = '%(asctime)s %(hostname)s %(class_name)s[%(process)d] %(levelname)s %(message)s'
        coloredlogs.install(level='DEBUG', logger=cls.logger,fmt=FORMAT)

    @classmethod
    def __get_name(cls, *name_parts):
        return '.'.join(n.strip() for n in name_parts if n.strip())

    @classmethod
    @functools.wraps(logging.debug)
    def debug(cls, msg, *args, **kwargs):
        if 'extra' in kwargs.keys():
            kwargs['extra'].update({'class_name': Logger.class_name})
        else:
            kwargs['extra'] = {'class_name': Logger.class_name}
        if msg:
            msg = "{}{}{}{}".format(cls.GREEN,cls.BOLD,msg,cls.RESET)
        cls.logger.debug(msg, *args, **kwargs)

    @classmethod
    @functools.wraps(logging.info)
    def info(cls, msg, *args, **kwargs):
        if 'extra' in kwargs.keys():
            kwargs['extra'].update({'class_name': Logger.class_name})
        else:
            kwargs['extra'] = {'class_name': Logger.class_name}
        if msg:
            msg = "{}{}{}{}".format(cls.BLACK,cls.UNDERLINE,msg,cls.RESET)
        cls.logger.info(msg, *args, **kwargs)

    @classmethod
    @functools.wraps(logging.warning)
    def warning(cls, msg, *args, **kwargs):
        if 'extra' in kwargs.keys():
            kwargs['extra'].update({'class_name': Logger.class_name})
        else:
            kwargs['extra'] = {'class_name': Logger.class_name}
        if msg:
            msg = "{}{}{}{}".format(cls.BG_BLACK,cls.YELLOW,msg,cls.RESET)
        cls.logger.warning(msg, *args, **kwargs)

    @classmethod
    @functools.wraps(logging.error)
    def error(cls, msg, *args, **kwargs):
        if 'extra' in kwargs.keys():
            kwargs['extra'].update({'class_name': Logger.class_name})
        else:
            kwargs['extra'] = {'class_name': Logger.class_name}
        if msg:
            msg = "{}{}{}{}".format(cls.RED,cls.BOLD,msg,cls.RESET)
        cls.logger.error(msg, *args, **kwargs)

    @classmethod
    @functools.wraps(logging.critical)
    def critical(cls, msg, *args, **kwargs):
        if 'extra' in kwargs.keys():
            kwargs['extra'].update({'class_name': str(Logger.class_name)})
        else:
            kwargs['extra'] = {'class_name': str(Logger.class_name)}
        if msg:
            msg = "{}{}{}{}".format(cls.BG_BLACK,cls.RED,cls.UNDERLINE,msg,cls.RESET)
        cls.logger.critical(msg, *args, **kwargs)

if __name__ == "__main__":
    # from log_utils import Logger
    logg = Logger()
    logg.critical("OUT OF\n MEMMORY")
    logg.info("This should not use this function for all case")
    logg.warning("No file found, Creating new one")
    logg.error("No method Exception")
    logg.debug("I'm here")