import random

print("🎮 WELCOME TO THE NUMBER GUESSING GAME")
print("RULES: The computer chooses a number between 1 and 10.")
print("You have 3 chances to guess the correct number.\n")

player_chances=3

while player_chances>0:
    computer=random.randint(1,10)
    guess=int(input("Enter your number: "))
    
    if(computer==guess):
        print("🎉 Hurray! You guessed the correct number.")
        break
    elif(computer>guess):
        print("To low")
    else:
        print("To High")  
    player_chances=player_chances-1
    print("Remaining chances:", player_chances)
if(player_chances==0):
    print("❌ You lost! The correct number was:", computer)    
print("Thanks for playing!")    
