from django.test import TestCase

class EntriesTest(TestCase):
	def setUp(self):
		self.response = self.client.get('/inscricao/inscritos/')

	def test_get(self):
		'Get /inscritos/ must return staus code 200'
		self.assertEqual(200, self.response.status_code)

	def test_template(self):
		'Response must be a renderes template'
		self.assertTemplateUsed(self.response, 'subscriptions/subscription_entries.html')