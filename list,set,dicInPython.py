#List In Python=A build in data type that store of values ,It Can store DIFFERNT type
marks=[45,3,4,5,244,244]
# print(marks)
student=["maya",100,"pratiksha" ,50]
# print(student[0],student[1])


#List Slicing

# marks[1 : 4]
# print(marks[1 : 4])

#List Methods=like function but only for list
# list=[2,3,1]
# list.append(6)
# print(list)
# list.sort()
# print(list)


# Sort for Decending
# list.sort(reverse=True)
# print(list)


# tuple:A build data type that us create immutable sequence of value
tup=(1,2,3,3,5)
# print(type(tup)); 

#method 
# print(tup.index(1))
# print(tup.count(3))
# WAP to ask to user to enter names of 3 fav movies & store in list
# movie=[]
# a=input("Enter fav movie1: ");
# b=input("Enter fav movie2: ");
# c=input("Enter fav movie3: ");
# movie.append(a);
# movie.append(b);
# movie.append(b);
# print(movie);

# WAP check if a list contains pallindrone of element.
# list1 =[1,2,1]
# x=list1.copy();
# x.reverse()
# if(x==list1):
#     print ("palin");
# else:
#     print("not palin");

# Dictionary in Python:Dictionory are used to store data values in key:values pairs
# They are unorded,mutable(changed)& dont'allow duplicate

# info={
#     "name" :"maya",
#     "age":23,
#     "marks":200,
#     "subjects" : ["python","c","java"]

# }
# print(info)


# Set In Python:set is the collection of the unorded items.
# Each element in the set must be unique & immutable
# set={1,2,4,3}
# print(type(set))
# set1={1,2,4,3,"hello","hello",3,4,2}
# print(set1)
# print(len(set1))
# create empty set
# collection= set()
# print(type(collection))

# union(set1) Combines both set value * return new
# set1={1,2,3}
# set2={2,3,5}
# print(set1.union(set2))#{1,2,3,5}

# set.intersection(set2) combine commom values & retuen new
# set1={1,2,3}
# set2={2,3,5}
# print(set1.intersection(set2))#{2,3}

#WAP enter marks of 3 subject in dic
# marks={};
# sub1=int(input("enter phy : "))
# marks.update({"phy" : sub1})

# sub1=int(input("enter che : "))
# marks.update({"che" : sub1})

# sub1=int(input("enter math : "))
# marks.update({"math" : sub1})

# print(marks)

#Loops in Python
# i=1
# while i<=10:
#     print(i*3)
#     i+=1

# num=[2,4,9,16]
# i=0
# while i<len(num):
#     print(num[i])
#     i+=1;


# list=(1,2,3,4,5,6)
# x=3
# i=0
# while i< len(list):
#     if(list[i]==x):
#         print("found ",i)
#     i+=1;

set={2,3,5,2,4,5}
for num in set:
    print(num)






