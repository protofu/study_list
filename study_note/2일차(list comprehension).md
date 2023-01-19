```python
# 1차원 list 
list_num=[0,0,0]
print(list_num)

list_num2=[0]*3
print(list_num2)

list_num3=[]
for _ in range(3):
    list_num3.append(0)
print(list_num3)  

list_num4=[0 for _ in range(3)] # 1차원 list comprehension
print(list_num4)

list_num2[0]=1
list_num4[0]=1

print(list_num2) # [1, 0, 0] 
print(list_num4) # [1, 0, 0]
```

```python
#2차원 list comprehension
list_num=[[0,0,0],[0,0,0],[0,0,0]]
print(list_num)

#list_num2=[[0]*3,[0]*3,[0]*3] 
list_num2=[[0]*3]*3
print(list_num2)

list_num3=[]
for _ in range(3):
    list_num3.append([0,0,0])
print(list_num3) 

list_num4=[[0 for _ in range(3)] for _ in range(3)] 
#list_num4=[[0]*3 for _ in range(3)] 같은 결과
print(list_num4) # 2차원 list comprehension 

list_num2[0][0] = 1
list_num4[0][0] = 1

print(list_num2) # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
print(list_num4) # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

print(id(list_num2[0])) #
print(id(list_num2[1])) # 같은 메모리의 주소를 참조하여 만듦
print(id(list_num2[2])) #

print(id(list_num4[0])) #
print(id(list_num4[1])) # 각자 다른 메모리를 사용.
print(id(list_num4[2])) # 

for i in range(3):
    list_num2[i][0]=1 # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
print(list_num2)
    #list_num4[]
```

