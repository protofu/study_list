m=int(input())
n=int(input())
num_list = []
for i in range(m, n+1):
    cnt = 0
    for k in range(2, i):
        
        if int(i % k) == 0:
            cnt+=1
    if cnt == 0:
        num_list.append(i)
print(sum(num_list))  
print(min(num_list))  
