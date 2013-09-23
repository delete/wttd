#coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscriptionsTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Fellipe Pinheiro',
			cpf='12345678901',
			email='pinheiro.llip@gmail.com',
			phone='21-00000000'
		)

	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.id)

	def test_has_created_at(self):
		'Subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		self.assertEqual(u'Fellipe Pinheiro', unicode(self.obj))

	def test_paid_default_value_is_False(self):
		'By default paid must be False'
		self.assertEqual(False, self.obj.paid)
		

class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		'Create a firt entry to force the colision'
		Subscription.objects.create(name='Fellipe Pinheiro', cpf='12345678901',
						 email='pinheiro.llip@gmail.com', phone='21-00000000')

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(name='Fellipe Pinheiro', cpf='12345678901',
						 email='outro@gmail.com', phone='21-00000000')
		self.assertRaises(IntegrityError, s.save)

	def test_email_can_repeat(self):
		'Email is not unique anymore'
		s = Subscription.objects.create(name='Fellipe Pinheiro', cpf='123456789012',
						 email='pinheiro.llip@gmail.com')
		self.assertEqual(2, s.pk)

	# def test_email_unique(self):
	# 	s = Subscription(name='Fellipe Pinheiro', cpf='00000000011',
	# 					 email='pinheiro.llip@gmail.com', phone='21-00000000')
	# 	self.assertRaises(IntegrityError, s.save)