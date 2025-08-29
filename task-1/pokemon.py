from itertools import combinations

Pokedex = {
"Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
"Lugia": ("Psychic", "Flying", "Water"),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}

def allPossibleTeams(k) :
    teams = combinations(Pokedex, k)
    for t in teams:
        print(t)

def strongestTeam(k) :
    maxNoOfTypes = 0
    bestTeam = None
    teams = combinations(Pokedex, k)
    for team in teams:
        noOfTypes = len(set().union(*(Pokedex[p] for p in team)))
        if noOfTypes > maxNoOfTypes :
            maxNoOfTypes = noOfTypes
            bestTeam = team 
    return bestTeam
    

print(strongestTeam(3))