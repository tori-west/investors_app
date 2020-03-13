"""
Author: Tori West
Date: 3/12/2020
Description: Two classes are used to create forms. Each is linked to the models.py
	file by using ModelForm and a Meta class. CharFields are used to decrease the
	size of the input box. However, they are unneccesary and may be removed in the
	future. If they are removed, labels will need to be added to the Meta classes. 
"""

from django import forms

# Import two classes from models.py to link forms to model
from .models import StockTable, BondTable


# Creates form to input new stocks into the StockTable database 
class StockEntry(forms.ModelForm):
	# Added to control the input box size
	stock_investor_id = forms.CharField(label="Enter your Investor ID #", max_length=10)
	company_stock_symbol = forms.CharField(label="Stock Symbol", max_length=10)
	number_of_stocks_owned = forms.CharField(label="Number of Stocks Purchased", max_length=10)
	purchase_price = forms.CharField(label="Purchase Price", max_length=10)
	current_price = forms.CharField(label="Current Price", max_length=10)
	purchase_date = forms.CharField(label="Date you Purchased the Stock(s)", max_length=10)

	class Meta:
		# Set to model class that links to database
		model = StockTable
		fields = ['stock_investor_id', 
			'company_stock_symbol', 
			'number_of_stocks_owned', 
			'purchase_price', 
			'current_price', 
			'purchase_date',
			]


# Creates form to input new bonds into the BondTable database 
class BondEntry(forms.ModelForm):
	# CharField used to shrink input box size
	bond_investor_id = forms.CharField(label="Enter your Investor ID #", max_length=10)
	company_stock_symbol = forms.CharField(label="Bond Symbol", max_length=10)
	number_of_stocks_owned = forms.CharField(label="Number of Bonds Purchased", max_length=10)
	purchase_price = forms.CharField(label="Purchase Price", max_length=10)
	current_price = forms.CharField(label="Current Price", max_length=10)
	purchase_date = forms.CharField(label="Date you Purchased the Bond(s)", max_length=10)
	bond_coupon = forms.CharField(label="Bond Coupon", max_length=10)		
	bond_yield = forms.CharField(label="Bond Yield", max_length=10)

	class Meta:
		# Set to model class that links to database
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

