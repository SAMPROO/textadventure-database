
def eat(conn, location_id, item):


    if item == None:

        print("What do you want to pick up?")
        item = input("--> ")
        eat(conn, location_id, item)

    cur = conn.cursor()

    #CHECK IF IN INVENTORY OR IN A LOCATION
    check_loc_inv = "SELECT name, item_location_id, item_character_id, addhp FROM item WHERE name = '" + item + "'"
    cur.execute(check_loc_inv)

    print(cur.fetchall()[0][1])

    name = cur.fetchall()[0][0]
    print(name)
    item_loc = cur.fetchall()[0][1]
    print(item_loc)
    item_cha = cur.fetchall()[0][2]
    addhp = cur.fetchall()[0][3]

    if name == item:

        if item_loc is not 0:
            sql = "SELECT name FROM item WHERE item_location_id = '" + str(location_id) + "' AND name = '" + item + "' AND eatable = 1"
            cur.execute(sql)

            if cur.rowcount >= 1:
                cur.execute("UPDATE character_ SET hp = hp + '" + addhp + "' WHERE character_id = 1")
                cur.execute("UPDATE item SET item_location_id = 0 AND item_character_id = 0 WHERE name = '" + item + "'")
                print(addhp + "hp added")
                conn.commit()

            else:
                print(item + "!! That's not eatable..")


        elif item_loc == 0 and item_cha == 1:
            sql = "SELECT name FROM item WHERE item_character_id = 1 AND name = '" + item + "' AND eatable = 1"
            cur.execute(sql)

            if cur.rowcount >= 1:
                cur.execute("UPDATE character_ SET hp = hp + '" + addhp + "' WHERE character_id = 1")
                cur.execute("UPDATE item SET item_location_id = 0 AND item_character_id = 0 WHERE name = '" + item + "'")
                print(addhp + "hp added")
                conn.commit()
            else:
                print(item + "!! That's not eatable..")

    else:
        print("I don't see such thing..")

    return location_id