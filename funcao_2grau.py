import matplotlib.pyplot as plt
import numpy as np

# Funcao 2o grau
def funcao2oGrau (a, b, c, x):
    return (a*x*x + b*x + c)

# Cria o valor de -7 a 7, aumentando de 0.1
vetorX = np.arange(-7, 7, 0.1)
print(vetorX)

# Coeficientes
a = 2
b = 5
c = -20

# Encontra os valores de y para cada valor de x
vetorY = [] # vetor y vazio
for x in vetorX:
    vetorY.append(funcao2oGrau(a, b, c, x)) # retorno da funcao vai para o vetorY
print(vetorY)

# prepara para salvar o grafico
fig = plt.figure(figsize=(5, 5))

# Plota (desenha) o grafico
plt.plot(vetorX, vetorY, label = 'Funcao 2o Grau', color = 'm')

plt.title('f(x) = ax^2 + bx + c')
plt.xlabel('eixo de x')         # nome para o eixo x
plt.ylabel('eixo de y')         # nome para o eixo y
plt.legend()                    # apresenta legenda do grafico
plt.grid(True, which='both')    # apresenta grade do plano cartesiano
plt.axhline(y=0, color='k')     # destaca o eixo y em preto ('k')
plt.axvline(x=0, color='k')     # destaca o eixo x em preto ('k')
plt.show()                      # mostra o grafico
fig.savefig('F2oGrau.png')