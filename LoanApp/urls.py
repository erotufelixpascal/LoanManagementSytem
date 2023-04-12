from django.urls import path
from LoanApp import views

app_name = 'LoanApp'

urlpatterns =[
    path('loan-request/', views.LoanRequest, name='loan_request'),
    path('loan-repayment/', views.LoanPayment, name='loan_payment'),
    path('user-transaction/', views.UserTransaction, name= 'user_transaction'),
    path('user-loan-history/', views.UserLoanHistory, name='user_loan_history'),
    path('user-dashboard/',views.UserDashboard, name='user_dashboard'),
    

]