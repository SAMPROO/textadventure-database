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

    sql2 = "SELECT npc.npc_id, location.location_id, npc.description FROM npc INNER JOIN location ON npc.npc_location_id = location.location_id WHERE location.location_id = '" + str(location_id) + "'"
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

    sql2 = "SELECT npc_id, name, npc_location_id FROM npc WHERE npc_location_id = '" + str(location_id) + "'"
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
    articles_list = []
    cur.execute(sql_articles)
    articles = cur.fetchall()
    for word in articles:
        articles = word[0]
        articles_list.append(articles)

    sql_verbs = "SELECT verbs FROM verbs"
    verbs_list = []
    cur.execute(sql_verbs)
    verbs = cur.fetchall()
    for word in verbs:
        verb = word[0]
        verbs_list.append(verb)

    print(verbs_list)


    sql_dictionary = "SELECT dictionary FROM dictionary"
    dictionary_list = []
    cur.execute(sql_dictionary)
    dictionary = cur.fetchall()
    for word in dictionary:
        noun = word[0]
        dictionary_list.append(noun)

    sql_prepositions = "SELECT * FROM prepositions"
    cur.execute(sql_prepositions)
    preposition_list = []
    prepositions = cur.fetchall()
    for word in prepositions:
        preposition = word[1]
        preposition_list.append(preposition)

    print(preposition_list)
    verb = None
    preposition = None
    preposition_1 = None
    direct = None
    preposition_2 = None
    indirect = None

    print("")
    input_string = input("--> ").lower().split()

    for word in input_string:

        if word in verbs_list and verb == None:
            sql = "SELECT id FROM verbs WHERE verbs = '" + word + "'"
            print(sql)
            cur.execute(sql)
            for row in cur:
                verb = row[0]
            continue

        if word in dictionary_list and direct == None:
            sql = "SELECT id FROM dictionary WHERE dictionary = '" + word + "'"
            cur.execute(sql)
            for row in cur:
                direct = row[0]
            continue

        if word in preposition_list and preposition == None:
            sql = "SELECT id FROM prepositions WHERE prepositions = '" + word + "'"
            cur.execute(sql)
            for row in cur:
                preposition = row[0]
            continue


        if word in dictionary_list and indirect == None:
            sql = "SELECT id FROM dictionary WHERE dictionary = '" + word + "'"
            cur.execute(sql)
            for row in cur:
                indirect = row[0]
            continue



    order = [verb, direct, preposition, indirect]
    for n, i in enumerate(order):
        if i == None:
            order[n] = 255



    sql_check = "SELECT subroutine FROM jump_table WHERE verb = {0} \
                AND direct_object = {1} AND preposition = {2} AND indirect_object = {3}".format(order[0], order[1], order[2], order[3])
    print(sql_check)
    cur.execute(sql_check)
    cur.fetchall()
    for row in cur:
        test = row[0]
        print(test)

    '''    
    #VERB CHECKER-----------------------
    cur.execute(sql_verbs)
    for row in cur:
        for command in input_string:
            if command in row:
                verb = command
    #----------------------------------
    #NOUN/DICTIONARY CHECKER----------------------
    cur.execute(sql_dictionary)
    for row in cur:
        for command in input_string:
            if command in row:
                direct = command

    #NOUN/DICTIONARY CHECKER----------------------
    cur.execute(sql_prepositions)
    for row in cur:
        for command in input_string:
            if command in row:
                preposition = command

    #NOUN/DICTIONARY CHECKER----------------------
    cur.execute(sql_dictionary)
    for row in cur:
        for command in input_string:
            if command in row:
                indirect = command

    '''

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
        exit()

    #ADD NPC (school)
    if action == "add":
        add()

    #CHANGE NAME WITH HIGHEST ID (school)
    if action == "change":
        change(location_id)
conn.rollback()