realPin = 1234
pin = int(input("Please enter your 4-digit PIN: ").strip()) 
balance = 5000
if pin == realPin:
    cust=input("would you like to withdraw or access your balance?  ").strip().lower()
    if cust== "access balance":
        print(f"Your current balance is: ${balance}")
    elif cust.lower() == "withdraw":
        withdrawal = float(input("Enter the amount you want to withdraw: ").strip())
        if withdrawal <= balance:
            balance -= withdrawal
            print(f"Withdrawal successful! Your new balance is: ${balance}")
        else:
            print("Insufficient funds. Please try again.")
else:
    print("Incorrect PIN. Please try again.")
