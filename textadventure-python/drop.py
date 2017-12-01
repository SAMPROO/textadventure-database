
def drop(conn, location_id, item):

    cur = conn.cursor()
    if item == 'all' or item == 'everything':

         items = "SELECT item.name FROM item WHERE item_character_id = 1"
         sql = "UPDATE item SET item_character_id = NULL, item_location_id = '" + str(location_id) + "' WHERE item_character_id = 1"

    else:

        items = "SELECT name FROM item WHERE item_character_id = 1 AND name = '" + item + "' "
        sql = "UPDATE item SET item_character_id = NULL, item_location_id = '" + str(location_id) + "' WHERE item.name = '" + item + "' AND item_character_id = 1 "

    cur.execute(items)
    print("Dropped: ")

    if cur.rowcount >= 1:
        for row in cur:
                print("  -" + row[0])
        cur.execute(sql)
    else:
        print("You don't have this item")

    return location_id