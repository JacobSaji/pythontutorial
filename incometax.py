def calculate_tax(income):
    tax = 0

    if income <= 400000:
        tax = 0
    else:
        if income > 2400000:
            tax += (income - 2400000) * 0.30
            income = 2400000

        if income > 2000000:
            tax += (income - 2000000) * 0.25
            income = 2000000

        if income > 1600000:
            tax += (income - 1600000) * 0.20
            income = 1600000

        if income > 1200000:
            tax += (income - 1200000) * 0.15
            income = 1200000

        if income > 800000:
            tax += (income - 800000) * 0.10
            income = 800000

        if income > 400000:
            tax += (income - 400000) * 0.05

    cess = tax * 0.04
    total_tax = tax + cess

    return total_tax


income = float(input("Enter your annual income: "))
tax_payable = calculate_tax(income)
print(f"Total Income Tax Payable: {tax_payable:.2f}")
