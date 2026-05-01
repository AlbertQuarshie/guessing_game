import random

def choose_difficulty():
    print("Select Difficulty Level: ")
    print("1: Easy")
    print("2: Moderate")
    print("3: Hard")


    while True:
        choice = input("Select Choice (1,2,3):")
    if choice == '1':
        return 10
    elif choice == '2':
        return 5
    elif choice == '3':
        return 3
    else:
        print("Invalid choice. Select 1, 2 or 3")

        