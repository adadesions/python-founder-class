import random

missons = [
    "Go to coding room",
    "Fix electricity",
    "Solve problem at meeting room",
    "Fix the generator",
    "Switch A to B"
]


def generate_player(name, missons, isImposter):
    return {
        'name': name,
        'missons': missons,
        'isImposter': isImposter
    }


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

    players_info = []
    for idx, p in enumerate(players):
        misson_index = random.randint(0, len(missons) - 1)
        isImposter = (1 == p)
        player = generate_player(idx, missons[misson_index], isImposter)

        players_info.append(player)
    
    print(players_info)

