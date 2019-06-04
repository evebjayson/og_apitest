import os

def get_path():
    path = os.path.abspath(__file__)
    fp = os.path.dirname(path)
    return fp

res = get_path()
print(res)