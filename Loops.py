# there is two types of loop for and while loop

# for lopp
# (start, stop, step)
# for loop is used where we have to perform such kind of number of iteration
a=int(input("enter the value"))
for i in range (2,a+1,1):  
    print(i)


# while loop is used when we have terminating condition

# initialisation
a=int(input("enter the value"))   
# loop condition or terminating value
while(a>0):
    print(a-1)
    # step
    a-=1

