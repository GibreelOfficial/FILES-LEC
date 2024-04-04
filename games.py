games=["soccer","dart","Draft","chess"]

school_score=[]

for school in range(3):
    school_name=input("school name: ")

    game_score=[]

    for game in games:
        score=input(f"\t{game}: ")
        game_score.append(score)

    school_score.append(game_score)

print(school_score)
