/*
table : enron_email

file_path
email_key_id
message_id
message_date
to_emails
to_ids
subject
keywords
tags
from_email
from_id
email_tags
email_cardinality:1-1,1-n,n-n
trans_type:Iinit, complete
content
thread_size
*/


create table enron_email (
email_key_id serial primary key,
file_path varchar(60) not null,
message_id varchar(128),
message_date varchar(60),
from_email varchar(60),
to_email_csv varchar(1000),
subject varchar(140),
keywords varchar(200),
tags varchar(200),
content varchar(2000)
);