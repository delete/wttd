#coding: utf-8

from django.test import TestCase

from eventex.subscriptions.models import Subscription

class DatailTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(name='Fellipe Pinheiro', cpf='000000000012',
							 email='pinheiro.llip@gmail.com', phone='21-00000000')
		self.response = self.client.get('/inscricao/%d/' % s.pk)

	def test_get(self):
		'GET /inscricao/1/ should return status 200'
		self.assertEqual(200, self.response.status_code)

	def test_template(self):
		'Uses template'
		self.assertTemplateUsed(self.response, 'subscriptions/subscription_detail.html')

	def test_context(self):
		'Context must have a subscription instance'
		subscription =self.response.context['subscription']
		self.assertIsInstance(subscription, Subscription)

	def test_html(self):
		'Check is subscrition data was rendered'
		self.assertContains(self.response, 'Fellipe Pinheiro')


class DatilNotFoundTest(TestCase):
	def test_not_found(self):
		response = self.client.get('/inscricao/0/')
		self.assertEqual(404, response.status_code)