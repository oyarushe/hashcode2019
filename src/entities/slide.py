class Slide:
    TYPE_COMBINED = 'C'
    TYPE_SINGLE = 'S'

    def __init__(self, *photos, _type=TYPE_SINGLE, idx=None):
        assert idx is not None
        self.idx = idx
        if _type == self.TYPE_SINGLE:
            self.tags = photos[0].tags
            self.type = self.TYPE_SINGLE
        elif _type == self.TYPE_COMBINED:
            self.tags = photos[0].tags.union(photos[1].tags) if len(photos) == 2 else photos[0].tags
            # for prepared vertical slides with one photo
            self.type = self.TYPE_COMBINED
        self.photos = list(photos)

    def add_photo(self, p):
        if len(self.photos) != 1:
            raise Exception("Malformed slide")
        self.photos.append(p)
        self.type = self.TYPE_COMBINED
        self.tags = self.tags.union(p.tags)

    def __hash__(self):
        return self.idx

    def __repr__(self):
        return f"Slide #{self.idx} ({self.type}, {len(self.photos)})"
