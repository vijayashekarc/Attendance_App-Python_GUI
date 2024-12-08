import csv
from datetime import date
today = date.today().strftime("%d-%m-%y")


f=open("attendance.csv","r")
stu=list(csv.reader(f))

ff=open("CSE_A04_"+today+".csv","a")
ff.write("Name,Reg_NO,Attendance\n")
pre,ab=0,0
for i in stu:
    print("\n")
    print("SrNO")
    print("Name   : ",i[2])
    print("Reg NO : ",i[1])
    a=input("Attendance: [A/P] : ").upper()
    ff.write("{0},{1},{2}\n".format(i[2],i[1],a))
    if a=="":
        pre=pre+1
    elif a=="B" :
        break
ff.close()
print("______________________________________")
print("\n\tAttendance on",today)
print("\tTotal:",len(stu))
print("\tPresent:",pre)
print("\tAbsent:",len(stu)-pre)
print("______________________________________")

