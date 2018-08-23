from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from marketboard.models import SERVER_LIST
from marketboard.tests.factories import TransactionFactory


class LandingPageTest(TestCase):

    def test_landing_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'landing.html')

    def test_all_servers_listed_on_landing_page(self):
        response = self.client.get('/')
        for server in [server for server in SERVER_LIST]:
            self.assertContains(response, server)


class HomePageTest(TestCase):

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/marketboard/Ultros')
        self.assertTemplateUsed(response, 'home.html')

    def test_old_transactions_not_being_passed_to_template(self):
        old_transaction = TransactionFactory(
            transaction_time=timezone.now() - timedelta(days=40),
            server='Ultros'
        )
        response = self.client.get('/marketboard/Ultros')
        self.assertNotContains(response, old_transaction)

    def test_other_servers_not_being_passed_to_template(self):
        other_server_transaction = TransactionFactory(
            server='Hyperion'
        )
        response = self.client.get('/marketboard/Ultros')
        self.assertNotContains(response, other_server_transaction)

    def test_valid_Transaction_is_being_passed_to_template(self):
        transaction = TransactionFactory(server='Ultros')
        response = self.client.get('/marketboard/Ultros')
        self.assertContains(response, transaction)

    def test_server_name_passed_to_template(self):
        response = self.client.get('/marketboard/Ultros')
        self.assertContains(response, 'Ultros')


class ItemDetailViewTest(TestCase):

    def test_detail_view_passes_matching_transactions_to_template(self):
        transaction = TransactionFactory(item_id=111, server='Ultros')
        response = self.client.get('/marketboard/Ultros/item/111')
        self.assertContains(response, transaction)