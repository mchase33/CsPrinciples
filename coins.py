def coins():
   cost = input("Enter cost here ")
   cost = int(cost) % 100
   change = 100 - int(cost)
   print(change)
  
coins()
