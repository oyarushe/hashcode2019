class BaseAlg:
    def solve(self, *args, **kwargs):
        raise NotImplementedError

    def score(self, *args, **kwargs):
        raise NotImplementedError

    def output(self, *args, **kwargs):
        raise NotImplementedError