import config
from sys import platform

def set_clear_command():
    if platform == 'win32':
        config.CLEAR_COMMAND = 'cls'
        return 'cls'
    else:
        config.CLEAR_COMMAND = 'clear'
        return 'clear'