import factory

from . import models


class AdvertiserFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Advertiser

    email = factory.Faker("email")
    name = factory.Faker("name")


class AddressFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Address

    advertiser = factory.SubFactory(AdvertiserFactory)
    street = factory.Faker("name")
    zip_code = factory.Faker("pyint")
    county = factory.Faker("name")
    city = factory.Faker("name")
    country = factory.Faker("name")


class BillingAddressFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.BillingAddress

    advertiser = factory.SubFactory(AdvertiserFactory)
    title = factory.Faker("pyint")
    street = factory.Faker("name")
    zip_code = factory.Faker("pyint")
    email = factory.Faker("email")
    tax_office = factory.Faker("name")
    tax_number = factory.Faker("name")
    county = factory.Faker("name")
    city = factory.Faker("name")
    country = factory.Faker("name")
