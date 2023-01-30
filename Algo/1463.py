# n = int(input())
# dp = [0] * 1000001
# dp[2] = 1
# dp[3] = 1

# for i in range(2,n+1):
#     a = 1000000
#     b = 1000000
#     c = dp[i-1] + 1
#     if i % 2 == 0:
#         a = dp[i // 2] + 1
#     if i % 3 == 0:
#         b = dp[i // 3] + 1
#     dp[i] = min(a,b,c)

# print(dp[n])

print(type(int))
