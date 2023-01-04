print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
person = int(input("How many people to split the bill?"))

total = "{:.2f}".format(round((bill/person) * ((tip+100)/100),2))

print(f"Each person should pay: ${total}")