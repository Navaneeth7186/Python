#identity operator 

a = None
print(a is None)
print(a is not None)

#bitwise operators
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)


#electric city bill calculator
units = int(input("Enter electricity units:2000"))  
rate = 6
bill = units * rate 

print("Electricity Bill: ",bill)


#travel expense calculator
Travel = float(input("Travel expense: "))
Food = float(input("Food expense: "))
hotel = float(input("Hotel expense: " ))

total = Travel + Food + hotel
print("Total Expense:", total)