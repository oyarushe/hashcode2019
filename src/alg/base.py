from path import OUTPUT_PATH
import sys
import os
import time
from entities.slide import Slide
from functools import lru_cache


class BaseAlg:

    def solve(self, *args, **kwargs):
        raise NotImplementedError

    @lru_cache(maxsize=None)
    def _dist(self, l, r):
        return min([
            len(l.tags.intersection(r.tags)),
            len(l.tags - r.tags),
            len(r.tags - l.tags)
        ])

    def _pairs(self, show):
        return zip(show, show[1:])

    def score(self, show: [Slide]):
        if len(show) < 2:
            return 0

        return sum(self._dist(l, r) for l, r in self._pairs(show))

    def output(self, show):
        result = [str(len(show)) + "\n"]
        for slide in show:
            result.append(" ".join([str(photo.i) for photo in slide.photos]) + "\n")
        with open(os.path.join(OUTPUT_PATH, f"{sys.argv[1]}_{self.score(show)}_{int(time.time())}"), 'w') as f:
            f.writelines(result)
