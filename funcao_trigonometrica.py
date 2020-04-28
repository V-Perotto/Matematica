import matplotlib.pyplot as plt
import numpy as np

# prepara para salvar o grafico
fig = plt.figure(figsize=(5, 5))

# Cria valores de x e corresponde y para criar coordenadas de ptos na curva do seno
x = np.arange(0, 3 * np.pi, 0.1)
ySin = np.sin(x)
plt.plot(x, ySin, label = 'f(x) = sen(x)', color = 'c')

# Cria valores de x e corresponde y para criar coordenadas de ptos na curva do cosseno
yCos = np.cos(x)
plt.plot(x, yCos, label = 'f(x) = cos(x)', color = 'g')

# Cria valores de x e corresponde y para criar coordenadas de ptos na curva da tangente
yTan = np.tan(x)
plt.plot(x, yTan, label = 'f(x) = tan(x)', color = 'm')

plt.title("Funcoes Trigonometricas Basicas")
plt.ylim([-10, 10])                 # Restringir o eixo y
plt.xlabel('eixo x')                # nome para o eixo x
plt.ylabel('eixo y')                # nome para o eixo y
plt.legend()                        # apresenta a legenda do grafico
plt.grid(True, which='both')        # apresenta grade do plano cartesiano
plt.axhline(y=0, color='k')         # destaca o eixo x em preto ('k')
plt.axvline(y=0, color='k')         # destaca o eixo y em preto ('k')
plt.show()
fig.savefig('FTrigo.png')