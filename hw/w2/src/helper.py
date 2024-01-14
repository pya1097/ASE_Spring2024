import math
import sys

def coerce(s1, fun):
    def fun(s2):
        return None if s2 == "nil" else s2 == "true" or (s2 != "false" and s2)
    
    return math.tointeger(s1) or float(s1) or fun(s1.strip())

def cells(s, t):
    t = []
    for s1 in s.split(','):
        t.append(coerce(s1))
    return t

def csv(src, i):
    i=0
    src = sys.stdin if src == "−" else open(src ,"r")
    for s in src:
        i += 1
        yield i, cells(s)
    src.close()

