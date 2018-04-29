import factory
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

from . import models


class RepresentativeFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Representative

    username = factory.LazyAttribute(lambda n: get_random_string())
    password = factory.LazyAttribute(lambda n: get_random_string())
    email = factory.Faker("email")
    first_name = factory.Faker("name")
    last_name = factory.Faker("name")


class StaffUser(factory.DjangoModelFactory):

    class Meta:
        model = get_user_model()

    username = factory.LazyAttribute(lambda _: get_random_string(8))
    password = factory.LazyAttribute(lambda _: get_random_string(8))
    email = factory.Faker("email")
    is_staff = True
