import time
from alg.base import BaseAlg
from entities.slide import Slide


class LSAlg(BaseAlg):
    def __init__(self, P):
        self.P = P
        self.N = len(P)
        self.best_score = 0
        self.best_show = []
        self.timer = 0

    def _2opt_next(self, best, current):
        if time.time() - self.timer > 60:
            self.output(current)
            print("Dumped")
            self.timer = time.time()
        n = len(current)
        for i in range(1, n - 1):
            for j in range(i + 2, n):
                old_local = self.score(current[i-1:i+1]) + self.score(current[j-1:j+1])
                new_local = self.score(
                    [current[i-1], current[j-1]]
                ) + self.score(
                    [current[i], current[j]]
                )
                if new_local > old_local:
                    new_path = current[:]
                    new_path[i:j] = current[j - 1:i - 1:-1]
                    score = best - old_local + new_local
                    # update the solution history
                    print(f"New best: {score} (+{score - best})")
                    return self._2opt_next(score, new_path)
        return best, current

    def _2opt_best(self, best, current):
        if time.time() - self.timer > 60:
            self.output(current)
            print("Dumped")
            self.timer = time.time()
        n = len(current)
        candidates = []
        for i in range(1, n - 1):
            for j in range(i + 2, min(n + 1, 100)):
                new_path = current[:]
                new_path[i:j] = current[j - 1:i - 1:-1]
                score = self.score(new_path)
                if score > best:
                    candidates.append((new_path, score))
        if not candidates:
            return  best, current
        new_path, new_score = max(candidates, key=lambda el: el[1])
        if new_score > best:
            # update the solution history
            print(f"New best: {new_score} (+{new_score - best})")
            return self._2opt_next(new_score, new_path)
        return best, current

    def solve(self, best_show, *args, **kwargs):
        self.best_show = best_show
        self.best_score = self.score(best_show)
        self.timer = time.time()
        score, show = self._2opt_next(self.best_score, best_show)
        # score, show = self._2opt_best(self.best_score, best_show)
        self.best_score, self.best_show = score, show
