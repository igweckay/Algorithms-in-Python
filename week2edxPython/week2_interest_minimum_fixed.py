'''
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

equations:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#interest_include = balance * annualInterestRate
for i in range(0,12):
	minimum_payment = balance * monthlyPaymentRate
	unpaid_balance = balance - minimum_payment
	interest = annualInterestRate/12.0 * unpaid_balance
	balance = unpaid_balance + interest

balance = round(balance,2)

print ('Remaining balance: ' + str(balance))



