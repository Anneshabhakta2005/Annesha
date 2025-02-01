'''
1 for snake
-1 for water
0 for gun
'''
computer= -1
you =input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
you=  youDict[you]
if(computer==-1 and you==1):
   print("You win")
elif(computer==-1 and you==0):
   print("You lose")
if(computer==1 and you==0):
   print("You win")
elif(computer==1 and you==-1):
   print("You lose")
if(computer==0 and you==-1):
    print("you win")
elif(computer==0 and you==1):
   print("you lose")
else:
  print("something went wrong")