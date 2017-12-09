import random
import move

def combat(conn, location_id, npc, direction):
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

        turn = random.randint(1, 5)#Decides whose turn it is with a 60% chance it's players turn
        if turn <= 3:

            player_turn = True
            npc_turn = False

        else:

            player_turn = False
            npc_turn = True

        while player_hp > 0 or npc_hp > 0:

            if player_turn: #Player turn
                command = input("\nAction:\n1) Attack\n2) Defencive formation\n3) Heal\n4) Run")

                if command == 1: #player attacks

                    if random.randint(player_luck, 100) > 80: #Checks if player strikes critically
                        dealt = player_att*2
                    else:
                        dealt = player_att

                    if random.randint(npc_dodge, 100) > 85: #Checks if npc dodges the attack
                        print("The opponent dodged the attack!")
                    else:
                        npc_hp = npc_hp - (npc_def - dealt)
                        print("You dealt: " + dealt)
                        print("The enemy has: " + npc_hp + " HP left!")

                if command == 2: #player goes into a defencive formation
                    player_def = player_def + 15
                    player_dodge = player_dodge + 10
                    player_att = player_att - 15
                    player_luck = player_luck - 10
                    print("You raise your defences!")

                if command == 3: #player heals
                    #eat(conn, location_id, item)
                    player_hp = player_hp + 25
                    print("You healed for 25 HP, your health is now: " + player_hp)

                if command == 4: #player runs away
                    move(conn, (location_id - 1), direction)

            else: #Npc turn

                if npc_hp < 20: #Npc heals
                    print("The opponent heals!")
                    npc_hp = npc_hp + 15

                if random.randint(1, 5) == 1: # 20% chance that npc goes into a defencive formation
                    print("The opponent goes into a defencive formation!")
                    npc_dodge = npc_dodge + 1
                    npc_def = npc_def + 3
                    npc_att = npc_att - 2
                    npc_luck = npc_luck - 2
                else: #Npc attacks
                    print("The opponent attacks you!")
                    if random.randint(npc_luck, 100) > 90: #Checks if critical strike hits
                        dealt2 = npc_att*2
                    else:
                        dealt2 = npc_att
                    if random.randint(player_dodge, 100) > 75: #Checks if player dodges the attack
                        print("You dodged the attack!")
                    else:
                        player_hp = player_hp - (player_def - dealt2)

            player_turn = not player_turn
            npc_turn = not npc_turn
        sql3 = "UPDATE npc SET npc.hp = '" + npc_hp + "'  WHERE location.location_id = '" + str(location_id) + "' AND npc.name = '" + str(npc) + "'"
        cur.execute(sql3)
        #conn.commit()?
    else:
        print("I can't fight with an " + npc)

    return location_id


