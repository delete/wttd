# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
	# name = forms.CharField(label=_('Nome'))
	# cpf = forms.CharField(label=_('CPF'), max_length=11)
	# email = forms.EmailField(label=_('Email'))
	# phone = forms.CharField(label=_('Telefone'))
	class Meta:
		model = Subscription
		exclude= ('paid',)