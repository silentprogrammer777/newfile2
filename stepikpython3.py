##a = int(input())
##b = int(input())
##c = int(input())
##p = ((a+b+c)/2)
##print ((p*(p-a)*(p-b)*(p-c))**0.5)

##A=int(input())
##if (-15 < A <= 12) or (14 < A < 17) or (19 <= A) :
##    print('True')
##else:
##    print('False')
    
##A = float (input())
##B = float (input())
##C = str (input())
##if C =='+':
##    print(A+B)
##elif C=='-':
##    print(A-B)
##elif C=='*':
##    print(A*B)
##elif C=='/' and B==0:
##    print("Деление на 0!")
##elif C=='/' and B!=0:
##    print(A/B)
##elif C=='mod' and B==0:
##    print('Деление на 0!')
##elif C=='mod' and B!=0:
##    print(A%B)
##elif C=='pow':
##    print(A**B)
##elif C=='div' and B==0:
##    print('Деление на 0!')
##elif C=='div' and B!=0:
##    print(A//B)

##a = int(input())
##b = int(input())
##c = int(input())
##if a<=b<=c:
##    print(c)
##    print(a)
##    print(b)
##elif a<=c<=b:
##    print(b)
##    print(a)
##    print(c)
##elif b<=a<=c:
##    print(c)
##    print(b)
##    print(a)
##elif b<=c<=a:
##    print(a)
##    print(b)
##    print(c)
##elif c<=b<=a:
##    print(a)
##    print(c)
##    print(b)
##elif c<=a<=b:
##    print(b)
##    print(c)
##    print(a)

s = int (input())
n1 =" программистов"
n2 =" программист"
n3 =" программиста"
if  s>=0:
  if s==0:
    print(str(s) + n1)
  elif s%100>=10 and s%100<=20:
    print(str(s) + n1)
  elif s%10==1:
    print(str(s) + n2)
  elif s%10>=2 and s%10<=4:
    print(str(s) + n3)
  else:
    print(str(s) + n1)

##n = int(input())
##if 5<=n or 0==n:
##    print(n,'программистов')
##elif n==1:
##    print(n, "программист")
##elif n==2 or n==3 or n==4:
##    print(n, 'программиста')
