score = {
    'python': 80,
    'django': 89,
    'web': 83
}
score['algorithm'] = 90
score['python'] = 85
sum_all = 0
for i in score.values():
    sum_all+=i

print(sum_all/len(score))

