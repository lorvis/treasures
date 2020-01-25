
class Hunter:

    def __init__(self, tres_map, start):
        self.pos = int(start)
        self.tres_map = tres_map

    def obtain(self):
        curr = str(self.pos)
        loot = self.tres_map[int(curr[0]) - 1][int(curr[1]) - 1]
        self.pos = loot
        return loot


class Organization:
    storage = []

    def __init__(self, tres_map, start):
        self.hunter = Hunter(tres_map, start)
        self.storage.append(int(start))

    def hunt(self):
        self.storage.append(self.hunter.obtain())
        while True:
            loot = self.hunter.obtain()
            if loot == self.storage[-1]:
                return self.storage
            else:
                self.storage.append(loot)







