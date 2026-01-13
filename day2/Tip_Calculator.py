print("Welcome to the Tip Calculator!")

bill = int(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10,12,or 15? "))
peoples = int(input("How many people to split the bill? "))

percentage_tip = tip / 100 * bill
add =  percentage_tip + bill 
total =  add / peoples
print(f"Each persom should pay:${total}")


  