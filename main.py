import random

varNumber = random.randint (1 , 100)

guess1 =  int( input("guess a number between 1 and 100 "))

if (guess1 > varNumber ):
  print( "your guess was too high  guess again")
elif(guess1 < varNumber ) :
  print(" your guess was too low guess again")
else:
  print("congrats correct!!!!")



guess2 =  int( input("guess a number between 1 and 100 "))

if (guess2 > varNumber ):
  print( "your guess was too high  guess again")
elif(guess2 < varNumber ) :
  print(" your guess was too low guess again")
else:
  print("congrats correct!!!!")


guess3 =  int( input("guess a number between 1 and 100 "))

if (guess3 > varNumber ):
  print( "your guess was too high  guess again")
  print("Sorry!! you lost game dun dun dahh ")
elif(guess3 < varNumber ) :
  print(" your guess was too low guess again")
  print("Sorry!! you lost the game dun dun dahhh")
else:
  print("congrats correct!!!!")
 
print("the correct number is ",varNumber )