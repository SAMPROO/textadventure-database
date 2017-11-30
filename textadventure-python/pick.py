

def pickup(conn, location_id, item):

    cur = conn.cursor()
    print(item)
    if item == None:
        print("What do you want to pick up?")
        item = input("--> ")
        pickup(conn, location_id, item)
    else:

        if item == 'all' or item == 'everything':
            items = "SELECT name FROM item WHERE pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
            p = "UPDATE item SET item_character_id = 1 WHERE pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
            s = "UPDATE item SET item_location_id = NULL WHERE item_location_id = '" + str(location_id) + "'"
        else:
            items = "SELECT name, pickable FROM item WHERE name = '" + item + "' AND item_location_id = '" + str(location_id) + "'"
            p = "UPDATE item SET item_character_id = 1 WHERE item.name= '" + item + "' AND pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
            s = "UPDATE item SET item_location_id = NULL WHERE item.name = '" + item + "' AND item_location_id = '" + str(location_id) + "'"

        cur.execute(items)
        for row in cur:
            item = row[0]
            pickable = row[1]

        if pickable == 1:
            cur.execute(p)
            if cur.rowcount >= 1:
                print("Picked up:")
                print("  -" + item)
            else:
                print("There's no " + item + " to be seen")
            cur.execute(s)
        else:
            print("The " + item + " is not pickable")

    return location_id


