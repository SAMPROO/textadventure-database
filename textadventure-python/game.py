import pymysql
#CONNECTION TO DATABASE
conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'sampo', database = 'textadventure-database')
cur = conn.cursor()


#GETTING LOCATION AFTER MOVEMENT
def get_location(location_id):
    cur = conn.cursor()
    sql = "SELECT location_name, description FROM location WHERE location_id='" + str(location_id) + "'"
    cur.execute(sql)
    for row in cur:
        print (row[0])
        if (row[1] != ""):
            print(row[1])
    return

#LOOK WITHIN A LOCATION
def look_around(location_id):
    print("-"*80)
    get_location(location_id)
    return

#MOVE BETWEEN LOCATIONS
def move(location_id, direction):
    cur = conn.cursor()
    sql = "SELECT from_location_id, neighbours.to_location_id, neighbour_direction_id FROM neighbours INNER JOIN \
           direction ON neighbours.neighbour_direction_id = direction.direction_id WHERE \
           direction.direction ='" + direction + "' OR  direction.direction_id = '" + direction + "' AND from_location_id = '" + str(location_id) + "'"

    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            location_id = row[1]
            get_location(location_id)
    else:
        print("You cant go that way")
    return location_id

#COMMAND LIST
directions = ['n', 's', 'w', 'e', 'u', 'd', 'north', 'south', 'west', 'east', 'up', 'down']
look = ["view", "look", "examine"]
quit = ['exit', 'quit', 'end', 'finnish']

all_commands = directions + look + quit

#STARTING VALUES
location_id = 1
look_around(location_id)
action = ""

#MAIN LOOP
while action not in quit:

    #ACTION TO LOWERCASE AND ONLY FIRST WORD
    print("")
    input_string = input("--> ").split()
    if len(input_string) >= 1:
        action = input_string[0].lower()
    else:
        action = ""

    #COMMAND NOT REGOGNIZED
    if action not in all_commands:
        print("I don't undestand")

    #LOOK AROUND
    if action in look:
        look_around(location_id);

    #MOVE AROUND
    if action in directions:
        move(location_id, action)

    #END GAME
    if location_id is 5:
        print("Game over")