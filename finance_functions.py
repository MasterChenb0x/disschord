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

def amortize(principal, pmt, rate):
    """
    Recursively amortize down to a zero balance
    """
    balSheet = []
    if principal <= 0:
        return balSheet
    else:
        balSheet.append(f"| {round(principal, 2)}\t | {pmt}\t | {round(principal*rate, 2)}\t | {round(pmt - (principal*rate), 2)}\t")
        return balSheet + amortize(principal - pmt, pmt, rate)


