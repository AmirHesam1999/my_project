#!/bin/python3
s = input("set proxy : ")
str = ""
i = s.rfind("server")
# get ip from s
if i > -1:
    i = i + len("server") + 1
    for j in s[i:]:
        if j != "&":
            str = str + j
        else:
            print("ip : " + str)
            break
# get port from s
str = ""
i = s.rfind("port")
if i > -1:
    i = i + len("port") + 1
    for j in s[i:]:
        if j != "&":
            str = str + j
        else:
            print("port : " + str)
            break
#get secret from s
i = s.rfind("secret")
if i > -1:
    i = i + len("secret") + 1
    print("secret : " + s[i:])
    
        