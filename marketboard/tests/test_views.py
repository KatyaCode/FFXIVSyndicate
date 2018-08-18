from django.test import TestCase

from marketboard.models import SERVER_LIST


class LandingPageTest(TestCase):

    def test_landing_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'landing.html')

    def test_all_servers_listed_on_landing_page(self):
        response = self.client.get('/')
        for server in [server_tuple[0] for server_tuple in SERVER_LIST]:
            self.assertContains(response, server)
