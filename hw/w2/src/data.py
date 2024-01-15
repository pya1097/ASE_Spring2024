#Read data file
from helper import *
from row import ROW
from cols import COLS
from sym import SYM

class DATA:
    def __init__(self, src=[], fun=None):
        self.rows = []
        self.cols = None
        if isinstance(src,str):
            for _,x in csv(src):
                self.add(x, fun)
        else:
            for _,x in enumerate(src):
                self.add(x, fun)
    
    def add(self, t, fun):
        row = ROW(t) if type(t) == list else t
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
           self.cols = COLS(row)

    def stats(self, fun = None, ndivs = None):
        u = {".N": len(self.rows)}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                u[col.txt] = col.mid()
            else:
                u[col.txt] = round(col.mid())
        return u