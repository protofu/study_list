# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

stake = 50000
vat = 0.15

print(f'스테이크   {stake}')
print(f'+ VAT     {round(stake*vat)}')
print(f'총계 ₩    {round(stake*(1+vat))}')
