import os
import unittest
import importlib
import argparse

def run_suite(suite_name, default_endpoint=None, prefix=None):
    suite_folder = f'tests/{suite_name}'
    if not os.path.exists(suite_folder):
        print(f"Suite {suite_name} folder not found.")
        return

    # Create a test suite
    test_suite = unittest.TestSuite()

    # Dynamically add tests to the suite
    for test_file in os.listdir(suite_folder):
        if test_file.endswith(".py") and test_file != '__init__.py':
            test_path = os.path.join(suite_folder, test_file)
            # Import the test module dynamically
            module_name = f'tests.{suite_name}.{test_file[:-3]}'  # Remove '.py'
            module = importlib.import_module(module_name)

            # Add each test case from the module to the test suite
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
                    if default_endpoint:
                        # Pass the endpoint as a class variable to test
                        obj.endpoint = default_endpoint
                    if prefix:
                        # Pass the prefix as a class variable to test
                        obj.prefix = prefix
                    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(obj))

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", required=True, help="Specify suite to run")
    parser.add_argument("--endpoint", help="Override endpoint for all tests in suite")
    parser.add_argument("--prefix", help="Prefix for the test name or usage", default=None)
    args = parser.parse_args()

    run_suite(args.suite, args.endpoint, args.prefix)
