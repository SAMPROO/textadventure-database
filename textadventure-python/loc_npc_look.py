
#GETTING LOCATION AFTER MOVEMENT----------------------------------------------------------------------------------------------
def get_location(conn, location_id):
    cur = conn.cursor()
    sql = "SELECT location_name, description FROM location WHERE location_id='" + str(location_id) + "'"
    cur.execute(sql)
    for row in cur:
        print (row[0])
        print(row[1])

    print_item(conn, location_id)
    print_npc(conn, location_id)

    return location_id
#PRINT ITEMS--------------------------------------------------------------------------------------------------------------
def print_item(conn, location_id):
    cur = conn.cursor()
    sql = "SELECT description FROM item WHERE item_location_id = '" + str(location_id) + "'"
    cur.execute(sql)
    for row in cur:
        print(row[0])

#PRINT NPC------------------------------------------------------------------------------------------------------------------
def print_npc(conn, location_id):
    cur = conn.cursor()
    sql = "SELECT npc.description FROM npc WHERE npc_location_id = '" + str(location_id) + "'"
    cur.execute(sql)
    for row in cur:
        print(row[0])


#LOOK WITHIN A LOCATION-------------------------------------------------------------------------------------------------------
def look_around(conn, location_id):
    print("-"*80)
    get_location(conn, location_id)
    return

#INSPECT ITEM
def inspect(conn, location_id, item):
    cur = conn.cursor()
    if location_id is not None:
        cur.execute("SELECT inspect FROM item WHERE item_location_id = '" + str(location_id) + "' AND name = '" + item + "'")
        if cur.rowcount >= 1:
            print(cur.fetchall()[0][0])
        else:
            print("This doest't interest me..")

    elif location_id is None:
        cur.execute("SELECT inspect FROM item WHERE item_character_id = 1 AND name = '" + item + "'")
        if cur.rowcount >= 1:
            print(cur.fetchall()[0][0])
        else:
            print("This doest't interest me..")

    return location_id

#MOVE BETWEEN LOCATIONS--------------------------------------------------------------------------------------------------------
def move(conn, location_id, direction):


    if direction == None:
        print("Where do you want move? ")
        return location_id
    else:
        cur = conn.cursor()
        sql2 = "SELECT direction FROM direction WHERE direction_id='" + direction + "'"

        cur.execute(sql2)
        if cur.rowcount >= 1:
            result2 = cur.fetchall()
            direction = result2[0][0]

        sql = "SELECT to_location_id FROM neighbours INNER JOIN  \
              direction ON neighbours.neighbour_direction_id = direction_id WHERE \
              direction.direction_id ='" + direction + "' OR direction.direction = '" + direction + "' AND \
              from_location_id = '" + str(location_id) + "'"

        cur.execute(sql)
        if cur.rowcount >= 1:
            for row in cur.fetchall():
                location_id = row[0]
                get_location(conn, location_id)
        else:
            print("You cant go that way")
        return location_id