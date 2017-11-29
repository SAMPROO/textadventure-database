def line():
    cur=db.cursor()
    sql="SELECT answer.description FROM answer"
    cur.execute(sql)
    result=cur.fetchall()[0]
    for line in result:
        print(line[0])
    choice=input("How do you want to answer? ")
    sql="SELECT answer.next_answer_line_id FROM answer WHERE answer.description='"+choice+"'"
    cur.execute(sql)
    result=cur.fetchall()
    if cur.rowcount>=1:
        sql="SELECT answer.subroutine FROM answer WHERE next_answer_line_id='"+str(result)+"'"
        cur.execute(sql)
        r=cur.fetchall()
        eval(r)()
