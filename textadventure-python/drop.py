def drop(conn, location_id, item):
    cur = conn.cursor()
    if item == 'all' or item == 'everything':
         items = "SELECT item.name FROM item WHERE item.character_id = 1"
         sql = "UPDATE item SET item_character_id = NULL, item_location_id = '" + str(location_id) + "' WHERE item_character_id = 1"
    else:
        items = "SELECT item.name FROM item WHERE item.character_id = 1 AND item.name = '" + item + "' "
        sql = "UPDATE item SET item_character_id = NULL, item_location_id = '" + str(location_id) + "' WHERE item.name = '" + item +"' AND item_character_id = 1 "
    cur.execute(sql)
    if cur.rowcount >= 1:
        print("Dropped: ")
        cur.execute(items)
        for row in cur.fetchall():
            print(" -" + row[0])
    else:
        print("You don't have this item")