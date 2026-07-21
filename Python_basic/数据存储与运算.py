# 变量交换案例:将a,b,c的值分别赋值给c，a，b，并将其输出
a, b, c = 100, 200, 300
d = a
a = b
b = c
c = d
print(a, b, c)
