"""
gate: guess, assess, try, expand
(c) 2023, Tim Menzies, BSD-2
Learn a little, guess a lot, try the strangest guess, repeat

USAGE:
  python3 gate.lua [OPTIONS] 

OPTIONS:
  -c --cohen  small effect size               = .35
  -f --file   csv data file name              = w2/data/auto93.csv
  -h --help   show help                       = False
  -k --k      low class frequency kludge      = 1
  -m --m      low attribute frequency kludge  = 2
  -s --seed   random number seed              = 31210
  -t --test   run test cases                  = None
  """

from helper import *
from tests import Tests

test_suite = Tests()
# for name in dir(test_suite):
#   if name.startswith('test_'):
#     print(getattr(test_suite, name))
inp_test_map = {name[5:]: getattr(test_suite, name) for name in dir(test_suite) if name.startswith('test_')}
# print(inp_test_map)
# e = test_suite.test_coerce
# print(e)
# inp_test_map = {
#     "coerce":test_suite.test_coerce
#     }

help_str = __doc__

the = {}


