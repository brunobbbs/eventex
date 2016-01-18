from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Bruno Barbosa', cpf='12345678901',
                    email='bsbruno1@gmail.com', phone='61-8121-0000')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'bsbruno1@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Bruno Barbosa',
            '12345678901',
            'bsbruno1@gmail.com',
            '61-8121-0000'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
