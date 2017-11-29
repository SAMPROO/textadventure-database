def pickup(location_id, item):
    cur=db.cursor()
    p="UPDATE item SET item_character_id=1 WHERE item.name='"+item+"' AND pickable=TRUE"
    s = "UPDATE item SET item_location_id=NULL WHERE item.name='"+item+"' AND item_location_id='"+ str(location_id)+ "' "
    cur.execute(p)
    if cur.rowcount>=1:
        print("Taken.")
    else:
        print("You can't take that.")
    cur.execute(s)


