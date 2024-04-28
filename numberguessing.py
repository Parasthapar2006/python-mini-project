import random
mynum = random.randint(0,9)

print(" i have a number in my mind!, can you guess it ?")

while True:
   usernum = int(input("enter the number you guessed :"))
   
   if(mynum == usernum):
      print("yes you are right")
      break
   elif (mynum > usernum ):
      print(" my number is greater than the number you gussed . try again" ,end="\n\n")
   else:
      print(" my number is smaller than the number you gussed. try again" ,end="\n\n")