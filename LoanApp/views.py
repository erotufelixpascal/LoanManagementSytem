from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoanRequestForm, LoanTransactionForm
from .models import loanRequest, loanTransaction, CustomerLoan
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.http import Sum


# Create your views here.

#@login_required(login_url='/account/login_customer')

def home(request):
    return render (request, 'home.html', context={})

@login_required(login_url='/account/login-customer')

def LoanRequest(request):
    form = LoanRequestForm()

    if request.method =='POST':
        form= LoanRequestForm(request.POST)

        if form.is_valid():
            loan_obj = form.save(commit=False)
            loan_obj.customer = request.user.customer
            loan_obj.save()
            return redirect('/')
    return render(request, 'LoanApp/loanrequest.html', context={'form':form})