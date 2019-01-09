def zero():
    return 0
def one():
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five():
    return 5
def six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
    return 9
text=open("read.txt","r")
operation=text.read()
length=len(operation)
locator=[0,0,0]
for i in range(0,length):
    if operation[i]=="(" or operation[i]==")":
        if(locator[0]==0):
            locator[0]=i
        elif(locator[1]==0):
            locator[1]=i
        elif(locator[2]==0):
            locator[2]=i
        else:
            break
a=["",""]
operand=""
i=0
while(i<locator[0]):
    a[0]=a[0]+operation[i]
    i+=1
#print a[0]
i+=1
while(i<locator[1]):
    operand=operand+operation[i]
    i+=1
#print operand
i+=1
while(i<locator[2]):
    a[1]=a[1]+operation[i]
    i+=1
#print a[1]
b=[0,0]
for i in range(0,2):
    if(a[i]=="zero"):
        b[i]=zero()
    elif(a[i]=="one"):
        b[i]=one()
    elif(a[i]=="two"):
        b[i]=two()
    elif(a[i]=="three"):
        b[i]=three()
    elif(a[i]=="four"):
        b[i]=four()
    elif(a[i]=="five"):
        b[i]=five()
    elif(a[i]=="six"):
        b[i]=six()
    elif(a[i]=="seven"):
        b[i]=seven()
    elif(a[i]=="eight"):
        b[i]=eight()
    else:
        b[i]=nine()
#print b[0]
#print b[1]
if(operand=="plus"):
    print b[0]+b[1]
elif(operand=="minus"):
    print b[0]-b[1]
else:
    print b[0]*b[1]
text.close()