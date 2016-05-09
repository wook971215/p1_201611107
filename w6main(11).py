"""
@author John
@since 160406
"""

print "Calculator Leap Year"

def CalculatorLeapYear():
    year=raw_input("Input year:")

    year=int(year)

    if year%4==0 and year%100==0 or year%400==0:
        print "Yes leap year"
    else:
        print "No leap year"

CalculatorLeapYear()

raw_input()

def main():
    CalculatorLeapYear()


if __name__=="__main__":
    main()