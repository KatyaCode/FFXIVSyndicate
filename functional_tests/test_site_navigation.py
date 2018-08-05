from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_can_visit_and_navigate_website(self):
        # Shovel has heard about a new WebApp for making tons of gil and visits the url
        self.browser.get(self.live_server_url)

        # He sees from the title and heading that this is the correct site
        self.assertIn('FFXIV Syndicate', self.browser.title)
        page_heading = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('FFXIV Syndicate', page_heading)

        # Curious, he decides to check how the markets are doing back on Ultros
        ultros_link = self.browser.find_element_by_link_text('Ultros')
        ultros_link.click()

        self.fail('Finish Writing')
