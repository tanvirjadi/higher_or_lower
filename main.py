from random import randint
from game_data import data
from art import *

print(logo)

def get_random_celebrity():
    return data[randint(0, len(data) - 1)]

a = get_random_celebrity()
b = get_random_celebrity()

def compare(celebrity, compare_word):
    print(f"{compare_word}: {celebrity["name"]}, a {celebrity["description"]}, from {celebrity["country"]}.")

def compare_with_followers(a_celebrity, b_celebrity):
    if a_celebrity["follower_count"] > b_celebrity["follower_count"]:
        return a_celebrity
    else:
        return b_celebrity

winner = compare_with_followers(a, b)
score = 0
is_game_over = False

while not is_game_over:
    compare(a, "Compare A")
    print(vs)
    compare(b, "Against B")
    guess = input(f"Who has more followers? Type 'A' for {a["name"]} or 'B' for {b["name"]}: ").upper()
    if guess == "A" and winner == a:
        b = winner
        a = get_random_celebrity()
        winner = compare_with_followers(a, b)
        score += 1
        print("\n" * 1000)
        print(logo)
        print(f"You're right! Current score: {score}.")
    elif guess == "B" and winner == b:
        a = winner
        b = get_random_celebrity()
        winner = compare_with_followers(a, b)
        score += 1
        print("\n" * 1000)
        print(logo)
        print(f"You're right! Current score: {score}.")
    else:
        is_game_over = True
        print("\n" * 1000)
        print(logo)
        print(f"Sorry, that's wrong, Final score: {score}")