import math

class SYM:
    # Create: Creates the initial object of type SYM 
    def __init__(self, s=" ", n=0):    
        self.txt = s
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    # Update: Used when update the SYM type cols when data rows are added
    def add(self, x):
        if x != "?":
            self.n = self.n + 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    #Query to return the mode of the column
    def mid(self):
        return self.mode
    
    def div(self, e=0):
        for v in self.has.values():
            e -= v / self.n * math.log(v / self.n, 2)
        return e

    def small(self):
        return 0

    # def like(self, x, prior):
    #     return ((self.has[x] or 0) + the.m * prior) / (self.n + the.m)