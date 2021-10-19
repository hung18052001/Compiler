import re
comment = re.compile(r'//(.)*\n')
print(comment.fullmatch('//hbshs\n'))