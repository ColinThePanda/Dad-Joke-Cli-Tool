import os

def add_to_path():
    """
    Adds a new directory to the PATH environment variable if it's not already present.
    """
    new_path = os.path.dirname(os.path.abspath(__file__))
    os.environ["PATH"] = new_path + os.pathsep + os.environ["PATH"]
