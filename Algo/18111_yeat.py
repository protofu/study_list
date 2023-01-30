# n, m, b = map(int, input().split())

# # ground = [[0 for _ in range(m)] for _ in range(n)] # 땅 생성 2차원 리스트

# # for i in range(n): # 땅 높이 설정.
# #     ground[i] = list(map(int, input().split()))

# # print(ground[2].count(0))

# ground = {}
# for _ in range(n):
#     for i in map(int, input().split()):
#         if i in ground:
#             ground[i] += 1
#         else:
#             ground[i] = 1
# a = sum([x*ground[x] for x in ground])
# b = sum(ground.values())
# std_g = round(a/b)
# print(std_g)
print(type(str))