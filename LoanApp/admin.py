from django.contrib import admin
from .models import loanRequest, CustomerLoan, loanTransaction, loanCategory

# Register your models here.
admin.site.register(loanRequest)
admin.site.register(loanCategory)
admin.site.register(loanTransaction)
admin.site.register(CustomerLoan)
