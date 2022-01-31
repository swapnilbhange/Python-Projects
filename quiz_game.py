print("Welcome to Quiz Game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play:)")
score = 0

answer = input("what does CPU stands for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stands for? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stands for? ").lower()
if answer == "power supply unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + "questions correct!")
print("you got " + str((score/4) *100 ) + "questions correct!")