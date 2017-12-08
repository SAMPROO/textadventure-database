import databaseconfig as cfg
import pymysql

conn = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['db'], cfg.mysql['port'])
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
        dodge = int(input("Item dodge value: "))
        luck = int(input("Item luck value: "))
        pickable = int(input("Item picable value (1 or 0): "))
        eatable = int(input("Item eatable value (1 or 0): "))
        addhp = int(input("Item addhp value: "))
        location = int(input("Item location: "))
    
        try:
            cur.execute("INSERT INTO item (item_id, item.name, description, inspect, attack, defence, dodge, luck, pickable, eatable, addhp, item_location_id, item_character_id) \
                                VALUES (NULL, '%s', '%s', '%s', %d, %d, %d, %d, %d, %d, %d, %d, NULL)" % (name, description, inspect, attack, defence, dodge, luck, pickable, eatable, addhp, location))
            conn.commit()
            print("SUCCES!!")
        except:
            conn.rollback()
            print("Something went wrong...")

        cur.execute("SELECT DISTINCT id FROM dictionary_group ORDER BY id DESC LIMIT 1 OFFSET 2")
        id = cur.fetchall()[0][0] + 1

        try:
            cur.execute("INSERT INTO dictionary_group (id, dictionary_group.name) VALUES (%d, '%s')" % (id, name))
            cur.execute("INSERT INTO dictionary (id, dictionary) VALUES (%d, '%s')" % (id, name))
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
        cur.execute("SELECT DISTINCT id FROM verb_group ORDER BY id DESC LIMIT 1 OFFSET 1")
        id = cur.fetchall()[0][0] + 1
        name = str(input("\nVerb name: "))

        try:
            cur.execute("INSERT INTO verb_group VALUES (%d, '%s')" % (id, name))
            cur.execute("INSERT INTO verbs VALUES (%d, '%s')" % (id, name))
            conn.commit()
            print("SUCCESS!")
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

    elif x == '7':
        cur.execute("SELECT id FROM verb_group")

        row = cur.fetchall()

        get = row[0][0]
        talk = row[2][0]
        drop = row[4][0]
        eat = row[5][0]
        attack = row[6][0]
        inspect = row[7][0]
        nothing = row[8][0]

        noun_list = []

        cur.execute("SELECT id FROM dictionary_group")

        for row in cur:
            noun_list.append(row[0])

        for word in noun_list:
            try:
                # GET
                cur.execute("INSERT INTO jump_table VALUES (%d, %d, %d, %d, '%s')" % (get, word, nothing, nothing, 'pick.pickup(conn, location_id, direct_str)'))
                cur.execute("INSERT INTO jump_table VALUES (%d, %d, %d, %d, '%s')" % (get, 4, nothing, word, 'pick.pickup(conn, location_id, indirect_str)'))
                conn.commit()
                print("SUCCESS!")
            except pymysql.err.IntegrityError:
                pass
            try:
                #EAT
                cur.execute("INSERT INTO jump_table VALUES (%d, %d, %d, %d, '%s')" % (eat, word, nothing, nothing, 'eat.eat(conn, location_id, direct_str)'))
                conn.commit()
                print("SUCCESS!")
            except pymysql.err.IntegrityError:
                pass
            try:
                #DROP
                cur.execute("INSERT INTO jump_table VALUES (%d, %d, %d, %d, '%s')" % (drop, word, nothing, nothing, 'drop.drop(conn, location_id, direct_str)'))
                conn.commit()
                print("SUCCESS!")
            except pymysql.err.IntegrityError:
                pass
            try:
                #TALK
                cur.execute("INSERT INTO jump_table VALUES (%d, %d, %d, %d, '%s')" % (talk, word, nothing, nothing, 'talk_answer.answer(conn, location_id, direct_str, 0)'))
                cur.execute("INSERT INTO jump_table VALUES (%d, %d, %d, %d, '%s')" % (talk, word, 5, nothing, 'talk_answer.answer(conn, location_id, direct_str, 0)'))
                conn.commit()
                print("SUCCESS!")
            except pymysql.err.IntegrityError:
                pass
            try:
                #COMBAT
                cur.execute("INSERT INTO jump_table VALUES (%d, %d, %d, %d, '%s')" % (attack, word, nothing, nothing, 'combat.combat(conn, location_id, direct_str)'))
                conn.commit()
                print("SUCCESS!")
            except pymysql.err.IntegrityError:
                pass
            try:
                #INSPECT
                cur.execute("INSERT INTO jump_table VALUES (%d, %d, %d, %d, '%s')" % (inspect, word, nothing, nothing, 'loc_npc_look.inspect(conn, location_id, direct_str)'))
                conn.commit()
                print("SUCCESS!")
            except pymysql.err.IntegrityError:
                pass




print("\n\n\nThank you!")


conn.close()













































