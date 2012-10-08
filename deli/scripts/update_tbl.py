import json
import psycopg2
import sys
import os

def conn_db():
    conn=psycopg2.connect("dbname=deli user=vjust")
    conn.autocommit=True
    return conn

def do_update():
            cur.execute("select id, tags from links where tag_list is null limit 5;")
            # we get a list of tuples
            for recs in cur:
                # in each tuple
                id=recs[0]
                tags_str=recs[1]
                tags_list=eval(tags_str)  # a list of dicts
                taglist_str=""
                for i in tags_list:
                    a_tag=i['term']
                    taglist_str=taglist_str + a_tag
                cur2.execute ("update links set tag_list = %s where id = %d", taglist_str, id)
        except:
            #print "~~~~~~~~~~~~~~~~ unexpected error ~~~~~~~~~~~~"
            #print obj
            error_count=error_count+1


conn=conn_db()
cur=conn.cursor()
cur2=conn.cursor()
do_update()

cur.close()
cur2.close()
conn.close()
conn.notices
