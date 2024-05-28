s=input('enter the username: ')
k=(input('enter the passwod: '))
f=open("emp.txt","r")
lines=f.read().split("\n")
print(lines)
for line in lines:
    data=line.split("\t")
    print(data)
    if data[0]==s:
        if data[2]==k:
            print("username",data[0])
            print("password",data[2])
            break
        
else:
    print("no")
      