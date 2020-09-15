'''
Design a cash register. Given the purchase price of the item and the cash provided 
by the customer, calculate the change that has to be returned to the customer. Your
register currently has the following bills/coins with it:
'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00
'''

class CashRegister:
    def __init__(self):
        self.register = {
            ".01": "PENNY",
            ".05": "NICKEL",
            ".10": "DIME",
            ".25": "QUARTER",
            ".50": "HALF DOLLAR",
            "1.00": "ONE",
            "2.00": "TWO",
            "5.00": "FIVE",
            "10.00": "TEN",
            "20.00": "TWENTY",
            "50.00": "FIFTY",
            "100.00": "ONE HUNDRED"
        }

    '''
    In floating point arithmetics, numbers like  0.1 + 0.2 don't add up to a round 0.3, 
    instead the result is 0.30000000000000004
    This is because Floating-point numbers are represented in computer hardware as 
    base 2 (binary) fractions. 
    More on this: https://docs.python.org/3/tutorial/floatingpoint.html
    '''
    def format_float(self, num):
        return float("{:.2f}".format(num))

    def calculate_change(self, price, cash):
        pp = float(price)
        ch = float(cash)
        res = []

        if ch < pp:
            return("ERROR")
        elif ch == pp:
            return("ZERO")
        change = ch - pp
        change = self.format_float(change)

        for coin in reversed(self.register.keys()):
            #print(res)
            if change <= 0.0:
                break
            if change >= float(coin):
                #print(change)
                ret = change // float(coin)
                change -= ret * float(coin)
                change = self.format_float(change)
                for _ in range(int(ret)):
                    res.append(self.register[coin])

        return ",".join(sorted(res))

obj = CashRegister()
print(obj.calculate_change(14.33, 16.00))