import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("http://localhost:8000")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
    def test_1(self):
        assert "sample" in self.driver.title

if __name__ == "__main__":
    unittest.main()