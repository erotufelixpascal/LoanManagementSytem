from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoanRequestForm, LoanTransactionForm
from .models import loanRequest, loanTransaction, CustomerLoan
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.db.models import Sum


# Create your views here.

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
 
    return render(request, 'LoanApp/loanrequest.html', )

@login_required(login_url='/account/login-customer')
def LoanPayment(request):
    form = LoanTransactionForm()
    if request.method == 'POST':
        form = LoanTransactionForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.customer = request.user.customer
            payment.save()
            # pay_save = loanTransaction()
            return redirect('/')

    return render(request, 'LoanApp/payment.html', context={'form': form})

@login_required(login_url='/account/login-customer')
def UserTransaction(requests):
    transactions = loanTransaction.objects.filter(customer=requests.user.customer)
    return render(requests, 'LoanApp/user_transaction.html', context={'transactions': transactions})

@login_required(login_url='/account/login-customer')
def UserLoanHistory(request):
    loans = loanRequest.objects.all().filter(customer=request.user.customer)
    return render(request, 'LoanApp/user_loan_history.html', context={'loans': loans})


@login_required(login_url='/account/login-customer')
def UserDashboard(request):

    requestLoan = loanRequest.objects.all().filter(customer=request.user.customer).count(),
    
    approved = loanRequest.objects.all().filter(customer=request.user.customer).filter(status='approved').count(),
    rejected = loanRequest.objects.all().filter(customer=request.user.customer).filter(status='rejected').count(),
    totalLoan = CustomerLoan.objects.filter(customer=request.user.customer).aggregate(Sum('total_loan'))['total_loan__sum'],
    totalPayable = CustomerLoan.objects.filter(customer=request.user.customer).aggregate(Sum('payable_loan'))['payable_loan__sum'],
    totalPaid = loanTransaction.objects.filter(customer=request.user.customer).aggregate(Sum('payment'))['payment__sum'],

    cdict = {
        'request': requestLoan[0],
        'approved': approved[0],
        'rejected': rejected[0],
        'totalLoan': totalLoan[0],
        'totalPayable': totalPayable[0],
        'totalPaid': totalPaid[0],


    }

    return render(request, 'LoanApp/user_dashboard.html', context=cdict)


def error_404_view(request, exception):
    print("not found")
    return render(request, 'notFound.html')




