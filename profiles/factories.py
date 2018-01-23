import factory
from django.utils.crypto import get_random_string

from . import models


class RepresentativeFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Representative

    username = factory.LazyAttribute(lambda n: get_random_string())
    password = factory.LazyAttribute(lambda n: get_random_string())
    email = factory.Faker('email')
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
