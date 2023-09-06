from django.contrib import admin
from .models import loanCategorys,loanRequests,loanTransactions,CustomerLoans

# Register your models here.
admin.site.register(loanRequests)
admin.site.register(loanCategorys)
admin.site.register(loanTransactions)
admin.site.register(CustomerLoans)


