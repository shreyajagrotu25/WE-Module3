import random

def roll_dice(num_dice):
    """Rolls a given number of dice."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def reroll_dice(dice):
    """Allows the player to reroll selected dice."""
    reroll_indices = input("Enter indices of dice to reroll (space-separated): ").split()
    for idx_str in reroll_indices:
        idx = int(idx_str)
        dice[idx - 1] = random.randint(1, 6)
    return dice

def print_dice(dice):
    """Prints the current roll of the dice."""
    print("Your roll:", " ".join(map(str, dice)))

def calculate_score(dice, category):
    """Calculates the score based on the chosen category."""
    if category == "chance":
        return sum(dice)
    elif category == "yahtzee" and len(set(dice)) == 1:
        return 50
    elif category[:-1] in ["ones", "twos", "threes", "fours", "fives", "sixes"]:
        try:
            multiplier = int(category[-1])
            return dice.count(multiplier) * multiplier
        except ValueError:
            print("Invalid category.")
            return 0
    else:
        print("Invalid category.")
        return 0

def play_round(round_num, categories, scores):
    """Plays a single round of the Yahtzee game."""
    print(f"\nRound {round_num}")
    dice = roll_dice(5)
    print_dice(dice)
    for _ in range(2):
        reroll_choice = input("Do you want to reroll? (y/n): ")
        if reroll_choice.lower() == 'y':
            dice = reroll_dice(dice)
            print_dice(dice)
        else:
            break
    category = choose_category(categories, scores)
    score = calculate_score(dice, category)
    scores[category] = score
    print(f"Your score for {category}: {score}")

def main():
    """Main function to orchestrate the game."""
    print("Welcome to Yahtzee!")
    categories = ["ones", "twos", "threes", "fours", "fives", "sixes", "chance", "yahtzee"]
    scores = {category: None for category in categories}
    for round_num, category in enumerate(categories, start=1):
        play_round(round_num, categories, scores)
    total_score = sum(filter(None, scores.values()))
    print(f"Total score: {total_score}")
    print("Game Over")

if __name__ == "__main__":
    main()
