import unittest
import xmlrunner

if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = 'tests/'

    suite = loader.discover(start_dir)

    runner = xmlrunner.XMLTestRunner(output='/tmp/test-results')
    runner.run(suite)