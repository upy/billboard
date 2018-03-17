from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from profiles import factories as profile_factories
from . import factories, models


class AdvertiserCreateViewTestCase(TestCase):
    def setUp(self):
        self.profile = profile_factories.RepresentativeFactory.create()
        self.profile.user_ptr.user_permissions.add(
            Permission.objects.get(codename='add_advertiser'))
        self.advertiser = factories.AdvertiserFactory.build()
        self.address = factories.AddressFactory.build()
        self.billing_address = factories.BillingAddressFactory.build()

    def test_create_form_page(self):
        self.client.force_login(self.profile.user_ptr)
        response = self.client.get(reverse('advertiser-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'advertisers/advertiser_create_form.html')

    def test_form_valid(self):
        self.client.force_login(self.profile.user_ptr)
        data = {
            'name': self.advertiser.name,
            'email': self.advertiser.email,
            'post-TOTAL_FORMS': 1,
            'post-INITIAL_FORMS': 0,
            'post-MIN_NUM_FORMS': 0,
            'post-MAX_NUM_FORMS': 1,
            'post-0-id': '',
            'post-0-advertiser': '',
            'post-0-street': self.address.street,
            'post-0-zip_code': self.address.zip_code,
            'post-0-county': self.address.county,
            'post-0-city': self.address.city,
            'post-0-country': self.address.country,
            'billing-0-id': '',
            'billing-0-advertiser': '',
            'billing-TOTAL_FORMS': 1,
            'billing-INITIAL_FORMS': 0,
            'billing-MIN_NUM_FORMS': 0,
            'billing-MAX_NUM_FORMS': 1,
            'billing-0-title': self.billing_address.title,
            'billing-0-street': self.billing_address.street,
            'billing-0-zip_code': self.billing_address.zip_code,
            'billing-0-email': self.billing_address.email,
            'billing-0-tax_office': self.billing_address.tax_office,
            'billing-0-tax_number': self.billing_address.tax_number,
            'billing-0-county': self.billing_address.county,
            'billing-0-city': self.billing_address.city,
            'billing-0-country': self.billing_address.country,
        }
        response = self.client.post(reverse('advertiser-add'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Advertiser.objects.last().name, data['name'])

    def test_form_invalid(self):
        self.client.force_login(self.profile.user_ptr)
        data = {
            'name': '',
            'email': self.advertiser.email,
            'post-TOTAL_FORMS': 1,
            'post-INITIAL_FORMS': 0,
            'post-MIN_NUM_FORMS': 0,
            'post-MAX_NUM_FORMS': 1,
            'post-0-id': '',
            'post-0-advertiser': '',
            'post-0-street': self.address.street,
            'post-0-zip_code': self.address.zip_code,
            'post-0-county': self.address.county,
            'post-0-city': self.address.city,
            'post-0-country': self.address.country,
            'billing-0-id': '',
            'billing-0-advertiser': '',
            'billing-TOTAL_FORMS': 1,
            'billing-INITIAL_FORMS': 0,
            'billing-MIN_NUM_FORMS': 0,
            'billing-MAX_NUM_FORMS': 1,
            'billing-0-title': self.billing_address.title,
            'billing-0-street': self.billing_address.street,
            'billing-0-zip_code': self.billing_address.zip_code,
            'billing-0-email': self.billing_address.email,
            'billing-0-tax_office': self.billing_address.tax_office,
            'billing-0-tax_number': self.billing_address.tax_number,
            'billing-0-county': self.billing_address.county,
            'billing-0-city': self.billing_address.city,
            'billing-0-country': self.billing_address.country,
        }
        response = self.client.post(reverse('advertiser-add'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'advertisers/advertiser_create_form.html')
        errors = list()
        errors.extend(response.context['form'].errors)
        errors.extend(response.context['address_form_set'].errors)
        errors.extend(response.context['billing_address_form_set'].errors)
        self.assertGreater(len(errors), 0)
        self.assertEqual(models.Advertiser.objects.count(), 0)
