def main():
    print("This is a monthly payment load calculator")
    print("")

    pricipal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interest_rate = apr/1200
    amount_of_months = years * 12
    monthly_payment = pricipal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print("The monthly payment for this loan is: %.2f " % monthly_payment)


main()