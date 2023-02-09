# This script calculates yearly compound interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# compound interest = p * (1 + r/100)^t


def compound_interest(a, b, c):
    return a * (pow((1 + c / 100), b))


if __name__ == "__main__":
    a = float(input("Enter the principal amount: "))
    b = float(input("Enter the time period: "))
    c = float(input("Enter the rate of interest: "))

    print("The compound interest is {:.2f}".format(compound_interest(a, b, c)))
