import random
while True:
   print(" 1. roll the dice        2. exit the game  ")
   user = int(input("what is your choice from the above? enter number :   "))
   if user ==1:
      number = random.randomint(1,6)
      print(number)
      print("------------------------------------------")
   else:
      break