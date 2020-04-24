import matplotlib.pyplot as plt
import numpy as np
import math

# Funcao Loagaritmica
def funcaoLogaritmica (x, b):
    return (math.log(x,b))

# Cria vetor de -7 a 7, aumentando de 0.1
vetorX = np.arange(0.1, 70, 0.1)
print(vetorX)

# Base do Logaritmo
b = 2

# Encontra os valores de y para cada valor de x
vetorY = [] # vetor y vazio
for x in vetorX:
    vetorY.append(funcaoLogaritmica(x, 2)) # retorno da funcao vai para o vetorY
print(vetorY)

# Prepara para salvar o grafico
fig = plt.figure(figsize=(5, 5))

# Plota (desenha) o grafico
plt.plot(vetorX, vetorY, label = 'f(x) = log2(x)', color = 'c')

plt.title('f(x) = logb(x)')
plt.xlabel('eixo x')            # nome para eixo x
plt.ylabel('eixo y')            # nome para eixo y
plt.legend()                    # apresenta a legenda do grafico
plt.grid(True, which='both')    # apresenta grade do plano cartesiano
plt.axhline(y=0, color='k')     # destaca o eixo y em preto ('k')
plt.axvline(x=0, color='k')     # destaca o eixo x em preto ('k')
plt.show()                      # mostra o grafico
fig.savefig('FLog.png')
