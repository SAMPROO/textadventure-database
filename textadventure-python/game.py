import pymysql
import time
#CONNECTION TO DATABASE------------------------------------------------------------------------------------------------------
conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'sampo', database = 'textadventure-database')
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

    sql2 = "SELECT locnpc_loc_id FROM locnpc WHERE locnpc_loc_id = '" + str(location_id) + "'"
    cur.execute(sql2)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            if location_id == row[0]:
                sql = "SELECT npc.description FROM npc"
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

    sql = "SELECT locnpc_loc_id FROM locnpc WHERE locnpc_loc_id = '" + str(location_id) + "'"
    cur.execute(sql)
    if cur.rowcount >= 1:
        for row in cur.fetchall():
            if location_id == row[0]:
                sql = "SELECT npc.name, npc.description FROM npc"
                cur.execute(sql)
                print("Who would you like to talk to?\n-------------------")
                name_list = []
                for row1 in cur:
                    print(row1[0])
                    name_list.append(row1[0])



                print()
                select_npc = input("--> ")
                if len(select_npc) >= 1:
                    select_npc[0].lower()

                if select_npc in name_list:

                    sql2 = "SELECT npc.name FROM npc WHERE npc.name = '" + select_npc + "'"
                    cur.execute(sql2)


                    sql3 = "SELECT line_id, line FROM line WHERE line_id = 1"
                    sql4 = "SELECT previous_answer_line_id, description FROM answer INNER JOIN line ON answer.previous_answer_line_id = line.line_id WHERE answer.previous_answer_line_id = 1"

                    cur.execute(sql3)

                    for row3 in cur:
                        print(select_npc + ": " + row3[1])

                    print()
                    cur.execute(sql4)
                    #time.sleep(3)
                    i = 0
                    for row4 in cur:
                        i += 1
                        print(str(i) + ": " + row4[1])

                    response = int(input("--> "))
                    sql5 = "SELECT previous_answer_line_id, description, next_answer_line_id FROM answer WHERE previous_answer_line_id = 1"
                    cur.execute(sql5)
                    if cur.rowcount >= 1:
                        row5 = cur.fetchall()
                        if response == 1:
                            next_line = row5[0][2]
                        if response == 2:
                            next_line = row5[1][2]
                    answer(next_line, select_npc)





                            #answer(response, next_line, select_npc)


                else:
                    print("Who?")
                        #if (row[1] != ""):
                         #   print(row3[1])

    else:
        print("There's no one here to talk to")

def answer(next_line, select_npc):
    sql3 = "SELECT line_id, line FROM line WHERE line_id = '" + str(next_line) + "'"
    sql4 = "SELECT previous_answer_line_id, description FROM answer INNER JOIN line ON answer.previous_answer_line_id = line.line_id WHERE answer.previous_answer_line_id = '" + str(next_line) + "'"

    cur.execute(sql3)

    for row3 in cur:
        print(select_npc + ": " + row3[1])

    print()
    cur.execute(sql4)
    # time.sleep(3)
    i = 0
    for row4 in cur:
        i += 1
        print(str(i) + ": " + row4[1])

    response = int(input("--> "))
    sql5 = "SELECT previous_answer_line_id, description, next_answer_line_id FROM answer WHERE previous_answer_line_id = '" + str(next_line) + "'"
    cur.execute(sql5)
    if cur.rowcount >= 1:
        row5 = cur.fetchall()
        if response == 1:
            next_line = row5[0][2]
        if response == 2:
            next_line = row5[1][2]


    while row3[1] is not "1":
        answer(next_line, select_npc)



#COMMAND LIST---------------------------------------------------------------------------------------------------------------
directions = ['n', 's', 'w', 'e', 'u', 'd', 'north', 'south', 'west', 'east', 'up', 'down']
look = ['view', 'look', 'examine', 'inspect']
quit = ['exit', 'quit', 'end', 'finnish']
talk_command = ['talk', 'speak', 'interact']
end_con = ['leave']
bla = ['ä']

all_commands = directions + look + quit + talk_command + end_con + bla

#STARTING VALUES------------------------------------------------------------------------------------------------------------
location_id = 1
look_around(location_id)
action = ""

#MAIN LOOP-----------------------------------------------------------------------------------------------------------------
while action not in quit:

    #ACTION TO LOWERCASE AND ONLY FIRST WORD
    print("")
    input_string = input("--> ").split()
    if len(input_string) >= 1:
        action = input_string[0].lower()
    else:
        action = ""

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

conn.rollback()