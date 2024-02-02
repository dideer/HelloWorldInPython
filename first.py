# print("hello world") 




# x,y,z="DIDIER","GWIZA","ISHIMWE"

# print(x)
# print(y) 
# print(z) 



# a=1

# for i in range(1,13,1):
    
#     for a in range(1,13,1):
#             b=i*a
#             print(i,'*',a,'=',b)
        
# print()
# for i in range(1,6,1):
#     for a in range(6,i,-1):
#             print('*',end="")
#     print()


# thislist=["apple","banana","cherry"]
# # thislist[1:3]=["watermelon"]
# thislist.pop()
# print(thislist)
# tropical=["mango","pineapple","papaya"]
# thislist.extend(tropical)

# print(thislist)

# for x in tropical:
#     print(x)

# i=0
# while i<len(tropical):
#     print(tropical[i])
#     i=i+1

# [print(x) for x in tropical]

fruits=["banana","apple","cherry","mango","kiwi"]

newlist=[]

for x in fruits:
    if "i" or "a" in x:
        newlist.append(x)
print(newlist)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

def myfunc(n):
    return abs(n -50)

thislist1=[100,50,65,82,23]
thislist1.sort(key=myfunc)
print(thislist1)

fruits.reverse()

print(fruits)

list1=["a","b","c"]
list2=[1,2,3]

for x in list2:
    list1.append(x)

print(list1)