import random

def tile_generation():

    # River generation
    river_location_x = random.randint(0, 4)

    if random.randint(1, 100) <= 50:
        river_location_y = 0
        river_start = 'bottom'
    else:
        river_location_y = 4
        river_start = 'top'

    templist = []

    while river_location_y != -1 and river_location_y != 5 and river_location_x != -1 and river_location_x != 5:
        templist.append((river_location_x, river_location_y))

        # Even
        if river_location_y % 2 == 0:
            river_location_x -= random.randint(0, 1)

        # Odd
        else:
            river_location_x += random.randint(0, 1)

        if river_start == 'top':
            river_location_y -= 1

        elif river_start == 'bottom':
            river_location_y += 1

    print(templist)

    return templist

# river goes left or right on it's way up or down. just change x left or right