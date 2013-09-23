# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SubscribeTest(TestCase):
	def setUp(self):
		self.response = self.client.get(r('subscriptions:subscribe'))

	def test_get(self):
		'GET /inscricao/ must return status code 200'
		self.assertEqual(200, self.response.status_code)

	def test_template(self):
		'Response must be a rendered template'
		self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

	def test_html(self):
		'Html must contain input controls'
		self.assertContains(self.response, '<form')
		self.assertContains(self.response, '<input', 7)
		self.assertContains(self.response, 'type="text"', 5)
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
		self.response = self.client.post(r('subscriptions:subscribe'), data)

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
		self.response = self.client.post(r('subscriptions:subscribe'), data)		

	def test_post(self):
		'Invalid POST should not redirect'
		self.assertEqual(200, self.response.status_code)

	def test_form_errors(self):
		'Form must contain errors'
		self.assertTrue(self.response.context['form'].errors)

	def test_dont_save(self):
		'Do not save data'
		self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
	def test_template_has_non_field_errors(self):
		'Check if non_field_errors are shown in template'
		invalid_data = dict(name='Fellipe Pinheiro', cpf='12345678901')
		response = self.client.post(r('subscriptions:subscribe'), invalid_data)

		self.assertContains(response, '<ul class="errorlist">')
