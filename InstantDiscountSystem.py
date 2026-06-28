print("hello customer!") 
amount = float(input("please enter the amount: "))
if amount <100:
    discount = 0
elif 100 <= amount < 500: 
    discount = amount * 0.1
else:
    discount = amount * 0.2
print(f"Your discount is: {discount}, and your total amount after discount is: {amount - discount}")
