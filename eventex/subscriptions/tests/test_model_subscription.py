from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Bruno Barbosa',
            cpf='12345678901',
            phone='61-8121-0000',
            email='bruno@email.com'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Bruno Barbosa', str(self.obj))

    def test_paid_default_to_false(self):
        """By default paid must be False"""
        self.assertEqual(False, self.obj.paid)