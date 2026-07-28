# 1. This function calculates the finances.

def calculate_finances(monthly_income: float,
                       tax_rate_in_percent: float,
                       currency_code: str,
                       expenses: dict[str, float] | None = None) -> None:

    """
    This function intends to calculate finance variables such as:

    1-Monthly Net Income
    2-Yearly Net Income
    3-Yearly Gross Income
    
    It takes variables as follows:
    
    monthly_income: float,
    tax_rate_in_percent: float,
    currency_code: str,
    expenses: dict[str, float] | None = None
    
    It also offers to calculate the users savings based on the provided expenses.
    
    """

    # 2. Calculating the required variables.

    monthly_tax_amount = monthly_income * (tax_rate_in_percent / 100)
    monthly_net_income = monthly_income - monthly_tax_amount
    yearly_income = monthly_income * 12
    yearly_tax_amount = monthly_tax_amount * 12
    yearly_net_income = yearly_income - yearly_tax_amount

    # 3. Displaying the calculated variables.

    print(f"{'-'*5} Finance Calculator {'-'*5}")
    print(f"Your Monthly Salary -> {currency_code} {monthly_income:.2f}")
    print(f"Tax Rate Applicable (%) -> {tax_rate_in_percent:.0f}%")
    print(f"Currency -> {currency_code}")
    print(f"{'-'*30}")

    labels = [
        "Monthly Net Salary",
        "Monthly Tax Amount",
        "Annual Salary",
        "Annual Tax Amount",
        "Annual Net Salary"
    ]
    values = [
        monthly_net_income,
        monthly_tax_amount,
        yearly_income,
        yearly_tax_amount,
        yearly_net_income
    ]

    for i, (label, value) in enumerate(zip(labels, values), start=1):
        print(f"{i} {label} {currency_code} {value:,.2f}")

    # 4. If user wants to calculate savings, i.e savings is set to True (Default=None)

    if expenses:
        total_expenses = sum(expenses.values())
        monthly_savings = monthly_net_income - total_expenses

        print(f"{'-'*30}")
        print("Expenses:")
        for name, amount in expenses.items():
            print(f"- {name}: {currency_code} {amount:,.2f}")

        print(f"Total Expenses -> {currency_code} {total_expenses:,.2f}")
        print(f"Monthly Savings -> {currency_code} {monthly_savings:,.2f}")

        if monthly_savings < 0:
            print("Warning: your expenses are greater than your monthly net income.")
    print(f"{'-'*30}")

# 5.The main entry point of the script, which gathers the required info.
def main():
    while True:
        try:
            monthly_income = float(input("Please enter your monthly income -> "))
            tax_rate_in_percent = float(input("Please enter your tax rate applicable -> "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    currency_code = input("Please enter your currency code -> ").upper()

    expenses: dict[str, float] = {}
    add_expenses = input("Do you want to add expenses? (y/n) -> ").lower()

    if add_expenses == "y":
        while True:
            expense_name = input("Expense name (or press Enter to stop) -> ").strip()
            if not expense_name:
                break

            while True:
                try:
                    expense_amount = float(input("Expense amount -> "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")

            expenses[expense_name] = expense_amount

    calculate_finances(monthly_income, tax_rate_in_percent, currency_code, expenses)

# 6. Runs the script.
if __name__ == "__main__":
    main()