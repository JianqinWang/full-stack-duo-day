#!/usr/bin/python3
from decimal import Decimal, getcontext

def pi_to_n(term):
    if type(term) is not int or term <= 0:
        print("PROF G, YOU CANT DO THAT!")
        return
    getcontext().prec=term
    print(sum(1/Decimal(16)**k *
              (Decimal(4)/(8*k+1) -
               Decimal(2)/(8*k+4) -
               Decimal(1)/(8*k+5) -
               Decimal(1)/(8*k+6)) for k in range(term)))

pi_to_n(100)
pi_to_n(50)
pi_to_n("a")
pi_to_n(True)
pi_to_n(-1)
pi_to_n(0)
