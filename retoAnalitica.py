print("Hello")
import math
def primos(n):
  primos=[]
  for i in range(2, n+1):
    isPrime= True
    limit=int(math.sqrt(i))
    for test in range(2,limit+1):
      if i % test ==0:
        isPrime=False
        break
    if isPrime:
      primos.append(i)
  return primos
def crossProductA(a,b):
  product=[a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
  return product
def crossProductB():
  file = open("vectors.txt", "r")
  linea1 = file.readline().strip()
  linea2 = file.readline().strip()
  file.close()
  vector1 = linea1.split(",")
  vector2 = linea2.split(",")
  for i in range(3):
    vector1[i] = float(vector1[i])
    vector2[i] = float(vector2[i])
  print(vector1)
  print(vector2)
  product = crossProductA(vector1, vector2)
  return product