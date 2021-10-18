from sys import platform

def clear_command():
    if platform == "win32":
        return 'cls'
    else:
        return 'clear'