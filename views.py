from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import StockTable, InvestorTable, BondTable

from .forms import BondEntry, StockForm

# Create your views here.
def index(request):
    investorObject = InvestorTable.objects.get(investor_id=1)
    stockObjects = StockTable.objects.all()
    bondObjects = BondTable.objects.all()
    context = {'stocks': stockObjects, 'investor': investorObject, 'bonds': bondObjects}
    return render(request, 'stocks_app/index.html', context)


def bond_form(request):
	"""Form to add new bonds"""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = BondEntry()
	else: 
		# POST data submitted; process data.
		form = BondEntry(data=request.POST)
		if form.is_valid():
			new_bond = BondTable.objects.all()
			form.save()
			return HttpResponseRedirect(reverse('stocks_app:index'))
	context = {'form': form}
	return render(request, 'stocks_app/bond_form.html', context)


def form(request):
	"""Form to add new stocks"""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = StockForm()
	else:
		form = StockForm(request.POST)
		if form.is_valid():
			input = form.save(commit=False)
			stock = Store.objects.get(stock='company_stock_symbol')
			input.stock = stock 
			input.save()
			'''
			stock_investor_id = form.cleaned_data['form']
			company_stock_symbol = form.cleaned_data['form']
			number_of_stocks_owned = form.cleaned_data['form']
			purchase_price = form.cleaned_data['form']
			current_price = form.cleaned_data['form']
			purchase_date = form.cleaned_data['form']
			'''

			return HttpResponseRedirect(reverse('stocks_app:index'))
			context = {'stock_investor_id': investor_id,
				'company_stock_symbol': stock_symbol,
				'number_of_stocks_owned': stock_number, 
				'purchase_price': purchase_price, 
				'current_price': current_price, 
				'purchase_date': purchase_date}
	context = {'form':form}		
	return render(request, 'stocks_app/form.html', context)



