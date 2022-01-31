from multiprocessing.connection import answer_challenge


name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end nad you go left or right. ehich way you would like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swin across")
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose")   
elif answer == "right":
    answer = input("You come to a bridge. it looks wobbly, do you want to cross it or head back (cross/walk)? ")
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stranger and they give you a Gold. You Win! ")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose")
        else:
            print("not a valid option, You lose")
    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

print("Thank you for Trying", name)
