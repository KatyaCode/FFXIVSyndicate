import time

from django.utils import timezone
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException

from marketboard.tests.factories import TransactionFactory

MAX_WAIT = 10


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        TransactionFactory(
            item_id='111',
            transaction_time=timezone.now(),
            server='Ultros',
            buyer='Katya Dankri'
        )
        TransactionFactory(
            item_id='444',
            transaction_time=timezone.now(),
            server='Hyperion',
        )

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def wait(fn):
        def modified_fn(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)

        return modified_fn

    @wait
    def wait_for(self, fn):
        return fn()

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

        # He finds himself on a page that looks specific to the Ultros server's market activity
        self.wait_for(lambda: self.assertIn('Ultros',
                                            self.browser.find_element_by_tag_name('h1').text))

        # He sees a list of recent item transactions specific to the Ultros server
        recent_transactions = self.browser.find_element_by_id('recentTransactions').text
        self.assertIn('111', recent_transactions)
        self.assertNotIn('404', recent_transactions)

        # Interested in what else he can learn, he clicks on the link to the
        # item details within the recent transactions table
        details_link = self.browser.find_element_by_link_text('111')
        details_link.click()

        # He's presented with a page showing the details of the item on Ultros,
        # listing recent transactions on that server involving that item, including the buyer.
        self.wait_for(lambda: self.assertIn('111',
                                            self.browser.find_element_by_tag_name('h1').text))
        recent_item_transactions = self.browser.find_element_by_id('recentTransactions')
        self.assertNotIn('444', recent_item_transactions)
        self.assertIn('111', recent_item_transactions)
        self.assertIn('Katya Dankri', recent_item_transactions)

        # Recognizing a familiar name, he clicks on the buyer link to see what his
        # friend has been purchasing

        buyer_link = self.browser.find_element_by_link_text('Katya Dankri')
        buyer_link.click()

        # He gets taken to another page showing a list of all transactions performed by
        # that buyer, including the item that he just navigated to that page from
        self.wait_for(lambda: self.assertIn('Katya Dankri',
                                            self.browser.find_element_by_tag_name('h1').text))
        recent_buyer_transactions = self.browser.find_element_by_id('recentTransactions')
        self.assertIn('111', recent_buyer_transactions)

        # Noting how useful the sight might be for him, Shovel closes his browser
        # and goes back to watching anime.
