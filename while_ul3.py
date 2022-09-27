x = 0
p = 0
while x != "koniec":
   x = input("zadaj meno: ")
   if x != "koniec":
       p = len(x)
       print(x, ",počet písmen:",p)