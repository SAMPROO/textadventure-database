def damage(conn, attacker, defender):
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
    sql = "SELECT attack, luck FROM character_"
    cur.execute(sql)
    result = cur.fechall()
    for row in result:
        att_att = (row[0])
        att_luck = (row[1])
    sql2 = "SELECT hp, defence, dodge,  FROM npc INNER JOIN location ON npc.npc_location_id = location.location_id WHERE location.location_id = '%d' AND npc.name = '+npc+'" % \
    (location_id)
    cur.execute(sql2)
    result2 = cur.fetchall()
    for row in result2:
        def_hp = (row[0])
        def_def = (row[1])
        def_dodge = (row[2])
    return att_att, att_luck, def_def, def_dodge, def_hp, location_id
