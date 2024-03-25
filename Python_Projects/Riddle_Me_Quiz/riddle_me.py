print("Welcome To Riddle Me - A Quiz Game")

playing = input("Continue To Game" )

if playing != "yes" or "y":
    print("Exiting the Game")
    quit()

print("The Game Begins")

answer = input("What does CPU stand for? ")

if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect")

