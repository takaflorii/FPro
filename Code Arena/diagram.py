l = int(input())
s = int(input())
r = l

if r < s:
    l = r
    r = s
    s = l

while True:
    if s <= r:       
        r = r - s
        if r == 0:
            break
    if r != 0:
        l = r
        r = s
        s = l

print(s)