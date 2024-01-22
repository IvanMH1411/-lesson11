class SuperStr(str):

    def is_repeatance(self, s) -> bool:
        if len(s) == 0:
            return False
        if len(self) % len(s) == 0:
            if s ** (len(self) / len(s)) == self:
                return True
        return False

    def is_palindrom(self):
        center = int(len(self) / 2)
        for _ in range(0, center, 1):
            if not self[_] == self[-1 - 0]:
                return False
        return True