import os


def get_path():
    path = os.path.dirname(os.path.abspath('*.py'))
    return path