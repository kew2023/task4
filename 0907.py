file = open('0907.txt')
allpas = file.readlines()
count = 0
for pas in allpas:
    k = 0
    temp = int(pas[:2]) + int(pas[3])/10
    items = pas[4:]
    if temp < 37:
        if 'KNIFE' in items or 'BOMB' in items or 'WEAPON' in items:
            continue
        else:
            if len(items) <= 1024:
                k += 1
            if items.count('PASSPORT') == 1:
                items = items.replace('PASSPORT', '',1)
                k += 1
            if 'MEDICALMASK' in items:
                items = items.replace('MEDICALMASK', '',1)
                k += 1
            if 'TICKET' in items:
                items = items.replace('TICKET', '',1)
                k += 1
    if k == 4:
        count += 1
print(count)
