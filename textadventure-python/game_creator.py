import databaseconfig as cfg
import pymysql

conn = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['db'])
cur = conn.cursor()


cur = conn.cursor()


x = ""
print("\nHello! Let's add words to the databases")

while x != '0':

    print("\nPress:\n---------------------\n1: Add item\n2: Add noun synonyms\n3: Connect existing nouns to synonyms (automatic)\n4: Add verb\n5: Add verb synonyms\n6: Add locations\n0: Quit\n")

    x = str(input("--> "))
    if x == '1':

        print("\nAlready existing items:")
        cur.execute("SELECT name FROM item")
        for row in cur:
            print("  -" + row[0])

        name = str(input("\nNew item name: "))
        description = str(input("Item description: "))
        inspect = str(input("Item inspect description: "))
        attack = int(input("Item attack value: "))
        defence = int(input("Item defence value: "))
        money = int(input("Item money value: "))
        addhp = int(input("Item addhp value: "))
        pickable = int(input("Item picable value (1 or 0): "))
        eatable = int(input("Item eatable value (1 or 0): "))
        location = int(input("Item location: "))
    
        try:
            cur.execute("INSERT INTO item (item_id, item.name, description, inspect, attack, defence, money, addhp, pickable, eatable, item_location_id, item_character_id) \
                                VALUES (NULL, '%s', '%s', '%s', %d, %d, %d, %d, %d, %d, %d, NULL)" % (name, description, inspect, attack, defence, money, addhp, pickable, eatable, location))
            conn.commit()
            print("SUCCES!!")
        except:
            conn.rollback()
            print("Something went wrong...")

        cur.execute("SELECT DISTINCT id FROM dictionary_group ORDER BY id DESC LIMIT 1 OFFSET 2")
        id = cur.fetchall()[0][0] + 1

        try:
            cur.execute(
                "INSERT INTO dictionary_group (id, dictionary_group.name) VALUES (%d, '%s')" % (id, name))
            conn.commit()
            print("SUCCES!!")
        except:
            conn.rollback()
            print("Something went wrong...")

    elif x == '2':

        print("Choose the word that you want to add synonyms to---------------")
        cur.execute("SELECT name FROM dictionary_group")
        for row in cur:
               print("  -" + row[0])
        print("---------------------------------------------------------------")
        word = str(input("\n--> "))

        cur.execute("SELECT id FROM dictionary_group WHERE name = '" + word + "'")
        id = cur.fetchall()[0][0]

        print("\nSynonyms already added for the word \"" + word + "\"----------------- ")
        cur.execute("SELECT dictionary FROM dictionary WHERE id = '" + str(id) + "'")
        for row in cur:
            print("  -" + row[0])
        print("-----------------------------------------------------\n")

        add = str(input("Add words: ")).split(",")
        add = [x.strip(' ') for x in add]

        try:
            for i in add:
                cur.execute("INSERT INTO dictionary (id, dictionary.dictionary) VALUES (%d, '%s')" % (id, i))
                conn.commit()
                print("SUCCESS!!\n")
        except:
            conn.rollback()

    elif x == '3':

        cur.execute("SELECT item.name FROM item INNER JOIN dictionary_group ON item.name = dictionary_group.name")
        for word in cur.fetchall():
            print(word[0])

            cur.execute("SELECT item_id FROM item WHERE name = '" + word[0] + "'")
            item_id = cur.fetchall()[0][0]

            cur.execute("SELECT id FROM dictionary_group WHERE name = '" + word[0] + "'")
            dic_id = cur.fetchall()[0][0]

            try:
                cur.execute("INSERT INTO item_word_table (item, dictionary_group) VALUES (%d, %d)" % (item_id, dic_id))
                print("SUCCESS!!")
                conn.commit()
            except pymysql.err.IntegrityError:
                pass

        print("\nConnections added------------------")
        cur.execute("SELECT item.name FROM item INNER JOIN item_word_table ON item.item_id = item_word_table.item")
        for row in cur:
            print("  -" + row[0])

    elif x == '4':
        print("\nAlready existing verb categories----------------")
        cur.execute("SELECT name FROM verb_group")
        for row in cur:
            print("  -" + row[0])
        cur.execute("SELECT DISTINCT id FROM verb_group ORDER BY id DESC LIMIT 1")
        id = cur.fetchall()[0][0]
        name = str(input("\nVerb name: "))

        try:
            cur.execute("INSERT INTO verb_group VALUES (%d, '%s')" % (id, name))
        except pymysql.err.IntegrityError:
            pass

    elif x == '5':

        print("Choose the verb that you want to add synonyms to---------------")
        cur.execute("SELECT name FROM verb_group")
        for row in cur:
            print("  -" + row[0])
        print("---------------------------------------------------------------")
        verb = str(input("\n--> "))

        cur.execute("SELECT id FROM verb_group WHERE name = '" + verb + "'")
        id = cur.fetchall()[0][0]

        print("\nSynonyms already added for the verb \"" + verb + "\"----------------- ")
        cur.execute("SELECT verbs FROM verbs WHERE id = '" + str(id) + "'")
        for row in cur:
            print("  -" + row[0])
        print("-----------------------------------------------------\n")

        add = str(input("Add verbs: ")).split(",")
        add = [x.strip(' ') for x in add]

        try:
            for i in add:
                cur.execute("INSERT INTO verbs (id, verbs) VALUES (%d, '%s')" % (id, i))
                conn.commit()
                print("SUCCESS!!\n")
        except:
            conn.rollback()

    elif x == '6':
        print("\nExisting locations----------")
        cur.execute("SELECT location_name FROM location")
        for row in cur:
            print("  -" + row[0])
        cur.execute("SELECT DISTINCT location_id FROM location ORDER BY location_id DESC LIMIT 1")

        id = cur.fetchall()[0][0]
        name = str(input("\nNew location name: "))
        description = str(input("Location description: "))

        try:
            cur.execute("INSERT INTO location VALUES (%d, '%s', '%s')" % (id, name, description))
        except pymysql.err.IntegrityError:
            pass

print("\n\n\nThank you!")


conn.close()













































