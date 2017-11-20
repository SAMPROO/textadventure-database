import pymysql
import time
import databaseconfig as cfg
#CONNECTION TO DATABASE------------------------------------------------------------------------------------------------------
conn = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['db'])
cur = conn.cursor()


#GETTING LOCATION AFTER MOVEMENT----------------------------------------------------------------------------------------------
def get_location(location_id):
    cur = conn.cursor()
    sql = "SELECT location_name, description FROM location WHERE location_id='" + str(location_id) + "'"
    cur.execute(sql)
    for row in cur:
        print (row[0])
        if (row[1] != ""):
            print(row[1])

    print_npc(location_id)

    return location_id

#PRINT NPC------------------------------------------------------------------------------------------------------------------
def print_npc(location_id):

    sql2 = "SELECT locnpc.locnpc_npc_id, locnpc.locnpc_loc_id, npc.description FROM locnpc INNER JOIN npc ON locnpc.locnpc_npc_id = npc.npc_id WHERE locnpc.locnpc_loc_id = '" + str(location_id) + "'"
    cur.execute(sql2)
    for row in cur.fetchall():
        if cur.rowcount >= 1:
            if location_id == row[1]:
                npc = row[0]
                sql = "SELECT npc.description FROM npc WHERE npc_id = '"+ str(npc) +"'"
                cur.execute(sql)
                for row in cur:
                    print(row[0])

#LOOK WITHIN A LOCATION-------------------------------------------------------------------------------------------------------
def look_around(location_id):
    print("-"*80)
    get_location(location_id)
    return

#MOVE BETWEEN LOCATIONS--------------------------------------------------------------------------------------------------------
def move(location_id, direction):
    cur = conn.cursor()

    sql2 = "SELECT direction FROM direction WHERE direction_id='" + direction + "'"

    cur.execute(sql2)
    if cur.rowcount >= 1:
        result2 = cur.fetchall()
        direction = result2[0][0]

    sql = "SELECT from_location_id, to_location_id, neighbour_direction_id FROM neighbours INNER JOIN  \
          direction ON neighbours.neighbour_direction_id = direction_id WHERE \
          direction.direction_id ='" + direction + "' OR direction.direction = '" + direction + "' AND \
          from_location_id = '" + str(location_id) + "'"


    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            location_id = row[1]
            get_location(location_id)
    else:
        print("You cant go that way")
    return location_id

#TALK TO AN NPC-------------------------------------------------------------------------------------------------------------------
def talk(location_id):
    cur = conn.cursor()

    sql2 = "SELECT npc.npc_id, npc.name, locnpc.locnpc_loc_id FROM npc INNER JOIN locnpc ON npc.npc_id = locnpc.locnpc_npc_id WHERE locnpc.locnpc_loc_id = '" + str(location_id) + "'"
    cur.execute(sql2)
    if cur.rowcount >= 1:
        print("Who would you like to talk to?\n-------------------")
        name_list = []
        for row in cur.fetchall():
            if location_id == row[2]:

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

                        select_npc = input("--> ")
                        if len(select_npc) >= 1:
                            select_npc[0].lower()
                        if select_npc in name_list:

                                sql2 = "SELECT npc.name, npc.npc_id FROM npc WHERE npc.name = '" + str(select_npc) + "'"
                                cur.execute(sql2)
                                for row in cur:
                                    id = row[1]

                                answer(select_npc, id, 0)
                        elif select_npc == "3":
                            look_around(location_id)
                            break
                        else:
                            print("\nWho?\n3) Leave\n")
    else:
        print("There's no one here to talk to")


