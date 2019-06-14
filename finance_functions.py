#!/usr/local/bin/python3

def monthly_payment(Principal, Rate, Periods):
    """
    Calculate the payment amount of an Nth term loan
    Formula: A = Principal*((rate(1 + rate)^60)/((1 + rate)^60-1)) 
    """
    top = Rate*((1 + Rate)**Periods)
    bottom = ((1 + Rate)**Periods-1)
    Pmt = Principal*(top/bottom)
    return round(Pmt, 2)

def amortize(principal, pmt):
    """
    Recursively amortize down to a zero balance
    """
    balSheet = []
    if principal <= 0:
        return balSheet
    else:
        balSheet.append(f"| Balnce: {round(principal, 2)} 	| Payment: {pmt}")
        return balSheet + amortize(principal - pmt, pmt)

# UAT
# rate = 3.9%
r = .039/12
n = 60 # 5 year loan
P = 24000

balance = amortize(P, monthly_payment(P, r, n))

for i in range(0,len(balance)):
    print(balance[i])
# print(monthly_payment(P, r, n))
