
for y in range (1,10):
    s = ''
    for x in range (1,y+1):
        s = s + f"{x}*{y}={x*y}\t"
    print (s)

for y in range (1,10):
    for x in range (1,y+1):
      print(f"{x}*{y}={x*y}",end='\t')
    print()
