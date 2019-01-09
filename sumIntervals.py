def sumIntervals(pinakas):
    a=len(pinakas)
    s=0
    #print pinakas
    pinakas.sort()
    #print pinakas
    for i in range(0,a-1):
        for j in range(i+1,a):
            if(pinakas[i][1]>pinakas[j][0]):
                if(pinakas[i][1]>=pinakas[j][1]):
                    pinakas[j][1]=0
                    pinakas[j][0]=0
                else:
                    pinakas[j][0]=pinakas[i][1]
    #print pinakas
    for i in range(0,a):
        s=s+pinakas[i][1]-pinakas[i][0]
        #print s
    #print s
    return s
    
        
        
#alist=[[1,5], [10, 20], [1, 6], [16, 19], [5, 11]]
#a=sumIntervals(alist)
#print a