import os
import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

ARTIFACTS = Path(__file__).parent.parent / "artifacts"


class PythonOrgSearch(unittest.TestCase):
    """
    An example selenium test case that makes an assertion
    takes a screenshot and checks runtime environment
    """

    @classmethod
    def setUpClass(cls) -> None:
        Path(ARTIFACTS).mkdir(exist_ok=True)

    def setUp(self):
        if os.getenv("GITHUB_ACTIONS") or os.getenv("HEADLESS"):
            options = Options()
            options.add_argument("--headless")
        else:
            options = None

        self.driver = webdriver.Chrome(options=options)

    def test_search_in_python_org(self):
        self.driver.get("http://www.python.org")
        self.driver.save_screenshot(str(Path(ARTIFACTS) / "screenshot.png"))
        self.assertIn("Python", self.driver.title)
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
