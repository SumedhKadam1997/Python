import datetime
now = datetime.datetime.now()
cur_date=now.strftime("%d-%m-%Y %H:%M:%S")
f=open('Simple Diary.txt','a+')
f.write("\r\nToday's Date and Time :%s\r\n" % (cur_date))
txt=str(input("How was your Day? Please describe it."))
f.writelines(txt)
f.close()
