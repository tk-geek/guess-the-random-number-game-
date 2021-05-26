import random

number = random.randint (1 , 100)

guess1 =  int( input("guess a number between 1 and 100 "))

if (guess1 > number ):
  print( "your guess was too high  guess again")
elif(guess1 < number ) :
  print(" your guess was too low guess again")
else:
  print("congrats correct!!!!")



guess2 =  int( input("guess a number between 1 and 10 "))

if (guess2 > number ):
  print( "your guess was too high  guess again")
elif(guess2 < number ) :
  print(" your guess was too low guess again")
else:
  print("congrats correct!!!!")


guess3 =  int( input("guess a number between 1 and 10 "))

if (guess3 > number ):
  print( "your guess was too high  guess again")
  print("Sorry!! you lost game dun dun dahh ")
elif(guess3 < number ) :
  print(" your guess was too low guess again")
  print("Sorry!! you lost the game dun dun dahhh")
else:
  print("congrats correct!!!!")
 