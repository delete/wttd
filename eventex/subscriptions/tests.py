# coding: utf-8

from django.test import TestCase

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
