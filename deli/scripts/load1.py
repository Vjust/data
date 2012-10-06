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
#--
#--create table links (
#--	id serial primary key,
#--	author varchar(40),
#--	link_id varchar(200),
#--	url varchar(200),
#--	type varchar(40),
#--	tags varchar(100),
#--	title varchar(200),
#--	value varchar(100),
#--	updated date);
#


import json
import psycopg2

file=open("/home/vjust/data/inputs/testfile")
lines=file.readlines()
file.close()



conn=psycopg2.connect("dbname=deli user=vjust")
conn.autocommit=True
cur=conn.cursor()

for ll in lines[:10]:
	obj=json.loads(ll)
	author=obj['author']
	link_id=obj['id']
	url=obj['link']
	#type1=obj['type']
	tags=obj['tags']
	title=obj['title']
	#value=obj['value']
	updated=obj['updated']
	print "author:%s\nlink_id:%s\nurl:%s\ntags:%s\ntitle:%s\nupdated:%s\n" % (author, link_id, url, tags, title,  updated)
    #cur.execute("insert into links (author, link_id, url, tags, title) values 
conn.close()
conn.notices
