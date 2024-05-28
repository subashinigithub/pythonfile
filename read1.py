a="sk3"
f=open("filenew1.txt","r")
lines=f.read().split("\n")
print(lines)
for line in lines:
    data=line.split("\t")
    if data[0]==a:
        print(data[0],"average",data[8])
        break
else:
    print("no")