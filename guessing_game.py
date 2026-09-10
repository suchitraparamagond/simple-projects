import random

def play_game():
    lucky_num=random.randint(1,50)

    while True:
        user_num=int(input("guess the lucky num:"))

        if user_num==lucky_num:
            print("yehhhhh!!!!!, YOU WON")
        elif user_num<lucky_num:
            print("Too Low")
        else:
            print("Too High")

    print("Thankyou for playing!!")

play_game()