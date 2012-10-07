#u'author': u'Irvinn',
# u'comments': u'http://delicious.com/url/90c6b38a375cf62280f9ebc89823f570',
# u'guidislink': False,
# u'id': u'http://delicious.com/url/90c6b38a375cf62280f9ebc89823f570#Irvinn',
# u'link': u'http://snagajob.com/',
# u'links': [{u'href': u'http://snagajob.com/',
#   u'rel': u'alternate',
#   u'type': u'text/html'}],
# u'source': {},
# u'tags': [{u'label': None,
#   u'scheme': u'http://delicious.com/Irvinn/',
#   u'term': u'Jobs'}],
# u'title': u'Jobs & Employment | Full & Part Time Job Search | SnagAJob.com',
# u'title_detail': {u'base': u'http://feeds.delicious.com/v2/rss/recent?min=1&count=100',
#  u'language': None,
#  u'type': u'text/plain',
#  u'value': u'Jobs & Employment | Full & Part Time Job Search | SnagAJob.com'},
# u'updated': u'Fri, 11 Sep 2009 15:07:02 +0000',
# u'wfw_commentrss': u'http://feeds.delicious.com/v2/rss/url/90c6b38a375cf62280f9ebc89823f570'}
#
 
import json
import psycopg2
import sys
import os

def conn_db():
    conn=psycopg2.connect("dbname=deli user=vjust")
    conn.autocommit=True
    return conn

def proc_file (filename):
    input_file=open("/home/vjust/data/deli/inputs/" + filename)   
    error_count=0
    row_count=0
    for ll in input_file.readlines():
        try:
            obj=json.loads(ll)
            author=obj['author']
            link_id=obj['id']
            url=obj['link']
            #type1=obj['type']
            tags=obj['tags']
            title=obj['title']
            #value=obj['value']
            updated=obj['updated']
            #print "author:%s\nlink_id:%s\nurl:%s\ntags:%s\ntitle:%s\nupdated:%s\n" % (author, link_id, url, tags, title,  updated)
            cur.execute("insert into links (author, link_id, url, tags, title) values (%s , %s, %s, %s, %s)", (author, link_id, url, str(tags), title))
            row_count=row_count+1
        except:
            print "~~~~~~~~~~~~~~~~ unexpected error ~~~~~~~~~~~~"
            print obj
            error_count=error_count+1

    print " Total Rows inserted:{0:3d}  Errors:{1:6d}".format(row_count,error_count)


conn=conn_db()
cur=conn.cursor()
for file in os.listdir('../inputs/')[1:2]:
    if file.startswith('delix'):
        proc_file(file)


cur.close()
conn.close()
conn.notices
