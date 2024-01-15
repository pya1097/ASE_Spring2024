"""
gate: guess, assess, try, expand
(c) 2023, Tim Menzies, BSD-2
Learn a little, guess a lot, try the strangest guess, repeat

USAGE:
  python3 gate.lua [OPTIONS] 

OPTIONS:
  -c --cohen  small effect size               = .35
  -f --file   csv data file name              = '../data/diabetes.csv'
  -h --help   show help                       = False
  -k --k      low class frequency kludge      = 1
  -m --m      low attribute frequency kludge  = 2
  -s --seed   random number seed              = 31210
  -t --todo   start up action                 = 'help'
  """

import sys
from helper import *
import re

def settings(s):
    t = {}
    opt_dir = {}
    options = re.findall(r'-(\w+)\s+--(\w+)\s+.*=\s*(\S+)', s)
    for option in options:
        short_form, full_form, default_value = option
        t[full_form] = coerce(default_value)
        opt_dir[short_form] = full_form
    return [t, opt_dir]

def cli(t, opt_dir):
    options_dict = {}
    options = sys.argv[1:]

    if("--help" in options or "-h" in options):
        t["help"]=True
        return t

    for i in range(0, len(options), 2):
        options_dict[options[i]] = options[i+1]

    for opt,val in options_dict.items():
        if opt.startswith('--'):
            t[opt[2:]] = coerce(val)
        elif opt.startswith('-'):
            t[opt_dir[opt[1:]]] = coerce(val)

    return t

help_str = __doc__
the = {}

t, opt_dir = settings(help_str)
t = cli(t, opt_dir)