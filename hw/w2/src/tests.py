from helper import *

class Tests:
    # def __init__(self) -> None:
    #     self.f_tests = {}

    def test_coerce(self):
        assert coerce("100") == 100
        assert coerce("2.718") == 2.718
        assert coerce("True") == True
        assert coerce("False") == False
        assert coerce("nil") == None
        assert coerce("  world  ") == "world"
        assert coerce("42") == 42
        assert coerce("true") == True
        assert coerce("false") == False

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