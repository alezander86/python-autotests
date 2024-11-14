import unittest
import requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress InsecureRequestWarning for SSL verification
warnings.simplefilter('ignore', InsecureRequestWarning)

class TestSuiteExample1(unittest.TestCase):

    def test_endpoint(self):
        url = self.endpoint
        response = requests.get(url, verify=False)  # Disable SSL verification
        self.assertEqual(response.status_code, 200)

        # Check if a specific prefix is used, for example, print it
        if hasattr(self, 'prefix'):
            print(f"Running test with prefix: {self.prefix}")

if __name__ == "__main__":
    unittest.main()
