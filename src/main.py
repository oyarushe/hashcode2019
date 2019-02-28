import sys
import os
from path import INPUT_PATH
from configs.logger import print

IN_FILE = os.path.join(INPUT_PATH, sys.argv[1])

print(f"Working with file {IN_FILE}")


class Photo(object):
    def __init__(self, t, tags):
        if not isinstance(t, str) or (t != 'H' and t != 'V'):
            raise ValueError

        if not isinstance(tags, set):
            raise ValueError

        self.t = t
        self.tags = tags


def read_file(file_in):
    photos = []
    with open(file_in) as f:
        l = f.readlines()

    for line in l[1:]:
        s_l = line.split()
        photos.append(Photo(s_l[0], set(s_l[2:])))
    return photos


if __name__ == '__main__':
    photos = read_file(IN_FILE)
