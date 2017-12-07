import pymysql
import databaseconfig as cfg
import loc_npc_look
import talk_answer
import inventory
import pick
import drop
import combat

#CONNECTION TO DATABASE------------------------------------------------------------------------------------------------------
conn = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['db'], cfg.mysql['port'])
cur = conn.cursor()

quit = ['exit', 'quit', 'end', 'finnish']

#STARTING VALUES------------------------------------------------------------------------------------------------------------
location_id = 1
loc_npc_look.look_around(conn, location_id)
action = ""


combat.combat(conn, 1, 'figure')

combat(conn, 1, 'figure')
#MAIN LOOP-----------------------------------------------------------------------------------------------------------------
#TEMPORARY LOOP
while action not in quit:



    #PARSER--------------------------------------------------------------------
    #TAKING THE WORDS FROM ALL THE WORD LISTS AND PUTTING THEM IN NEW LISTS
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

    verb = None
    preposition = None
    direct = None
    indirect = None
    direct_str = None

    print("")
    input_string = input("--> ").lower().split()

    #CHECKING IF GIVEN INPUT WORDS ARE IN THE LISTS
    #IF WORD IN LISTS CHANGE IT TO THE WORDS ID AND ADD IT TO ORDER LIST
    for word in input_string:

        if word in verbs_list and verb == None:
            sql = "SELECT id FROM verbs WHERE verbs = '" + word + "'"
            cur.execute(sql)
            for row in cur:
                verb = row[0]
            continue

        if word in dictionary_list and direct == None:
            direct_str = word
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
            indirect_str = word
            sql = "SELECT id FROM dictionary WHERE dictionary = '" + word + "'"
            cur.execute(sql)
            for row in cur:
                indirect = row[0]
            continue

    order = [verb, direct, preposition, indirect]

    #CHANGE None VALUES TO 255
    for n, i in enumerate(order):
        if i == None:
            order[n] = 255
    print(order)

    #CHECKING IF GIVEN WORD ORDER HAS A SUBROUTINE IN THE DATABASE
    sql_check = "SELECT subroutine FROM jump_table WHERE verb = {0} \
                AND direct_object = {1} AND preposition = {2} AND indirect_object = {3}".format(order[0], order[1], order[2], order[3])
    cur.execute(sql_check)
    for row in cur:
        subroutine = row[0]

    #RUNS THE FUNCTION
    try:
        location_id = eval(subroutine)
    except NameError:
        print("I don't understand")
        pass

conn.rollback()