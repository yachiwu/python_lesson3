import decimal
print(decimal.Decimal('8.333333').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN))
# Decimal('8.33')