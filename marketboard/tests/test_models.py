from contextlib import contextmanager

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from marketboard.models import Transaction, SERVER_LIST


class TransactionModelTest(TestCase):

    @contextmanager
    def assertValidationErrors(self, fields):
        """
        Assert that a validation error is raised, containing all the specified fields,
        and only the specified fields.
        """
        try:
            yield
            raise AssertionError('ValidationError not raised')
        except ValidationError as e:
            self.assertEqual(set(fields), set(e.message_dict.keys()))

    def test_cannot_create_empty_transaction(self):
        transaction = Transaction()
        with self.assertValidationErrors(['item_id', 'quantity', 'quality', 'price',
                                          'transaction_time', 'buyer', 'server']):
            transaction.full_clean()

    def test_cannot_create_transaction_with_invalid_buyer_name(self):
        transaction = Transaction(item_id=1, quantity=1, quality=False, price=1, server='Ultros',
                                  transaction_time=timezone.now(), buyer='A name that is very much too long')
        with self.assertValidationErrors(['buyer']):
            transaction.full_clean()

    def test_cannot_save_transaction_with_invalid_server_choice(self):
        transaction = Transaction(item_id=1, quantity=1, quality=False, price=1,
                                  transaction_time=timezone.now(), buyer='Shovel Akaza',
                                  server='Cloud')
        with self.assertValidationErrors(['server']):
            transaction.full_clean()
