from helper import *
from num import NUM
from sym import SYM
class Tests:

    def test_add_sym(self):
        sym = SYM("origin",5)
        sym.add("1")
        assert sym.n == 1
        assert sym.has == {"1": 1}
        assert sym.mode == "1"
        assert sym.most == 1

        # testing by adding a row with same origin value
        sym.add("1")
        assert sym.n == 2
        assert sym.has == {"1": 2}
        assert sym.mode == "1"
        assert sym.most == 2

    def test_mid_sym(self):
        sym = SYM("origin",5)
        sym.add("1")
        sym.add("2")
        assert sym.mid() == "1"

    def test_div_sym(self):
        sym = SYM("origin",5)
        sym.add("1")
        sym.add("1")

        assert sym.div() == 0

    def test_small_sym(self):
        sym = SYM("origin",5)
        sym.add("1")

        assert sym.small() == 0

    def test_coerce(self):
        assert coerce("true") == True
        assert coerce("93") == 93
        assert coerce("46.18") == 46.18
        assert coerce("  coerce  ") == "coerce"
        assert coerce("nil") == None
    
    def test_cells(self):
        input = "homework, 44, false, true, 22.94"
        output = cells(input)
        assert output == ["homework", 44, False, True, 22.94]
    
    def test_roundoff(self):
        assert round(42.5421, 2) == 42.54
        assert round(70.853, 2) == 70.85
        #assert round("rounding") == "rounding"

    def test_mid_num(self):
        test_num = NUM()
        test_num.add(10)
        test_num.add(12)
        assert test_num.mid() == 11

    def run(self):
        print("-------------------Test Results--------------------")
        test_functions = [func for func in dir(self) if func.startswith('test_') and callable(getattr(self, func))]
        for test_func_name in test_functions:
            test_func = getattr(self, test_func_name)
            try:
                test_func()
                print("Test "+test_func_name+" passed.")
            except Exception as e:
                print("Test "+test_func_name+" failed: "+str(e))

if __name__ == '__main__':
    test_suite = Tests()
    test_suite.run_tests()