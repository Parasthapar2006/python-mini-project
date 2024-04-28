party1= input("enter 1st party name:")
party2 = input("enter 2nd party name:")
party3 = input("enter 3rd party name:")
party4 = input("enter 4th party name:")

p1_votes = 0
p2_votes = 0
p3_votes = 0
p4_votes = 0

voters_id = [1,2,3,4,5,6,7,8,9]
no_of_votes = len(voters_id)

while True:
   voters = int(input("enetr your voter id:"))
   if voters in voters_id:
      print("you are eligible voter:")
      voters_id.remove(voters)
   else:
      print("sorry, you are not eligible to vote")
      break

   print(f"to vote {party1},press key 1...")
   print(f"to vote {party2},press key 2...")
   print(f"to vote {party3},press key 3...")
   print(f"to vote {party4},press key 4...")
   vote = int(input("enter your valuable vote:"))
   if vote == 1:
      p1_votes +=1
      print(f"{party1},thank you for giving your important vote")
      print("--------------------------------------------------")
   elif vote == 2:
      p1_votes +=1
      print(f"{party2},thank you for giving you important vote")
      print("-------------------------------------------------")
   if vote == 3:
      p1_votes +=1
      print(f"{party3},thank you for giving your important vote")
      print("--------------------------------------------------")
   elif vote == 4:
      p1_votes +=1
      print(f"{party4},thank you for giving you important vote")
      print("-------------------------------------------------")
   elif vote > 4:
      print("you are pressing wrong key")
   else:
      print("sorry you are not eligible to vote")
      
   if voters_id ==[]:
      print("voting session is over")
      break