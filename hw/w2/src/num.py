
class NUM:
    # Inititalizing  NUM instance
    def __inti__(self, s = "", n=0):
        self.txt = s
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = 0 if s.endswith("-") else 1
    
    # Updating class variables
    def add(self, x):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d/self.n
            self.m2 += d*(x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)



    # Class methods (queries)
    def mid(self):
        return self.mu
    
    def div(self):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** 0.5
    
    def small(self):
        return the.cohen * self.div()

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1E-30)
    
    def like(self, x, _, nom=None, denom=None):
        mu, sd = self.mid(), self.div() + 1E-30
        nom = 2.718**(-0.5 * (x - mu)**2 / (sd**2))
        denom = sd * 2.5 + 1E-30
        return nom / denom 
