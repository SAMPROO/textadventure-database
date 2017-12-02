
def drop(conn, location_id, item):

    #CONNECTS THE ITEM AND DICTIONARY TABLE
    cur = conn.cursor()
    unite_dictionary = "SELECT item.name FROM item INNER JOIN item_word_table ON item.item_id = item_word_table.item \
                           INNER JOIN dictionary ON item_word_table.dictionary_group = dictionary.id WHERE dictionary.dictionary = '" + item + "'"
    cur.execute(unite_dictionary)

    if cur.rowcount >= 1:
        row = cur.fetchall()
        item = row[0][0]

    cur = conn.cursor()
    if item == 'all' or item == 'everything':

         items = "SELECT item.name FROM item WHERE item_character_id = 1"
         sql = "UPDATE item SET item_character_id = NULL, item_location_id = '" + str(location_id) + "' WHERE item_character_id = 1"

    else:

        items = "SELECT name FROM item WHERE item_character_id = 1 AND name = '" + item + "' "
        sql = "UPDATE item SET item_character_id = NULL, item_location_id = '" + str(location_id) + "' WHERE item.name = '" + item + "' AND item_character_id = 1 "

    cur.execute(items)
    if cur.rowcount >= 1:
        print("Dropped: ")
        for row in cur:
                print("  -" + row[0])
        cur.execute(sql)
    else:
        print("You don't have this item")

    return location_id