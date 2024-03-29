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
            #for _,x in enumerate(src):
            self.add(src, fun)
    
    def add(self, t, fun=None):
        row = t if type(t) == ROW else ROW(t)
        # row = ROW(t) if type(t) == list else t
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
        #    print('here', row)
           self.cols = COLS(row)

    def stats(self, fun = None, ndivs = None):
        u = {".N": len(self.rows)}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                u[col.txt] = int(col.mid())
            else:
                u[col.txt] = roundoff(col.mid())
        return u
    
    def classes_data(self):
        table = {}
        col = self.cols.klass
        table["N"] = len(self.rows)
        table["klasses"] = len(col.has)
        for key, val in col.has.items():
            table[key] = val
            table[key+"%"] = roundoff(val*100/len(self.rows), 2)
        return table