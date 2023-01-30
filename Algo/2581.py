m=int(input())
n=int(input())
num_list = []
for i in range(m, n+1):
    cnt = 0
    for k in range(2, i):
        
        if i % k == 0:
            cnt+=1
            break
    if cnt == 0 and i!=1:
        num_list.append(i)
if num_list:
    print(sum(num_list))  
    print(min(num_list)) 
else:
    print('-1')
