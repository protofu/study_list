n = int(input())
num_list = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
    dp[0] = num_list[0]
    dp[i] = max(dp[i-1] + num_list[i], num_list[i])
print(max(dp))