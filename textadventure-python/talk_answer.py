import loc_npc_look
import time
import combat

#TALK TO AN NPC-------------------------------------------------------------------------------------------------------------------
def talk(conn,location_id):
    cur = conn.cursor()

    sql2 = "SELECT npc_id, npc_location_id FROM npc WHERE npc_location_id = '" + str(location_id) + "'"
    cur.execute(sql2)
    if cur.rowcount >= 1:
        print("Who would you like to talk to?\n-------------------")
        name_list = [] #NPC NAME LIST THAT ARE IN THE ROOM
        for row in cur.fetchall():
            if location_id == row[1]:

                npc_id = row[0]
                sql = "SELECT name FROM npc WHERE npc_id = '" + str(npc_id) + "'"
                cur.execute(sql)

                for row1 in cur:
                    name_list.append(row1[0])
                    name_list.append(row1[0].lower())
                    print(row1[0])
        print()
        select_npc = ""
        while select_npc not in name_list:

                        select_npc = input("--> ") #INPUT WHO TO TALK TO
                        if len(select_npc) >= 1:
                            select_npc[0].lower()
                        if select_npc in name_list:

                                answer(conn, location_id, select_npc, 0)

                        elif select_npc == "3":
                            loc_npc_look.look_around(conn, location_id)
                            break
                        else:
                            print("\nWho?\n3) Leave\n")
    else:
        print("There's no one here to talk to")
    return location_id


def answer(conn, location_id, select_npc, next_line):
    #ENDS CONVO WHEN LAST LINE = "0"
    #-------------------
    cur = conn.cursor()
    sql_id = "SELECT npc_id FROM npc WHERE name = '" + str(select_npc) + "'"
    cur.execute(sql_id)
    if cur.rowcount >= 1:
        id = cur.fetchall()[0][0]
        sql_end = "SELECT line_id, met_npc FROM npc INNER JOIN line ON npc.npc_id = line.line_npc_id WHERE line = '0' AND npc.npc_id = '" + str(id) + "'"
        cur.execute(sql_end)
        for row in cur.fetchall():
            if row[0] is not next_line and row[1] is 0:
        #---------------------
                if next_line == 0:
                    sql3 = "SELECT MIN(line_id), line, line_subroutine FROM line INNER JOIN npc ON line.line_npc_id = npc.npc_id WHERE npc.name = '" + select_npc + "'"
                    sql4 = "SELECT previous_answer_line_id, description, next_answer_line_id FROM answer WHERE answer.previous_answer_line_id = (SELECT MIN(line_id) FROM line)"
                else:
                    sql3 = "SELECT line, line_subroutine FROM line INNER JOIN npc ON line.line_npc_id = npc.npc_id WHERE npc.npc_id = '" + str(id) + "' AND line_id = '" + str(next_line) + "'"
                    sql4 = "SELECT previous_answer_line_id, description, next_answer_line_id FROM answer WHERE answer.previous_answer_line_id = '" + str(next_line) + "'"
                cur.execute(sql3)
                for row3 in cur:
                    if row3[2] is None:
                        if row3[1] is not "0":
                            print(select_npc.upper() + ": " + row3[1])
                            print()
                            cur.execute(sql4)
                            i = 0
                            for row4 in cur:
                                i += 1
                                print(str(i) + ": " + str(row4[1]))
                            print()
                            while True:
                                try:
                                    response = int(input("--> "))
                                    break
                                except ValueError:
                                    print("--> Sorry I'm a bit tired.. What I meant to say was: ")

                            if response == 1:
                                sql5 = "SELECT next_answer_line_id, answer_subroutine FROM answer WHERE previous_answer_line_id = '" + str(row4[0]) + "'"
                                cur.execute(sql5)
                                if cur.rowcount >= 1:
                                    row5 = cur.fetchall()
                                    if row5[0][1] is None:
                                        next_line = row5[0][0]

                                        answer(conn, location_id, select_npc, next_line)
                                    else:
                                        sql2 = "UPDATE npc SET met_npc = TRUE WHERE npc_id = '" + str(row3[0]) + "'"
                                        cur.execute(sql2)
                                        location_id = eval(combat.combat(conn, location_id, select_npc))

                            elif response == 2:
                                sql5 = "SELECT next_answer_line_id, answer_subroutine FROM answer WHERE previous_answer_line_id = '" + str(row4[0]) + "'"
                                cur.execute(sql5)
                                if cur.rowcount >= 1:
                                    row5 = cur.fetchall()
                                    if row5[1][1] is None:
                                        next_line = row5[1][0]

                                        answer(conn, location_id, select_npc, next_line)
                                    else:
                                        sql2 = "UPDATE npc SET met_npc = TRUE WHERE npc_id = '" + str(row3[0]) + "'"
                                        cur.execute(sql2)
                                        location_id = eval(combat.combat(conn, location_id, select_npc))
                    else:
                        print(row3[0])
                        time.sleep(1.5)
                        sql2 = "UPDATE npc SET met_npc = TRUE WHERE npc_id = '" + str(row3[0]) + "'"
                        cur.execute(sql2)

                        location_id = eval(combat.combat(conn, location_id, select_npc))
            else:
                sql_met = "UPDATE npc SET met_npc = met_npc + 1 WHERE npc_id = '" + str(id) + "'"
                cur.execute(sql_met)
                print(str(select_npc.upper()) + ": I got nothing to say to you anymore..")
                time.sleep(1)
                print()
                print()
                loc_npc_look.look_around(conn, location_id)

    else:
        print("Why em I trying to talk to an " + select_npc)


