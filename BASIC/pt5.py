def calculategmean(a,b):
    gmean=(a*b)/(a+b)
    print("geometric mean=",gmean)


a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))

calculategmean(a,b)
calculategmean(c,d)

#function arguments
def avaragek(a=2,b=5):
    print("the avarage is equal to",(a+b)/2)


avaragek()
avaragek(1,8) #ignores the default values
avaragek(4)   #value of a changes
avaragek(b=87)

#for multiple arguments
def aver(*numb):
    sum=0
    for i in numb:
        sum=sum+i
        
    print("average of all the numbers="sum/len(numb))

aver(3,45,677,43,22,76)
