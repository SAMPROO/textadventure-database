import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'sampo', database = 'textadventure-database')
cur = conn.cursor()

def get_location(location_id):
    ret = None
    cur = conn.cursor()
    sql = "SELECT location_name, description FROM location WHERE location_id='" + location_id + "'"
    cur.execute(sql)
    for row in cur:
        print (row[0])
        if (row[1] != ""):
            print(row[1])
    return


def look(location_id):
    cur = conn.cursor()
    sql = "SELECT description FROM location WHERE location_id = '" + id + "'"
    cur.execute(sql)
    for row in cur:
        print (row[0])
        if (row[1] != ""):
            print(row[1])
    return
#..
def look_around(location_id):
    print("-"*80)
    get_location(location_id)
    return



def github():
    print()

def move(from_loc, to_loc, direction):
    from_loc = location_id
    to_loc = location_id
    cur = conn.cursor()
    sql = "SELECT from_location_id, to_location_id, neighbour_direction_id FROM neighbours WHERE from_location_id = '" + from_loc + "' AND to_location_id = '" + to_loc + "' AND neighbour_direction_id = '" + direction + "'"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            to_locaction_id = row[0]
    else:
        to_locaction_id = location_id;  # movement not possible
    return to_locaction_id


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
    elif (action == "n" or action == "s" or action == "w" or action == "e" or action == "u" or action == "d" or action == "north" or action == "south" or action == "west" or action == "east" or action == "up" or action == "down"):
        move(location_id, location_id, action)

conn.rollback()