import sys


# this is a module - I want to stop people executing it directly
if __name__ == '__main__':
    sys.exit()

def myfunc():
    pass

print(__name__)
