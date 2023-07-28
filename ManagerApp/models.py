from django.db import models
import uuid
from LoginApp.models import CustomerSignUp

# Create your models here.

class loanCategorys(models.Model):
    loan_names = models.CharField(max_length=250)
    creation_dates = models.DateField(auto_now_add=True)
    update_dates = models.DateField(auto_now=True)

    def __str__(self):
        return self.loan_names

class loanRequests(models.Model):
    customers = models.ForeignKey(CustomerSignUp, on_delete=models.CASCADE, related_name='loan_customers')
    categorys = models.ForeignKey(loanCategorys, on_delete= models.CASCADE, null=True)
    request_dates = models.DateField(auto_now=True)
    status_dates = models.DateField(max_length=150, null= True, blank = True, default=None)
    status = models.CharField(max_length=100, default='Pending')
    reason_for_rejection_approval = models.TextField()
    amounts = models.PositiveIntegerField(default=0)
    amount_approved= models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.customers.user
    
class loanTransactions(models.Model):
    customers = models.ForeignKey(CustomerSignUp,on_delete= models.CASCADE, related_name='transaction_customers')
    transactions = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    payments = models.PositiveIntegerField(default=0)
    payment_dates = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customers.user
    
class CustomerLoans(models.Model):
    customers = models.ForeignKey(CustomerSignUp,on_delete= models.CASCADE, related_name='loan_users')
    total_loans = models.PositiveIntegerField(default=0)
    payable_loans = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.customers.user
    

    

