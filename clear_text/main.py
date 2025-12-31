#!/bin/python3
# get value for edit inner text 
import os

s = input("Is commit (y/n): ")
name = ""
if s == "y":
    name = input("Enter name: ")
    
    name = name.replace('"', "'")

    print("--------------------------")
    print(name)
    os.system('echo "' +name+'"'+" | xclip -selection clipboard")
    
elif s == "n":
    name = input("Enter name: ")

    # replace value " " to "_"
    name = name.replace(" ", "_")

    name = name.replace("/", "_or_")

    # if text has "|" before "|" add "\"
    i = 0
    i = name .rfind("|")
    if i != -1:
        name = name[:i]+ '\\' + name[i:] 

    i = 0
    i = name .rfind("(")
    if i != -1:
        name = name[:i]+ '\\' + name[i:] 

    i = 0
    i = name .rfind(")")
    if i != -1:
        name = name[:i]+ '\\' + name[i:] 
    
    i = 0
    i = name .rfind("!")
    if i != -1:
        name = name[:i]+ '\\' + name[i:] 
    print(name)
    os.system('echo "' +name+'"'+" | xclip -selection clipboard")


