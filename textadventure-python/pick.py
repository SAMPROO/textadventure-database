

def pickup(conn, location_id, item):

    if item == None:
        print("What do you want to pick up?")
        item = input("--> ")
        pickup(conn, location_id, item)
    else:
        # CONNECTS THE ITEM AND DICTIONARY TABLE
        cur = conn.cursor()
        unite_dictionary = "SELECT item.name FROM item INNER JOIN item_word_table ON item.item_id = item_word_table.item \
                                INNER JOIN dictionary ON item_word_table.dictionary = dictionary.id WHERE dictionary.dictionary = '" + item + "'"
        cur.execute(unite_dictionary)
        if cur.rowcount >= 1:
            row = cur.fetchall()
            item = row[0][0]

        if item == 'all' or item == 'everything':
            items = "SELECT name, pickable FROM item WHERE pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
            p = "UPDATE item SET item_character_id = 1 WHERE pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
            s = "UPDATE item SET item_location_id = NULL WHERE item_location_id = '" + str(location_id) + "'"
        else:
            items = "SELECT name, pickable FROM item WHERE name = '" + item + "' AND item_location_id = '" + str(location_id) + "'"
            p = "UPDATE item SET item_character_id = 1 WHERE item.name= '" + item + "' AND pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
            s = "UPDATE item SET item_location_id = NULL WHERE item.name = '" + item + "' AND item_location_id = '" + str(location_id) + "'"

        cur.execute(items)
        if cur.rowcount >= 1:
            row1 = cur.fetchall()

            if row1[0][1] is 1:
                cur.execute(items)
                print("Picked up:")
                for row in cur:
                        print("  -" + row[0])
            else:
                print("The " + row1[0][0] + " is not pickable")
            cur.execute(p)
            cur.execute(s)
        else:
            print("There's no " + item + "'s here")



    return location_id


