from world import World


def mainprogram():
    print("\n--- Welcome to Game Of Life by Gjerry ---\n")
    rows = int(input("How many rows: "))
    cols = int(input("\nHow many cols: "))
    world = World(rows, cols)

    world.draw()

    inp = input("Press enter to continue or q to quit\n> ").lower()
    while inp != "q":
        world.update()
        world.draw()
        inp = input("Press enter to continue or q to quit\n> ").lower()

    print("\n --- GAME OF LIFE FINISHED ---\n")

mainprogram()
