from alg.base import BaseAlg
from entities.slide import Slide


class LSAlg(BaseAlg):
    def __init__(self, P):
        self.P = P
        self.N = len(P)
        self.best_score = 0
        self.best_show = []

    def _first_set(self):
        X = []
        last_v_slide = None
        for i, p in enumerate(self.P):
            if p.t == 'H':
                X.append(Slide(p))
            elif p.t == 'V':
                if not last_v_slide:
                    last_v_slide = Slide(p, _type=Slide.TYPE_COMBINED)
                    X.append(last_v_slide)
                else:
                    last_v_slide.add_photo(p)
                    last_v_slide = None
        return X

    def _2opt_next(self, best, current):
        n = len(current)
        for i in range(1, n - 1):
            for j in range(i + 2, n + 1):
                new_path = current[:]
                new_path[i:j] = current[j - 1:i - 1:-1]
                score = self.score(new_path)
                if score > best:
                    # update the solution history
                    print(f"New best: {score} (+{score - best})")
                    return self._2opt_next(score, new_path)
        return best, current

    def solve(self, *args, **kwargs):
        X = self._first_set()
        self.best_show = X
        self.best_score = self.score(X)
        score, show = self._2opt_next(self.best_score, X)
        self.best_score, self.best_show = score, show
