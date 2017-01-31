'''
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

equations...
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
		
annualInterestRate = .2
balance = 0
monthly_payments = 10
monthly_interest_rate = annualInterestRate/12.0
new_balance = balance




while new_balance > 0:
		new_balance = balance
		for month in range(0,12):
			monthly_unpaid_balance = new_balance - monthly_payments
			new_balance = monthly_unpaid_balance + monthly_interest_rate*monthly_unpaid_balance
		monthly_payments += 10

if balance == 0:
	print ('Lowest Payment: 0')
elif annualInterestRate == 0:
	print ('Lowest Payment: ' + str(round(ba lance/12.0, 2)))
else:
	print ('Lowest Payment: ' + str(monthly_payments - 10))



