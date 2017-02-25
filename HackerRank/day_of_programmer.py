y = int(input().strip())

if y == 1918:
    """Exception for transition"""
    print('27.09.{}'.format(y))
elif y < 1918:
    """Julian Calendar"""
    if y % 4 == 0:
        print('12.09.{}'.format(y))
    else:
        print('13.09.{}'.format(y))
else:
    """Gregorian Calendar"""
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        print('12.09.{}'.format(y))
    else:
        print('13.09.{}'.format(y))
