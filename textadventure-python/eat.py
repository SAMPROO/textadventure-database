
def eat(conn, location_id, item):


    if item == None:

        print("What do you want to eat?")
        item = input("--> ")
        eat(conn, location_id, item)

    cur = conn.cursor()

    #CHECK IF IN INVENTORY OR IN A LOCATION
    check_loc_inv = "SELECT name, item_location_id, item_character_id, addhp FROM item WHERE name = '" + item + "'"
    cur.execute(check_loc_inv)

    for row in cur:
        name = row[0]
        item_loc = row[1]
        item_cha = row[2]
        addhp = row[3]

    if name == item:

        if item_loc is not None:
            sql = "SELECT name FROM item WHERE item_location_id = '" + str(location_id) + "' AND name = '" + item + "' AND eatable = 1"
            cur.execute(sql)

            if cur.rowcount >= 1:

                cur.execute("UPDATE character_ SET hp = hp + '" + str(addhp) + "' WHERE character_id = 1")
                cur.execute("UPDATE item SET item_location_id = NULL, item_character_id = NULL WHERE name = '" + item + "'")
                print("-" + str(addhp) + "hp added-")

            else:
                print(item + "!! That's not eatable..")


        elif item_loc == None and item_cha == 1:
            sql = "SELECT name FROM item WHERE name = '" + item + "' AND item_character_id = 1  AND eatable = 1"
            cur.execute(sql)

            if cur.rowcount >= 1:

                cur.execute("UPDATE character_ SET hp = hp + '" + str(addhp) + "' WHERE character_id = 1")
                cur.execute("UPDATE item SET item_location_id = NULL, item_character_id = NULL WHERE name = '" + item + "'")
                print("-" + str(addhp) + "hp added-")

                check_loc_inv = "SELECT name, item_location_id, item_character_id, addhp FROM item WHERE name = '" + item + "'"
                cur.execute(check_loc_inv)

            else:
                print(item + "!! That's not eatable..")
        else:
            print("I don't have any " + item + '\'s to eat')

    else:
        print("I don't see such thing..")

    return location_id