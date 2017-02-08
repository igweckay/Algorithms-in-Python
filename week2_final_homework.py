annualInterestRate = .2
balance = 999999

new_balance = balance

monthly_interest_rate = annualInterestRate/12.0
monthly_payments_lower = balance/12.0
monthly_payments_upper = (balance * (1 + monthly_interest_rate ** 12.0))/12.0

while new_balance > 0:
		monthly_payments = (monthly_payments_lower + monthly_payments_upper)/2
        trail_amount = (monthly_payments * 12) - balance
        if (trail_amount == 0):
            new_balance = 0
        elif (trail_amount < 0):
            monthly_payments_lower = monthly_payments
        else:
            monthly_payments_upper = monthly_payments

if balance == 0:
	print ('Lowest Payment: 0')
else:
	print ('Lowest Payment: ' + str(monthly_payments))
