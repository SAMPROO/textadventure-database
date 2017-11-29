def inventory ():
    cur=db.cursor()
    i="SELECT item.name FROM item INNER JOIN character_ ON item.item_character_id=character_.character_id "
    cur.execute(i)
    if cur.rowcount>=1:
        print("You are carrying: ")
        items=cur.fetchall()
        for item in items:
            print("'"+item[0]+"'")
    else:
        print("You don't have any items ")
