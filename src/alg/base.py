from path import OUTPUT_PATH
import sys
import os
import time


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
        result = [str(len(show))]
        for slide in show:
            result.append(" ".join([photo.i for photo in slide.photos]))
        with open(os.path.join(OUTPUT_PATH, f"{sys.argv[1]}_{int(time.time())}"), 'w') as f:
            f.writelines(result)



