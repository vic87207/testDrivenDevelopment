from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Lauren has heard about a cool new online to-do list app. She goes to check the home
        # page
        self.browser.get("http://localhost:8000")

        # the new django page vs the book from 2017 has different words in the browser title.
        # She notices the page title and header mentioned todo list
        self.assertIn("TO-DO", self.browser.title)
        self.fail("Finish the test!")
        # She is invited to enter a to-do item right away

        # She types "Buy new journal for 2025" into the text box (One of Lauren's hobby is
        # junk journaling)

        # When she hits enter, the page updates, and now the page lists "1. Buy new journal
        # for 2025" as an item on the todo list

        # There's still a text box inviting her to add another item. She enters "use items in the
        # house to make junk journal" (Lauren uses newspaper and magazine cutouts for her junk
        # journals)

        # The page updates again, now showing both items

        # Lauren wonders if the site will remember her list. Then she sees that the site has generated
        # a unique url for her -- there is some explanation text to that effect

        # She visits the url, her items are still there

        # Satisfied, she goes and watch the Good Witch on Hall Mark.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
