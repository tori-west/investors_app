"""
Author: Tori West
Date: 3/12/2020
Description: After all the necessary imports, three functions are used to request 
	information. The first function pulls data from the database for display through
	the HTML file. The stock_form and bond_form functions are used to save data that
	has been inputted into each form. 
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Imported three classes from models.py
from .models import StockTable, InvestorTable, BondTable

# Imported two classes from forms.py
from .forms import BondEntry, StockEntry


# Create your views here.

def index(request):
	"""For Investor Tracking page to pull data from database tables"""
	investorObject = InvestorTable.objects.get(investor_id=1)
	stockObjects = StockTable.objects.all()
	bondObjects = BondTable.objects.all()
	context = {'stocks': stockObjects, 'investor': investorObject, 'bonds': bondObjects}
	return render(request, 'stocks_app/index.html', context)


def stock_form(request):
	"""Form to add new stocks"""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = StockEntry()
	else:
		# For submitted data
		form = StockEntry(request.POST)
		if form.is_valid():
			# Form data is cleaned
			investor_id = form.cleaned_data['stock_investor_id']
			symbol = form.cleaned_data['company_stock_symbol']
			stock_number = form.cleaned_data['number_of_stocks_owned']
			purchase_price = form.cleaned_data['purchase_price']
			current_price = form.cleaned_data['current_price']
			purchase_date = form.cleaned_data['purchase_date']
			# Data associated with model class
			stock = StockTable(stock_investor_id=investor_id,
				company_stock_symbol=symbol,
				number_of_stocks_owned=stock_number, 
				purchase_price=purchase_price, 
				current_price=current_price, 
				purchase_date=purchase_date)
			stock.save()
			# Returns user to the main page
			return HttpResponseRedirect(reverse('stocks_app:index'))
			# Identifying new variables
			context = {'stock_investor_id': investor_id,
				'company_stock_symbol': symbol,
				'number_of_stocks_owned': stock_number, 
				'purchase_price': purchase_price, 
				'current_price': current_price, 
				'purchase_date': purchase_date}
			
	context = {'form':form}		
	return render(request, 'stocks_app/stock_form.html', context)


def bond_form(request):
	"""Form to add new bonds"""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = BondEntry()
	else: 
		# POST data submitted; process data.
		form = BondEntry(request.POST)
		if form.is_valid():
			form.save()
			# Returns user to the main page
			return HttpResponseRedirect(reverse('stocks_app:index'))
	context = {'form': form}
	return render(request, 'stocks_app/bond_form.html', context)



