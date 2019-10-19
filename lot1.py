import random

dice=['○', '×', '×', '×', '×']

while True:
    s=input("Enterを押して(qで終了)")
    if s=='q':
        break
    else:
        a=random.randint(0, 4)
        print("{} ".format(dice[a]))
