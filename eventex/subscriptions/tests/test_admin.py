from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def test_has_action(self):
        """Action mark as paid should be installed"""
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.assertIn('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid"""
        Subscription.objects.create(
            name='Bruno Barbosa',
            cpf='12345678901',
            phone='61-8121-0000',
            email='bruno@email.com'
        )
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)

        queryset = Subscription.objects.all()
        model_admin.mark_as_paid(None, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())