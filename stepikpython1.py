X = int(input())
H = int(input())
M = int(input())
c = (M+(X%60))//60
b = (H+(X//60)+c)
a = (M+(X%60))
d = (M+(X%60))%60
print (b)
print (d)

