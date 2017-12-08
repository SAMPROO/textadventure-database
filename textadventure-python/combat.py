import random

def combat(conn, location_id, npc):
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

        turn = random.randint(1, 5)
        if turn <= 3:

            player_turn = True
            npc_turn = False

        else:

            player_turn = False
            npc_turn = True

        while player_hp > 0 or npc_hp > 0:

            if player_turn:
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

                if command == 2: #player goes into a defencive formation
                    player_def = player_def + 15
                    player_dodge = player_dodge + 10
                    player_att = player_att - 10
                    player_luck = player_luck + 15

                if command == 3: #player heals
                    #tänne heal functio
                    #eli pitää importtaa eat ja iha perustavalla kutsua sitä
                    player_hp = player_hp + 25

                #if command == 4: #player runs away
                    #jotain et kutsut move functiota jossa vaan miinustat nykysestä locatiosta 1
                    #sit sun pitää miettiä miten taistelulle käy jääkö vihun hp samaks vaiko reset jnejne
            else:

                if npc_hp < 20:
                    print("The opponent heals!")
                    npc_hp = npc_hp + 15

                if random.randint(1, 5) == 1: # 20% chance that npc goes into a defencive formation
                    print("The opponent goes into a defencive formation!")
                    npc_dodge = npc_dodge + 10
                    npc_def = npc_def + 15
                    npc_att = npc_att - 5
                    npc_luck = npc_luck - 15
                else:
                    print("The opponent attacks you!")
                    if random.randint(npc_luck, 100) > 90:
                        dealt2 = npc_att*2
                    else:
                        dealt2 = npc_att
                    if random.randint(player_dodge, 100) > 75:
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

