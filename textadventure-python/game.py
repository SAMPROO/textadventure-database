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

#MOVE BETWEEN LOCATIONS
def move(location_id, direction):
    cur = conn.cursor()
    sql = "SELECT from_location_id, to_location_id, neighbour_direction_id FROM neighbours WHERE from_location_id = '" + str(location_id) + "'AND neighbour_direction_id = '" + str(direction) + "'"

    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            location_id = row[1]
            get_location(location_id)
    else:
        print("You cant go that way")


directions = ['n',
              's',
              'w',
              'e',
              'u',
              'd',
              'north',
              'south',
              'west',
              'east',
              'up',
              'down']


location_id = 1
action = ""

look_around(location_id)
#MAIN LOOP
while action != "exit" or "quit" or "end":

    print("")
    input_string = input("--> ").split()
    if len(input_string) >= 1:
        action = input_string[0].lower()
    else:
        action = ""

    # look
    if (action == "look" or action == "examine" or action == "view"):
        look_around(location_id);

    elif (action in directions):
        #MOVE TO GIVEN LOCATION
        newLocation = move(location_id, action)
        location_id = newLocation

if location_id is 5:
    print("Game over")