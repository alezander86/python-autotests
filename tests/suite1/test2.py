import unittest
import requests

class TestSuiteExample1(unittest.TestCase):

    def test_endpoint(self):
        url = "https://www.google.com"
        response = requests.get(url, verify=False)  # Disable SSL verification
        self.assertEqual(response.status_code, 200)
        # Save the response content in a variable
        page_content = response.text.lower()

        # Print a snippet of the page content (first 500 characters)
        print("Page Content Snippet:")
        print(page_content[:500])  # Display the first 500 characters of the page content

if __name__ == "__main__":
    unittest.main()
