#Code to optimize the least amount of material (least amount of dollars/coins).
from decimal import Decimal
initial = Decimal(1237.59) #Input
text_cost = str(initial)
formatted_cost = ('{0:.2f}'.format(float(initial)))
cents = int(formatted_cost[-2:])/100
formatted_cents = (round(Decimal(cents), 2))
initial = (round(initial, 2))
dollars = initial - formatted_cents
print("Dollars:",dollars, "Cents:",formatted_cents)
ones = str(formatted_cents)[-1:]
tens = (int(cents*10)*10)
if int(ones) <= 9:
    if int(ones) < 5:
        print(ones, 'pennies.')
    elif int(ones) > 5:
        print((int(ones) - 5), 'pennies and one nickel.')
    else:
        print('One nickel.')
if tens%25 == 0:
    print(int(tens/25), 'quarters.')
elif tens%10 == 0:
    print(int(tens/10), 'dimes.')
elif tens%5 == 0:
    print(int(tens/5), 'nickels.')
else:
    ('Error (tens of cents).')
dollars_singles = round(dollars/10)*10
if dollars_singles > dollars:
    dollars_singles -= 10
    singles = dollars - dollars_singles
    print(singles, 'single dollar bill(s).')
else:
    singles = dollars - dollars_singles
    print(singles, 'single dollar bill(s).')
dollar_tens = dollars_singles
dollar_hundreds = 0
while dollar_tens > 100:
    dollar_hundreds += 1
    dollar_tens -= 100
print(dollar_hundreds, 'one-hundred dollar bill(s).')
if dollar_tens%100 == 0:
    print(dollar_tens/100, 'one-huunded dollar bill(s).')
elif dollar_tens%50 == 0:
    print(dollar_tens/50, 'fifty dollar bill(s).')
elif dollar_tens%20 == 0:
    print(dollar_tens/20, 'twenty dollar bill(s).')
elif dollar_tens%10 == 0:
    print(dollar_tens/10, 'ten dollar bill(s).')
elif dollar_tens%5 == 0:
    print(dollar_tens/5, 'five dollar bill(s).')
else:
    print(dollar_tens, 'single dollar bill(s).')



