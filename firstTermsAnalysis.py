number= input('enter an integer :')
div=2
a=""
while(number!=1):
    if(number%div==0):
        counter=0
        while(number%div==0):
            number=number/div
            counter+=1
        if(counter>1):
            a=a+"("+str(div)+"**"+str(counter)+")"
        else:
            a=a+"("+str(div)+")"
    else:
        div+=1
print a

    