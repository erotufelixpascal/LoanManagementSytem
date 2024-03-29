from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import AdminLoginForm
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from LoanApp.models import loanCategory, loanRequest, CustomerLoan, loanTransaction
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

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('ManagerApp:dashboard'))
                else :
                    return render(request, 'ManagerApp/templates/ManagerApp/adminLogin.html',context={'form' :form, 'error':"You are not Super user"})
            
            else:
                return render(request, 'ManagerApp/adminLogin.html', context={'form':form,'error':"Invalid username or password"})
    return render (request, 'ManagerApp/adminLogin.html', context={'form':form, 'user': "Admin Login"})

# @user_passes_test(lambda u: u.is_superuser)
@staff_member_required(login_url='/manager/admin-login')

def dashboard(request):

    totalCustomer = CustomerSignUp.objects.all().count(),
    requestloan  = loanRequest.objects.all().filter(status='pending').count(),
    approved = loanRequest.objects.all().filter(status='approved').count(),
    rejected = loanRequest.objects.all().filter(status='rejected').count(),
    totalLoan = CustomerLoan.objects.aggregate(Sum('total_loan'))['total_loan__sum'],
    totalPayable = CustomerLoan.objects.aggregate(Sum('payable_loan'))['payable_loan__sum'],
    totalPaid = loanTransaction.objects.aggregate(Sum('payment'))['payment__sum'],

    dict ={
        'totalCustomer': totalCustomer[0],
        'request' : requestloan[0],
        'approved' : approved[0],
        'rejected' : rejected[0],
        'totalLoan' : totalLoan[0],
        'totalPayable' : totalPayable[0],
        'totalPaid' : totalPaid[0],
    }

    print(dict)

    return render(request, 'ManagerApp/dashboard.html', context= dict)

@staff_member_required(login_url='/manager/admin-login')
def add_category(request):
    form = LoanCategoryForm()
    if request.method =='POST':
        form = LoanCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ManagerApp:dashboard')
    return render(request, 'ManagerApp/admin_add_category.html', {'form': form})

@staff_member_required(login_url='/manager/admin-login')
def total_users(request):
    users = CustomerSignUp.objects.all()

    return render(request, 'ManagerApp/customer.html', context={'user':users})

@staff_member_required(login_url='/manager/admin-login')
def user_remove(request,pk):
    CustomerSignUp.objects.get(id=pk).delete()
    user = User.objects.get(id=pk)
    user.delete()
    return HttpResponseRedirect('/manager/users')

@staff_member_required(login_url='/manager/admin-login')
def loan_request(request):
    loanrequest = loanRequest.objects.filter(status='pending')
    return render(request, 'ManagerApp/request_user.html', context={'loanrequest': loanrequest})

@staff_member_required(login_url='/manager/admin-login')
def approved_request(request,id):
    today= date.today()
    status_date = today.strftime("%B %d, %Y")
    loan_obj = loanRequest.objects.get(id=id)
    loan_obj.status_date = status_date
    loan_obj.save()
    year = loan_obj.year

    approved_customer = loanRequest.objects.get(id=id).customer
    if CustomerLoan.objects.filter(customer =approved_customer).exists():

        #find prevoius amount of customer
        PreviousAmount= CustomerLoan.onjects.get(customer= approved_customer).total_loan
        PreviousPayable = CustomerLoan.objects.get(customer= approved_customer).payable_loan

        #update balance
        CustomerLoan.objects.filter(customer =approved_customer).update(total_loan = int(PreviousAmount)+ int(loan_obj.amount))
        CustomerLoan.objects.filter(customer = approved_customer).update(payable_loan= int(PreviousPayable)+ int(loan_obj.amount)+ int(loan_obj.amount)*0.12 * int(year))
    
    else:
        #request customer

        #customerloan object creation

        save_loan = CustomerLoan()

        save_loan.customer = approved_customer
        save_loan.total_loan =int(loan_obj.amount)
        save_loan.payable_loan = int(loan_obj.amount)+int(loan_obj.amount)*0.12* int(year)
        save_loan.save()

    loanRequest.objects.filter(id=id).update(status= 'approved')
    loanrequest = loanRequest.objects.filter(status='pending')
    return render(request, 'ManagerApp/request_user.html', context={'loanrequest':loanrequest})


@staff_member_required(login_url='/manager/admin-login')
def rejected_request(request, id):

    today= date.today()
    status_date= today.strftime("%B %d, %Y")
    loan_obj = loanRequest.objects.get(id=id)
    loan_obj.status_date = status_date
    loan_obj.save()
    # rejected_customer = loanRequest.objects.get(id=id).customer
    # print(rejected_customer)
    loanRequest.objects.filter(id=id).update(status='rejected')
    loanrequest = loanRequest.objects.filter(status='pending')
    return render(request, 'ManagerApp/request_user.html', context={'loanrequest': loanrequest})

@staff_member_required(login_url='/manager/admin-login')
def approved_loan(request):
    # print(datetime.now())
    approvedLoan = loanRequest.objects.filter(status='approved')
    return render(request, 'ManagerApp/approved_loan.html', context={'approvedLoan': approvedLoan})


@staff_member_required(login_url='/manager/admin-login')
def rejected_loan(request):
    rejectedLoan = loanRequest.objects.filter(status='rejected')
    return render(request, 'ManagerApp/rejected_loan.html', context={'rejectedLoan': rejectedLoan})


@staff_member_required(login_url='/manager/admin-login')
def transaction_loan(request):
    transactions = loanTransaction.objects.all()
    return render(request, 'ManagerApp/transaction.html', context={'transactions': transactions})








