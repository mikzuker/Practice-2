from decimal import Decimal
def add_fractions(a, b, c, d):
    return Decimal((a*d + b*c)/(b*d)).as_integer_ratio()