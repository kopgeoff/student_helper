import psycopg2


try:
    conn = psycopg2.connect(database="classplandb", user="simple", password="123456", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    try:
        cur.execute("select * from users where id='%s'" % "123456")
        conn.commit()
        if len(cur.fetchall()) == 0:
            cur.execute("insert into users(id,password) values('%s','%s')" % ("123456", "123456123456"))
            conn.commit()
        else:
            cur.execute("update users set password = '%s' where id = '%s'" % ("12345612345", "123456"))
            conn.commit()
        cur.execute("select * from users where id='%s'" % "123456")
        conn.commit()
        s = cur.fetchall()
        print(s)
    except Exception as e:
        print(e)
    finally:
        conn.close()
except Exception as e:
    print(e)

# 如果不需要数据库，请忽略此文件，并建议使用sqlite
