from django.test import TestCase
from django.db import IntegrityError, DataError
from django.utils import timezone

from marketboard.models import Transaction


class TransactionModelTest(TestCase):

    def test_cannot_create_empty_transaction(self):
        transaction = Transaction()
        with self.assertRaises(IntegrityError):
            transaction.save()

    def test_cannot_create_transaction_with_invalid_buyer_name(self):
        transaction = Transaction(item_id=1, quantity=1, quality=False, price=1,
                                  transaction_time=timezone.now(), buyer='A name that is very much too long')
        with self.assertRaises(DataError):
            transaction.save()
