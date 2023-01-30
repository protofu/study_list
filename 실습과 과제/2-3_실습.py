str_lst = input('문자열을 입력하세요. : ')

str_lst=str_lst.upper()

a, b, c = list(str_lst.split())

if a[-1] == b[0] and b[-1] == c[0]:
    print('Pass')
else:
    print('Fail')