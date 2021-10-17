from sys import platform

def clear_command():
    if platform == "darwin":
        return 'clear'
    elif platform == "win32":
        return 'cls'