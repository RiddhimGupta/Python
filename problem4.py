#!usr/bin/python3
import os
import crypt
uname=raw_input()
count=0
for i in uname:
        if i.isdigit():
                count=1
if count == 0 :
        upass="hello"+uname
        uenc = crypt.crypt(upass,"22")
        os.system("useradd -m -p" +uenc +" "+uname)
