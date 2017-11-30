

def pickup(conn, location_id, item):

    cur = conn.cursor()
    print("-------------------")
    print("Input item = " + item)

    if item == 'all' or item == 'everything':
        items = "SELECT name FROM item WHERE pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
        p = "UPDATE item SET item_character_id = 1 WHERE pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
        s = "UPDATE item SET item_location_id = NULL WHERE item_location_id = '" + str(location_id) + "'"
    else:
        items = "SELECT name FROM item WHERE name = '" + item + "' AND pickable = TRUE AND item_location_id = '" + str(location_id) + "'"
        p = "UPDATE item SET item_character_id = 1 WHERE item.name= '" + item + "' AND pickable = TRUE"
        s = "UPDATE item SET item_location_id = NULL WHERE item.name = '" + item + "' AND item_location_id = '" + str(location_id) + "'"


    print("SQL query = " + items)
    print("----------------------")
    cur.execute(p)
    if cur.rowcount >= 1:
        print("Picked up:")
        cur.execute(items)
        for row in cur:
            print("  -" + row[0])
    else:
        print("You can't take that.")
    cur.execute(s)

    return location_id


