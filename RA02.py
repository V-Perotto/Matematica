import math

# funcao conversao de GRAUS para RAD
def converterGrausParaRad(numero):
    rad = (numero / 180) * math.pi
    return rad

    # funcao conversao de RAD para GRAUS


def converterRadParaGraus(numero):
    rad = (numero * 180) / math.pi
    return rad


# inicio do programa
print("---- FUNCOES TRIGONOMETRICAS ----\n")

angRad = float(input("DIGITE O VALOR DO ÂNGULO (rad): "))
angGrad = float(input("DIGITE O VALOR DO ÂNGULO (graus): "))
rad = converterGrausParaRad(angGrad)
grad = converterRadParaGraus(angRad * math.pi)
print("")
print("Angulo ({:.2f}) graus    = ({:.2f}) pi rad".format(angGrad, (rad / math.pi)))
print("Angulo ({:.2f}) pi rad   = ({:.2f}) graus".format(angRad, grad))