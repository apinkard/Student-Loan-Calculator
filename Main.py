from ClassLoan import Loan

user_amount = int(input("Loan amount at then end of your studies: "))
user_age = int(input("Desired years to pay off loan: "))
user_interest = float(input("Interest Amount: "))

user_loan = Loan(user_amount, user_interest, user_age)
user_monthly_payment = user_loan.loan_calculation()

print(user_monthly_payment)