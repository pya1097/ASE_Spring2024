from helper import *
from num import NUM

class Tests:
    # def __init__(self) -> None:
    #     self.f_tests = {}

    def test_coerce(self):
        assert coerce("true") == True
        # assert coerce("false") == False
        assert coerce("93") == 93
        # assert coerce("46.18") == 46.18
        # assert coerce("  coerce  ") == "coerce"
        # assert coerce("  29  ") == 29
        assert coerce("42") == 42
        assert coerce("3.14") == 3.14
    
    def test_cells(self):
        input = "homework, 44, false, true, 22.94"
        output = cells(input)
        assert output == ["homework", 44, False, True, 22.94]
    
    def test_roundoff(self):
        assert roundoff(42.5421, 2) == 42.54
        assert roundoff(70.853, 2) == 70.85
        assert roundoff("rounding") == "rounding"

    def test_mid_num(self):
        test_num = NUM()
        test_num.add(10)
        test_num.add(12)
        assert test_num.mid() == 11

    def run_test(self, test_func, test_name):
        try:
            test_func()
            print(f"Test {test_name} passed.")
        except Exception as e:
            # self.f_tests[test_name[5:]] = test_name[5:]  # append to failing test lists
            print(f"Test {test_name} failed: {e}")

    def run_tests(self):
        print("Running tests in TestSuite")
        test_functions = [func for func in dir(self) if func.startswith('test_') and callable(getattr(self, func))]
        for test_func_name in test_functions:
            test_func = getattr(self, test_func_name)
            self.run_test(test_func, test_func_name)  

if __name__ == '__main__':
    test_suite = Tests()
    test_suite.run_tests()