from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import AdminLoginForm
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_reqiured
from django.contrib.auth.decorators import user_passes_test
from LoanApp.models import loanCategory, loanRequest, CustomerLoan, LoanTransaction
from .forms import LoanCategoryForm
from LoginApp.models import CustomerSignUp
from django.contrib.auth.models import User
from datetime import date 

from django.db.models import Sum
# Create your views here.

def super_login_view(request):
    form = AdminLoginForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method =='POST':
            form = AdminLoginForm(data = request.POST)
        
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(request, username= username, password =password)



