from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row_text for row in rows])

    def test_can_start_a_todo_list(self):
        # Lauren has heard about a cool new online to-do list app. She goes to check the home
        # page
        self.browser.get("http://localhost:8000")

        # the new django page vs the book from 2017 has different words in the browser title.
        # She notices the page title and header mentioned todo list
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)
        # She is invited to enter a to-do item right away
        inputbox = self.browser.find_element(By.ID, "id_new_item")

        # She types "Buy new journal for 2025" into the text box (One of Lauren's hobby is
        # junk journaling)
        inputbox.send_keys("Buy new journal for 2025")
        # When she hits enter, the page updates, and now the page lists "1. Buy new journal
        # for 2025" as an item on the todo list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # There's still a text box inviting her to add another item. She enters "use items in the
        # house to make junk journal" (Lauren uses newspaper and magazine cutouts for her junk
        # journals)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("use items in the house to make junk journal")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, now showing both items
        self.check_for_row_in_list_table("1. Buy new journal for 2025")
        self.check_for_row_in_list_table(
            "2. use items in the house to make junk journal"
        )
        # Lauren wonders if the site will remember her list. Then she sees that the site has generated
        # a unique url for her -- there is some explanation text to that effect

        # She visits the url, her items are still there

        # Satisfied, she goes and watch the Good Witch on Hall Mark.


if __name__ == "__main__":
    unittest.main()
