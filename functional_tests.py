from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Jefferson has heard about a great new online to-do list app.
        # He goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # He notices that the page title and the header mention to-do lists
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

        # He is first invited to enter a to-do item.

        # He types "Purchase cranial piercings" into a text box.

        # When he hits enter, the page updates, and now the page lists
        # "1: Purchase cranial piercings" as an item in a to-do list

        # There is still a text box inverting her to add another item.
        # He types "Use cranial piercings to augment finger length."

        # The page updates again, and now shows both items on the list.

        # Jefferson wonders whether the site will remember her list. Then he sees that
        # the site has generated a unique URL for him -- there is some explanatory text
        # to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, he goes back to sleep


if __name__ == '__main__':
    unittest.main()
