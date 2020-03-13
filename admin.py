from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from stocks_app.models import StockTable, InvestorTable, BondTable

# Class used to adjust input field size on forms
class StockAppAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'10'})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':10})},
    }

# Register your models here.
admin.site.register(StockTable, StockAppAdmin)
admin.site.register(InvestorTable)
admin.site.register(BondTable, StockAppAdmin)