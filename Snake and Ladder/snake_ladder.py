from random import randint

# UC1: Start the game (Initialize player positions)
def start():
    return 0

# UC2: Roll the die (Returns a number between 1-6)
def rolldie():
    return randint(1, 6)

# UC3: Determine play type (0: No Play, 1: Ladder, 2: Snake)
def moveToPlay():
    return randint(0, 2)

# UC4: Move the player, ensuring restart at 0 if position < 0
def move(pos):
    movereceived = moveToPlay()
    steps = rolldie()

    if movereceived == 0:  # No Play
        print(f"No Play. Current Position: {pos}\n")
        return pos

    elif movereceived == 1:  # Ladder
        new_pos = pos + steps
        print(f"🎉 Ladder! You move forward {steps} steps.")
        return new_pos

    else:  # Snake
        new_pos = pos - steps
        if new_pos < 0:
            print(f"🐍 Snake! You rolled {steps}, but can't go below 0. Restarting at 0.\n")
            return 0
        else:
            print(f"🐍 Snake! You move back {steps} steps.")
            return new_pos

# UC5: Ensure the player reaches exactly 100 to win
def check_win_condition(pos):
    if pos > 100:
        print(f"You rolled too high! Staying at {pos - (pos - 100)} until you roll exactly {100 - (pos - (pos - 100))}.\n")
        return pos - (pos - 100)  # Stay at the previous position
    return pos

# UC6: Report the number of dice rolls and positions after every roll
def report_dice_roll(player, rolls):
    print(f"🎲 {player} has rolled {rolls} times. Current Position: {player}\n")

# UC7: Play the game with 2 players and track everything
def play_game():
    player_A = start()
    player_B = start()
    dice_count_A = 0
    dice_count_B = 0

    while player_A != 100 and player_B != 100:
        print("Player A MOVES:")
        player_A = move(player_A)
        player_A = check_win_condition(player_A)
        dice_count_A += 1
        report_dice_roll("Player A", dice_count_A)

        if player_A == 100:
            print(f"🏆 Player A WINS in {dice_count_A} dice rolls!")
            break

        print("Player B MOVES:")
        player_B = move(player_B)
        player_B = check_win_condition(player_B)
        dice_count_B += 1
        report_dice_roll("Player B", dice_count_B)

        if player_B == 100:
            print(f"🏆 Player B WINS in {dice_count_B} dice rolls!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
