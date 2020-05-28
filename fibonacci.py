fibo_series = [0,1]
for i in range(30):
	num = fibo_series[-1]+ fibo_series[-2]
	fibo_series.append(num)

print(fibo_series)