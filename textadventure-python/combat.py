import random

def damage(conn, character, npc):
    #laitoin game.py esimerkki kutsun näille siellä näät sitten mitä arvoja tulee ja mistä tulee erroreita

    #muutin nimet selvennyksen vuoksi
    #se miten määrität kumpi hyökkää eka voi olla vaikka jonkun arvon mukaan esim skill tai damage tai jotain

    #ei tarvitse tehdä for looppia
    #--------------------------
    player_hp = character[0]
    print(character[0])
    print(character[1])
    print(npc)
    #-------------------------
    for row in character:
        player_hp = (row[0])
        player_att = (row[1])
        player_def = (row[2])
        player_dodge = (row[3])
        player_luck = (row[4])
    for row in npc:
        npc_hp = (row[0])
        npc_att = (row[1])
        npc_def = (row[2])
        npc_dodge = (row[3])
        npc_luck = (row[4])

    #sitten sun pitää lisää while loopin sisään vaihtoehdot mitä pelaaja voi tehdä
    #hyökkää puolusta healaa pakene
    #ja jokanen valinta kutsuu sitten omaa functiotaan
    while player_hp > 0 or npc_hp >0: #looppaa vuoroja niin kauan kunnes toinen on kuollut

        if random.randint(player_luck, 100) > 50:
            dealt = player_att*2
        else:
            dealt = player_att

        dmg = npc_hp - (npc_def - dealt)

        if random.randint(npc_dodge, 100) > 50:
            print(npc + "dodged the attack!")
        else:
            #muuta tässä sql sellaseen helpommin luettavaan muotoon
            #en nyt ymmärrä mitä haet tällä sql kyselyllä mutta etköhän sä näillä pääse vauhtiin
            #tänne pitää myös lisää sitten se commit jotta se muuttaa arvoja tietokannassa
            #mitä sitten kun taistelu on käyty tapahtuu?
            sql = "UPDATE '%s' SET hp = '%d' WHERE '%s'.'%s'_id" % (npc, dmg, npc, npc)


    return


def combat(conn, location_id, npc):

    cur = conn.cursor()

    sql = "SELECT hp, attack, defence, dodge, luck FROM character_"
    cur.execute(sql)
    character = cur.fetchall()[0]
    print(character)

    sql2 = "SELECT hp, attack, defence, dodge, luck FROM npc INNER JOIN location ON npc.npc_location_id = location.location_id \
            WHERE location.location_id = '" + str(location_id) + "' AND npc.name = '" + str(npc) + "'"
    #kirjotetaan sql kyselyt tälleen. Mun mielestä paljon helpompi luke kuin sillä %s tavalla
    cur.execute(sql2)
    npc = cur.fetchall()[0]
    print(npc) #hyvä tulostaa aina niin näet millasen tuloksen se antaa. Sitten tiedät mitä pitää korjata

    #tässä pitää kutsua damage functiota
    damage(conn, character, npc)

    return location_id

