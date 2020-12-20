from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is first invited to enter a to-do item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Purchase cranial piercings" into a text box.
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, the page updates, and now the page lists
        # "1: Purchase cranial piercings" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a text box inverting her to add another item.
        # He types "Use cranial piercings to augment finger length."
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on the list.

        # Jefferson wonders whether the site will remember her list. Then he sees that
        # the site has generated a unique URL for him -- there is some explanatory text
        # to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, he goes back to sleep


if __name__ == '__main__':
    unittest.main()
