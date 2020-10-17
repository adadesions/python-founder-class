import random


if __name__ == '__main__':
    num_player = int(input("Enter number of players: "))
    players = [0] * num_player

    num_imposter = int(input("Enter number of imposter: "))
    imposters = []

    while len(imposters) < num_imposter:
        imposter_index = random.randint(0, num_player - 1)
        if imposter_index in imposters:
            continue

        imposters.append(imposter_index)

        # 0 = Crewmate, 1 = imposter
        players[imposter_index] = 1

    # Show player list
    print(players)
    print("Imposter amount:", len(imposters))

