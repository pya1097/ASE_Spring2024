import math, re
import sys, ast

def coerce(x):
    try : return ast.literal_eval(x)
    except Exception: return x.strip()

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

def round(n, ndecs=None):
    if type(n) == str:
        return n
    if math.floor(n) == n:
        return n
    mult = 10**(ndecs or 2)
    return math.floor(n * mult + 0.5) / mult

def settings(s):
    inp = {}
    s_inp = {}
    options = re.findall(r'-(\w+)\s+--(\w+)\s+.*=\s*(\S+)', s)
    for option in options:
        short_form, full_form, default_value = option
        inp[full_form] = coerce(default_value)
        s_inp[short_form] = full_form
    options_dict = {}
    options = sys.argv[1:]

    if("--help" in options or "-h" in options):
        inp["help"]=True
        return inp,s_inp

    for i in range(0, len(options), 2):
        options_dict[options[i]] = options[i+1]

    for opt,val in options_dict.items():
        if opt.startswith('--'):
            inp[opt[2:]] = coerce(val)
        elif opt.startswith('-'):
            inp[s_inp[opt[1:]]] = coerce(val)

    return inp,s_inp