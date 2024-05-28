s1=input('enter a student name: ')
s2=int(input('enter a student age: '))
m1=int(input('enter a mark1: '))
m2=int(input('enter a mark2: '))
m3=int(input('enter a mark3: '))
m4=int(input('enter a mark4: '))
m5=int(input('enter a mark5: '))
total=m1+m2+m3+m4+m5
avg=total/5
if(avg>80):
    print("You will be passed with distinction")
elif(avg>70):
    print("You will be passed with first class")
elif(avg>60):
    print("You will be passed with second class")
else:
    print("You will be failed")


f=open("filenew1.txt","a")
f.write("\n")
f.write(s1)
f.write("\t")
f.write(str(s2))
f.write("\t")
f.write(str(m1))
f.write("\t")
f.write(str(m2))
f.write("\t")
f.write(str(m3))
f.write("\t")
f.write(str(m4))
f.write("\t")
f.write(str(m5))
f.write("\t")
f.write(str(total))
f.write("\t")
f.write(str(avg))
                                                                 

