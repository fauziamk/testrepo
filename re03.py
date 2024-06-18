import re
hand = open('regex_sum_42.txt')
for s in hand:
    s = s.rstrip()
    x= re.findall('([0-9]+)', s)
    if len(x) > 0:
        print(x)