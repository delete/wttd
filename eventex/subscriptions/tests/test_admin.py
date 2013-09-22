from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin

class MarxAsPaidTest(TestCase):
	def setuUp(self):
		#Instancia o Model Admin
		self.model_admin = SubscriptionAdmin(Subscription, admin.site)

	def test_has_action(self):
		'Action is installed'
		self.assertIn('mark_as_paid', self.model_admin.actions)
