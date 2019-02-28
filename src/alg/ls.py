from entities.slide import Slide


class LSAlg:
    def __init__(self, P, T):
        self.P = P
        self.N = len(P)
        self.T = T
        self.best = 0

    def _first_set(self):
        X = []
        last_v_slide = None
        for i, p in enumerate(self.P):
            if p.t == 'H':
                X.append(Slide(p))
            elif p.t == 'V':
                if not last_v_slide:
                    last_v_slide = Slide(p)
                    X.append(last_v_slide)
                else:
                    last_v_slide.add_photo(p)
                    X.append(Slide)


    def _2opt_next(self, best, current_path):
        n = len(self.D)
        for i in range(1, n - 1):
            for j in range(i + 2, n + 1):
                new_path = current_path[:]
                new_path[i:j] = current_path[j - 1:i - 1:-1]
                if self.score(new_path) < best:
                    # update the solution history
                    self.progress.append(new_path)

                    return self._2opt_next(self.score(new_path), new_path)
        return best, current_path

    def solve(self, *args, **kwargs):
        pass

    def score(self, X):
        raise NotImplementedError

    def output(self, *args, **kwargs):
        raise NotImplementedError
