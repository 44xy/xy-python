sum=0
a=1
for i in range(100,201):             #range()函数生成迭代序列
    if i % 2 == 0:                   #条件判断和2取余数为0的为偶数
        print(i)                     #输出i的值检查是否为偶数
        sum += i                     #sum变量起累加器的作用
        a *= i
print("100到200中所有偶数的和为：",sum)
print("100到200中所有偶数的积为：",a)
#range(start, stop[, step])，分别是起始、终止和步长

sum=0
a=1
for i in range(100,201,2):
  print(i)
  sum += i
  a *= i
print(a,sum)