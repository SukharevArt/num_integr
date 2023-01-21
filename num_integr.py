from numpy import random,arange
from math import sin,cos
import matplotlib.pyplot as plt
from prettytable import PrettyTable 

# function = arr[0] * sin(arr[1]*x) + arr[2] * cos(arr[3]*x) +
#             + arr[4] + arr[5]*x + arr[6]*x^2 + arr[7]*x^3 + arr[8]*x^4

def gen_func():
    arr=[]
    for i in range(9):
        arr.append(random.uniform(-10,10))
    return arr

def function(arr,x):
    res = 0.0
    res += arr[0]*sin(arr[1]*x)
    res += arr[2]*cos(arr[3]*x)
    res += arr[4]+arr[5]*x+arr[6]*(x**2)+arr[7]*(x**3)+arr[8]*(x**4)
    return res

def antiderivative_function(arr,x):
    res = 0.0
    res += -arr[0]*cos(arr[1]*x)/arr[1]
    res += arr[2]*sin(arr[3]*x)/arr[3]
    res += arr[4]*x+arr[5]*(x**2)/2+arr[6]*(x**3)/3+arr[7]*(x**4)/4+arr[8]*(x**5)/5
    return res

def gen_vector(arr,l,r,n):
    vector=[]
    len = (r-l)/n
    for i in range(n+1):
        vector.append(function(arr,l+i*len))
    return vector

def right_integr(arr,l,r):
    return antiderivative_function(arr,r)-antiderivative_function(arr,l)

def simpson(arr,n,len):
    res = 0.0
    for i in range(0,(n+1)-2,2):
        res += arr[i] + 4*arr[i+1] + arr[i+2]
    res = res * len * 2 / 6
    return res

def three_eights(arr,n,len):
    res = 0.
    for i in range(0,(n+1)-3,3):
        res += arr[i] + 3*arr[i+1] + 3*arr[i+2] + arr[i+3]
    res = res * len * 3 / 8
    return res

def five_points(arr,n,len):
    res = 0.0
    for i in range(0,(n+1)-4,4):
        res += 7*arr[i] + 32*arr[i+1] + 12*arr[i+2] + 32*arr[i+3] + 7*arr[i+4]
    res = res * len * 4 / 90
    return res

def calc_for_num_lines(n,flag):
    k=5000
    a,b,c = 0,0,0
    r = 40
    l = -40
    for i in range(k):
        arr = gen_func()
        vector = gen_vector(arr, l, r, n)
        best = right_integr(arr, l, r)
        
        simp = simpson(vector, n, (r-l)/n)
        te = three_eights(vector, n, (r-l)/n)
        fp = five_points(vector, n, (r-l)/n)
        
        a+=abs((simp-best)/best)
        b+=abs((te-best)/best)
        c+=abs((fp-best)/best)
    a/=k
    b/=k
    c/=k
    if flag==1:
        return a
    if flag==2:
        return b
    if flag==3:
        return c


x = arange(24, 181, 12)
simpsonarr = [calc_for_num_lines(i,1) for i in x]
tearr = [calc_for_num_lines(i,2) for i in x]
fparr = [calc_for_num_lines(i,3) for i in x]

plt.figure(figsize=(10, 5))
plt.plot(x, simpsonarr, label='Simpson')
plt.plot(x, tearr, label='Three_eights')
plt.plot(x, fparr, label='Five_points')
plt.legend(loc='best', fontsize=12)
plt.show()

table = PrettyTable(["Кол-во интервалов","Формула Симпсона","Формула \"трех восьмых\"","Четырехинтервальная формула Боде"])

for i in range(len(simpsonarr)):
    table.add_row([x[i],simpsonarr[i],tearr[i],fparr[i]])
print(table)

