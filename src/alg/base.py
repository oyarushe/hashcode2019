from path import OUTPUT_PATH
import sys
import os
import time
from entities.slide import Slide


class BaseAlg:

    def solve(self, *args, **kwargs):
        raise NotImplementedError

    def score(self, show: [Slide]):

        if len(show) < 2:
            return 0

        s = 0
        for l, r in zip(show, show[1:]):
            s += min([
                len(l.tags.intersection(r.tags)),
                len(l.tags - r.tags),
                len(r.tags - l.tags)
            ])

        return s

    def output(self, show):
        result = [str(len(show)) + "\n"]
        for slide in show:
            result.append(" ".join([str(photo.i) for photo in slide.photos]) + "\n")
        with open(os.path.join(OUTPUT_PATH, f"{sys.argv[1]}_{self.score(show)}_{int(time.time())}"), 'w') as f:
            f.writelines(result)



