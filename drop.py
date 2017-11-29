def drop(location_id, item):
    cur=db.cursor()
    sql="UPDATE item SET item_character_id=NULL WHERE item.name='"+item+"'"
    sql1="UPDATE item SET item_location_id = '"+str(location_id)+"' WHERE item.name='"+item+"'"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("Dropped")
    else:
        print("You don't have this item")
    cur.execute(sql1)