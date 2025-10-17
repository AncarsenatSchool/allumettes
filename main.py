import random, os, time

def clear_screen():
    try:
        os.system("clear")
        # os.system("cls") WINDOWS
    except:
        print("could not clear screen (unsupported os ?)")

PLR_WIN = 1

HUMAN = 0
AI = 1

def ask_for_input(matches):
    while True:
        try:
            line = int(input("Choose a line (1 or 2): ")) - 1
            if line not in [0, 1]:
                print("Invalid line. Please choose 1 or 2.")
                continue
            qtt = int(input("Number of matches to remove: "))
            if qtt <= 0:
                print("Please enter a positive number.")
                continue
            if matches[line] < qtt:
                print(f"Not enough matches on line {line + 1}. Try again.")
                continue
            matches[line] -= qtt
            return matches
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def ai_think(matches,AI):
    if AI==1: # Always wins (récupéré sur un fandom)
        xor_value = matches[0] ^ matches[1]
        if xor_value == 0:
            line = random.choice([i for i in range(len(matches)) if matches[i] > 0])
            qtt = random.randint(1, matches[line])
        else:
            for i in range(2):
                target = matches[i] ^ xor_value
                if target < matches[i]:
                    line = i
                    qtt = matches[i] - target
                    break
        matches[line] -= qtt
        print(f"AI removed {qtt} matches from line {line + 1}.")
        return matches
    elif AI==2: # Random
        line = random.choice([i for i in range(len(matches)) if matches[i] > 0])
        qtt = random.randint(1, matches[line])
        matches[line] -= qtt
        print(f"AI removed {qtt} matches from line {line + 1}.")
        return matches
    elif AI==3: # 
        return NotImplementedError


def draw_matches(matches):
    for i, count in enumerate(matches):
        print(f"Line {i + 1}: " + "| " * count)

def main(Players):
    matches = [8, 8]
    player_turn=random.randint(0,len(Players)-1)
    while True:
        time.sleep(1)
        clear_screen()

        draw_matches(matches)
        if Players[player_turn] == HUMAN:
            print("Your turn:")
            matches = ask_for_input(matches)
        else:
            print("AI's turn:")
            AiLevel = Players[player_turn][1]
            matches = ai_think(matches,AiLevel)

        # Check for game end
        if sum(matches) == 0:
            if player_turn == HUMAN:
                print("Game over! You win!")
            else:
                print("Game over! AI wins!")
            return

        player_turn+=1
        if player_turn>=len(Players):
            player_turn=0


while True:
    main([(HUMAN),(AI,1)])