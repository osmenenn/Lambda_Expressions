
#Ismoil BOboev 
#Lambda Expressions
#SEVD Exercises 

#Squaring
my_list = [4,5,7]

new_list = list(map(lambda num: num**2, my_list))
print(*new_list)

#List Sorting 
a = [(0,2), (4,3), (10, -1), (9, 9)]
a.sort(key=lambda x:x[1])
print(a)
