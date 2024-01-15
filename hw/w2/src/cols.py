from num import NUM
from sym import SYM

class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = [], [], []
        self.klass = None
        self.names = row.cells
        for at,txt in enumerate(row.cells):
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at)
            self.all.append(col)
            if not txt.endsWith("X"):
                if txt.endsWith("!"):
                    self.klass = col
                (txt.find("[!+-]$") and self.y or self.x)[at] = col 
    
    def add(self, row):
        for _,cols in [self.x, self.y]:
            for col in cols:
                col.add(row.cells[col.at])
            return row