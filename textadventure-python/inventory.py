def inventory (conn, location_id):

    cur = conn.cursor()
    i = "SELECT name FROM item WHERE item_character_id = 1"
    cur.execute(i)
    if cur.rowcount >= 1:
        print("You are carrying: ")
        items = cur.fetchall()
        for item in items:
            print("  -" + item[0])
    else:
        print("You don't have any items ")

    return location_id