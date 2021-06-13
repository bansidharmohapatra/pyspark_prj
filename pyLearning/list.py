import copy
"""
nos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_no = [i for i in nos if i % 2 == 0]
odd_no=[i for i in nos if i % 2 !=0]
evOdd=["even" if i % 2 ==0 else "odd" for i in nos]
print(even_no)
print(odd_no)
print (evOdd) """

#Transposing a matrix

matrix = [[1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]]
output= [[row[i] for row in matrix] for i in range(5)]
print(output)

lst=[1,2,3,4,5]
lst1=lst
print(lst)
print(lst1)
print("after lst chage")
lst[2]=10
print(lst)
print(lst1)
print("after lst1 change")
lst1[2]=20
print(lst)
print(lst1)
lst2= copy.copy(lst)
print(lst2)
lst2[2]=30
print("after shallow copy changes to lst2")
print (lst)
print(lst2)
print("after shallow original change")
lst[2]=40
print(lst)
print(lst2)