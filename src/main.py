import sys
import os
import time
from path import INPUT_PATH
from configs.logger import print
from alg.ls import LSAlg
from alg.gr import GrAlg

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


def main():
    photos = read_file(IN_FILE)

    print(f"File {IN_FILE} loaded")

    ga = GrAlg(photos)

    print("Greedy initiated")

    start = time.time()

    ga.solve()

    long = time.time() - start

    print(f"""
            Greedy: 
             - score: {ga.best_score}
             - time: {long}
            """)

    ga.output(ga.best_show)

    ls = LSAlg(photos)

    print("LS initiated")

    start = time.time()

    ls.solve(ga.best_show)

    long = time.time() - start

    print(f"""
        Local search: 
         - score: {ls.best_score}
         - time: {long}
        """)

    ls.output(ls.best_show)


if __name__ == '__main__':
    # import cProfile
    #
    # cProfile.run('main()')
    main()