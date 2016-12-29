n = 15
num = [2]*15

weight_sum = 0
average = 0
for i in range(n):
    weight = (float(i)+0.5)/(n * (n*1.0/2)) ##normalized by area of n by 1 triangle
    weight_sum += weight
    average += num[i]*weight
    print weight

print weight_sum,average



