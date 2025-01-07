def find_next_blck(str, chr):
    for i in range(len(str)):
        if str[i]== chr:
            return i
def get_index_numbers(str):
    for i in range(len(str)):
        if str[i].isdigit():
            return i
file = open('./logs.txt','r') 
j = 0
s = e = ""
for i in file:
    e = ""
    j = find_next_blck(i, 'K')
    e = e + i[j+2:]
    j = get_index_numbers(e)
    d = e[j] + e[j+1]
    s = s + d + " " + e
file.close()
file = open('./logs2.txt','w')
file.writelines(s)
file.close()

 