def star(n):
    global paint

    if n == 3: # 가장 최소단위일 때 1,3번줄 채우고 2번줄 중앙 비우기
        paint[0][:3] = paint[2][:3] = [1, 1, 1] 
        paint[1][:3] = [1, 0, 1]
        return
    a = n//3 #n을 최소 단위로 쪼개기
    star(a)

    for i in range(3): # 세로
        for j in range(3): # 가로
            if i == 1 and j == 1: # 2차원 list 상 (1,1) 위치에 공백
                continue
            for k in range(a): # 한칸
                paint[a*i+k][a*j:a*(j+1)] = paint[k][:a]




n=int(input())
paint = [[0 for _ in range(n)] for _ in range(n)] # 2차원 list 생성
star(n)

for i in paint: # paint 리스트의 한 원소 씩 소환
    for j in i: # 한 원소의 원소를 소환
        if j: # 그 값이 True 즉 1일 경우
            print('*',end='') # 별을 출력
        else: # Flase이면 공백
            print(' ',end='')
    print()