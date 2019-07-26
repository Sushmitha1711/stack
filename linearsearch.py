def searchLinear(lst,ele):

    index=0
    for i in lst:
        
        if i==ele:
            return index
        index+=1   
    return -1

ele=66
res=searchLinear([1,2,3,4,5,6,7,8],ele)
if res==-1:
    print(f"{ele} is not found:")
else:
    print(f"{ele} is found at :{res}")