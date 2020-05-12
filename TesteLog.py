import math

print ("Logaritmo base 10 de 1000 eh : ", end="")
print (math.log(1000, 10))

print ("Logaritmo base 10 de 1000 eh : ", end="")
print ('{:.2}'.format(math.log(1000, 10)))

print ("Logaritmo base 2 de 64 eh : ", end="")
print ('{:.2}'.format(math.log(64, 2)))

print ("Logaritmo base 2 de 1/128 eh : ", end="")
print ('{:.2}'.format(math.log(1.0/128, 2)))

print ("Raiz de 15 : ", end="")
print ('{:.4}'.format(math.sqrt(15)))