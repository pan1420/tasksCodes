pyMaster= input("are you good at Python? (yes/no): ").strip().lower()
experience = int(input("How many years of experience do you have in Python? ").strip())
certified = input("do you have a computer science degree or a bootcamp certificate? (yes/no): ").strip().lower()
if pyMaster == "yes" and (experience >= 2 or certified == "yes"):
    print("Congratulations! You are eligible for the next stage of the application process.")
else:
    print("Sorry, you do not meet the eligibility criteria for the next stage of the application process.")
