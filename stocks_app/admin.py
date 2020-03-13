"""
Author: Tori West
Date: 3/12/2020
Description: Three new models are registered. 
"""

from django.contrib import admin
from django.db import models

from stocks_app.models import StockTable, InvestorTable, BondTable

# Register your models here.
admin.site.register(StockTable)
admin.site.register(InvestorTable)
admin.site.register(BondTable)