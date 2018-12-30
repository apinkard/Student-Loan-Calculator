import sys

# Main Loan
class Loan:

	# Initializer / Instance Attributes
	def __init__(self, amount, interest, age):
		self.amount = amount  # Total Loan Amount
		self.interest = interest / 100 
		self.age = age  # Age should be in years
		
	# Loan Calculation Method
	def loan_calculation(self):
		
		# Initial Variables for Loan Calculation
		months = self.age * 12
		principal_payment = self.amount / months
		monthly_interest = self.interest / 12
		
		# Set Up for Monthly Loan Calculation
		amount0 = self.amount
		months_array = range(months)  # Array from 1-120
		monthly_payments = [None] * months  # To be filled with required monthly payments
		
		# Monthly Loan Calculation
		for i in months_array:
			interest_payment = amount0 * monthly_interest
			required_monthly_payment = interest_payment + principal_payment
			monthly_payments[i] = required_monthly_payment
			amount0 = amount0 - principal_payment
			
		calculated_monthly_payment = sum(monthly_payments) / months
		result0 = "You must pay {} a month for {} years".format(calculated_monthly_payment, age)
		
		return result0
		
# Custom Loan
class Custom_Loan(Loan):
	def __init__(self, amount, interest, age, c_amount, c_years):
		Loan.__init__(self, amount, interest, age)
		self.c_amount = c_amount  # Custom Amount
		self.c_years = c_years  # Custom Years
		
		if self.c_years > age:
			print("Invalid amount of custom years")
			sys.exit()
		
	def custom_calculation(self):
		c_months = self.c_years * 12
		r_months = months - c_months
		
		c_months_array = range(c_months)
		r_months_array = range(r_months)
		c_monthly_payments = [None] * c_months
		
		amount1 = self.amount
		
		for i in c_months_array:
			c_interest_payment = amount1 * monthly_interest
			c_monthly_payment = c_interest_payment + self.c_amount
			c_monthly_payments[i] = c_monthly_payment
			amount1 = amount1 - self.c_amount
			if amount1 <= 0:
				completion = i + 1
				string1 = "You can pay off your loans in {} months".format(completion)
				result1 = print(string1)
				break
			
		c_principal_payment = amount1 / r_months
		r_monthly_payments = [None] * r_months
				
		for i in r_months_array:
			r_interest_payment = c_principal_payment * monthly_interest
			r_monthly_payment = r_interest_payment + c_principal_payment
			r_monthly_payments[i] = r_monthly_payment
			amount1 = amount1 - c_principal_payment
				
		new_monthly_payment = sum(r_monthly_payments) / r_months
				
		string2 = "If you pay {} for {} years, ".format(self.c_amount, self.c_years)
		string3 = "you must pay {} for {} years.".format(new_monthly_payment, r_months / 12)
		result1 = string2 + string3
		
		return result1
						
	