#Check if the small list is the sublist of big list

def check(smlst, biglst):
    r=0
    for i in range(len(biglst)):
        if  r<len(smlst) and biglst[i]==smlst[r]:
            r+=1
    
    print(r==len(smlst))

smlst=[8,2,6]
biglst=[5,6,8,4,2,5,4,1]
check(smlst,biglst)