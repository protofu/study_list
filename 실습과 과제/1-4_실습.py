n=1000
num_list = []
for i in range(1,n):
    if i%2==0 or i%7 == 0:
        num_list.append(i)
print(sum(num_list))
