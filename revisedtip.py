# Take in a number
# split tip/calculate the tip per person
# has to be a large enough number
# code must work properly
# must ask whats the total of bill
# must ask how many people
# must return a tip per person

# num3 = num1/num2
# make this more precise500

# calculate tip percentage
# create new bill total 
# divide new bill total by number of people

bill_total = int(float(input(' what is the total of the bill: ')))
# This asks for user input on bill total
# print(bill_total)

total_amount_of_people = int(float(input(' how many people are in your party? ')))
# This asks users to input the number of people serviced

tip_total= float(input(' what is the tip percentage for the waiter? '))
# # This asks users what percentage tip they would like to leave for the service

tip_amount = float(tip_total/100) * 100
# this defines the tip amount

tip_per_person = tip_amount / total_amount_of_people
print(f"this is what what each person tips ${tip_per_person:.2f}.\n")
# this allows users to know the tip per person

tax = bill_total * 0.08
new_total = tax + bill_total + tip_amount
print(f'Your total included with tip and tax is ${new_total:.2f}.\n')
# this calculated the new total which included tax and tip

amount_per_person = new_total/total_amount_of_people
print(f"Each person will pay : ${amount_per_person:.2f}")
# This divided the total bill equally for each guest

print("Thank you for using my new tip calculator")






