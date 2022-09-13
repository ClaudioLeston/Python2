print("-------------------------------------------------------")
print("Trabajo 5.")
print("-------------------------------------------------------")

print("Ingrese la cantidad de GB: ")
GB = float( input())

MG = GB*1024
MD = MG/1.44

print("\nSALIDA: ")
print("-------------------------------------------------------")
print(MD)

print("la cantidad de Discos necesarios es: ", math.ceil(MD))