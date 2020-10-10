import math
import sys
#The sys.exit function was used here in order to prevent the program
#from running when the BOND calculation was complete. Without, it would
#give an error message with regards to the INVESTMENT option.

#This is a welcome message

print('''Welcome to Second Investment Bank.
We are an investment bank established to cater to your investment desires.''')

#The boolean variable was created to verify valid input from the user.

valid_input = True


inv_option = str(input('''We can assist you in calculating the following:
- Investment: The amount of interest earned on your investment
- Bond: The amount you would need to pay on a home loan
Which of the aforementioned calculators would you like to access?:'''))

#The characrer count helps in determining an invalid input by the user.
#The following section will aid in validating the input of the user.
#The numbers 4 & 10 correspond to the number of characters in bond &
#investment respectively. The logical statement was added to further
#validate the users input.

num_of_char = len(inv_option)

if (num_of_char > 4 <= 10 and inv_option == "investment"):
    valid_input = True

if (num_of_char > 4 <= 10 and inv_option != "investment"):
    valid_input = False
    print('''An error has occured in trying to identify your
selection. Please select one of the aforementioned calculators.''')


if (num_of_char < 4):
    valid_input = False
    print('''An error has occured in trying to identify your
selection. Please select one of the aforementioned calculators.''')

    
       
#This section will cover the investment & bond calculator

if (valid_input == True and inv_option == "investment"):
    P = float(input("How much are you willing to deposit?:"))
    r = float(input("What is your desired interest rate?:"))
    t = float(input("How many years are you willing to invest?:"))
    interest = str(input('''Are you willing to invest on simple interest or
compound interest?:'''))
    
elif (valid_input == True and inv_option == "bond"):
    P = float(input("What is the present value of your home?:"))
    i = float(input("What is your annual interest rate?:"))
    n = float(input("How many months are you paying towards your bond:"))
    bond_pay = round(((((i/100)/12))*P)/(1-(1+((i/100)/12))**(-n)), 0)
    print(f"Your month payment towards your bond is R{bond_pay}.")
    sys.exit()
#See the comment above with regards to the sys.exit() function


#This is dependent on the selection of the user, whether they choose
#simple or compound interest.
    
simple = round(float(P*(1+(r/100)*t)), 0)
compound = round(float(P*math.pow((1+(r/100)),t)), 0)

if (interest == "simple"):
    print(f"Return on investment with simple interest {simple}.")
elif(interest == "compound"):
    print(f'''Your retrun on investment with compound interest
is {compound}.''')



    



    
    



    
    


    
   



                       




