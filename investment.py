amount=int(input("Enter the initial investment amount: "))
annual_rate=float(input("Enter the annual interest rate (in %): "))
years=int(input("Enter the number of years for investment: "))
print("Year\tAmount")
for i in range(1, years + 1):
    amount=amount + (amount * (annual_rate / 100))
    print(f"{i}\t{amount:.2f}")