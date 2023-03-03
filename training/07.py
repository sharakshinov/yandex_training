import math
from math import ceil

Ah, Am, As = map(int, input().split(':'))
Bh, Bm, Bs = map(int, input().split(':'))
Ch, Cm, Cs = map(int, input().split(':'))

ds1 = Ah * 3600 + Am * 60 + As
ds3 = Ch * 3600 + Cm * 60 + Cs

if ds3 > ds1:
    result = math.ceil((ds3 - ds1) / 2)
else:
    result = math.ceil((ds3 + 24 * 60 * 60 - ds1) / 2)

ds2 = Bh * 3600 + Bm * 60 + Bs

result = ds2 + result

rh = result // 3600
rm = (result - rh * 3600) // 60
rs = result - rh * 3600 - rm * 60

if rs > 60:
    rm += 1
    rs -= 60
if rm > 60:
    rh += 1
    rm -= 60

if rh >= 24:
    rh = rh % 24

if len(str(rh)) < 2:
    rh = '0' + str(rh)
if len(str(rm)) < 2:
    rm = '0' + str(rm)
if len(str(rs)) < 2:
    rs = '0' + str(rs)

print(f"{rh}:{rm}:{rs}")
