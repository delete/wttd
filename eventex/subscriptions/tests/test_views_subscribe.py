# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeTest(TestCase):
	def setUp(self):
		self.response = self.client.get('/inscricao/')

	def test_get(self):
		'GET /inscricao/ must return status code 200'
		self.assertEqual(200, self.response.status_code)

	def test_template(self):
		'Response must be a rendered template'
		self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

	def test_html(self):
		'Html must contain input controls'
		self.assertContains(self.response, '<form')
		self.assertContains(self.response, '<input', 6)
		self.assertContains(self.response, 'type="text"', 4)
		self.assertContains(self.response, 'type="submit"')

	def test_csrf(self):
		'Html must contain csrf token'
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_has_form(self):
		'Context must have the subscription form'
		form = self.response.context['form']
		self.assertIsInstance(form, SubscriptionForm)


class SubscribePostTest(TestCase):
	def setUp(self):
		data = dict(name='Fellipe Pinheiro', cpf='12345678901',
						 email='pinheiro.llip@gmail.com', phone='21-00000000')
		self.response = self.client.post('/inscricao/', data)

	def test_post(self):
		'Valid POST should redirect to /inscricao/1/'
		self.assertEqual(302, self.response.status_code)

	def test_save(self):
		'Valid POST must be saved'
		self.assertTrue(Subscription.objects.exists())

class SubscriveInvalidPostTest(TestCase):
	def setUp(self):
		data = dict(name='Fellipe Pinheiro', cpf='000000000012',
							 email='pinheiro.llip@gmail.com', phone='21-00000000')
		self.response = self.client.post('/inscricao/', data)		

	def test_post(self):
		'Invalid POST should not redirect'
		self.assertEqual(200, self.response.status_code)

	def test_form_errors(self):
		'Form must contain errors'
		self.assertTrue(self.response.context['form'].errors)

	def test_dont_save(self):
		'Do not save data'
		self.assertFalse(Subscription.objects.exists())