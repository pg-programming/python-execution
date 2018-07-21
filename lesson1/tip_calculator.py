#tip 20%
tip_percent = int(20)
#tax 6.5%
tax_percent = int(6.5)
#meal cost
meal_cost = float(30.0)
#server name
server = 'John'

tip = meal_cost * tip_percent / 100
tax = meal_cost * tax_percent / 100
total_bill = meal_cost + tip + tax

print("The tip amount is: $" + str(tip))
print("The total amount for my meal is: $" + str(total_bill))
print("Thanks for your service " + server)
