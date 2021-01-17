import random
import time

min = 1
max = 6

roll_dice = "yes"

while roll_dice == "yes" or roll_dice == "y":
  print("Roll the dices... ")
  time.sleep(2.5)
  print("The value is... \n")
  time.sleep(1.5)
  print("First number is: ", random.randint(min, max))
  print("Second number is: ", random.randint(min, max))

  roll_dice = input("\n Roll again: ")
  
#################
##Output::
#Roll the dices... 
#The value is... 
#
#First number is:  3
#Second number is:  4
#
#Roll again: 
