from itertools import *
k = 0
for i in product('УКЫСМ', repeat = 5):
    k += 1
    s = ''.join(i)
    if (s.count('Ы') <= 1) and (s.count('У') == 2) and (s.count('С') == 0):
        print(k)