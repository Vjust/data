#!/usr/bin/python
import os
import os.path
import pprint
import sys
import glob
import psycopg2
import re

def dbquote(s):
    return "\"" + re.escape(s) + "\""

def conn_db():
    conn=psycopg2.connect("dbname=netflix user=<user-id>")
    #cur1=conn.cursor()
    #cur1.execute ("insert into enron_email values ('a', 'a', 'a', 'a', 'a', 'a')")
    #dd=cur1.fetchall()
    #cur1.close()
    #conn.commit()
    conn.autocommit=True
    return conn


conn=conn_db()
cur=conn.cursor()

def proc_email_files(dir, pattern):
    print "hi"
    tdir=dir +"/*"
    for username in glob.glob(tdir):
        print "username : " , username
        for emailfile in glob.glob(username + '/*/*'):
            folder=os.path.basename(os.path.dirname(emailfile))
            proc_file (username, folder, emailfile)
            #print 'Username : %s Emal sent  # :%s' % (os.path.basename(username), os.path.basename(emailfile))
            #print os.path.basename(username)
            #for emailfile in glob.glob(username + '/deleted_items/*'):
            #proc_file (username, "deleted_item", emailfile)
            #print 'Username : %s Emal sent  # :%s' % (os.path.basename(username), os.path.basename(emailfile))
            #print os.path.basename(username)
            #for emailfile in glob.glob(username + '/inbox/*'):
            #proc_file(username, "inbox", emailfile)
            #print 'Username : %s Emal recd # :%s' % (os.path.basename(username), os.path.basename(emailfile))



# each email file contains one email, hence one DB record-insert per file
def proc_file (username, folder, filename):
    if not os.path.isfile(filename):
        return
    print "in Proc-file %s %s" % (folder, filename)
    basename=filename
    input_file=open(filename)
    error_count=0
    row_count=0
    email_lines=input_file.readlines()
    #print "line count %d" % len(email_lines)

    parse_msgId = emailfile_get_msgid(email_lines[0])
    parse_date = emailfile_get_date(email_lines[1])
    parse_from = emailfile_get_from(email_lines[2])
    parse_to = emailfile_get_to(email_lines[3])
    parse_subject = emailfile_get_subject(email_lines[4])
    parse_body = "".join (email_lines[5:])
    #print "".join(email_lines[5:])

    #print " msgId {1} from {3} to {4} subject {5} username {6}".format(filename, parse_msgId, parse_date, parse_from, parse_to, parse_subject, filename)
    try:
        cur.execute("insert into enron_email_text (user_id, email_type, email_number, email_text, email_from, email_to) values ('%s' , '%s', '%s', E'%s' ,'%s', '%s')" % (os.path.basename(username), folder, os.path.basename(basename), "\"" + re.escape(parse_body) + "\"", parse_from, parse_to))
        #row_count=row_count+1
    except psycopg2.Error as e:
        print e.pgerror
        #error_count=error_count+1

    #print " File: {2} Total Rows inserted:{0:3d}  Errors:{1:6d}".format(row_count,error_count,filename)


def emailfile_get_msgid(line):
    restring=r"^(Message-ID)\W*(\<)(.*)(\>)(.*$)"
    t2=re.match(restring, line)
    if t2 == None :
        return ""
    return t2.groups()[2].strip()

def emailfile_get_date(line):
    restring=r"^(Date:)\W*(.*$)"
    t2=re.match(restring, line)
    if t2 == None :
        return ""
    return t2.groups()[1].strip()

def emailfile_get_from(line):
    restring=r"^(From:)\W*(.*$)"
    t2=re.match(restring, line)
    if t2 == None :
        return ""
    return t2.groups()[1].strip()

def emailfile_get_to(line):
    restring=r"^(To:)\W*(.*$)"
    t2=re.match(restring, line)
    if t2 == None :
        return ""
    return t2.groups()[1].strip()

def emailfile_get_subject(line):
    restring=r"^(Subject:)\W*(.*$)"
    t2=re.match(restring, line)
    if t2 == None :
        return ""
    return t2.groups()[1].strip()




start_dir=sys.argv[1]
pattern=sys.argv[2]
#os.path.walk (start_dir, visit, pattern)
proc_email_files (start_dir, pattern)


cur.close()
conn.commit()
conn.close()
conn.notices