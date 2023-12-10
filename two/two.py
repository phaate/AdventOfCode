LIMITS = {"red": 12, "green": 13, "blue": 14}

FILEINPUT = "./input.txt"
with open(file=FILEINPUT, mode="r") as file:
    games = file.read().splitlines()

sumOfIds = 0

for game in games:
    splitted = game.split(":")
    gameNum = int(splitted[0][5::])
    splittedGames = splitted[1].split(";")
    process = True
    for splittedGame in splittedGames:
        cubes = splittedGame.split(",")
        for cube in cubes:
            if process:
                cubesSplit = cube.strip().split(" ")
                check = True
                isitokay = LIMITS[cubesSplit[1]]
                if int(cubesSplit[0]) > isitokay:
                    process = False
                    check = False



    if check:
        sumOfIds += gameNum

print(sumOfIds)
