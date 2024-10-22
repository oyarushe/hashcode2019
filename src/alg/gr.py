from alg.base import BaseAlg
from entities.slide import Slide


class GrAlg(BaseAlg):
    def __init__(self, P):
        self.P = P
        self.N = len(P)
        self.best_score = 0
        self.best_show = []

    def _first_set(self):
        X = []
        last_v_slide = None
        slide_idx = 0
        for i, p in enumerate(self.P):
            if p.t == 'H':
                X.append(Slide(p, idx=slide_idx))
                slide_idx += 1
            elif p.t == 'V':
                if not last_v_slide:
                    last_v_slide = Slide(p, _type=Slide.TYPE_COMBINED, idx=slide_idx)
                    slide_idx += 1
                    X.append(last_v_slide)
                else:
                    last_v_slide.add_photo(p)
                    last_v_slide = None
        return X

    def _find_best(self, show, X):
        cur = 0
        b_x = None
        for x in X[:10]:
            score = self.score([show[-1], x])
            if b_x is None or cur < score:
                b_x = x
                cur = score
        print(f"{cur} {len(show)}")
        return b_x

    def solve(self, *args, **kwargs):

        X = self._first_set()
        show = [X[0]]

        X.remove(X[0])
        for i in range(len(X)):
            x = self._find_best(show, X)
            show.append(x)
            X.remove(x)

        self.best_score, self.best_show = self.score(show), show
