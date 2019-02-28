import sys
import os
import time
from path import INPUT_PATH
from configs.logger import print
from alg.ls import LSAlg

IN_FILE = os.path.join(INPUT_PATH, sys.argv[1])

print(f"Working with file {IN_FILE}")


class Photo(object):
    def __init__(self, t, tags, i):
        if not isinstance(t, str) or (t != 'H' and t != 'V'):
            raise ValueError

        if not isinstance(tags, set):
            raise ValueError

        self.t = t
        self.tags = tags
        self.i = i


def read_file(file_in):
    photos = []
    with open(file_in) as f:
        l = f.readlines()

    t_v = 0

    for i, line in enumerate(l[1:]):
        s_l = line.split()
        photos.append(Photo(s_l[0], set(s_l[2:]), i))
        if s_l[0] == 'V':
            t_v += 1

    return photos


if __name__ == '__main__':
    photos = read_file(IN_FILE)

    print(f"File {IN_FILE} loaded")

    ls = LSAlg(photos)

    print("LS initiated")

    start = time.time()

    ls.solve()

    long = time.time() - start

    print(f"""
    Local search: 
     - score: {ls.best_score}
     - time: {long}
    """)

    ls.output(ls.best_show)
