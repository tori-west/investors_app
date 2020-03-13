from django import forms


from .models import StockTable, BondTable

'''
class FormEntry(forms.Form):
	stock_investor_id = forms.CharField(label="Investor ID #", max_length=10)
	company_stock_symbol = forms.CharField(label="Stock Symbol", max_length=10)
	number_of_stocks_owned = forms.CharField(label="Number of Stocks", max_length=10)
	purchase_price = forms.CharField(label="Purchase Price", max_length=10)
	current_price = forms.CharField(label="Current Price", max_length=10)
	purchase_date = forms.CharField(label="Purchase Date", max_length=10)
'''
class BondEntry(forms.ModelForm):
	class Meta:
		model = BondTable
		fields = ['bond_investor_id', 
			'company_stock_symbol', 
			'number_of_stocks_owned', 
			'purchase_price', 
			'current_price', 
			'purchase_date',
			'bond_coupon',
			'bond_yield',
			]
		labels = {'bond_investor_id': 'Enter your Investor ID #',
			'company_stock_symbol': 'Bond Symbol',
			'number_of_stocks_owned': 'Number of Bonds Purchased', 
			'purchase_price': 'Purchase Price', 
			'current_price': 'Current Price', 
			'purchase_date': 'Date you Purchased the Bond(s)',
			'bond_coupon': 'Bond Coupon',
			'bond_yield': 'Bond Yield',
			}	

class StockForm(forms.ModelForm):

	class Meta:
		model = StockTable
		fields = ['stock_investor_id', 
			'company_stock_symbol', 
			'number_of_stocks_owned', 
			'purchase_price', 
			'current_price', 
			'purchase_date',
			]
		labels = {'stock_investor_id': 'Enter your Investor ID #',
			'company_stock_symbol': 'Stock Symbol',
			'number_of_stocks_owned': 'Number of Stocks Purchased', 
			'purchase_price': 'Purchase Price', 
			'current_price': 'Current Price', 
			'purchase_date': 'Date you Purchased the Stock(s)',
			}

