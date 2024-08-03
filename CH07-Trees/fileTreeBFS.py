from os import listdir
from os.path import isfile, join

# listdir("pics") => ['2001','arc.png']


def printnames(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            printnames(fullpath)


printnames("pics")
