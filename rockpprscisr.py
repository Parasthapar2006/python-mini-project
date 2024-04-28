import random
choice = ["rock" , "paper" , "scissor"]
while True:
      print("rock paper scissor game :")
      youwin ,computerwin = 0,0
      for i in range(1,6):
            print("round",i, "start:")
            print("please select any one option:")
            print("1.rock" , "2.paper" , "3.scissor" , sep="\n")
            yourchoice = int(input())
            if yourchoice ==1:
                 print("you select rock")
                 yourchoice = "rock"
            elif yourchoice ==2:
                 print("you select paper")
                 yourchoice = "paper"
            elif yourchoice == 3:
                 print(" you select scissor")
                 yourchoice = " scissor"
            else:
                print("invalid choice")
                break
            computerchoice= random.choice(choice)
            print(" computer select :" , computerchoice)

            if yourchoice == computerchoice:
                youwin+=1
                computerwin+=1
                print(" this round is drwan:")
            elif (yourchoice =="paper" and computerchoice =="rock") or (yourchoice =="rock" and computerchoice =="scissor") or (yourchoice =="scissor" and computerchoice =="paper"):
                youwin+=1
                print("you win this round")
            else:
                computerwin+=1
                print("computer won this round")

      if youwin >computerwin:
          print("you win the game:")
          print("score is :", "your score:",youwin,"computer score:",computerwin,sep=" ")
      elif computerwin > youwin:
          print("you lose the game, computer win the game:")
          print("score is :", "your score:",youwin,"computer score:",computerwin,sep=" ")
      else:
          print("match drawn")
          print("score is :", "your score:",youwin,"computer score:",computerwin,sep=" ")
      user_choice = input(" want to playagain?(yes/exit)")
      if user_choice =="yes" or user_choice=="Yes" or user_choice == "YES":
          continue
      else:
          break