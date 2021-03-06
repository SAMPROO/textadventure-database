import time
import textwrap

#GETTING LOCATION AFTER MOVEMENT----------------------------------------------------------------------------------------------
def get_location(conn, location_id):
    cur = conn.cursor()
    sql = "SELECT location_name, description FROM location WHERE location_id='" + str(location_id) + "'"
    cur.execute(sql)
    for row in cur:
        print("-" + row[0] + "-")
        print("--------------------------")
        for line in textwrap.wrap(row[1], 72):
            print(line)

    print_npc(conn, location_id)
    print_item(conn, location_id)


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
    return location_id

#INSPECT ITEM
def inspect(conn, location_id, item):
    cur = conn.cursor()

    if item == None:

        print("What do you want to inspect?")
        item = input("--> ")
        inspect(conn, location_id, item)

    else:

            cur.execute("SELECT inspect FROM item WHERE item_location_id = '" + str(location_id) + "' AND name = '" + item + "'")
            if cur.rowcount >= 1:
                for row in cur:
                    for line in textwrap.wrap(row[0][0], 72):
                        print(line)
            else:
                cur.execute("SELECT inspect FROM item WHERE item_character_id = 1 AND name = '" + item + "'")
                if cur.rowcount >= 1:
                    print(cur.fetchall()[0][0])
                else:
                    print("\nThis doest't interest me..")

    return location_id

#MOVE BETWEEN LOCATIONS--------------------------------------------------------------------------------------------------------
def move(conn, location_id, direction):

    cur = conn.cursor()

    move.counter += 1

    voice = "SELECT voice FROM voice WHERE move_counter = '" + str(move.counter) + "'"
    cur.execute(voice)

    if cur.rowcount >= 1:
        row = cur.fetchall()[0][0]
        print(row + "\n")
        time.sleep(1.7)

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
            row = cur.fetchall()[0]
            new_location_id = row[0]

            check_item = "SELECT needed_item, no_item, yes_item, item_character_id FROM location INNER JOIN item ON needed_item = item_id WHERE location_id = '" + str(new_location_id) + "'"
            cur.execute(check_item)

            if cur.rowcount >= 1:

                row = cur.fetchall()[0]
                if row[3] is None:
                    print(row[1])
                    return new_location_id
                elif row[3] is 1:
                    print(row[2] + "\n")
                    time.sleep(2)
                    get_location(conn, new_location_id)
                    return new_location_id
                else:
                    print("ERROR")
            else:
                get_location(conn, new_location_id)
                return new_location_id
        else:
            print("You cant go that way")
            return location_id

move.counter = 0


def quit():
    print("Thank you for playing!")