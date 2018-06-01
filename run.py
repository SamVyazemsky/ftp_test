import unittest
import test_ftp


def main():
    """
    Running tests for ftp
    :return:
    """
    test_result = unittest.TestResult()
    test_load = unittest.TestLoader()
    suit = test_load.loadTestsFromModule(test_ftp)
    runner = unittest.TextTestRunner(verbosity=1)
    test_result = runner.run(suit)
    print("errors")
    print(len(test_result.errors))
    print("failures")
    print(len(test_result.failures))
    print("skipped")
    print(len(test_result.skipped))
    print("testsRun")
    print(test_result.testsRun)


if __name__ == '__main__':
    main()
