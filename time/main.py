import datetime
hour = int(input("Please set hour : "))
min = int(input("Please set minute : "))
sec = int(input("Please set second : "))
first_date = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, datetime.datetime.now().day, hour, min, sec)
total_seconds = hour * 3600 + min * 60 + sec
print("------------------------")
# تقسیم زمان بر 4
divided_seconds = total_seconds / 4

# تبدیل ثانیه به ساعت/دقیقه/ثانیه
new_time = datetime.timedelta(seconds=divided_seconds)
li = [new_time, new_time * 2]
li.append(li[1]+li[0])
li.append(li[2] + li[0])
li2 = [False, False, False, False]
print("time 1 :", li[0])
print("time 2 :", li[1])
print("time 3 :", li[2])
print("time 4 :", li[3])
print("--------------------")
for item in range(4):
    n = input("Read Part " + str(item + 1) +" : ")
    li2[item] = True
    print("time 1 :", li[0]," read : " ,li2[0])
    print("time 2 :", li[1]," read : " ,li2[1])
    print("time 3 :", li[2]," read : " ,li2[2])
    print("time 4 :", li[3]," read : " ,li2[3])
    print("------------------------")