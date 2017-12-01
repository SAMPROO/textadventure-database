import databaseconfig as cfg
import pymysql

conn = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['db'])
cur = conn.cursor()


cur = conn.cursor()
print("Hello! Let's add words to the databases")
print("Press:\n1: Add item\n2: Quit\n")

x = str(input("--> "))
while x is not '0':
    if x == '1':
    
        name = str(input("Item name: "))
        description = str(input("Item description: "))
        attack = int(input("Item attack value: "))
        defence = int(input("Item defence value: "))
        money = int(input("Item money value: "))
        addhp = int(input("Item addhp value: "))
        pickable = int(input("Item picable value (1 or 0): "))
        location = int(input("Item location: "))
    
    try:
        cur.execute("INSERT INTO item (item_id, item.name, description, attack, defence, money, addhp, pickable, item_location_id, item_character_id) \
                            VALUES (NULL, '%s', '%s', %d, %d, %d, %d, %d, %d, NULL)" % (name, description, attack, defence, money, addhp, pickable, location))
        conn.commit()
    except:
        conn.rollback()



    item_list = "SELECT name FROM item"
    cur.execute(item_list)
    for row in cur:
        print(row[0])
conn.close()