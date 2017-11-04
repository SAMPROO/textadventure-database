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


def move(from_loc, to_loc, direction):
    cur = conn.cursor()
    sql = "SELECT from_location_id, to_location_id, neighbour_direction_id FROM neighbours WHERE from_location_id = '" + str(from_loc) + "' AND to_location_id = '" + str(to_loc) + "' AND neighbour_direction_id = '" + str(direction) + "'"
    cur.execute(sql)
    newroom = get_location(to_loc)
    if newroom is None:
        print("You cant go that way")
    else:
        get_location(to_loc)


location_id = 1
action = ""

look(location_id)

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
    if (action == "n" or "s" or "w" or "e" or "u" or "d" or "north" or "south" or "west" or "east" or "up" or "down"):
        move(location_id, location_id, action)

