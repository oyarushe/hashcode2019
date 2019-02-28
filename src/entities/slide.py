class Slide:
    TYPE_COMBINED = 1
    TYPE_SINGLE = 2

    def __init__(self, *photos):
        if len(photos) == 1:
            self.tags = photos[0].tags
            self.type = self.TYPE_SINGLE
        elif len(photos) == 2:
            self.tags = photos[0].tags.union(photos[1].tags)
            self.type = self.TYPE_COMBINED
        else:
            raise Exception("Invalid slide")
        self.photos = photos

    def add_photo(self, p):
        if len(self.photos) != 1:
            raise Exception("Malformed slide")
        self.photos.append(p)
        self.type = self.TYPE_COMBINED
        self.tags = self.tags.union(p.tags)
