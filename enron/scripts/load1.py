# coding: utf-8


in_lines = open("testfile").readlines()
#pos_message_id, pos_date, pos_from, pos_to, pos_subject=0,1,2,3,4
pos_message_id, pos_date, pos_from, pos_to, pos_subject="Message-ID:", "Date:", "From:", "To:", "Subject:"
        
def proc_line (pos_string, line):
    if line.startswith(pos_string):
        return line.replace(pos_string)

for li in in_lines[:10]:
    if li.startswith(pos_message_id):
        print proc_line(pos_message_id, li)
        
