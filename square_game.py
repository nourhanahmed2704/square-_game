# Purpose: "this a  strategic game for two called Subtract a Square, players compete to take the last coin from a shared pile. They can only remove square numbers of coins at each turn. The winner is the one who makes the final move."
# Author: Nourhan Ahmed Hussien


# List of non-zero square numbers
non_zero_square_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441,
                           484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024]

# Welcome message
print("Welcome to Game 3")

# Prompt the user to select the method for choosing the initial number of coins
choice = input("If you want to choose manually, select (A). If you want to select randomly, select (B): ").upper()

# Validate the user's choice
while choice != "A" and choice != "B":
    choice = input(
        "Please select a valid choice! If you want to choose manually, select (A). If you want to select randomly, select (B): ").upper()

# Assign the initial number of coins based on the user's choice
if choice == "A":
    n_coins = int(input("Enter the number of coins you want to start with: "))
    while n_coins < 1:
        n_coins = int(input("Please enter a positive number: "))
elif choice == "B":
    import random
    n_coins = random.randint(1, 1000)
    while n_coins in non_zero_square_numbers:
        n_coins = random.randint(1, 1000)
    print("The random number is:", n_coins)

# Input player names
player1 = input("Enter the name of the first player: ")
player2 = input("Enter the name of the second player: ")

# Game loop
while n_coins > 1:
    print(player1, ", please take a non-zero square number less than", n_coins)
    take = int(input())

    # Ensure the selected number is a non-zero square number and less than the remaining coins
    if take in non_zero_square_numbers and take < n_coins:
        n_coins -= take
        print("Now we have", n_coins)

        # Check the winner
        if n_coins == 1:
            print(player2, "is the winner!")
            break

        # Player 2's turn
        elif n_coins > 1:
            while n_coins > 1:
                print(player2, ", please take a non-zero square number less than", n_coins)
                take = int(input())

                # Ensure the selected number is a non-zero square number and less than the remaining coins
                if take in non_zero_square_numbers and take < n_coins:
                    n_coins -= take
                    print("Now we have", n_coins)

                    # Check the winner
                    if n_coins == 1:
                        print(player1, "is the winner!")
                        break
                    else:
                        break
