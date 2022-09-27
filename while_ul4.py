x = int(input("zadaj cislo: "))
p = 0
s = x
while x != 0:
  x = int(input("zadaj cislo: "))
  p +=1
  s += x
print("Súčet čísel je:",s,", čísel je:",p,",aritmeticky priemer je:",s/p)
