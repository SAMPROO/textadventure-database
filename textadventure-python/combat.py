import random
import loc_npc_look
import eat
import time


def combat(conn, location_id, npc):
    x = 1
    cur = conn.cursor()
    print("------------------------")
    sql = "SELECT hp, attack, defence, dodge, luck FROM character_"
    cur.execute(sql)

    for row in cur:
        player_hp = (row[0])
        player_att = (row[1])
        player_def = (row[2])
        player_dodge = (row[3])
        player_luck = (row[4])


    sql2 = "SELECT hp, attack, defence, dodge, luck FROM npc INNER JOIN location ON npc.npc_location_id = location.location_id \
            WHERE location.location_id = '" + str(location_id) + "' AND npc.name = '" + str(npc) + "'"
    cur.execute(sql2)

    if cur.rowcount >= 1:

        for row in cur:
            npc_hp = (row[0])
            npc_att = (row[1])
            npc_def = (row[2])
            npc_dodge = (row[3])
            npc_luck = (row[4])

#----------------------------------------------------------------
        turn = random.randint(1, 5)#Decides whose turn it is with a 60% chance it's players turn
        if turn <= 3:

            player_turn = True
            npc_turn = False

        else:

            player_turn = False
            npc_turn = True
#------------------------------------------------------------------
        while player_hp > 0 and npc_hp > 0:

            sql3 = "SELECT hp FROM character_"
            cur.execute(sql3)
            for row in cur:
                player_hp = (row[0])
            sql4 = "SELECT hp FROM npc INNER JOIN location ON npc.npc_location_id = location.location_id \
                    WHERE location.location_id = '" + str(location_id) + "' AND npc.name = '" + str(npc) + "'"
            cur.execute(sql4)
            for row in cur:
                npc_hp = (row[0])
            print("\n--------------------------\nYou have: " + str(player_hp)+ " hitpoints")
            print("The opponent has: " + str(npc_hp) + " hitpoints\n--------------------------\n")

            if player_turn: #Player turn
                print("It's your turn...")
                command = input("\nAction:\n1) Attack\n2) Defence\n3) Heal\n4) Run\n -->\n ")

                if command == '1' or command == 'attack': #player attacks

                    if random.randint(player_luck, 100) > 80: #Checks if player strikes critically
                        dealt = player_att*2
                        print("Player crit dmg: " + str(dealt))
                    else:
                        dealt = player_att
                        print("Player dmg: " + str(dealt))

                    if random.randint(npc_dodge, 100) > 95: #Checks if npc dodges the attack
                        print("The opponent dodged the attack!")
                    else:
                        if dealt > npc_def:

                            npc_hp = npc_hp + (npc_def - dealt)

                            print("You dealt: " + str(dealt))
                            print("The enemy absorbed: " + str(npc_def) + " damage.")
                            print("The enemy has: " + str(npc_hp) + " HP left!")

                            sql7 = "UPDATE npc SET npc.hp = '" + str(npc_hp) + "' WHERE npc.name = '" + npc + "' "
                            cur.execute(sql7)
                        else:
                            print("Your attack was fully absorbed.")

                elif command == '2' or command == 'defence': #player goes into a defencive formation
                    player_def = player_def + 15
                    player_dodge = player_dodge + 10
                    player_att = player_att - 15
                    player_luck = player_luck - 10
                    print("You raise your defences!")

                elif command == '3' or command == 'heal': #player heals
                    item = None
                    eat.eat(conn, location_id, item)
                    print("You ate, your health is now: " + str(player_hp))

                elif command == '4' or command == 'run': #player runs away
                    location_id = location_id - 1
                    loc_npc_look.get_location(conn, location_id)
                    npc_hp = npc_hp + 100
                    sql9 = "UPDATE npc SET npc.hp = '" + str(npc_hp) + "' WHERE npc.name = '" + npc + "' "
                    cur.execute(sql9)
                    player_hp = player_hp + 100
                    sql10 = "UPDATE character_ SET hp = '" + str(player_hp) +"' WHERE character_id = 1"
                    cur.execute(sql10)
                    break
                else:
                    print("ERROR")

            else: #Npc turn
                print("It's NPC's turn...\n")
                time.sleep(1)

                if npc_hp < 20: #Npc heals
                    print("The opponent heals!")
                    npc_hp = npc_hp + 15

                elif random.randint(1, 5) == 1: # 20% chance that npc goes into a defencive formation
                    while x == 1:
                        npc_dodge = npc_dodge + 10
                        npc_def = npc_def + 15
                        npc_att = npc_att - 15
                        npc_luck = npc_luck - 10
                        print("The opponent goes into a defencive formation!")
                        x = x - 1
                else: #Npc attacks
                    print("The opponent attacks you! ")
                    if random.randint(npc_luck, 100) > 99: #Checks if critical strike hits
                        dealt2 = npc_att*2
                    else:
                        dealt2 = npc_att

                    if random.randint(player_dodge, 100) > 99: #Checks if player dodges the attack
                        print("You dodged the attack!")

                    else:

                        if dealt2 > player_def:
                            player_hp = player_hp + (player_def - dealt2)
                            sql8 = "UPDATE character_ SET hp = '" + str(player_hp) +"'"
                            cur.execute(sql8)
                            print("The enemy dealt: " + str(dealt2) + " damage!")
                            print("You absorbed: " + str(player_def) + " damage.")
                        else:
                            print("You absorbed the attack")

            #print("Player: " + str(player_hp))
            #print("NPC: " + str(npc_hp))
            player_turn = not player_turn
            npc_turn = not npc_turn
        if npc_hp <= 0:
            sql5 = "UPDATE npc SET npc.hp = '" + str(npc_hp) + "' WHERE npc.name = '" + npc + "' "
            cur.execute(sql5)
            sql6 = "UPDATE character_ SET character_.hp = '" + str(player_hp) +"'"
            cur.execute(sql6)
            sql11 ="SELECT location_id FROM location INNER JOIN npc ON location.location_id = npc.npc_location_id"
            cur.execute(sql11)
            row = cur.fetchall()[0]
            print(row[0])
            sql12 = "UPDATE location SET needed_item = NULL, no_item = NULL, yes_item = NULL WHERE location_id = '"+ row[0] + "'"
            cur.execute(sql12)
            sql8 = "UPDATE npc SET npc_location_id = NULL, met_npc = 1 WHERE npc.name= '" + npc + "'"
            cur.execute(sql8)
        elif player_hp <= 0:
            print("You Died")
            loc_npc_look.get_location(conn, location_id - 1)
            npc_hp = npc_hp + 100
            sql9 = "UPDATE npc SET npc.hp = '" + str(npc_hp) + "' WHERE npc.name = '" + npc + "' "
            cur.execute(sql9)
            player_hp = player_hp + 100
            sql10 = "UPDATE character_ SET hp = '" + str(player_hp) + "' WHERE character_id = 1"
            cur.execute(sql10)


    elif npc == None:
        print("Who do you want to attack?")
        npc = input("--> ")
        combat(conn, location_id, npc)
    else:
        print("I can't fight with an " + npc)

    return location_id

