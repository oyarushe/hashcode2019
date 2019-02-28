from path import OUTPUT_PATH
import sys
import os


class BaseAlg:

    def solve(self, *args, **kwargs):
        raise NotImplementedError

    def score(self, show):
        s = 0
        for l, r in zip(show, show[1:]):
            s += min([
                len(l.intersection(r)),
                len(l - r),
                len(r - l)
            ])

        return s

    def output(self, show):
        with open(os.path.join(OUTPUT_PATH, sys.argv[1])):
            pass

