
def eat(conn, location_id, item):
    sql = "SELECT name FROM item WHERE item_location_id = '" + str(location_id) + "' AND eatable = 1"
    sql = "SELECT name FROM item WHERE item_character_id = 0 AND name = '" + item + "'"