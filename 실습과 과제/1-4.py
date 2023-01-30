s = input('숫자를 입력해주세요 : ')
s_list = list(s)
sum_all = 0
for i in s_list:
    sum_all += int(i)
print(sum_all)