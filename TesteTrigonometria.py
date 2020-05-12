import math
#funcao conversao de GRAUS para RAD
def converterGrausParaRad(numero):
 rad = (numero/180)*math.pi
 return rad

# inicio do programa
print("---- FUNCOES TRIGONOMETRICAS ----\n")
a = input("DIGITE O VALOR DO ÂNGULO: ")
angulo = float(a)
seno = math.sin(converterGrausParaRad(angulo))
cos = math.cos(converterGrausParaRad(angulo))
print("")
print("Calculo para angulo ({} graus): seno = {:.2f} cosseno = {:.2f}" . format(a, seno, cos))

seno = math.sin(angulo)
cos = math.cos(angulo)
print("")
print("Calculo para angulo ({} graus): seno = {:.2f} cosseno = {:.2f}" . format(a, seno, cos))