print("-------------------------------------------------------")
print("Trabajo 3.")
print("-------------------------------------------------------")

print("Ingrese la cantidad de respuestas correctas: ")
RC = int( input())

print("Ingrese la cantidad de respuestas incorrectas: ")
RI = int( input())

print("Ingrese la cantidad de respuestas en blanco: ")
RB = int( input())

PCR = RC*3
PRI = RI*-1
PRB = RB*0

PF = PCR + PRI + PRB

print("El puntaje final es:", PF)