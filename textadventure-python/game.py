import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'sampo', database = 'textadventure-database')
cur = conn.cursor()



def get_location(location_id):
    ret = None
    cur = conn.cursor()
    sql = "SELECT location_name, description FROM location WHERE location_id='" + str(location_id) + "'"
    cur.execute(sql)
    for row in cur:
        print (row[0])
        if (row[1] != ""):
            print(row[1])
    return

#LOOK WITHIN A LOCATION
def look(location_id):
    cur = conn.cursor()
    sql = "SELECT description FROM location WHERE location_id = '" + str(location_id) + "'"
    cur.execute(sql)
    for row in cur:
        print (row[0])
    return
#..
def look_around(location_id):
    print("-"*80)
    get_location(location_id)
    return

def set_location(newLocation):
    location_id = newLocation

#MOVE BETWEEN LOCATIONS
def move(location_id, direction):
    cur = conn.cursor()
    sql = "SELECT from_location_id, neighbours.to_location_id, neighbour_direction_id FROM neighbours INNER JOIN \
           direction ON neighbours.neighbour_direction_id = direction.direction_id WHERE \
           direction.direction ='" + direction + "' OR  direction.direction_id = '" + direction + "' AND from_location_id = '" + str(location_id) + "'"

   # sql = "SELECT from_location_id, neighbours.to_location_id, neighbour_direction_id FROM neighbours WHERE from_location_id = '" + str(location_id) + "' AND neighbour_direction_id = '" + str(direction) + "'"
    #print(sql)
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            location_id = row[1]
            get_location(location_id)
    else:
        print("You cant go that way")
    return location_id
#TRYING
def directions1(input_action):
    cur = conn.cursor()
    sql = "SELECT to_location_id,direction_id, direction FROM neighbours INNER JOIN direction ON neigbours.neighbour_direction_id = direction.direction_id WHERE direction.direction_id = direction.direction = '" + input_action + "'"
    print(sql)
    cur.execute(sql)
    move(location_id, input_action)






    cur.execute(sql)


directions = ['n', 's', 'w', 'e', 'u', 'd', 'north', 'south', 'west', 'east', 'up', 'down']
look = ["view", "look", "examine"]
quit = ['exit', 'quit', 'end', 'finnish']

location_id = 1
action = ""

look_around(location_id)

#MAIN LOOP

while action not in quit:

    print("")
    input_string = input("--> ").split()
    if len(input_string) >= 1:
        action = input_string[0].lower()
    else:
        action = ""

    # look
    if (action in look):
        look(location_id);

    if action in directions:
        #directions1(action)

        newLocation = move(location_id, action)
        location_id = newLocation


    if location_id is 5:
        print("Game over")