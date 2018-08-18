from enum import Enum

from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices

SERVER_LIST = [
    'Aegis',
    'Atomos',
    'Carbuncle',
    'Garuda',
    'Gungnir',
    'Kujata',
    'Ramuh',
    'Tonberry',
    'Typhon',
    'Unicorn',
    'Alexander',
    'Bahamut',
    'Durandal',
    'Fenrir',
    'Ifrit',
    'Ridill',
    'Tiamat',
    'Ultima',
    'Valefor',
    'Yojimbo',
    'Zeromus',
    'Anima',
    'Asura',
    'Belias',
    'Chocobo',
    'Hades',
    'Ixion',
    'Mandragora',
    'Masamune',
    'Pandemonium',
    'Shinryu',
    'Titan',
    'Adamantoise',
    'Balmung',
    'Cactuar',
    'Coeurl',
    'Fairy',
    'Gilgamesh',
    'Goblin',
    'Jenova',
    'Mateus',
    'Midgardsormr',
    'Sargatanas',
    'Siren',
    'Zalera',
    'Behemoth',
    'Brynhildr',
    'Diabolos',
    'Excalibur',
    'Exodus',
    'Famfrit',
    'Hyperion',
    'Lamia',
    'Leviathan',
    'Malboro',
    'Ultros',
    'Cerberus',
    'Lich',
    'Louisoix',
    'Moogle',
    'Odin',
    'Omega',
    'Phoenix',
    'Ragnarok',
    'Shiva',
    'Zodiark',
]

SERVER_TUPLES = Choices(*SERVER_LIST)


class Transaction(TimeStampedModel):
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    quality = models.BooleanField()
    price = models.IntegerField()
    transaction_time = models.DateTimeField()
    buyer = models.CharField(max_length=21)
    server = models.CharField(
        max_length=12,
        choices=SERVER_TUPLES
    )
