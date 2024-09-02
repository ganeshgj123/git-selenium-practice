#Writing Fibonacci Series
"""f1=0
f2=1
print(f1)
print(f2)

for i in range(2,8):
    f3= f1+f2
    print(f3)
    f1= f2
    f2= f3"""

#######OR######################

fib = [0,1]
# Range starts from 0 by default
for i in range(5):
    fib.append(fib[-1] + fib[-2])
print(fib)

# Converting the list of integers to string
#print(', '.join(str(e) for e in fib))

