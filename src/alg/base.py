from path import OUTPUT_PATH
import sys
import os
from entities.slide import Slide


class BaseAlg:

    def solve(self, *args, **kwargs):
        raise NotImplementedError

    def score(self, show: [Slide]):
        s = 0
        for l, r in zip(show, show[1:]):
            s += min([
                len(l.tags.intersection(r.tags)),
                len(l.tags - r.tags),
                len(r.tags - l.tags)
            ])

        return s

    def output(self, show):
        with open(os.path.join(OUTPUT_PATH, sys.argv[1])):
            pass

