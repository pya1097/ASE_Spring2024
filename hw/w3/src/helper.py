import math, re
import sys, ast
# from config import the


def coerce(s):
    def fun(s2):
        return None if s2.lower() in ["null", "nil", "none"] else s2.lower() == "true" or (s2.lower() != "false" and s2)
    try:
        return float(s)
    except ValueError:
        return fun(re.match(r'^\s*(.*\S)', s).group(1)) if isinstance(s, str) else s

def cells(s):
    t = []
    for s1 in s.split(','):
        t.append(coerce(s1))
    return t

def csv(src):
    i=0
    src = sys.stdin if src == "−" else open(src ,"r")
    for s in src:
        i += 1
        yield i, cells(s)
    src.close()

def roundoff(n, ndecs=None):
    if type(n) == str:
        return n
    if math.floor(n) == n:
        return n
    mult = 10**(ndecs or 2)
    return math.floor(n * mult + 0.5) / mult



