from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from ManagerApp import AdminLoginForm
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


