import psycopg2


try:
    conn = psycopg2.connect(database="classplandb", user="simple", password="123456", host="127.0.0.1", port="3389")
    cur = conn.cursor()
    try:
        cur.execute("select * from users where id='%s'" % "20174529")
        conn.commit()
        if len(cur.fetchall()) == 0:
            cur.execute("insert into users(id,password) values('%s','%s')" % ("20174529", "woming123456"))
            conn.commit()
        else:
            cur.execute("update users set password = '%s' where id = '%s'" % ("woming12345", "20174529"))
            conn.commit()
        cur.execute("select * from users where id='%s'" % "20174529")
        conn.commit()
        s = cur.fetchall()
        print(s)
    except Exception as e:
        print(e)
    finally:
        conn.close()
except Exception as e:
    print(e)
