import math

welcome_message = print ('''
Choose either 'investment' or 'bond' from the menu below to proceed: 

Investment - to calculate the amount of interest you will earn on your investment 
Bond - to calculate the amount you will have to pay on a home loan''')

# Asking user input or choice
user_choice = input("\nPlease select either you want to use 'investment' or 'bond': ").lower()

if user_choice == "investment": 
    investment_amount = float(input("\nHow much are you depositing? R: "))
    interest_rate = float(input("\nAt which interest rate percentile? " ))
    interest_rate = float(interest_rate / 100)
    period = float(input("\nHow many years are you planning to invest for? "))
    interest = str(input("\nChoose 'Simple' or 'Compound' interest. ")).lower()
    
    if interest.lower() == "simple":
            "simple" == interest
            sample_total = investment_amount * (1 + interest_rate * period)
            print (f"\nYour interest earned over {period} years will be R{sample_total:.2f}".format())
            
    elif interest.lower() == "compound":
            "compound" == interest
            compound_total = investment_amount * math.pow((1 + interest_rate), period)
            print (f"\nYour interest earned over {period} years will be R{compound_total:.2f}".format())

elif user_choice == "bond":
    bond_amount = float(input("\nWhat is the current value of the house? R: ")) 
    interest_rate = float(input("\nAt which interest rate percentile? " )) 
    interest_rate = float((interest_rate/100)/12)
    months = float(input("\nHow many months you plan to repay? ")) 
    monthly = float(math.floor((interest_rate * bond_amount)/(1 - (1 + interest_rate)**(-months))))
    print(f"\nYour monthly repayment will be {monthly:.2f}".format())

else:
    print("\nPlease enter a valid input. Try again.") 