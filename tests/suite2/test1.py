import unittest
import requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress InsecureRequestWarning for SSL verification
warnings.simplefilter('ignore', InsecureRequestWarning)

class TestSuiteExample1(unittest.TestCase):

    def test_endpoint(self):
        url = "https://your-api-endpoint.com"
        response = requests.get(url, verify=False)  # Disable SSL verification
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
