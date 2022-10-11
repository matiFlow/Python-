import time

def f(n):
   inicio = time.time()
   for i in range(n):
         for j in range(n):
            k = 2 + 2
   fin = time.time()
   return inicio - fin
f(5000)