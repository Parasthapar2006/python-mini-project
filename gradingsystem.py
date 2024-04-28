h=int(input("enter marks of 1st subject:"))
e=int(input("enter marks of 2nd subject:"))
m=int(input("enter marks of 3rd subject:"))
s=int(input("enter marks of 4th subject:"))
g=int(input("enter marks of 5th subject:"))

total= h+e+m+s+g
percentage=total/5
print("Total Marks are",total)
print("percentage",percentage,"%","out of 500")

if percentage>=85:

   print("Grade = A")

elif percentage>=75:
   print("Grade = B")

elif percentage>=50:
   print("Grade = C")

elif percentage>=30:

   print("Grade = D")

else :
    print("Reappear")