def damage(conn, attacker, defender):
    for row in attacker:
        player_hp = (row[0])
        player_att = (row[1])
        player_def = (row[2])
        player_dodge = (row[3])
        player_luck = (row[4])
    for row in defender:
        npc_hp = (row[0])
        npc_att = (row[1])
        npc_def = (row[2])
        npc_dodge = (row[3])
        npc_luck = (row[4])
    while player_hp > 0 or npc_hp >0:

        if random.randint(att_luck, 100) > 50:
            dealt = att_att*2
        else:
            dealt = att_att

        dmg = def_hp - (def_def - dealt)

        if random.randint(def_dodge, 100) > 50:
            print(defender + "dodged the attack!")
        else:
            sql = "UPDATE '%s' SET hp = '%d' WHERE '%s'.'%s'_id" % (defender, dmg, defender, defender)
    return


def combat(conn, location_id, npc):
    sql = "SELECT hp, attack, defence, dodge, luck FROM character_"
    cur.execute(sql)
    attacker = cur.fechall()
    sql2 = "SELECT hp, attack, defence, dodge, luck FROM npc INNER JOIN location ON npc.npc_location_id = location.location_id WHERE location.location_id = '%d' AND npc.name = '+npc+'" % \
    (location_id)
    cur.execute(sql2)
    defender = cur.fetchall()

    return location_id
