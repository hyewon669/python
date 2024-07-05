##f=open("example.txt","w")
##for i in range(1,4):
####     f.write("Line %d\n" % i)
##f.close()

##f=open("example.txt","a")
##alphabet=['A','B','C','D','E']
##for c in alphabet:
##     f.write(c)
##f.close()

##f=open("example.txt","r")
##data=f.read()
##print(data)
##f.close()

##f=open("example.txt","r")
##while True:
##     line = f.readline()
##     if not line:
##          break
##     print(line,end= ")
##f.close()

##f=open("example.txt","r")
##data=f.readlines()
##for line in data:
##     print(line, end ='')
##f.close()

##f=open("example.txt", "r")
##while True:
##     print(f.tell(),end = ' ')
##     line = f.readline()
##     print(line.strip())
##     if not line : break
##f.seek(26)
##print("after setting a pointer: %d(%s)" % (f.tell(), f.read()[0]))
##f.close()

##f=open("profile.txt", "w")
##name=input("Name : ")
##age = input("Age : ")
##f.write("Name : %s\n" % name)
##f.write("Age : %s\n" % age)
##f.close()

##f=open("profile.txt","a")
##school=input("School:")
##f.write("School: %s\n" % school)
##f.close()

##f=open("profile.txt","r")
##data=f.read()
##print(data)
##f.close()

##f=open("profile.txt","r")
##f.seek(28)
##line=f.readline()
##print(line)

##f=open("alphabet.txt","w")
##f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
##f.close()

##f=open("alphabet.txt","r")
##index=int(input())
##f.seek(index)
##line=f.readline()
##print(line)

##f=open("fruit.txt","r")
##data=f.readlines()
##print(data)
##for i in range(0,11):
##     word=len(data[i])
##     if word>=11:
##          print(data[i])           

f=open("anna.txt","r")
line = f.readline()
line=line.split()
for word in line:
     if 'b' in word:
          print(word)
f.close()
