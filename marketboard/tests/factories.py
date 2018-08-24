from datetime import timedelta

import factory
from django.utils import timezone
from factory import Faker
from factory.fuzzy import FuzzyInteger, FuzzyChoice, FuzzyDateTime

from marketboard.models import SERVER_LIST


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'marketboard.Transaction'

    item_id = FuzzyInteger(1, 50)
    quantity = FuzzyInteger(1, 99)
    quality = Faker('pybool')
    price = FuzzyInteger(1, 100000)
    transaction_time = timezone.now()
    buyer = Faker('name')
    server = FuzzyChoice(SERVER_LIST)