def answer(select_npc, id, next_line):
    #ENDS CONVO WHEN LAST LINE = "0"
    #-------------------
    sql_end = "SELECT line_id, met_npc FROM npc INNER JOIN line ON npc.npc_id = line.line_npc_id WHERE line = '0' AND npc.npc_id = '" + str(id) + "'"
    cur.execute(sql_end)
    for row in cur.fetchall():
        if row[0] is not next_line and row[1] is 0:
    #---------------------
            if next_line == 0:
                sql3 = "SELECT line_id, line, line_npc_id FROM line INNER JOIN npc ON line.line_npc_id = npc.npc_id = '" + str(id) + "' AND line_id = 1"
                sql4 = "SELECT previous_answer_line_id, description, next_answer_line_id FROM answer WHERE answer.previous_answer_line_id = 1"
            else:
                sql3 = "SELECT line_id, line, line_npc_id FROM line INNER JOIN npc ON line.line_npc_id = npc.npc_id = '" + str(id) + "' AND line_id = '" + str(next_line) + "'"
                sql4 = "SELECT previous_answer_line_id, description, next_answer_line_id FROM answer WHERE answer.previous_answer_line_id = '" + str(next_line) + "'"
            cur.execute(sql3)
            for row3 in cur:
                    if row3[1] is not "0":
                        print(select_npc.upper() + ": " + row3[1])
                        print()
                        cur.execute(sql4)
                        # time.sleep(3)
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
                                sql5 = "SELECT next_answer_line_id FROM answer WHERE previous_answer_line_id = '" + str(row4[0]) + "'"
                                cur.execute(sql5)
                                if cur.rowcount >= 1:
                                    row5 = cur.fetchall()
                                    next_line = row5[0][0]

                                answer(select_npc, id, next_line)
                        elif response == 2:
                            sql5 = "SELECT next_answer_line_id FROM answer WHERE previous_answer_line_id = '" + str(row4[0]) + "'"
                            cur.execute(sql5)
                            if cur.rowcount >= 1:
                                row5 = cur.fetchall()
                                next_line = row5[1][0]

                            answer(select_npc, id, next_line)
        else:
            sql_met = "UPDATE npc SET met_npc = met_npc + 1 WHERE npc_id = '" + str(id) + "'"
            cur.execute(sql_met)
            print(str(select_npc.upper()) + ": I got nothing to say to you anymore..")
            time.sleep(2)
            look_around(location_id)

def add():
    cur = conn.cursor()
    id = 5
    name = str(input("NAME: "))
    des = str(input("DESCRIPTION: "))
    hp = int(input("HP: "))
    loc = int(input("LOCATION (1 - 5): "))

    sql = "INSERT INTO npc VALUES('%d', '%s', '%s', '%d', 0, 1)" % \
            (id, name, des , hp)
    cur.execute(sql)
    sql = "INSERT INTO locnpc VALUE ('%d', '%d')" % \
          (id, loc)
    cur.execute(sql)
    id = id + 1

    #conn.commit()
def change():
    cur = conn.cursor()
    print_npc(location_id)
    name = str(input("CHANGE NAME WITH OF THE HIGHEST ID NPC TO: "))
    sql = "UPDATE npc SET name = '%s' WHERE npc_id = (SELECT MAX(npc_id))" % \
          (name)
    cur.execute(sql)
    #conn.commit()


#COMMAND LIST---------------------------------------------------------------------------------------------------------------
directions = ['n', 's', 'w', 'e', 'u', 'd', 'north', 'south', 'west', 'east', 'up', 'down']
look = ['view', 'look', 'examine', 'inspect']
quit = ['exit', 'quit', 'end', 'finnish']
talk_command = ['talk', 'speak', 'interact']
end_con = ['leave']
bla = ['ä', 'add', 'change']

all_commands = directions + look + quit + talk_command + end_con + bla

#STARTING VALUES------------------------------------------------------------------------------------------------------------
location_id = 1
look_around(location_id)
action = ""

#MAIN LOOP-----------------------------------------------------------------------------------------------------------------
while action not in quit:

    #ACTION TO LOWERCASE AND ONLY FIRST WORD
    #PARSER--------------------------------------------------------------------
    sql_articles = "SELECT * FROM articles"
    sql_verbs = "SELECT * FROM verbs"
    sql_dictionary = "SELECT * FROM dictionary"

    verb = None
    noun = None
    print("")
    input_string = input("--> ").split()

    #VERB CHECJER-----------------------
    cur.execute(sql_verbs)
    for row in cur:
        for command in input_string:
            if command in row:
                verb = command
    #----------------------------------
    #NOUN CHECKER----------------------
    cur.execute(sql_dictionary)
    for row in cur:
        for command in input_string:
            if command in row:
                noun = command

    order = [verb, noun]

    if len(input_string) >= 1:
        action = input_string[0].lower()
    else:
        action = ""
    #---------------------------------------------------------------------------
    if action in quit:
        print("Are you sure you want to quit? Y/N")
        answer = input("")
        if answer is "y":
            break
        else:
            look_around(location_id)
            action = "ä"

    #COMMAND NOT REGOGNIZED
    if action not in all_commands:
        print("I don't undestand")

    #LOOK AROUND
    if action in look:
        look_around(location_id);

    #MOVE AROUND
    if action in directions:
        #direction(action)
        newLocatin = move(location_id, action)
        location_id = newLocatin

    #INTERACTION
    if action in talk_command:
        talk(location_id)

    #END GAME
    if location_id is 5:
        print("Game over")

    #ADD NPC (school)
    if action == "add":
        add()

    #CHANGE NAME WITH HIGHEST ID (school)
    if action == "change":
        change()
conn.rollback()