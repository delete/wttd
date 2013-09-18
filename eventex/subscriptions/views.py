# coding: utf-8
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.shortcuts import get_object_or_404


def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def new(request):
	return render(request, 'subscriptions/subscription_form.html',
		{'form': SubscriptionForm()})


def create(request):
	form = SubscriptionForm(request.POST)
	if not form.is_valid():
		return render(request, 'subscriptions/subscription_form.html',
			{'form': form})
	obj = form.save()

	return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

def detail(request, pk):
	subscription = get_object_or_404(Subscription, pk=pk)
	return render(request, 'subscriptions/subscription_detail.html',
				  {'subscription': subscription})


import urllib2
import re
from bs4 import BeautifulSoup


def entries(request):
	#entries = Subscription.objects.all()
	req = urllib2.Request('http://websro.correios.com.br/sro_bin/txect01$.Inexistente?P_LINGUA=001&P_TIPO=002&P_COD_LIS=PG416270837BR')
	page = urllib2.urlopen(req)

	lista = []
	dicionario = {}
	item = []
	itens = []     
	linha = 0

	for line in page:
		if 'rowspan' in line:                
			lista.append(line)                                            

    #os.remove('/tmp/t.txt')
	for linha in lista:
		soup = BeautifulSoup(linha)
		tag = soup.tr
		data = tag.contents[0].contents[0]      
		local = tag.contents[1].contents[0]
		situacao = tag.contents[2].contents[0].contents[0]
		#Cria uma lista de dicionarios
		item = {'data': data, 'local': local, 'situacao': situacao}
		itens.append(item)

	dicionario = {'dados': itens}
	
	return render(request, 'subscriptions/subscription_entries.html',
				   {'entries': dicionario})