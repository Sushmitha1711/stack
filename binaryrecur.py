def binarySearch(lst,l,h,key):
   
    if l<=h:
        mid=(l+h)//2
        print(f"{l}  {h} and {mid}")
        if lst[mid]==key:
            return mid
        elif key>lst[mid]:
            l=mid+1
        else:
            h=mid-1
    return -1



ele=6
res=binarySearch([1,2,3,4,5,6,7,8],ele)
if res==-1:
    print(f"{ele} is not found:")
else:
    print(f"{ele} is found at :{res}")